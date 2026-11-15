#!/usr/bin/env python3
"""Auditable generated-question and generated-answer evaluation using Codex CLI.
Deterministic checks always run. Model judgments are provisional and never auto-approved.
"""
import argparse
import csv
import difflib
import hashlib
import json
import math
import re
import shutil
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
QSCHEMA = BASE/'pipeline'/'question.schema.json'
ASCHEMA = BASE/'pipeline'/'answer.schema.json'

def read_csv(path):
    with open(path, encoding='utf-8-sig', newline='') as f:
        reader=csv.DictReader(f)
        fields=reader.fieldnames or []
        if len(set(fields))!=len(fields): raise ValueError(f'Duplicate headers: {path}')
        rows=list(reader)
        if any(None in row for row in rows): raise ValueError(f'Malformed CSV: {path}')
        return fields, rows

def jload(v, default=None):
    try: return json.loads(v) if isinstance(v,str) else v
    except (ValueError,TypeError): return default

def norm(s): return re.sub(r'\s+', ' ',str(s or '').strip().casefold())

def signature(row): return (str(row.get('question_id','')),str(row.get('response_id','')))

def sha_file(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for buf in iter(lambda:f.read(1024*1024),b''):h.update(buf)
    return h.hexdigest()

def dump(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix('.tmp')
    tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    tmp.replace(path)

def write_csv(path,records,headers):
    path.parent.mkdir(parents=True,exist_ok=True)
    with open(path,'w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=headers,extrasaction='ignore');w.writeheader();w.writerows(records)

def rubric(row):
    raw=jload(row.get('rubric_criteria'))
    if not isinstance(raw,list) or not raw: raise ValueError('rubric_criteria must be nonempty JSON array')
    result=[]
    for i,c in enumerate(raw,1):
        if not isinstance(c,dict):raise ValueError('criterion must be object')
        cid=str(c.get('criterion_id') or f'C{i}')
        maximum=float(c.get('max_score',c.get('max_points',c.get('points',0))))
        if not math.isfinite(maximum) or maximum<=0:raise ValueError(f'invalid max for {cid}')
        anchor=c.get('scoring_levels')
        allowed=None
        if isinstance(anchor,list) and anchor:
            allowed={0.0, maximum}
            allowed.update(float(v['score']) for v in anchor if isinstance(v,dict) and 'score' in v)
        result.append({'id':cid,'max':maximum,'allowed':allowed,'description':c.get('description','')})
    if len(set(c['id'] for c in result))!=len(result): raise ValueError('duplicate criterion IDs')
    declared=row.get('rubric_max_score')
    if declared not in (None,'') and not math.isclose(sum(c['max'] for c in result),float(declared),abs_tol=1e-5):
        raise ValueError('sum of rubric maxima != rubric_max_score')
    return result

def score_analysis(row,criteria):
    entries=jload(row.get('rubric_analysis'))
    if not isinstance(entries,list):return None, ['missing_or_invalid_rubric_analysis']
    given={};issues=[]
    for item in entries:
        if not isinstance(item,dict): issues.append('invalid_rubric_entry');continue
        key=str(item.get('criterion_id',''))
        if key in given: issues.append('duplicate_criterion_in_label')
        given[key]=item
    expected_ids={c['id'] for c in criteria}
    if set(given)!=expected_ids:issues.append('rubric_criterion_ids_mismatch')
    scores=[]
    for c in criteria:
        try:
            v=float(given[c['id']]['awarded_score'])
            if not math.isfinite(v) or not -1e-6<=v<=c['max']+1e-6:raise ValueError()
            if c['allowed'] is not None and not any(math.isclose(v,a,abs_tol=1e-5) for a in c['allowed']):
                issues.append('label_invalid_scoring_anchor:'+c['id'])
            scores.append(v)
        except (ValueError,TypeError,KeyError):issues.append('invalid_label_score:'+c['id']);scores.append(None)
    return scores,issues

def scoring_guide(row):
    explicit = row.get('rubric_scoring_guide')
    if explicit and str(explicit).strip():
        return jload(explicit, explicit)
    criteria = jload(row.get('rubric_criteria'))
    if isinstance(criteria, list) and criteria and all(
        isinstance(c, dict) and isinstance(c.get('full_credit'), str)
        and c['full_credit'].strip() and isinstance(c.get('partial_credit'), str)
        and c['partial_credit'].strip() for c in criteria
    ):
        return [{'criterion_id': c.get('criterion_id'),
                 'full_credit': c['full_credit'], 'partial_credit': c['partial_credit']}
                for c in criteria]
    return None


def check_question(row, reference_texts):
    issues=[]
    qid=row.get('question_id','')
    question=row.get('question_text','')
    if not qid.strip():issues.append('missing_question_id')
    if not question.strip():issues.append('missing_question_text')
    if not str(row.get('solution','')).strip():issues.append('missing_solution')
    if not scoring_guide(row):issues.append('missing_scoring_guide')
    try: criteria=rubric(row)
    except (ValueError,TypeError) as ex:criteria=[];issues.append('invalid_rubric:'+str(ex))
    near=[]
    normalized=norm(question)
    for ref_id,ref_text in reference_texts:
        ratio=difflib.SequenceMatcher(None,normalized,norm(ref_text),autojunk=False).ratio()
        if ratio>=0.87:near.append({'reference_id':ref_id,'similarity':round(ratio,3)})
    near.sort(key=lambda x:-x['similarity'])
    if near:issues.append('high_text_similarity_to_reference')
    return criteria,issues,near[:3]

def check_answer(row, question, criteria):
    issues=[]
    if not row.get('answer_text','').strip():issues.append('missing_answer_text')
    if row.get('question_text') and norm(row['question_text'])!=norm(question.get('question_text')):
        issues.append('answer_question_text_mismatch')
    if row.get('rubric_criteria') and norm(row['rubric_criteria'])!=norm(question.get('rubric_criteria')):
        issues.append('answer_rubric_mismatch')
    original, problems=score_analysis(row,criteria)
    issues+=problems
    try:
        claimed=float(row.get('expected_score',''))
        if not math.isfinite(claimed):raise ValueError()
    except (ValueError,TypeError):claimed=None;issues.append('invalid_expected_score')
    if original is not None and all(v is not None for v in original) and claimed is not None:
        if not math.isclose(sum(original),claimed,abs_tol=1e-5):issues.append('expected_score_sum_mismatch')
    limit=sum(c['max'] for c in criteria)
    if claimed is not None and not 0<=claimed<=limit:issues.append('expected_score_out_of_range')
    kind=norm(row.get('sample_type',''))
    if claimed is not None and kind=='partial' and not 0<claimed<limit:issues.append('partial_score_not_partial')
    if claimed is not None and kind=='full' and not math.isclose(claimed,limit,abs_tol=1e-5):issues.append('full_score_not_full')
    if claimed is not None and kind=='wrong' and claimed != 0:issues.append('wrong_sample_nonzero_credit')
    if kind not in ('full','partial','wrong'):issues.append('invalid_sample_type')
    if row.get('generation_target_status')=='mismatch':issues.append('generation_target_mismatch')
    if re.search(r'\b(synthetic answer|according to the rubric|i intentionally made|as an ai)\b',row.get('answer_text',''),re.I):
        issues.append('meta_student_response')
    return original,claimed,issues

def call_codex(payload, instruction, schema, path, executable):
    if not shutil.which(executable):raise RuntimeError(f'{executable} not found. Install/authenticate Codex CLI, or use --dry-run.')
    prompt=(instruction+'\nINPUT_JSON:\n'+json.dumps(payload,ensure_ascii=False))
    cmd=[executable,'exec','--ephemeral','--skip-git-repo-check','--sandbox','read-only','--output-schema',str(schema),'-o',str(path),'-']
    path.parent.mkdir(parents=True,exist_ok=True)
    res=subprocess.run(cmd,input=prompt,text=True,encoding='utf-8',capture_output=True,cwd=BASE)
    if res.returncode:raise RuntimeError('Codex CLI failed: '+res.stderr[-2500:])
    try:return json.loads(path.read_text(encoding='utf-8'))
    except (OSError,ValueError) as err:raise RuntimeError('Invalid Codex JSON: '+str(err))

QUESTION_INSTRUCTIONS='''You are a university mathematics/engineering exam audit reviewer, NOT a question generator.
Assess the generated question, its solution, and each rubric criterion. Independently solve/check the problem; do not assume the provided solution is correct. Check solvability, ambiguity, self-contained statement, conceptual alignment, difficulty plausibility, mathematical correctness of EACH solution step, rubric coverage and fair independent scoring. If reference questions are provided, assess mathematical originality beyond superficial number changes; if not, report originality as unverifiable. Do not claim web-based plagiarism checking. Answer in the required JSON shape. Use 0-4 for clarity, solvability, solution_correctness, rubric_alignment, originality (if no references, set originality=0 and add limitation). Return verdict pass/review/fail and concrete issues with cited mathematics, but do not rewrite the input. Do not access files or tools; use only INPUT_JSON.'''
ANSWER_INSTRUCTIONS='''You are an independent rubric grader and student response quality reviewer. Check each response AS WRITTEN against question, official solution and rubric. Treat official solution as a reference, accept mathematically equivalent methods; do not reward missing evidence. Preserve partial-credit anchors if listed. Report per criterion score with evidence, and overall student-like authenticity, meaningful mistake, answer/label match, and semantic overlap among provided answers. Do not force scores to be partial merely because input label says partial. Grade without using the provided expected_score (it is deliberately withheld). Detect copied/near-identical responses, rubric mentions and fabricated metacommentary. Return one evaluation per response_id in input order, with exact IDs and criterion IDs. If an answer is wrong or full, report actual score. Verdict pass/review/fail refers to validity of the student response and scoring evidence, not that it achieved the target label. No external files/tools. JSON only.'''

ANSWER_INSTRUCTIONS += ''' A valid dataset response can be FULL (all credit), PARTIAL (some credit), or WRONG (zero credit). An authentic student's mathematical mistake is expected data, not by itself a reason for a review/fail verdict. Use review/fail for ambiguous grading evidence, unsupported scores, inauthentic text, copying, or other dataset-quality problems. For a fully correct response meaningful_error=false is appropriate. Never repair student mistakes. Keep genuine uncertainty for review.'''


def training_rows(rows, question_report, answer_report, dry_run=False):
    if dry_run: return []
    good_questions={r['question_id'] for r in question_report
                    if r['ai_verdict']=='pass' and r['review_required']=='no'}
    good_answers={signature(r) for r in answer_report
                  if r['ai_verdict']=='pass' and r['review_required']=='no'}
    required=('question_id','response_id','question_text','solution','rubric_criteria',
              'rubric_max_score','answer_text','sample_type','expected_score','rubric_analysis')
    return [r for r in rows if r.get('question_id') in good_questions
            and signature(r) in good_answers and all(str(r.get(k) or '').strip() for k in required)
            and r.get('generation_target_status')!='mismatch']


def assess_question_response(result):
    dims=result.get('dimensions',{})
    for key in ('clarity','solvability','solution_correctness','rubric_alignment','originality'):
        if type(dims.get(key)) is not int or not 0<=dims[key]<=4: raise ValueError('invalid question dimension '+key)
    if result.get('verdict') not in ('pass','review','fail'):raise ValueError('invalid question verdict')
    if not isinstance(result.get('issues'),list):raise ValueError('invalid question issues')
    return result

def assess_answers_result(result, batch,criteria):
    evaluations=result.get('evaluations')
    if not isinstance(evaluations,list) or len(evaluations)!=len(batch):raise ValueError('evaluation count mismatch')
    if [e.get('response_id') for e in evaluations] != [r['response_id'] for r in batch]:raise ValueError('response IDs/order mismatch')
    ids=[c['id'] for c in criteria]
    parsed=[]
    for e in evaluations:
        grades=e.get('rubric_scores')
        if not isinstance(grades,list) or [x.get('criterion_id') for x in grades]!=ids:raise ValueError('criterion IDs mismatch')
        scores=[]
        for gr,c in zip(grades,criteria):
            v=float(gr['awarded_score'])
            if not math.isfinite(v) or v < 0 or v > c['max']+1e-6:raise ValueError('invalid adjudicated score')
            if c['allowed'] is not None and not any(math.isclose(v,a,abs_tol=1e-5) for a in c['allowed']):raise ValueError('invalid scoring anchor')
            if not str(gr.get('evidence','')).strip():raise ValueError('missing rubric evidence')
            scores.append(v)
        if e.get('verdict') not in ('pass','review','fail'):raise ValueError('invalid answer verdict')
        parsed.append((e,scores))
    return parsed

def input_questions(rows):
    grouped=defaultdict(list)
    for r in rows:
        if r.get('question_id'):grouped[r['question_id']].append(r)
    return {q: rr[0] for q,rr in grouped.items()},grouped

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--questions',type=Path,required=True,help='Generated questions CSV, may also contain student answers')
    parser.add_argument('--answers',type=Path,help='Generated student answers CSV; defaults to rows of --questions when answer_text exists')
    parser.add_argument('--references',type=Path,help='Original/reference question CSV for text novelty comparison')
    parser.add_argument('--out',type=Path,default=BASE/'output'/'evaluation')
    parser.add_argument('--max-questions',type=int)
    parser.add_argument('--max-answers',type=int,help='Per-question answer limit for pilot')
    parser.add_argument('--batch-size',type=int,default=8)
    parser.add_argument('--dry-run',action='store_true',help='Only deterministic checks, no model calls')
    parser.add_argument('--resume',action='store_true')
    parser.add_argument('--codex-bin',default='codex')
    args=parser.parse_args(argv)
    if args.batch_size<1:parser.error('--batch-size must be positive')
    fields,qrows=read_csv(args.questions)
    for key in ('question_id','question_text','rubric_criteria'):
        if key not in fields:parser.error('Missing question column: '+key)
    questions,grouped=input_questions(qrows)
    if not questions:parser.error('No question rows')
    if args.answers:
        afields,arows=read_csv(args.answers)
    else:afields,arows=fields,qrows if 'answer_text' in fields else []
    answer_source_fields=list(afields)
    reftexts=[]
    if args.references:
        _, refs=read_csv(args.references)
        reftexts=[(r.get('question_id',''),r.get('question_text','')) for r in refs if r.get('question_text')]
    inputs={'questions':sha_file(args.questions),'answers':sha_file(args.answers) if args.answers else None,'references':sha_file(args.references) if args.references else None}
    manifest_path=args.out/'manifest.json'
    if args.resume and manifest_path.exists():
        manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
        if manifest['hashes']!=inputs or manifest['batch_size']!=args.batch_size or manifest.get('evaluation_version')!=2:raise ValueError('Resume input/config mismatch; use a new --out folder')
    args.out.mkdir(parents=True,exist_ok=True)
    dump(manifest_path,{'hashes':inputs,'evaluation_version':2,'batch_size':args.batch_size,'dry_run':args.dry_run,'questions_total':len(questions),'answers_total':len(arows)})
    selected=list(questions)
    if args.max_questions is not None:selected=selected[:args.max_questions]
    count_by_q=Counter(r.get('question_id','') for r in arows)
    used_ids=Counter(r.get('response_id','') for r in arows if r.get('response_id'))
    question_report=[];answer_report=[];stage=args.out/'stages'
    for qid in selected:
        q=questions[qid]
        criteria,qissues,near=check_question(q,[(rid,text) for rid,text in reftexts if rid!=qid])
        for col in ('question_text','solution','rubric_criteria','rubric_scoring_guide','rubric_max_score'):
            vals={norm(r.get(col,'')) for r in grouped[qid]}
            if len(vals)>1:qissues.append('inconsistent_question_field:'+col)
        question_ai=None; qerr=''
        path=stage/(hashlib.sha256(qid.encode()).hexdigest()[:14]+'_question.json')
        if not args.dry_run and criteria and not any('invalid_rubric' in a for a in qissues):
            try:
                if args.resume and path.exists():question_ai=json.loads(path.read_text(encoding='utf-8'))
                else:
                    qp={k:q.get(k,'') for k in ('question_id','subject','topic','concept_tags','difficulty','question_type','question_text','solution','rubric_criteria','rubric_scoring_guide','rubric_max_score')}
                    qp['rubric_criteria']=jload(qp['rubric_criteria'],qp['rubric_criteria'])
                    qp['rubric_scoring_guide']=scoring_guide(q)
                    closest=sorted(((difflib.SequenceMatcher(None,norm(q.get('question_text','')),norm(t),autojunk=False).ratio(),rid,t) for rid,t in reftexts if rid!=qid),reverse=True)[:12]
                    qp['references']=[{'question_id':rid,'question_text':t} for _,rid,t in closest]
                    question_ai=call_codex(qp,QUESTION_INSTRUCTIONS,QSCHEMA,path,args.codex_bin)
                assess_question_response(question_ai)
            except (RuntimeError,ValueError,KeyError) as ex:qerr=str(ex);question_ai=None
        question_report.append({'question_id':qid,'subject':q.get('subject',''),'topic':q.get('topic',''),
             'deterministic_status':'flagged' if qissues else 'pass','deterministic_issues':' | '.join(qissues),
             'similar_reference_questions':json.dumps(near,ensure_ascii=False),
             'ai_verdict':question_ai.get('verdict','') if question_ai else '',
             'ai_dimensions':json.dumps(question_ai.get('dimensions',{}),ensure_ascii=False) if question_ai else '',
             'ai_issues':json.dumps(question_ai.get('issues',[]),ensure_ascii=False) if question_ai else '',
             'ai_summary':question_ai.get('summary','') if question_ai else '',
             'model_error':qerr,'review_required':'yes' if qissues or qerr or (question_ai and question_ai.get('verdict')!='pass') else ('not_assessed' if args.dry_run else 'no')})
        batch_rows=[r for r in arows if r.get('question_id')==qid]
        if args.max_answers is not None:batch_rows=batch_rows[:args.max_answers]
        for ix in range(0,len(batch_rows),args.batch_size):
            batch=batch_rows[ix:ix+args.batch_size]
            diagnostics=[]
            for r in batch:
                labels, claimed, issues=check_answer(r,q,criteria)
                if used_ids.get(r.get('response_id',''),0)>1: issues.append('duplicate_response_id')
                same=[b for b in batch_rows if b is not r and norm(b.get('answer_text'))==norm(r.get('answer_text'))]
                if same and r.get('answer_text','').strip():issues.append('duplicate_answer_text_within_question')
                diagnostics.append((labels,claimed,issues))
            evaluated=None;error=''
            path=stage/(hashlib.sha256(qid.encode()).hexdigest()[:14]+f'_answers_{ix:04d}.json')
            if not args.dry_run and criteria and q.get('solution','').strip() and all(r.get('response_id') for r in batch):
                try:
                    if args.resume and path.exists(): evaluated=json.loads(path.read_text(encoding='utf-8'))
                    else:
                        payload={'question_id':qid,'question_text':q.get('question_text',''), 'solution':q.get('solution',''),
                          'rubric_criteria':jload(q.get('rubric_criteria'),q.get('rubric_criteria')),
                          'rubric_scoring_guide':scoring_guide(q),
                          'student_responses':[{'response_id':r.get('response_id'),'answer_text':r.get('answer_text','')} for r in batch]}
                        evaluated=call_codex(payload,ANSWER_INSTRUCTIONS,ASCHEMA,path,args.codex_bin)
                    parsed=assess_answers_result(evaluated,batch,criteria)
                except (RuntimeError,ValueError,KeyError,TypeError) as ex:error=str(ex);parsed=[]
            else:parsed=[]
            for n,r in enumerate(batch):
                original,claimed,issues=diagnostics[n]
                ae,grade=parsed[n] if n<len(parsed) else (None,None)
                discrepancy=[]
                if grade is not None and original is not None:
                    for c,old,new in zip(criteria,original,grade):
                        if old is not None and not math.isclose(old,new,abs_tol=1e-5):discrepancy.append(c['id'])
                model_total=round(sum(grade),6) if grade is not None else None
                if claimed is not None and model_total is not None and not math.isclose(claimed,model_total,abs_tol=1e-5):issues.append('expected_score_vs_independent_grading')
                if discrepancy:issues.append('rubric_level_disagreement')
                if grade is None and not args.dry_run:issues.append('model_evaluation_unavailable')
                answer_report.append({'question_id':qid,'response_id':r.get('response_id',''),'sample_type':r.get('sample_type',''),
                     'expected_score':r.get('expected_score',''),'rubric_label_vector':json.dumps(original),
                     'independent_score':model_total if model_total is not None else '',
                     'independent_rubric_vector':json.dumps(grade) if grade is not None else '',
                     'disputed_criteria':';'.join(discrepancy),'deterministic_issues':' | '.join(issues),
                     'ai_verdict':ae.get('verdict','') if ae else '',
                     'authenticity_score':ae.get('authenticity_score','') if ae else '',
                     'is_meaningful_error':ae.get('meaningful_error','') if ae else '',
                     'ai_issues':json.dumps(ae.get('issues',[]),ensure_ascii=False) if ae else '',
                     'ai_rubric_evidence':json.dumps(ae.get('rubric_scores',[]),ensure_ascii=False) if ae else '',
                     'ai_feedback':ae.get('feedback','') if ae else '',
                     'model_error':error,'review_required':'yes' if issues or error or (ae and ae.get('verdict')!='pass') else ('not_assessed' if args.dry_run else 'no')})
        print('Checked',qid,'answers',len(batch_rows),flush=True)
    qfields=['question_id','subject','topic','deterministic_status','deterministic_issues','similar_reference_questions','ai_verdict','ai_dimensions','ai_issues','ai_summary','model_error','review_required']
    afields=['question_id','response_id','sample_type','expected_score','rubric_label_vector','independent_score','independent_rubric_vector','disputed_criteria','deterministic_issues','ai_verdict','authenticity_score','is_meaningful_error','ai_issues','ai_rubric_evidence','ai_feedback','model_error','review_required']
    write_csv(args.out/'question_evaluation.csv',question_report,qfields)
    write_csv(args.out/'answer_evaluation.csv',answer_report,afields)
    flagged_questions=[r for r in question_report if r['review_required']=='yes']
    flagged_answers=[r for r in answer_report if r['review_required']=='yes']
    candidates=training_rows(arows,question_report,answer_report,args.dry_run)
    write_csv(args.out/'training_candidates.csv',candidates,answer_source_fields)
    write_csv(args.out/'review_queue.csv',
         [{'entity':'question','question_id':r['question_id'],'response_id':'','reason':r['deterministic_issues']+' '+r['ai_issues']} for r in flagged_questions]+
         [{'entity':'answer','question_id':r['question_id'],'response_id':r['response_id'],'reason':r['deterministic_issues']+' '+r['ai_issues']} for r in flagged_answers],
         ['entity','question_id','response_id','reason'])
    report={'mode':'deterministic_only' if args.dry_run else 'deterministic_plus_codex_provisional',
        'question_count':len(question_report),'answer_count':len(answer_report),
        'training_candidate_count':len(candidates),
        'training_sample_types':dict(Counter(r['sample_type'].upper() for r in candidates)),
        'training_score_bands':dict(Counter(r.get('actual_score_band','unknown') for r in candidates)),
        'questions_flagged':len(flagged_questions),'answers_flagged':len(flagged_answers),
        'questions_not_model_assessed':sum(not r['ai_verdict'] for r in question_report),
        'answers_not_model_assessed':sum(not r['ai_verdict'] for r in answer_report),
        'label_score_disagreements':sum('expected_score_vs_independent_grading' in r['deterministic_issues'] for r in answer_report),
        'rubric_level_disagreements':sum(bool(r['disputed_criteria']) for r in answer_report),
        'limitations':['Model opinions are not independently verified ground truth',
                       'Text similarity is not a proof of plagiarism or mathematical equivalence',
                       'If reference questions are absent, originality cannot be validated',
                       'A pass is an evaluation recommendation, not automatic dataset approval']}
    dump(args.out/'summary.json',report)
    print(json.dumps(report,indent=2))
    return report

if __name__=='__main__':main()
