import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pipeline'))
from evaluate import rubric,check_answer,check_question,assess_answers_result,score_analysis,scoring_guide,training_rows
import json
class Tests(unittest.TestCase):
    def setUp(self):
        self.row={'question_id':'Q1','question_text':'Find x','solution':'x=1','rubric_criteria':json.dumps([{'criterion_id':'C1','max_points':1,'scoring_levels':[{'score':0},{'score':0.5},{'score':1}]}]),'rubric_max_score':'1','rubric_scoring_guide':'Use anchors', 'response_id':'R1','answer_text':'x is about 1','sample_type':'PARTIAL','expected_score':'0.5','rubric_analysis':'[{"criterion_id":"C1","awarded_score":0.5}]'}
    def test_rubric_formats(self):
        cs=rubric(self.row);self.assertEqual(cs[0]['max'],1);self.assertIn(0.5,cs[0]['allowed'])
    def test_native_question_guidance(self):
        r=dict(self.row)
        r.pop('rubric_scoring_guide')
        c={'criterion_id':'C1','max_points':1,'full_credit':'Correct reasoning',
           'partial_credit':'Credit a valid intermediate step'}
        r['rubric_criteria']=json.dumps([c])
        self.assertEqual(check_question(r,[])[1],[])
        self.assertEqual(scoring_guide(r)[0]['partial_credit'],c['partial_credit'])
        c['partial_credit']=''
        r['rubric_criteria']=json.dumps([c])
        self.assertIn('missing_scoring_guide',check_question(r,[])[1])
    def test_explicit_guidance_takes_precedence(self):
        self.assertEqual(scoring_guide(self.row),'Use anchors')
    def test_score_sum(self):
        cs=rubric(self.row);self.assertEqual(check_answer(self.row,self.row,cs)[2],[])
    def test_bad_score(self):
        r=dict(self.row,expected_score='1');self.assertIn('expected_score_sum_mismatch',check_answer(r,self.row,rubric(r))[2])
    def test_reference_duplicate(self):
        cs,issues,near=check_question(self.row,[('OLD','Find x')]);self.assertIn('high_text_similarity_to_reference',issues)
    def test_model_scoring(self):
        result={'evaluations':[{'response_id':'R1','rubric_scores':[{'criterion_id':'C1','awarded_score':0.5,'evidence':'Approximation'}],'verdict':'review'}]}
        self.assertEqual(assess_answers_result(result,[self.row],rubric(self.row))[0][1],[0.5])
    def test_invalid_anchor(self):
        result={'evaluations':[{'response_id':'R1','rubric_scores':[{'criterion_id':'C1','awarded_score':0.3,'evidence':'Approximation'}],'verdict':'review'}]}
        with self.assertRaises(ValueError):assess_answers_result(result,[self.row],rubric(self.row))
    def test_wrong_means_zero(self):
        r=dict(self.row,sample_type='WRONG')
        self.assertIn('wrong_sample_nonzero_credit',check_answer(r,r,rubric(r))[2])
    def test_training_gate(self):
        q={'question_id':'Q1','ai_verdict':'pass','review_required':'no'}
        a=dict(q,response_id='R1')
        self.assertEqual(training_rows([self.row],[q],[a]),[self.row])
        self.assertEqual(training_rows([self.row],[q],[a],True),[])
        self.assertEqual(training_rows([self.row],[dict(q,review_required='yes')],[a]),[])
        self.assertEqual(training_rows([self.row],[q],[dict(a,review_required='yes')]),[])
        self.assertEqual(training_rows([dict(self.row,generation_target_status='mismatch')],[q],[a]),[])
        self.assertEqual(training_rows([dict(self.row,answer_text='')],[q],[a]),[])
    def test_cli_exports_complete_candidates_and_dry_run_none(self):
        import csv, tempfile
        from unittest.mock import patch
        import evaluate
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/'input.csv'; out=root/'evaluated'
            row=dict(self.row,split='train',family_id='F1',label_review_status='unreviewed')
            with source.open('w',encoding='utf-8',newline='') as f:
                writer=csv.DictWriter(f,fieldnames=list(row));writer.writeheader();writer.writerow(row)
            def judge(payload,instruction,schema,path,executable):
                if schema==evaluate.QSCHEMA:
                    return {'dimensions':dict.fromkeys(['clarity','solvability','solution_correctness','rubric_alignment','originality'],4),'verdict':'pass','issues':[]}
                self.assertNotIn('expected_score',json.dumps(payload))
                return {'evaluations':[{'response_id':'R1','rubric_scores':[{'criterion_id':'C1','awarded_score':0.5,'evidence':'Observed'}],'verdict':'pass','issues':[]}]}
            args=['--questions',str(source),'--out',str(out)]
            with patch.object(evaluate,'call_codex',side_effect=judge):
                report=evaluate.main(args)
            fields,rows=evaluate.read_csv(out/'training_candidates.csv')
            self.assertEqual(fields,list(row))
            self.assertEqual(rows,[row])
            self.assertEqual(report['training_candidate_count'],1)
            evaluate.main(args+['--dry-run'])
            self.assertEqual(evaluate.read_csv(out/'training_candidates.csv')[1],[])
if __name__=='__main__':unittest.main()
