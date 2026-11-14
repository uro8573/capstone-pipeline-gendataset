import csv
from pathlib import Path
import tempfile
import unittest

from pipeline.question_registry import QuestionRegistry, import_csv


class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / 'registry.sqlite3'

    def tearDown(self):
        self.tmp.cleanup()

    def test_cross_run_exact_numeric_and_resume(self):
        with QuestionRegistry(self.path) as db:
            self.assertIsNone(db.reserve('run1','Q1','Integrate x + 2 on [0, 1].','train','F1','one'))
        with QuestionRegistry(self.path) as db:
            self.assertIsNone(db.reserve('run1','Q1','Integrate x + 2 on [0, 1].','train','F1','one'))
            self.assertEqual(len(db.rows),1)
            hit=db.reserve('run2','Q1','  INTEGRATE   x + 2 on [0, 1]. ','test','F2','two')
            self.assertEqual(hit['kind'],'exact_duplicate')
            self.assertTrue(hit['cross_split'])
            self.assertEqual(hit['matched_source'],'one')
            hit=db.reserve('run2','Q2','Integrate x + 7 on [0, 3].','test','F2','two')
            self.assertEqual(hit['kind'],'numeric_variant')
            self.assertEqual(len(db.rows),1)

    def test_changed_identity_and_split_fail_closed(self):
        with QuestionRegistry(self.path) as db:
            db.reserve('a','q','Find the rank of matrix A.','train','f','source')
            self.assertEqual(db.reserve('a','q','Different question','train','f','source')['kind'],'identity_conflict')
            self.assertEqual(db.reserve('a','q','Find the rank of matrix A.','test','f','source')['kind'],'identity_conflict')

    def test_near_duplicate_and_distinct(self):
        with QuestionRegistry(self.path,0.85) as db:
            db.reserve('a','q','Explain why the columns of an invertible square matrix are linearly independent.','train','f','source')
            hit=db.reserve('b','q','Explain why the columns of an invertible square matrix must be linearly independent.','train','g','source2')
            self.assertEqual(hit['kind'],'near_duplicate')
            self.assertIsNone(db.reserve('b','other','Compute the probability of drawing an ace from a deck.','test','z','source2'))

    def test_rollback_on_failure(self):
        with QuestionRegistry(self.path): pass
        with self.assertRaises(RuntimeError):
            with QuestionRegistry(self.path) as db:
                db.reserve('a','q','Calculate a derivative.','train','f','source')
                raise RuntimeError('export failed')
        with QuestionRegistry(self.path) as db:
            self.assertEqual(db.rows,[])

    def test_import_existing_csv_is_idempotent(self):
        source=Path(self.tmp.name)/'seed.csv'
        with source.open('w',newline='',encoding='utf-8') as f:
            writer=csv.DictWriter(f,fieldnames=['question_id','question_text'])
            writer.writeheader();writer.writerow({'question_id':'old1','question_text':'Prove the binomial theorem.'})
        self.assertEqual(import_csv(self.path,source,'old')['accepted'],1)
        self.assertEqual(import_csv(self.path,source,'old')['accepted'],1)
        with QuestionRegistry(self.path) as db:
            self.assertEqual(len(db.rows),1)
            hit=db.reserve('new','q','Prove the binomial theorem.','train','f','new')
            self.assertEqual(hit['matched_run_id'],'import:old')


if __name__ == '__main__': unittest.main()
