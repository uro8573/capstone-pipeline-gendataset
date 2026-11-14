"""Stage-isolated ChatGPT prompts. Never leak gold solutions into question prompts."""
from __future__ import annotations
import json
from collections import defaultdict
from pathlib import Path
from .core import json_dump, normalize_row

CONVENTIONS = (
    "CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). "
    "DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. "
    "Use LaTeX mathematical notation and preserve the target university midterm level."
)


def as_json(item: dict) -> str:
    return json.dumps(item, ensure_ascii=False, indent=2)


def prompt_for(stage: str, slot: dict, data: dict) -> str:
    qid = slot["question_id"]
    qmap = {q["question_id"]: normalize_row(q) for q in data["questions"]}
    smap = {s["question_id"]: normalize_row(s) for s in data["solutions"]}
    rm = defaultdict(list)
    for rubric in data["rubrics"]:
        rm[rubric["question_id"]].append(normalize_row(rubric))
    instruction = f"Question slot: {qid}\nMathematical conventions: {CONVENTIONS}\n"
    if stage == "questions":
        return (
            "ROLE: University mathematics examination writer. Generate exactly ONE ORIGINAL question. "
            "Follow the approved blueprint slot. Change mathematical structure, representation, constraints, "
            "or reasoning requirement; changing numbers only is prohibited. Do not introduce unsupported topics. "
            "Do not show official reference solutions or simulated student answers. "
            "Return ONLY a JSON object with question_id, question_text, question_type, learning_objective, "
            "topic, subtopic, difficulty, concept_tags, reference_question_ids, rubric_max_score. "
            "Keep rubric_max_score consistent with the slot.\n"
            + instruction + "BLUEPRINT SLOT:\n" + as_json(slot)
        )
    if stage == "solutions":
        return (
            "ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any "
            "previous/official solution. Check assumptions, boundary cases, signs, indices and final result; "
            "perform a second verification method if practical. If ambiguous or inconsistent, explain it rather "
            "than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, "
            "mathematical_review_notes.\n" + instruction + "QUESTION ONLY (NO GOLD ANSWER):\n"
            + as_json(qmap[qid])
        )
    if stage == "rubrics":
        return (
            "ROLE: Math grading-rubric designer. Split the solution into independently observable criteria "
            "with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. "
            "Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing "
            "question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, "
            "partial_credit, common_mistakes, reference_question_ids.\n"
            + instruction + "QUESTION:\n" + as_json(qmap[qid])
            + "\nSOLUTION:\n" + as_json(smap[qid])
        )
    if stage == "review":
        return (
            "ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical "
            "algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and "
            "meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. "
            "Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, "
            "independent_checks_performed.\n"
            + instruction + "BLUEPRINT SLOT:\n" + as_json(slot)
            + "\nQUESTION:\n" + as_json(qmap[qid])
            + "\nGOLD SOLUTION (REVIEW STAGE ONLY):\n" + as_json(smap[qid])
            + "\nRUBRIC:\n" + as_json(rm[qid])
        )
    raise ValueError(f"Unknown stage: {stage}")


def write_packets(blueprint: dict, data: dict, dest: Path, stages: tuple[str, ...] = ("questions", "solutions", "rubrics", "review")) -> dict:
    counts = {}
    for stage in stages:
        stage_dir = dest / stage
        stage_dir.mkdir(parents=True, exist_ok=True)
        manifest = []
        for slot in blueprint["slots"]:
            qid = slot["question_id"]
            filename = f"{qid}_{stage}.md"
            text = prompt_for(stage, slot, data)
            (stage_dir / filename).write_text(text + "\n", encoding="utf-8")
            manifest.append({"question_id": qid, "file": filename})
        json_dump(stage_dir / "manifest.json", manifest)
        counts[stage] = len(manifest)
    return counts
