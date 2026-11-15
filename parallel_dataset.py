"""Five isolated Docker shards, with a single host-side dataset exporter.

Workers own disjoint question IDs and only write their own stages/job folders.
The host exporter retains the original registry identity and applies cross-run
deduplication before publishing any response or training candidate.
"""
import argparse
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time

from run_full_dataset import ROOT, QUESTIONS, ANSWERS, EVAL, split_candidates

OUTPUT = ROOT / 'output/parallel_dataset'
QUESTION_OUTPUT = QUESTIONS / 'output/university_math_1000'


def now():
    return datetime.now(timezone.utc).isoformat()


def replace_with_retry(source, destination, attempts=40):
    """Windows bind mounts can briefly deny rename while a reader holds the file.

    Keep the old valid file until atomic replacement succeeds. Retry only access
    conflicts, for at most about 19 seconds; persistent failures remain errors.
    """
    for attempt in range(attempts):
        try:
            source.replace(destination)
            return
        except PermissionError:
            if attempt + 1 == attempts:
                raise
            time.sleep(min(0.05 * 2 ** min(attempt, 4), 0.5))


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    replace_with_retry(temporary, path)


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def exclusive(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    stream = path.open('a+b')
    if stream.tell() == 0:
        stream.write(b'0'); stream.flush()
    stream.seek(0)
    if os.name == 'nt':
        import msvcrt
        msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
    else:
        import fcntl
        fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    return stream


def bulk_module():
    sys.path.insert(0, str(QUESTIONS))
    spec = importlib.util.spec_from_file_location('parallel_bulk', QUESTIONS / 'generate_dataset.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def source_fingerprint():
    files = [Path(__file__), QUESTIONS / 'generate_dataset.py', QUESTIONS / 'pipeline/core.py',
             ANSWERS / 'pipeline/run.py', EVAL / 'pipeline/evaluate.py']
    return hashlib.sha256(b''.join(p.read_bytes() for p in files)).hexdigest()


def shard(slots, index, workers):
    if not 0 <= index < workers:
        raise ValueError('Invalid worker index')
    return slots[index::workers]


def select_200(slots, prioritized_ids=()):
    """Keep original IDs/families/splits; choose 20 questions in each of 10 topics."""
    topics={}
    for slot in slots:
        topics.setdefault(slot['topic'],{}).setdefault(slot['family_id'],[]).append(slot)
    if len(topics)!=10: raise ValueError('The 200-question subset requires ten source topics')
    priority=set(prioritized_ids)
    selected=set()
    for families in topics.values():
        coverage=Counter()
        for split,quota in (('train',8),('validation',1),('test',1)):
            candidates=[family for family in families.values() if family[0]['split']==split]
            if any(len(family)!=2 or any(s['split']!=split for s in family) for family in candidates):
                raise ValueError('Expected intact two-question families')
            chosen=[family for family in candidates if any(s['question_id'] in priority for s in family)]
            if len(chosen)>quota: raise ValueError('Started families exceed the requested split quota')
            for family in chosen: coverage[family[0]['subtopic']]+=1
            while len(chosen)<quota:
                remaining=[family for family in candidates if family not in chosen]
                if not remaining: raise ValueError('Insufficient families for subset')
                family=min(remaining,key=lambda f:(coverage[f[0]['subtopic']],f[0]['question_id']))
                chosen.append(family);coverage[family[0]['subtopic']]+=1
            selected.update(s['question_id'] for family in chosen for s in family)
    return [s for s in slots if s['question_id'] in selected]


def prepare(workers, refresh_code=False):
    bulk = bulk_module()
    config = read_json(QUESTIONS / 'config/generation.university_math.json')
    slots = bulk.prepare(config, QUESTION_OUTPUT)
    selection=OUTPUT / 'selection.json'
    if selection.exists():
        ids=set(read_json(selection)['question_ids'])
        slots=[s for s in slots if s['question_id'] in ids]
        if len(slots)!=len(ids): raise ValueError('Selected question IDs are not in the source plan')
    manifest = {'workers': workers, 'config': config, 'slots': slots,
                'source_fingerprint': source_fingerprint()}
    path = OUTPUT / 'manifest.json'
    if path.exists() and read_json(path) != manifest and (
        any(OUTPUT.glob('worker-*.json')) or any((OUTPUT / 'jobs').glob('*'))
    ):
        previous=read_json(path)
        states=[read_json(p) for p in OUTPUT.glob('worker-*.json')]
        same_plan=all(previous[k]==manifest[k] for k in ('workers','config','slots'))
        if not refresh_code or not same_plan or any(s['status']=='running' for s in states):
            raise ValueError('Parallel run identity changed; stop workers before an explicit code refresh')
        write_json(OUTPUT / ('deployment-' + str(time.time_ns()) + '.json'),
                   {'previous_fingerprint':previous['source_fingerprint'],
                    'new_fingerprint':manifest['source_fingerprint'],'updated_at':now()})
    write_json(path, manifest)
    print(json.dumps({'workers':workers, 'questions':len(slots),
                      'shard_sizes':[len(shard(slots,i,workers)) for i in range(workers)]}))


def bootstrap_auth():
    """Copy the read-only mounted login into each container's private tmp home."""
    target = Path(os.environ['CODEX_HOME'])
    target.mkdir(parents=True, exist_ok=True)
    shutil.copyfile('/run/secrets/codex_auth.json', target / 'auth.json')
    (target / 'auth.json').chmod(0o600)
    model = os.environ.get('KRUGRADE_MODEL', 'gpt-6-astra')
    effort = os.environ.get('KRUGRADE_REASONING', 'medium')
    (target / 'config.toml').write_text(
        f'model = {json.dumps(model)}\nmodel_reasoning_effort = {json.dumps(effort)}\napproval_policy = "never"\n',
        encoding='utf-8')


def resume(workers, refresh_code=False):
    with exclusive(OUTPUT / 'supervisor.lock'), exclusive(ROOT / 'output/full_dataset/run.lock'):
        states=[read_json(p) for p in OUTPUT.glob('worker-*.json')]
        if any(s['status']=='running' for s in states):
            raise ValueError('Workers are still active; wait for them to stop before resuming')
        prepare(workers,refresh_code)
        for index in range(workers):
            write_json(OUTPUT / f'worker-{index}.json',
                       {'worker':index,'status':'pending','phase':'resuming','updated_at':now()})
        (OUTPUT / 'STOP').unlink(missing_ok=True)


def reduce_to_200(workers):
    with exclusive(OUTPUT / 'supervisor.lock'), exclusive(ROOT / 'output/full_dataset/run.lock'):
        states=[read_json(p) for p in OUTPUT.glob('worker-*.json')]
        if any(s['status']=='running' for s in states):
            raise ValueError('Wait for workers to finish their current questions before resizing')
        old=read_json(OUTPUT / 'manifest.json')
        full=bulk_module().make_plan(old['config'])
        started={p.name for p in (QUESTION_OUTPUT / 'stages').iterdir()
                 if p.is_dir() and any(p.glob('*.json'))}
        selected=select_200(full,started)
        write_json(OUTPUT / ('plan-before-resize-'+str(time.time_ns())+'.json'),old)
        write_json(OUTPUT / 'selection.json',{'question_ids':[s['question_id'] for s in selected],
                   'target_questions':200,'topics':dict(Counter(s['topic'] for s in selected)),
                   'splits':dict(Counter(s['split'] for s in selected)),'updated_at':now()})
        new=dict(old,slots=selected,source_fingerprint=source_fingerprint())
        write_json(OUTPUT / 'manifest.json',new)
        for index in range(workers):
            write_json(OUTPUT / f'worker-{index}.json',{'worker':index,'status':'pending',
                       'phase':'resized_to_200','assigned':len(shard(selected,index,workers)),'updated_at':now()})
        (OUTPUT / 'STOP').unlink(missing_ok=True)
        print(json.dumps({'questions':len(selected),'responses_target':len(selected)*5,
                         'shards':[len(shard(selected,i,workers)) for i in range(workers)],
                         'splits':dict(Counter(s['split'] for s in selected))}))


def run_cli(command, cwd, log_path):
    with log_path.open('a', encoding='utf-8') as log:
        log.write('\nRUN ' + now() + '\n'); log.flush()
        process = subprocess.Popen([sys.executable, '-B', '-X', 'utf8', *command], cwd=cwd,
                                   stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        try:
            code = process.wait(timeout=1200)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait()
            raise RuntimeError('Model phase timed out; completed stages were retained')
    if code:
        raise RuntimeError(f'Phase exited {code}; inspect {log_path}')


class DataReviewRequired(Exception):
    pass


def validation_failure(report):
    failures=[q for q in report.get('questions',[]) if q.get('status')=='failed']
    return bool(failures) and all(q.get('error_type') in ('ValueError','KeyError','TypeError') for q in failures)


def worker(index, workers):
    with exclusive(OUTPUT / f'worker-{index}.lock'):
        return work_shard(index, workers)


def work_shard(index, workers):
    manifest = read_json(OUTPUT / 'manifest.json')
    if manifest['workers'] != workers or manifest['source_fingerprint'] != source_fingerprint():
        raise ValueError('Worker code/config does not match prepared run')
    bootstrap_auth()
    bulk = bulk_module()
    config = manifest['config']
    assigned = shard(manifest['slots'], index, workers)
    state = {'worker':index, 'assigned':len(assigned), 'completed':0, 'pid':os.getpid(),
             'status':'running', 'started_at':now(), 'container':os.environ.get('HOSTNAME','')}

    def update(**values):
        state.update(values); state['updated_at'] = now()
        write_json(OUTPUT / f'worker-{index}.json', state)

    update(phase='starting')
    for slot in assigned:
        if (OUTPUT / 'STOP').exists():
            update(status='stopped', phase='stop_requested')
            return 1
        qid = slot['question_id']
        job = OUTPUT / 'jobs' / qid
        marker = job / 'done.json'
        if marker.exists():
            state['completed'] += 1
            continue
        job.mkdir(parents=True, exist_ok=True)
        try:
            update(question_id=qid, phase='question_generation')
            bulk.generate(config, [slot], QUESTION_OUTPUT, 1, 'codex')
            original = QUESTION_OUTPUT / 'stages' / qid
            review = read_json(original / 'review.json')['result']
            if review['status'] != 'PASS' or review['issues']:
                write_json(marker, {'status':'question_review_required','question_id':qid,'finished_at':now()})
                state['completed'] += 1
                update(phase='question_review_required')
                continue
            # A per-question snapshot is immutable, so downstream resume hashes
            # remain valid as other workers add questions to the global dataset.
            local = job / 'question'
            destination = local / 'stages' / qid
            destination.mkdir(parents=True, exist_ok=True)
            for phase in bulk.STAGES:
                shutil.copyfile(original / (phase + '.json'), destination / (phase + '.json'))
            bulk.export(config, [slot], local, job / 'local_registry.sqlite3')
            question_csv = local / 'dataset/all_in_one.csv'
            answer_dir = job / 'answers'
            eval_dir = job / 'evaluation'
            update(phase='answer_generation_and_grading')
            try:
                run_cli(['pipeline/run.py','--input',str(question_csv),'--out',str(answer_dir),
                         '--mode','balanced','--count','5','--resume'], ANSWERS, job / 'answers.log')
            except RuntimeError as error:
                report_path=answer_dir / 'validation_report.json'
                if report_path.exists() and validation_failure(read_json(report_path)):
                    raise DataReviewRequired('Answer validation failed; inspect answers/validation_report.json') from error
                raise
            update(phase='independent_evaluation')
            run_cli(['pipeline/evaluate.py','--questions',str(question_csv),
                     '--answers',str(answer_dir / 'new_samples.csv'),
                     '--references',str(QUESTIONS / 'output/dataset/all_in_one.csv'),
                     '--out',str(eval_dir),'--resume'], EVAL, job / 'evaluation.log')
            summary = read_json(eval_dir / 'summary.json')
            if summary['questions_not_model_assessed'] or summary['answers_not_model_assessed']:
                raise RuntimeError('Evaluation model calls incomplete; inspect evaluation reports before resume')
            write_json(marker, {'status':'evaluated','question_id':qid,'finished_at':now(),
                                'summary':summary})
            state['completed'] += 1
            update(phase='question_finished')
        except Exception as error:
            if isinstance(error,DataReviewRequired) or isinstance(error.__cause__,(ValueError,KeyError,TypeError)):
                write_json(marker,{'status':'data_review_required','question_id':qid,
                                   'error':str(error),'finished_at':now()})
                state['completed'] += 1
                update(phase='data_review_required')
                continue
            update(status='error', error=str(error))
            # Stop other shards after their current job; do not retry quota
            # errors repeatedly or hide failed outputs.
            (OUTPUT / 'STOP').touch(exist_ok=True)
            raise
    update(status='finished', phase='finished')
    return 0


def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        return list(reader.fieldnames or []), list(reader)


def merge_rows(tables, accepted_ids):
    fields, merged, seen = [], [], set()
    for headers, rows in tables:
        for field in headers:
            if field not in fields: fields.append(field)
        for row in rows:
            if row.get('question_id') not in accepted_ids: continue
            key = (row['question_id'], row.get('response_id',''))
            if key in seen: raise ValueError('Duplicate response identity during merge: ' + str(key))
            seen.add(key); merged.append(row)
    return fields, merged


def write_csv(path, fields, rows):
    temporary = path.with_suffix('.tmp')
    with temporary.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)
    replace_with_retry(temporary, path)


def collect(manifest):
    """Only the host calls this, retaining Windows registry identities."""
    bulk = bulk_module()
    bulk.export(manifest['config'], manifest['slots'], QUESTION_OUTPUT)
    _, questions = read_csv(QUESTION_OUTPUT / 'dataset/all_in_one.csv')
    accepted = {r['question_id'] for r in questions}
    jobs = [p.parent for p in sorted((OUTPUT / 'jobs').glob('*/done.json'))
            if read_json(p)['status'] == 'evaluated']
    outputs = {'new_samples.csv':('answers','new_samples.csv'),
               'training_candidates.csv':('evaluation','training_candidates.csv'),
               'answer_evaluation.csv':('evaluation','answer_evaluation.csv'),
               'review_queue.csv':('evaluation','review_queue.csv')}
    counts = {}
    candidate_rows = []
    for name, parts in outputs.items():
        fields, rows = merge_rows([read_csv(job.joinpath(*parts)) for job in jobs], accepted)
        if name=='review_queue.csv':
            fields=['entity','question_id','response_id','reason']
            for marker in sorted((OUTPUT / 'jobs').glob('*/done.json')):
                result=read_json(marker)
                if result['status']!='evaluated' and result['question_id'] in {s['question_id'] for s in manifest['slots']}:
                    rows.append({'entity':'question','question_id':result['question_id'],
                                 'response_id':'','reason':result.get('error',result['status'])})
            _,question_queue=read_csv(QUESTION_OUTPUT / 'review_queue.csv')
            for row in question_queue:
                if row['reason'] not in ('incomplete_or_invalid','model_review'):
                    rows.append({'entity':'question','question_id':row['question_id'],
                                 'response_id':'','reason':row['reason']+': '+row['detail']})
        if not fields:
            fields = ['question_id','response_id','family_id','split','answer_text','expected_score']
        write_csv(OUTPUT / name, fields, rows)
        counts[name] = len(rows)
        if name == 'training_candidates.csv': candidate_rows = rows
    counts['splits'] = split_candidates(OUTPUT / 'training_candidates.csv', OUTPUT)
    counts['sample_types'] = dict(Counter(r['sample_type'].upper() for r in candidate_rows))
    counts['score_bands'] = dict(Counter(r.get('actual_score_band','unknown') for r in candidate_rows))
    counts['accepted_questions'] = len(accepted)
    return counts


def supervise(workers, once=False):
    manifest = read_json(OUTPUT / 'manifest.json')
    if manifest['workers'] != workers: raise ValueError('Worker count mismatch')
    lock = exclusive(OUTPUT / 'supervisor.lock')
    # Also block the former sequential runner from starting over these stages.
    sequential_lock = exclusive(ROOT / 'output/full_dataset/run.lock')
    previous = None
    counts = {}
    while True:
        states = [read_json(p) for p in sorted(OUTPUT.glob('worker-*.json'))]
        selected_ids={s['question_id'] for s in manifest['slots']}
        completed = sum(p.parent.name in selected_ids for p in (OUTPUT / 'jobs').glob('*/done.json'))
        failures = [s for s in states if s['status']=='error']
        if failures: (OUTPUT / 'STOP').touch(exist_ok=True)
        finished = len(states)==workers and all(s['status']=='finished' for s in states)
        stopped = len(states)==workers and all(s['status'] in ('error','stopped','finished') for s in states)
        if previous != completed or finished or stopped or once:
            counts = collect(manifest)
            previous = completed
        write_json(OUTPUT / 'status.json', {'status':'finished' if finished else ('stopped' if stopped else 'running'),
                   'pid':os.getpid(),'workers':workers,'completed_questions':completed,
                   'target_questions':len(manifest['slots']),'target_responses':len(manifest['slots'])*5,
                   'worker_states':states,'outputs':counts,'updated_at':now(),
                   'note':'Counts are provisional AI labels; final filtering can reduce coverage.'})
        if once or finished or stopped: return 1 if stopped and not finished else 0
        time.sleep(15)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['prepare','resume','reduce-to-200','worker','supervise','collect','auth-check'])
    parser.add_argument('--workers',type=int,default=5)
    parser.add_argument('--index',type=int)
    parser.add_argument('--refresh-code',action='store_true')
    args = parser.parse_args()
    if args.workers != 5: parser.error('This deployment is configured for exactly five workers')
    if args.command=='prepare': prepare(args.workers,args.refresh_code); return 0
    if args.command=='resume': resume(args.workers,args.refresh_code); return 0
    if args.command=='reduce-to-200': reduce_to_200(args.workers); return 0
    if args.command=='auth-check':
        bootstrap_auth()
        return subprocess.call(['codex','login','status'])
    if args.command=='worker':
        if args.index is None: parser.error('--index is required')
        return worker(args.index,args.workers)
    return supervise(args.workers,once=args.command=='collect')


if __name__=='__main__':
    raise SystemExit(main())
