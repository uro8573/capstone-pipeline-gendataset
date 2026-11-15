import csv
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('full_dataset', Path(__file__).resolve().parents[1] / 'run_full_dataset.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class ExportTests(unittest.TestCase):
    def export(self, rows):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        source = root / 'candidates.csv'
        with source.open('w', encoding='utf-8', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=['family_id', 'split', 'answer_text', 'expected_score'])
            writer.writeheader()
            writer.writerows(rows)
        return root, source

    def test_split_preserves_rows_and_scores(self):
        rows = [{'family_id':'F1','split':'train','answer_text':'คำตอบ','expected_score':'2.5'},
                {'family_id':'F2','split':'test','answer_text':'Wrong','expected_score':'0'}]
        root, source = self.export(rows)
        self.assertEqual(runner.split_candidates(source, root), {'train':1,'validation':0,'test':1})
        with (root / 'train.csv').open(encoding='utf-8-sig', newline='') as stream:
            self.assertEqual(list(csv.DictReader(stream)), [rows[0]])

    def test_rejects_family_leakage(self):
        root, source = self.export([{'family_id':'F1','split':'train'}, {'family_id':'F1','split':'test'}])
        with self.assertRaisesRegex(ValueError, 'crosses'):
            runner.split_candidates(source, root)

    def test_rejects_missing_split(self):
        root, source = self.export([{'family_id':'F1','split':''}])
        with self.assertRaisesRegex(ValueError, 'Missing'):
            runner.split_candidates(source, root)


if __name__ == '__main__':
    unittest.main()
