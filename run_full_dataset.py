"""Resume the full question -> balanced response -> evaluation dataset run.

Run with the same arguments to resume after a model/quota failure. Each phase
logs to output/full_dataset; no input datasets are overwritten.
"""
import argparse
import csv
import json
import os
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
DIRECT = ROOT / 'krugrade-questions-pipeline/CEDT_KruGradeAI_Direct_Pipeline'
QUESTIONS = DIRECT / 'question_generation'
ANSWERS = DIRECT / 'answer_generation'
EVAL = ROOT / 'krugrade-eval-pipeline/krugrade-eval-pipeline'


def save(path, value):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    temporary.replace(path)


def split_candidates(source, destination):
    with source.open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        fields, rows = reader.fieldnames, list(reader)
    families = {}
    for row in rows:
        split, family = row.get('split'), row.get('family_id')
        if split not in ('train', 'validation', 'test') or not family:
            raise ValueError('Missing family/split on training candidate')
        if family in families and families[family] != split:
            raise ValueError('Family crosses dataset splits: ' + family)
        families[family] = split
    counts = {}
    for split in ('train', 'validation', 'test'):
        selected = [r for r in rows if r['split'] == split]
        with (destination / (split + '.csv')).open('w', encoding='utf-8-sig', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=fields)
            writer.writeheader()
            writer.writerows(selected)
        counts[split] = len(selected)
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--codex-bin', default='codex')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    output = ROOT / 'output/full_dataset'
    question_output = QUESTIONS / 'output/university_math_1000'
    answer_output = ANSWERS / 'output/university_math_full'
    eval_output = EVAL / 'output/university_math_full'
    question_csv = question_output / 'dataset/all_in_one.csv'
    answers_csv = answer_output / 'new_samples.csv'
    config = json.loads((QUESTIONS / 'config/generation.university_math.json').read_text(encoding='utf-8'))
    total = sum(topic['count'] for topic in config['topics'])
    if args.dry_run:
        print(json.dumps({'questions': total, 'target_responses': total * 5,
                          'question_output': str(question_output), 'answer_output': str(answer_output),
                          'evaluation_output': str(eval_output), 'model_calls': 0}, indent=2))
        return 0
    output.mkdir(parents=True, exist_ok=True)
    # OS releases this lock even if the worker crashes. Prevent duplicate runs
    # from writing the same cached stages or consuming quota simultaneously.
    lock = (output / 'run.lock').open('a+b')
    if lock.tell() == 0:
        lock.write(b'0')
        lock.flush()
    lock.seek(0)
    try:
        if os.name == 'nt':
            import msvcrt
            msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        print('A full dataset run is already active.', file=sys.stderr)
        return 1
    state = {'pid': os.getpid(), 'status': 'running', 'target_questions': total,
             'target_responses': total * 5, 'started_at': datetime.now(timezone.utc).isoformat()}

    def update(**values):
        state.update(values)
        state['updated_at'] = datetime.now(timezone.utc).isoformat()
        save(output / 'status.json', state)

    def run(phase, folder, command):
        update(phase=phase)
        with (output / (phase + '.log')).open('a', encoding='utf-8') as log:
            log.write('\nRUN ' + datetime.now(timezone.utc).isoformat() + '\n')
            log.flush()
            result = subprocess.run([sys.executable, '-B', '-X', 'utf8', *command],
                                    cwd=folder, stdout=log, stderr=subprocess.STDOUT)
        if result.returncode:
            raise RuntimeError(f'{phase} exited {result.returncode}; inspect {phase}.log and resume this command')

    try:
        update(phase='questions')
        # Export every 20 newly processed questions; all four raw stages are
        # independently cached. Existing pilot stages are reused unchanged.
        while True:
            complete = sum(json.loads(p.read_text(encoding='utf-8')).get('status') == 'complete'
                           for p in (question_output / 'stages').glob('*/status.json'))
            update(completed_question_stages=complete)
            if complete >= total:
                break
            try:
                run('questions', QUESTIONS, ['generate_dataset.py', 'generate', '--out', str(question_output),
                    '--limit', '20', '--codex-bin', args.codex_bin])
            except RuntimeError:
                # Materialize completed results even when the provider stops.
                run('question_checkpoint', QUESTIONS, ['generate_dataset.py', 'export', '--out', str(question_output)])
                raise
        run('question_export', QUESTIONS, ['generate_dataset.py', 'export', '--out', str(question_output)])
        question_summary = json.loads((question_output / 'summary.json').read_text(encoding='utf-8'))
        update(exported_questions=question_summary['exported_provisional'])
        if not question_summary['exported_provisional']:
            raise RuntimeError('No accepted questions available for answer generation')
        run('answers', ANSWERS, ['pipeline/run.py', '--input', str(question_csv), '--out', str(answer_output),
            '--mode', 'balanced', '--count', '5', '--resume', '--codex-bin', args.codex_bin])
        run('evaluation', EVAL, ['pipeline/evaluate.py', '--questions', str(question_csv),
            '--answers', str(answers_csv), '--references', str(QUESTIONS / 'output/dataset/all_in_one.csv'),
            '--out', str(eval_output), '--resume', '--codex-bin', args.codex_bin])
        summary = json.loads((eval_output / 'summary.json').read_text(encoding='utf-8'))
        split_counts = split_candidates(eval_output / 'training_candidates.csv', output)
        # Model failures can be reported in CSV even when evaluator exits zero.
        incomplete = summary['questions_not_model_assessed'] or summary['answers_not_model_assessed']
        update(status='needs_resume' if incomplete else 'finished', phase='finished',
               evaluation=summary, candidate_split_counts=split_counts,
               candidates=str(eval_output / 'training_candidates.csv'),
               note='Finished means processed, not quota fulfilled or human-verified labels.')
        return 1 if incomplete else 0
    except Exception as error:
        update(status='stopped', error=str(error))
        print(str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
