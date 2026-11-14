import importlib.util, json, unittest
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'pipeline'/'run.py'
spec=importlib.util.spec_from_file_location('runner',p); m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.row={'question_id':'Q1','question_text':'Compute x','rubric_criteria':json.dumps([{'criterion_id':'C1','max_score':1},{'criterion_id':'C2','max_score':1}]),'rubric_scoring_guide':'Score independently','rubric_max_score':'2','solution':'secret solution','sample_type':'partial','answer_text':'old answer','response_id':'old1','expected_score':'1','rubric_analysis':'[]'}
    def test_blind_no_solution(self):
        g=m.generation_payload('Q1',[self.row],5)
        self.assertNotIn('solution',g)
        self.assertNotIn('secret solution',m.generation_prompt(g))
        self.assertEqual(g['requested_count'],5)
    def test_criteria(self):self.assertEqual(len(m.criteria_for(self.row)),2)
    def test_duplicate(self):
        with self.assertRaises(ValueError):m.validate_generation({'samples':[{'answer_text':'old answer','error_pattern':'sign'}]},1,[self.row])
    def test_grade(self):
        e={'rubric_scores':[{'criterion_id':'C1','awarded_score':1,'reasoning':'Evidence'},{'criterion_id':'C2','awarded_score':0,'reasoning':'Missing'}], 'missed_concepts':['calculation'],'error_categories':['omission'],'error_location':'step 2','grader_feedback':'Correct first step','improvement_suggestion':'Finish step 2'}
        s=m.score_evaluations({'evaluations':[e]},[{'answer_text':'test'}],m.criteria_for(self.row),'Q1')
        self.assertEqual(s[0]['total'],1)
        self.assertEqual(s[0]['covered'],['C1']);self.assertEqual(s[0]['missed'],['C2'])
    def test_full_not_partial(self):
        e={'rubric_scores':[{'criterion_id':x,'awarded_score':1,'reasoning':'Evidence'} for x in ('C1','C2')], 'missed_concepts':[],'error_categories':[],'error_location':'n/a','grader_feedback':'ok','improvement_suggestion':'ok'}
        with self.assertRaises(ValueError):m.score_evaluations({'evaluations':[e]},[{}],m.criteria_for(self.row),'Q1')
if __name__=='__main__':unittest.main()
