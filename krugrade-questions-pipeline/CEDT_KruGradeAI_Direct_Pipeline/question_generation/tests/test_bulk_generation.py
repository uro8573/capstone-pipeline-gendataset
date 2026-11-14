import copy
import json
from pathlib import Path
import tempfile
import unittest
import shutil
from unittest.mock import patch

import generate_dataset as bulk


class BulkTests(unittest.TestCase):
    def setUp(self):
        self.config = json.loads((bulk.ROOT / 'config/generation.university_math.json').read_text(encoding='utf-8'))

    def test_balanced_reproducible_plan_and_group_splits(self):
        slots = bulk.make_plan(self.config)
        self.assertEqual(slots, bulk.make_plan(self.config))
        self.assertEqual(len(slots), 1000)
        self.assertEqual(len({s['question_id'] for s in slots}), 1000)
        families = {}
        for slot in slots:
            families.setdefault(slot['family_id'], set()).add(slot['split'])
        self.assertTrue(all(len(v) == 1 for v in families.values()))
        self.assertEqual(bulk.Counter(s['split'] for s in slots), {'train':800,'validation':100,'test':100})
        for topic in self.config['topics']:
            rows = [s for s in slots if s['topic'] == topic['topic']]
            self.assertEqual(bulk.Counter(s['difficulty'] for s in rows), {'Easy':20,'Medium':50,'Hard':30})
            self.assertEqual(len({s['question_type'] for s in rows}), 6)

    def test_invalid_config(self):
        for key, value in [('variants_per_family',0), ('near_duplicate_threshold',2), ('topics',[])]:
            c = copy.deepcopy(self.config); c[key] = value
            with self.assertRaises(ValueError): bulk.make_plan(c)

    def test_prompt_isolation(self):
        slot = bulk.make_plan(self.config)[0]
        prior = {'questions':{'question_text':'QUESTION'},'solutions':{'solution':'SECRET'},'rubrics':{}}
        self.assertNotIn('SECRET', bulk.prompt('questions', slot, prior, self.config))
        self.assertNotIn('SECRET', bulk.prompt('solutions', slot, prior, self.config))
        self.assertIn('SECRET', bulk.prompt('review', slot, prior, self.config))

    def test_reject_bad_rubric(self):
        slot = bulk.make_plan(self.config)[0]
        with self.assertRaises(ValueError):
            bulk.check_result('rubrics', {'criteria':[{'max_points':float('nan')}]}, slot)

    def test_resume_export_duplicates_and_config_lock(self):
        c = copy.deepcopy(self.config)
        c['topics'] = [dict(c['topics'][0],count=3)]
        calls = []
        def fake(text, schema, destination, config, executable):
            stage = destination.stem
            context = json.loads(text.split('\n',1)[1]); slot = context['slot']
            calls.append(stage)
            if stage == 'questions': return {'question_id':slot['question_id'],'question_text':'Compute the derivative of x squared.'}
            if stage == 'solutions': return {'question_id':slot['question_id'],'solution':'Power rule gives 2x.','final_answer':'2x'}
            if stage == 'rubrics': return {'criteria':[{'criterion':'Power rule','max_points':slot['rubric_max_score'],'full_credit':'Correct derivative','partial_credit':'0 if incorrect','common_mistakes':'Wrong exponent'}]}
            return {'question_id':slot['question_id'],'status':'PASS','issues':[],'independent_checks_performed':'Differentiate polynomial'}
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            slots = bulk.prepare(c, out)
            with patch.object(bulk, 'call_model', side_effect=fake):
                bulk.generate(c, slots, out, 2, 'unused')
                self.assertEqual(len(calls),8)
                bulk.generate(c, slots, out, 2, 'unused')
                self.assertEqual(len(calls),12)
                bulk.generate(c, slots, out, 2, 'unused')
                self.assertEqual(len(calls),12)
            bulk.export(c, slots, out, out / "registry.sqlite3")
            summary=json.loads((out/'summary.json').read_text())
            self.assertEqual(summary['exported_provisional'],1)
            self.assertEqual(summary['review_or_incomplete'],2)
            rows=json.loads((out/'dataset/all_in_one.json').read_text())
            self.assertEqual(rows[0]['label_review_status'],'unreviewed')
            self.assertIn('family_id',rows[0])
            bulk.export(c, slots, out, out / 'registry.sqlite3')
            self.assertEqual(json.loads((out/'summary.json').read_text())['exported_provisional'],1)
            other = out / 'second_run'
            bulk.prepare(c, other)
            shutil.copytree(out / 'stages', other / 'stages')
            bulk.export(c, slots, other, out / 'registry.sqlite3')
            self.assertEqual(json.loads((other/'summary.json').read_text())['exported_provisional'],0)
            c['seed'] += 1
            with self.assertRaises(ValueError): bulk.prepare(c,out)

    def test_failed_stage_stops_and_resumes(self):
        c=copy.deepcopy(self.config);c['topics']=[dict(c['topics'][0],count=2)]
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp);slots=bulk.prepare(c,out)
            with patch.object(bulk,'call_model',side_effect=RuntimeError('quota')) as model:
                with self.assertRaises(RuntimeError): bulk.generate(c,slots,out,2,'unused')
                self.assertEqual(model.call_count,1)
            bulk.export(c,slots,out,out / "registry.sqlite3")
            self.assertEqual(json.loads((out/'summary.json').read_text())['exported_provisional'],0)


if __name__ == '__main__': unittest.main()
