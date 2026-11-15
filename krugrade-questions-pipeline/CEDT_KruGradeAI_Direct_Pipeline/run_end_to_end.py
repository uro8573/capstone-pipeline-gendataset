#!/usr/bin/env python3
"""Directly pass native Question Generation all_in_one.csv to Answer Generation.
No adapter or intermediate schema conversion file is used.
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
DEFAULT_INPUT=ROOT/'question_generation'/'output'/'dataset'/'all_in_one.csv'

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--question-csv',type=Path,default=DEFAULT_INPUT)
    ap.add_argument('--out',type=Path,default=ROOT/'answer_generation'/'output'/'cedt')
    ap.add_argument('--count',type=int,default=5)
    ap.add_argument('--mode',choices=['balanced','partial'],default='balanced')
    ap.add_argument('--max-questions',type=int)
    ap.add_argument('--dry-run',action='store_true')
    ap.add_argument('--resume',action='store_true')
    ap.add_argument('--rebuild-questions',action='store_true',help='Run question pipeline first, from its source inputs')
    args=ap.parse_args()
    if args.rebuild_questions:
        subprocess.run([sys.executable,str(ROOT/'question_generation'/'run_pipeline.py'),'run'],cwd=ROOT/'question_generation',check=True)
    if not args.question_csv.is_file():
        ap.error(f'Question CSV not found: {args.question_csv}')
    cmd=[sys.executable,str(ROOT/'answer_generation'/'pipeline'/'run.py'),
         '--input',str(args.question_csv.resolve()),'--out',str(args.out.resolve()),'--count',str(args.count),'--mode',args.mode]
    if args.max_questions is not None: cmd.extend(['--max-questions',str(args.max_questions)])
    if args.dry_run: cmd.append('--dry-run')
    if args.resume: cmd.append('--resume')
    return subprocess.call(cmd)

if __name__=='__main__': raise SystemExit(main())
