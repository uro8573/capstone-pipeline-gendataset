"""Persistent cross-run duplicate screening; conservative heuristics, not semantic proof."""
from __future__ import annotations

import argparse
import csv
from difflib import SequenceMatcher
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import unicodedata


def normalized(text):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", text)).strip().casefold()


def structure(text):
    # Ignore numeric constants, retaining operators and variable names. This is
    # intentionally conservative: flagged items need review, not automatic deletion.
    return re.sub(r"(?<![\w])\d+(?:\.\d+)?(?:[eE][+-]?\d+)?", "<number>", text)


class QuestionRegistry:
    def __init__(self, path, threshold=0.9):
        if not 0 < threshold <= 1:
            raise ValueError("Duplicate threshold must be in (0, 1]")
        self.path = Path(path).resolve()
        self.threshold = threshold

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(self.path, timeout=30)
        try:
            self.db.execute("BEGIN IMMEDIATE")
            self.db.execute('''CREATE TABLE IF NOT EXISTS questions (
                run_id TEXT NOT NULL, question_id TEXT NOT NULL, question_text TEXT NOT NULL,
                normalized TEXT NOT NULL, structure TEXT NOT NULL, split TEXT NOT NULL,
                family_id TEXT NOT NULL, source TEXT NOT NULL,
                PRIMARY KEY (run_id, question_id))''')
            self.rows = [dict(zip(('run_id','question_id','question_text','normalized','structure','split','family_id','source'), row))
                         for row in self.db.execute("SELECT * FROM questions ORDER BY rowid")]
            return self
        except BaseException:
            self.db.close()
            raise

    def __exit__(self, kind, value, traceback):
        try:
            if kind is None:
                self.db.commit()
            else:
                self.db.rollback()
        finally:
            self.db.close()

    def check(self, run_id, question_id, text, split, family_id):
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Question text must be nonempty")
        clean = normalized(text)
        skeleton = structure(clean)
        for row in self.rows:
            own = row['run_id'] == run_id and row['question_id'] == question_id
            if own:
                if row['normalized'] == clean and row['split'] == split and row['family_id'] == family_id:
                    continue  # Idempotent export/resume, still compare against other records.
                return self.evidence('identity_conflict', 1.0, row, split)
            if clean == row['normalized']:
                return self.evidence('exact_duplicate', 1.0, row, split)
            if skeleton == row['structure']:
                return self.evidence('numeric_variant', 1.0, row, split)
            matcher = SequenceMatcher(None, clean, row['normalized'], autojunk=False)
            if matcher.quick_ratio() >= self.threshold:
                similarity = matcher.ratio()
                if similarity >= self.threshold:
                    return self.evidence('near_duplicate', similarity, row, split)
        return None

    @staticmethod
    def evidence(kind, similarity, row, split):
        return {'kind': kind, 'similarity': round(similarity, 6),
                'matched_run_id': row['run_id'], 'matched_question_id': row['question_id'],
                'matched_split': row['split'], 'matched_family_id': row['family_id'],
                'matched_source': row['source'], 'cross_split': row['split'] != split}

    def reserve(self, run_id, question_id, text, split, family_id, source):
        match = self.check(run_id, question_id, text, split, family_id)
        if match:
            return match
        row = {'run_id':run_id, 'question_id':question_id, 'question_text':text,
               'normalized':normalized(text), 'structure':structure(normalized(text)),
               'split':split, 'family_id':family_id, 'source':str(source)}
        cursor = self.db.execute("INSERT OR IGNORE INTO questions VALUES (?,?,?,?,?,?,?,?)", tuple(row.values()))
        if cursor.rowcount:
            self.rows.append(row)
        return None


def import_csv(registry_path, csv_path, dataset_id, threshold=0.9):
    report = {'accepted': 0, 'flagged': []}
    # Explicit dataset identity makes re-import safe if the source file is copied.
    run_id = 'import:' + dataset_id
    with QuestionRegistry(registry_path, threshold) as registry:
        with Path(csv_path).open(encoding='utf-8-sig', newline='') as stream:
            reader = csv.DictReader(stream)
            if not {'question_id', 'question_text'}.issubset(reader.fieldnames or []):
                raise ValueError('CSV requires question_id and question_text')
            for row in reader:
                if not row['question_id'].strip():
                    raise ValueError('Empty question_id in input CSV')
                match = registry.reserve(run_id, row['question_id'], row['question_text'],
                                         row.get('split') or 'unknown', row.get('family_id') or row['question_id'],
                                         str(Path(csv_path).resolve()))
                if match:
                    report['flagged'].append({'question_id': row['question_id'], **match})
                else:
                    report['accepted'] += 1
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--registry', required=True, type=Path)
    parser.add_argument('--dataset-id', required=True)
    parser.add_argument('--threshold', type=float, default=0.9)
    args = parser.parse_args()
    try:
        print(json.dumps(import_csv(args.registry, args.input, args.dataset_id, args.threshold), ensure_ascii=False, indent=2))
    except (ValueError, OSError, sqlite3.Error) as exc:
        parser.exit(1, str(exc) + '\n')


if __name__ == '__main__':
    main()
