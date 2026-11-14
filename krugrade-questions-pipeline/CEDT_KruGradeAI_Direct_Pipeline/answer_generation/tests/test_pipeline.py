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


class CEDTDirectIntegrationTests(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.tmp=tempfile.TemporaryDirectory()
        self.csv=Path(self.tmp.name)/'all_in_one.csv'
        self.row={
            'question_id':'GEN_001','question_text':'Find x',
            'solution':'PRIVATE OFFICIAL ANSWER', 'rubric_max_score':'2',
            'rubric_criteria':json.dumps([
                {'criterion_id':'GEN_001_R1','max_points':1,'criterion':'Setup','full_credit':'right setup','partial_credit':'0.5 for incomplete setup'},
                {'criterion_id':'GEN_001_R2','max_points':1,'criterion':'Conclusion','full_credit':'right conclusion','partial_credit':'0.5 for minor error'}
            ]), 'topic':'Signals'
        }
        import csv
        with self.csv.open('w',encoding='utf-8',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(self.row));w.writeheader();w.writerow(self.row)
    def tearDown(self): self.tmp.cleanup()
    def test_question_csv_without_answer_columns(self):
        fields,rows=m.read_csv(self.csv)
        self.assertIn('answer_text',fields)
        self.assertIn('response_id',fields)
        self.assertEqual(rows[0]['answer_text'],'')
        self.assertEqual(len(m.get_questions(rows)),1)
        guide=m.scoring_guide(rows[0]);self.assertEqual(guide[0]['full_credit'],'right setup')
        blind=m.generation_payload('GEN_001',rows,5)
        self.assertNotIn('solution',blind)
        self.assertNotIn('PRIVATE OFFICIAL ANSWER',json.dumps(blind))
        self.assertEqual(blind['existing_partial_examples'],[])
    def test_native_graded_export(self):
        fields,rows=m.read_csv(self.csv)
        sample=[{'answer_text':'Some correct working but incorrect conclusion','error_pattern':'wrong conclusion'}]
        rubric=m.criteria_for(rows[0]);self.assertEqual(len(rubric),2)
        response={'evaluations':[{'rubric_scores':[
            {'criterion_id':'GEN_001_R1','awarded_score':1,'reasoning':'Setup is correct'},
            {'criterion_id':'GEN_001_R2','awarded_score':0,'reasoning':'Incorrect conclusion'}],
            'missed_concepts':['conclusion'],'error_categories':['interpretation'],
            'error_location':'last step','grader_feedback':'Setup correct','improvement_suggestion':'Fix conclusion'}]}
        grades=m.score_evaluations(response,sample,rubric,'GEN_001')
        out=m.build_rows(fields,{'GEN_001':rows},'GEN_001',sample,grades,set())
        self.assertEqual(out[0]['sample_type'],'PARTIAL')
        self.assertEqual(out[0]['expected_score'],'1.0')
        self.assertEqual(out[0]['solution'],'PRIVATE OFFICIAL ANSWER')
        self.assertEqual(out[0]['adjudication_status'],'not_required')
        self.assertEqual(out[0]['label_review_status'],'unreviewed')
