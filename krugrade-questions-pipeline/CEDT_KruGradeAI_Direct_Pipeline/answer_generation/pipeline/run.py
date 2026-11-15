#!/usr/bin/env python3
"""KruGradeAI blind synthetic response pipeline, using Codex CLI for generation and grading.
Standard library only. No generated response is represented as independently verified ground truth.
"""
import argparse, csv, hashlib, json, math, re, shutil, subprocess, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GEN_SCHEMA = ROOT / 'pipeline' / 'generation.schema.json'
GRADE_SCHEMA = ROOT / 'pipeline' / 'grading.schema.json'
# Native CEDT question-pipeline CSV is a first-class input: answer columns are
# created only for the output. Existing KruGradeAI response CSVs still work.
QUESTION_REQUIRED = {'question_id','question_text','rubric_criteria','rubric_max_score','solution'}
ANSWER_FIELDS = ['sample_type','answer_text','expected_score','rubric_analysis',
    'covered_rubric_points','missed_rubric_points','partially_covered_rubric_points',
    'missed_concepts','error_categories','error_location','grader_feedback',
    'improvement_suggestion','response_id','student_id','attempt_id','response_origin',
    'adjudication_status','label_review_status','label_source',
    'requested_sample_type','target_score_band','actual_score_band','generation_target_status']


def read_csv(path):
    with open(path, newline='', encoding='utf-8-sig') as f:
        r=csv.DictReader(f)
        if not r.fieldnames: raise ValueError('Missing CSV headers')
        if len(set(r.fieldnames))!=len(r.fieldnames): raise ValueError('Duplicate column names')
        missing=QUESTION_REQUIRED-set(r.fieldnames)
        if missing: raise ValueError(f'Missing question fields: {sorted(missing)}')
        rows=list(r)
        if not rows: raise ValueError('Empty CSV')
        if any(None in row for row in rows): raise ValueError('Malformed CSV row with extra cells')
        # Keep all original columns and append only the missing answer columns.
        fields=list(r.fieldnames)+[k for k in ANSWER_FIELDS if k not in r.fieldnames]
        for row in rows:
            for k in fields: row.setdefault(k,'')
        return fields, rows


def scoring_guide(row):
    """Read rubric natively; do not require a separately generated adapter file."""
    existing=row.get('rubric_scoring_guide','')
    if str(existing).strip():
        return as_json(existing,existing)
    criteria=as_json(row.get('rubric_criteria'))
    if not isinstance(criteria,list): raise ValueError('Invalid rubric_criteria')
    return [{
        'criterion_id':c.get('criterion_id'),
        'criterion':c.get('criterion',c.get('description','')),
        'max_points':c.get('max_points',c.get('max_score')),
        'full_credit':c.get('full_credit',''),
        'partial_credit':c.get('partial_credit',''),
        'common_mistakes':c.get('common_mistakes',''),
        **({'scoring_levels':c['scoring_levels']} if 'scoring_levels' in c else {})
    } for c in criteria]

def as_json(text, default=None):
    try: return json.loads(text)
    except (TypeError, ValueError): return default


def criteria_for(row):
    cs=as_json(row['rubric_criteria'])
    if not isinstance(cs,list) or not cs: raise ValueError(f"Invalid rubric_criteria: {row['question_id']}")
    out=[]
    for i,c in enumerate(cs):
        if not isinstance(c,dict): raise ValueError('Rubric criterion is not an object')
        cid=str(c.get('criterion_id') or f'C{i+1}')
        maximum=c.get('max_score',c.get('max_points',c.get('points')))
        if maximum is None: raise ValueError(f'Missing max on {cid}')
        maximum=float(maximum)
        if maximum<=0: raise ValueError(f'Invalid max on {cid}')
        anchors=c.get('scoring_levels')
        scores=None
        if isinstance(anchors,list) and anchors:
            scores={0.0,maximum}
            for anchor in anchors:
                if isinstance(anchor,dict) and 'score' in anchor: scores.add(float(anchor['score']))
        out.append((cid,maximum,scores))
    if len({c[0] for c in out})!=len(out): raise ValueError('Duplicate rubric criterion IDs')
    declared=float(row['rubric_max_score'])
    if not math.isclose(sum(c[1] for c in out),declared,abs_tol=1e-6):
        raise ValueError(f"Rubric max mismatch {row['question_id']}: {sum(c[1] for c in out)} != {declared}")
    return out


