import copy
import csv
import json
import tempfile
import unittest
from pathlib import Path
from pipeline.core import (
    read_sources, validate, export_all, make_blind_dataset, build_combined, build_blueprint,
)
from pipeline.prompting import prompt_for

ROOT = Path(__file__).resolve().parents[1]

class PipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = read_sources(ROOT / "input" / "source")
        cls.blueprint = json.loads((ROOT / "config" / "blueprint.json").read_text(encoding="utf-8"))

    def test_original_seed_structural_validation(self):
        report = validate(self.source, self.blueprint)
        self.assertEqual(report["status"], "PASS", report["errors"])
        self.assertEqual(report["questions"], 30)
        self.assertEqual(report["rubric_criteria"], 141)
        self.assertEqual(report["rubric_score_total"], 190)
        self.assertEqual(report["independent_mathematical_review"], "NOT_PERFORMED")

    def test_corrupted_score_is_rejected(self):
        broken = copy.deepcopy(self.source)
        broken["rubrics"][0]["max_points"] = "1000"
        report = validate(broken, self.blueprint)
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(any("Rubric total mismatch GEN_001" in e for e in report["errors"]))

    def test_duplicate_id_is_rejected(self):
        broken = copy.deepcopy(self.source)
        broken["questions"][1]["question_id"] = "GEN_001"
        report = validate(broken, self.blueprint)
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(any("Duplicate IDs" in e for e in report["errors"]))

    def test_blind_has_no_gold_keys(self):
        with tempfile.TemporaryDirectory() as t:
            out = Path(t)
            make_blind_dataset(self.source, out)
            self.assertFalse((out / "solutions.json").exists())
            payload = json.loads((out / "blind_generation_inputs.json").read_text(encoding="utf-8"))
            self.assertEqual(len(payload), 30)
            for record in payload:
                self.assertNotIn("solution", record)
                self.assertNotIn("final_answer", record)
                self.assertEqual(sorted(record), sorted(["question_id", "question_text", "rubric_max_score", "rubric_criteria"]))

    def test_question_prompts_do_not_embed_existing_solutions(self):
        slot = self.blueprint["slots"][0]
        text = prompt_for("questions", slot, self.source)
        self.assertIn("GEN_001", text)
        self.assertNotIn(self.source["solutions"][0]["solution"], text)
        solution_stage = prompt_for("solutions", slot, self.source)
        self.assertNotIn(self.source["solutions"][0]["solution"], solution_stage)
        review_stage = prompt_for("review", slot, self.source)
        self.assertIn(json.dumps(self.source["solutions"][0]["solution"], ensure_ascii=False)[1:-1], review_stage)

    def test_csv_json_roundtrip(self):
        with tempfile.TemporaryDirectory() as t:
            out = Path(t)
            report = validate(self.source, self.blueprint)
            export_all(self.source, out, report)
            with (out / "questions.csv").open(encoding="utf-8-sig",newline="") as f:
                csv_rows=list(csv.DictReader(f))
            json_rows=json.loads((out / "questions.json").read_text(encoding="utf-8"))
            joined=json.loads((out / "all_in_one.json").read_text(encoding="utf-8"))
            self.assertEqual(len(csv_rows),len(json_rows))
            self.assertEqual(len(joined),30)
            self.assertEqual(csv_rows[0]["question_text"],json_rows[0]["question_text"])
            self.assertEqual(len(joined[0]["rubric_criteria"]),5)
            self.assertEqual(len({x["question_id"] for x in joined}),30)

    def test_blueprint_copy_matches_saved(self):
        bp = build_blueprint(self.source)
        self.assertEqual(bp["slots"], self.blueprint["slots"])

if __name__ == "__main__":
    unittest.main()
