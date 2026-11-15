import importlib.util
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import parallel_dataset as runner


class ParallelTests(unittest.TestCase):
    def test_status_write_retries_transient_windows_lock(self):
        import tempfile
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as temp:
            destination=Path(temp)/'worker-0.json'
            runner.write_json(destination,{'status':'old'})
            real_replace=Path.replace
            calls=[]
            def locked_replace(source,target):
                calls.append(target)
                if len(calls)<=2:
                    self.assertEqual(runner.read_json(destination),{'status':'old'})
                    raise PermissionError('Windows sharing conflict')
                return real_replace(source,target)
            with patch.object(Path,'replace',locked_replace),patch.object(runner.time,'sleep') as sleep:
                runner.write_json(destination,{'status':'running'})
            self.assertEqual(len(calls),3)
            self.assertEqual(sleep.call_count,2)
            self.assertEqual(runner.read_json(destination),{'status':'running'})
            self.assertFalse(destination.with_suffix('.tmp').exists())

    def test_persistent_file_denial_still_fails(self):
        from unittest.mock import Mock,patch
        source=Mock()
        source.replace.side_effect=PermissionError('Permanent denial')
        with patch.object(runner.time,'sleep'),self.assertRaises(PermissionError):
            runner.replace_with_retry(source,Path('target'),attempts=3)
        self.assertEqual(source.replace.call_count,3)

    def test_unrelated_io_error_is_not_retried(self):
        from unittest.mock import Mock,patch
        source=Mock()
        source.replace.side_effect=FileNotFoundError('Missing temporary file')
        with patch.object(runner.time,'sleep') as sleep,self.assertRaises(FileNotFoundError):
            runner.replace_with_retry(source,Path('target'))
        sleep.assert_not_called()

    def test_200_subset_preserves_started_families_and_splits(self):
        from collections import Counter
        slots=[]
        for topic in range(10):
            for family in range(50):
                split='train' if family<40 else ('validation' if family<45 else 'test')
                for variant in range(2):
                    slots.append({'question_id':f'Q{len(slots):04d}', 'topic':str(topic),
                                  'family_id':f'{topic}_{family}', 'subtopic':str(family%5), 'split':split})
        priority=[s['question_id'] for s in slots[:15]]
        selected=runner.select_200(slots,priority)
        self.assertEqual(len(selected),200)
        self.assertEqual(set(Counter(s['topic'] for s in selected).values()),{20})
        self.assertEqual(Counter(s['split'] for s in selected),{'train':160,'validation':20,'test':20})
        self.assertEqual(set(Counter(s['family_id'] for s in selected).values()),{2})
        self.assertTrue(set(priority).issubset(s['question_id'] for s in selected))
        self.assertEqual(selected,runner.select_200(slots,priority))
        self.assertEqual([len(runner.shard(selected,i,5)) for i in range(5)],[40]*5)
        for slot in selected:self.assertIn(slot,slots)

    def test_five_shards_cover_plan_once(self):
        slots = list(range(1000))
        shards = [runner.shard(slots, i, 5) for i in range(5)]
        self.assertEqual([len(s) for s in shards], [200]*5)
        flattened = [q for s in shards for q in s]
        self.assertEqual(len(flattened), len(set(flattened)))
        self.assertEqual(sorted(flattened), slots)

    def test_merge_applies_global_duplicate_filter(self):
        fields = ['question_id','response_id','answer_text','expected_score','split','family_id']
        good = dict(zip(fields,['Q1','R1','คำตอบ','2.5','train','F1']))
        duplicate_question = dict(good,question_id='Q2',response_id='R2')
        headers, rows = runner.merge_rows([(fields,[good,duplicate_question])], {'Q1'})
        self.assertEqual(headers,fields)
        self.assertEqual(rows,[good])

    def test_merge_rejects_duplicate_response_identity(self):
        row = {'question_id':'Q1','response_id':'R1'}
        with self.assertRaisesRegex(ValueError,'Duplicate'):
            runner.merge_rows([(list(row),[row,row])],{'Q1'})
    def test_data_validation_is_not_a_provider_error(self):
        self.assertTrue(runner.validation_failure({'questions':[{'status':'failed','error_type':'ValueError'}]}))
        self.assertFalse(runner.validation_failure({'questions':[{'status':'failed','error_type':'RuntimeError'}]}))
        self.assertFalse(runner.validation_failure({'questions':[]}))

    def test_checkpoint_skips_completed_job(self):
        import tempfile
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as temp:
            output=Path(temp)
            slot={'question_id':'Q1'}
            runner.write_json(output/'manifest.json',{'workers':5,'source_fingerprint':'test','config':{},'slots':[slot]})
            runner.write_json(output/'jobs/Q1/done.json',{'status':'evaluated'})
            with patch.object(runner,'OUTPUT',output), patch.object(runner,'source_fingerprint',return_value='test'), \
                 patch.object(runner,'bootstrap_auth'), patch.object(runner,'bulk_module') as bulk:
                self.assertEqual(runner.worker(0,5),0)
                bulk.return_value.generate.assert_not_called()
            state=runner.read_json(output/'worker-0.json')
            self.assertEqual(state['completed'],1)
            self.assertEqual(state['status'],'finished')

    def test_stop_prevents_new_model_calls(self):
        import tempfile
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as temp:
            output=Path(temp)
            runner.write_json(output/'manifest.json',{'workers':5,'source_fingerprint':'test','config':{},'slots':[{'question_id':'Q1'}]})
            (output/'STOP').touch()
            with patch.object(runner,'OUTPUT',output), patch.object(runner,'source_fingerprint',return_value='test'), \
                 patch.object(runner,'bootstrap_auth'), patch.object(runner,'bulk_module') as bulk:
                self.assertEqual(runner.worker(0,5),1)
                bulk.return_value.generate.assert_not_called()


if __name__=='__main__':
    unittest.main()
