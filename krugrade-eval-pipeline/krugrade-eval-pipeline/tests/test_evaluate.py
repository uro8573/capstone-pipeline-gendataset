import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pipeline'))
from evaluate import rubric,check_answer,check_question,assess_answers_result,score_analysis
import json
class Tests(unittest.TestCase):
    def setUp(self):
        self.row={'question_id':'Q1','question_text':'Find x','solution':'x=1','rubric_criteria':json.dumps([{'criterion_id':'C1','max_points':1,'scoring_levels':[{'score':0},{'score':0.5},{'score':1}]}]),'rubric_max_score':'1','rubric_scoring_guide':'Use anchors', 'response_id':'R1','answer_text':'x is about 1','sample_type':'PARTIAL','expected_score':'0.5','rubric_analysis':'[{"criterion_id":"C1","awarded_score":0.5}]'}
    def test_rubric_formats(self):
        cs=rubric(self.row);self.assertEqual(cs[0]['max'],1);self.assertIn(0.5,cs[0]['allowed'])
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
if __name__=='__main__':unittest.main()