def get_questions(rows):
    groups=defaultdict(list)
    for r in rows: groups[r['question_id']].append(r)
    for q, rr in groups.items():
        base=rr[0]
        for r in rr[1:]:
            for field in ('question_text','rubric_criteria','rubric_max_score','solution'):
                if r[field]!=base[field]: raise ValueError(f'Inconsistent {field} for {q}')
        criteria_for(base)
    return groups


def normalize(t): return re.sub(r'\s+',' ',str(t).strip().lower())


def digest(obj): return hashlib.sha256(json.dumps(obj,ensure_ascii=False,sort_keys=True).encode()).hexdigest()


def save_json(path, obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    tmp.replace(path)


def sample_plan(count):
    bands=['FULL','LOW','MID','HIGH','WRONG']
    return [{'sample_type': b if b in ('FULL','WRONG') else 'PARTIAL', 'score_band': b}
            for b in (bands[i % len(bands)] for i in range(count))]


def score_band(total, maximum):
    if total == 0: return 'WRONG'
    if math.isclose(total, maximum, rel_tol=0, abs_tol=1e-6): return 'FULL'
    return 'LOW' if total/maximum < 1/3 else ('MID' if total/maximum < 2/3 else 'HIGH')


def generation_payload(q, existing, count, mode='partial'):
    r=existing[0]
    # Deliberately no solution, answer, canonical_* or previous grading from solution.
    # Existing examples are provided strictly as student RESPONSE text and optional score pattern.
    previous=[{'answer_text':x.get('answer_text','')} for x in existing if x.get('sample_type','').lower()=='partial']
    payload={'question_id':q,'question_text':r['question_text'],
            'rubric_criteria':as_json(r['rubric_criteria']),
            'rubric_scoring_guide':scoring_guide(r),
            'rubric_max_score':r['rubric_max_score'], 'existing_partial_examples':previous,
            'requested_count':count}
    if mode=='balanced': payload['requested_samples']=sample_plan(count)
    return payload


def generation_prompt(payload):
    return ('You generate authentic exam student responses, not grading commentary. '
       'Use ONLY the attached JSON context; do not read local files, tools, repositories or official solutions. '
       'Produce exactly requested_count answers in requested_samples order when supplied; otherwise all PARTIAL. '
       'FULL should earn all rubric credit, WRONG should earn zero, PARTIAL earns some but not all credit. '
       'For PARTIAL aim for LOW (0 < fraction < 1/3), MID (1/3 <= fraction < 2/3), HIGH (2/3 <= fraction < 1). '
       'These are generation goals only; a separate grader will determine actual scores. Never include target scores in answers. '
       'Write as unaware students; realistic work and varied errors. '
       'Prioritize novel rubric satisfaction/failure patterns and distinct mathematical misunderstandings. '
       'Never paste or paraphrase previous answers, never mention rubrics in answer_text. '
       'PARTIAL answers should mix correct and incorrect work. FULL answers need complete reasoning; WRONG answers should contain plausible fundamental misconceptions. '
       'For FULL use error_pattern to describe its distinct correct approach, without inventing an error. '
       'Different error_pattern labels must reflect different substantive mistakes. '
       'Return ONLY JSON matching the schema.\n\nCONTEXT:\n'+json.dumps(payload,ensure_ascii=False))


def grading_prompt(payload):
    return ('Act as an independent rubric grader. You may inspect ONLY the JSON below; do not inspect other files. '
       'Use the official solution and listed scoring guide. Grade each answer as WRITTEN, not desired scores. '
       'Return an evaluation for EACH answer in the same order, with each criterion represented ONCE. '
       'Use scoring anchor values where explicitly specified, support every awarded point by actual answer evidence. '
       'Do not invent credit for missing evidence. Provide short concept labels in missed_concepts, not rubric prose. '
       'Avoid score targeting: if FULL or WRONG, report its actual score. Output ONLY schema-valid JSON.\n\nCONTEXT:\n'
       +json.dumps(payload,ensure_ascii=False))


def invoke_codex(prompt,schema,path,exe='codex'):
    if not shutil.which(exe): raise RuntimeError(f'{exe} is not installed or is not on PATH; run `codex login` first.')
    path.parent.mkdir(parents=True,exist_ok=True)
    command=[exe,'exec','--ephemeral','--skip-git-repo-check','--sandbox','read-only','--output-schema',str(schema),'-o',str(path),'-']
    result=subprocess.run(command,input=prompt,text=True,encoding='utf-8',capture_output=True,cwd=str(ROOT))
    if result.returncode!=0: raise RuntimeError('Codex failed: '+result.stderr[-3500:])
    try: return json.loads(path.read_text(encoding='utf-8'))
    except (ValueError,OSError) as e: raise RuntimeError('Codex output is not valid JSON: '+str(e))


def validate_generation(result, count, existing):
    samples=result.get('samples')
    if not isinstance(samples,list) or len(samples)!=count: raise ValueError(f'Expected {count} samples')
    known={normalize(x.get('answer_text','')) for x in existing}
    patterns=set()
    for s in samples:
        if not isinstance(s,dict) or not str(s.get('answer_text','')).strip(): raise ValueError('Missing answer_text')
        a=normalize(s['answer_text'])
        if a in known: raise ValueError('Duplicate answer text')
        known.add(a)
        p=normalize(s.get('error_pattern',''))
        if not p or p in patterns: raise ValueError('Error patterns missing or duplicated')
        patterns.add(p)
        if re.search(r'\b(rubric|synthetic|as an ai|i intentionally)\b',a,re.I):
            raise ValueError('Student answer contains meta commentary')
    return samples


def score_evaluations(result, samples, criteria, question_id, partial_only=True):
    ev=result.get('evaluations')
    if not isinstance(ev,list) or len(ev)!=len(samples): raise ValueError('Wrong number of evaluations')
    ids=[c[0] for c in criteria]
    output=[]
    for sample,e in zip(samples,ev):
        grades=e.get('rubric_scores')
        if not isinstance(grades,list) or [x.get('criterion_id') for x in grades]!=ids:
            raise ValueError(f'Criterion IDs mismatch in {question_id}')
        total=0.; analysis=[]; covered=[]; missed=[]; partly=[]
        for gr,(cid,maximum,anchors) in zip(grades,criteria):
            try: score=float(gr['awarded_score'])
            except (KeyError,ValueError,TypeError): raise ValueError(f'Invalid awarded_score on {cid}')
            if not math.isfinite(score) or score < 0 or score > maximum+1e-6:
                raise ValueError(f'Out-of-range score on {cid}')
            if anchors is not None and not any(math.isclose(score,a,abs_tol=1e-6) for a in anchors):
                raise ValueError(f'Score not one of allowed anchors on {cid}: {score}')
            reasoning=str(gr.get('reasoning','')).strip()
            if not reasoning: raise ValueError(f'Missing justification on {cid}')
            status='covered' if math.isclose(score,maximum,abs_tol=1e-6) else ('missed' if math.isclose(score,0,abs_tol=1e-6) else 'partial')
            entry={'criterion_id':cid,'max_score':maximum,'awarded_score':score,'status':status,'reasoning':reasoning}
            analysis.append(entry);total+=score
            if status=='covered': covered.append(cid)
            else: missed.append(cid)
            if status=='partial': partly.append(cid)
        if partial_only and not (0 < total < sum(c[1] for c in criteria)):
            raise ValueError(f'Sample is not PARTIAL in {question_id}, actual score={total}')
        for k in ('grader_feedback','improvement_suggestion','error_location'):
            if not str(e.get(k,'')).strip():
                if k != 'grader_feedback' and math.isclose(total,sum(c[1] for c in criteria),rel_tol=0,abs_tol=1e-6):
                    e=dict(e);e[k]='not_applicable'
                else: raise ValueError(f'Blank {k}')
        concepts=e.get('missed_concepts',[])
        categories=e.get('error_categories',[])
        if not isinstance(concepts,list) or not all(isinstance(v,str) for v in concepts):raise ValueError('Invalid missed_concepts')
        if not isinstance(categories,list) or not all(isinstance(v,str) for v in categories):raise ValueError('Invalid error_categories')
        output.append({'total':round(total,6),'analysis':analysis,'covered':covered,'missed':missed,'partial':partly,'concepts':concepts,'categories':categories,'evaluation':e})
    return output


def unique_id(prefix, used):
    i=1
    while True:
        candidate=f'{prefix}_{i:03d}'
        if candidate not in used: used.add(candidate);return candidate
        i+=1


def build_rows(fields, groups, question_id, gen, scored, used_ids):
    base=groups[question_id][0]; out=[]
    for i,(s,g) in enumerate(zip(gen,scored),1):
        r=dict(base)
        for k in fields:
            if k in ('reviewer_feedback','reviewed_answer','reviewed_solution','label_review_notes','label_reviewer','answer_image_path','answer_excerpt','grader_feedback_v2','improvement_suggestion_v2','missed_concept_ids'):
                r[k]=''
        band=score_band(g['total'],float(base['rubric_max_score']))
        kind=band if band in ('FULL','WRONG') else 'PARTIAL'
        r['response_id']=unique_id(f'{question_id}_SYN_{kind}',used_ids)
        if 'student_id' in r:r['student_id']=f"SYN_{question_id}_{i:02d}"
        if 'attempt_id' in r:r['attempt_id']=f"SYN_{question_id}_{i:02d}_A1"
        r['sample_type']=kind.lower() if base.get('sample_type','').islower() else kind
        target=s.get('target',{'sample_type':'PARTIAL','score_band':'PARTIAL'})
        r['requested_sample_type']=target['sample_type']
        r['target_score_band']=target['score_band']
        r['actual_score_band']=band
        r['generation_target_status']='matched' if target['score_band'] in (band,kind) else 'mismatch'
        r['answer_text']=s['answer_text'];r['expected_score']=str(g['total'])
        r['rubric_analysis']=json.dumps(g['analysis'],ensure_ascii=False,separators=(',',':'))
        r['covered_rubric_points']=';'.join(g['covered']);r['missed_rubric_points']=';'.join(g['missed'])
        if 'partially_covered_rubric_points' in r:r['partially_covered_rubric_points']=';'.join(g['partial'])
        r['missed_concepts']=json.dumps(g['concepts'],ensure_ascii=False)
        r['error_categories']=';'.join(g['categories'])
        r['error_location']=g['evaluation']['error_location']
        r['grader_feedback']=g['evaluation']['grader_feedback']
        r['improvement_suggestion']=g['evaluation']['improvement_suggestion']
        if 'response_origin' in r:r['response_origin']='synthetic'
        if 'adjudication_status' in r:r['adjudication_status']='not_required'
        if 'label_review_status' in r:r['label_review_status']='unreviewed'
        if 'label_source' in r:r['label_source']='synthetic_codex_unverified'
        if 'image_review_status' in r:r['image_review_status']='not_required' if base.get('image_review_status')=='not_required' else ''
        out.append(r)
    return out


def write_csv(path,fields,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with open(path,'w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='raise');w.writeheader();w.writerows(rows)


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',required=True,type=Path)
    p.add_argument('--out',type=Path,default=ROOT/'output')
    p.add_argument('--count',type=int,default=5)
    p.add_argument('--mode',choices=['balanced','partial'],default='balanced',help='Balanced cycles FULL/LOW/MID/HIGH/WRONG; count is total per question')
    p.add_argument('--max-questions',type=int,default=None,help='Limit questions for a pilot')
    p.add_argument('--codex-bin',default='codex')
    p.add_argument('--dry-run',action='store_true',help='Prepare manifest only; no model calls')
    p.add_argument('--resume',action='store_true',help='Reuse completed stages (hash-checked)')
    args=p.parse_args(argv)
    if args.count<1: p.error('--count must be positive')
    if args.mode=='balanced' and args.count<5: p.error('Balanced mode requires --count >= 5')
    fields,rows=read_csv(args.input);groups=get_questions(rows)
    qs=list(groups)
    if args.max_questions is not None: qs=qs[:args.max_questions]
    args.out.mkdir(parents=True,exist_ok=True)
    manifest={'input':str(args.input),'input_sha256':hashlib.sha256(args.input.read_bytes()).hexdigest(),
              'original_rows':len(rows),'questions_total':len(groups),'questions_selected':len(qs),
              'count_per_question':args.count,'mode':args.mode,'columns':len(fields),'question_ids':qs,
              'input_mode':'existing_answers' if any(r['answer_text'].strip() for r in rows) else 'question_pipeline_direct'}
    save_json(args.out/'manifest.json',manifest)
    print(f"Input: {len(rows)} rows, {len(groups)} questions, {len(fields)} columns; selected {len(qs)} x {args.count}",flush=True)
    if args.dry_run: return 0
    used={r['response_id'] for r in rows};generated=[];report=[]
    stages=args.out/'stages';stages.mkdir(exist_ok=True)
    for n,q in enumerate(qs,1):
        rr=groups[q];criteria=criteria_for(rr[0]);gp=generation_payload(q,rr,args.count,args.mode)
        key=digest({'input_sha256':manifest['input_sha256'],'generation_payload':gp,'schema_version':2})
        stage=stages/f'{n:03d}_{hashlib.sha256(q.encode()).hexdigest()[:10]}'
        stage.mkdir(exist_ok=True)
        meta=stage/'meta.json';gen_file=stage/'generation.json';grading_file=stage/'grading.json'
        match=args.resume and meta.exists() and as_json(meta.read_text(encoding='utf-8'),{}).get('key')==key
        try:
            if match and gen_file.exists(): gen=as_json(gen_file.read_text(encoding='utf-8'))
            else:
                gen=invoke_codex(generation_prompt(gp),GEN_SCHEMA,gen_file,args.codex_bin)
                save_json(meta,{'key':key,'question_id':q})
            samples=validate_generation(gen,args.count,rr)
            if args.mode=='balanced':
                samples=[dict(s,target=t) for s,t in zip(samples,sample_plan(args.count))]
            grade_input={'question_id':q,'question_text':rr[0]['question_text'],
                'solution':rr[0].get('solution',''),'rubric_criteria':as_json(rr[0]['rubric_criteria']),
                'rubric_scoring_guide':scoring_guide(rr[0]),
                'rubric_max_score':rr[0]['rubric_max_score'],
                'student_answers':[x['answer_text'] for x in samples]}
            # Solution is intentionally introduced for the FIRST TIME here.
            if not grade_input['solution'].strip():
                raise ValueError('Official solution is empty; cannot validate scores')
            if match and grading_file.exists():grade=as_json(grading_file.read_text(encoding='utf-8'))
            else:grade=invoke_codex(grading_prompt(grade_input),GRADE_SCHEMA,grading_file,args.codex_bin)
            scored=score_evaluations(grade,samples,criteria,q,partial_only=args.mode=='partial')
            vector=[tuple(g['analysis'][j]['awarded_score'] for j in range(len(criteria))) for g in scored]
            added=build_rows(fields,groups,q,samples,scored,used)
            generated+=added
            report.append({'question_id':q,'status':'accepted_provisionally','samples':len(added),
                           'distinct_score_vectors':len(set(vector)),'rubric_count':len(criteria),
                           'actual_score_bands':dict(Counter(r['actual_score_band'] for r in added)),
                           'target_mismatches':sum(r['generation_target_status']=='mismatch' for r in added),
                           'note':'Model-graded; independent human/adjudicated review not performed'})
            print(f'[{n}/{len(qs)}] {q}: {len(added)} provisionally validated samples',flush=True)
        except (ValueError,RuntimeError,KeyError,TypeError) as exc:
            report.append({'question_id':q,'status':'failed','error':str(exc),'error_type':type(exc).__name__})
            print(f'[{n}/{len(qs)}] {q}: FAILED: {exc}',file=sys.stderr,flush=True)
        save_json(args.out/'validation_report.json',{'manifest':manifest,'questions':report,
              'generated_rows':len(generated),'warning':'Model assessments are provisional, not independently verified ground truth.'})
        write_csv(args.out/'new_samples.csv',fields,generated)
        write_csv(args.out/'new_partial_samples.csv',fields,[r for r in generated if r['sample_type'].upper()=='PARTIAL'])
        write_csv(args.out/'generation_review_queue.csv',fields,[r for r in generated if r['generation_target_status']=='mismatch'])
        write_csv(args.out/'expanded_dataset.csv',fields,rows+generated)
    failures=sum(x['status']=='failed' for x in report)
    print(f'Done: {len(generated)} new samples, {failures} failed questions. Files in {args.out}',flush=True)
    return 1 if failures else 0


if __name__=='__main__':sys.exit(main())
