"""Deterministic exam-dataset validation, transformation and generation packets.

No model call is made by this module. Mathematical correctness is NOT inferred
from an earlier AI-generated PASS label.
"""
from __future__ import annotations

import csv
import json
import hashlib
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

TOPIC_TARGET = {
    "Fourier Transform & Sampling": 4,
    "Linear / Circular Convolution": 4,
    "Fourier Series": 3,
    "CTFT Convolution Identity": 4,
    "Inverse DTFT": 4,
    "DFT & DTFS": 4,
    "First-Order Frequency Response": 4,
    "LTI Inverse & Echo Cancellation": 3,
}
DIFFICULTY_TARGET = {"Medium": 19, "Hard": 11}
LIST_FIELDS = {"reference_question_ids", "concept_tags", "expected_methods"}
TABLES = ("questions", "solutions", "rubrics", "metadata")
QUESTION_REQUIRED = ("question_id", "subject", "topic", "subtopic", "difficulty", "question_type", "learning_objective", "question_text")
SOLUTION_REQUIRED = ("question_id", "solution", "final_answer")
RUBRIC_REQUIRED = ("question_id", "criterion_id", "rubric_order", "criterion", "max_points", "full_credit", "partial_credit")
META_REQUIRED = ("question_id", "reference_question_ids", "concept_tags", "variation_strategy", "generation_rationale")


def read_csv(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_sources(source: Path) -> dict[str, list[dict[str, Any]]]:
    return {table: read_csv(source / f"{table}.csv") for table in TABLES}


def parse_list(value: Any) -> list:
    if isinstance(value, list):
        return value
    if value is None or value == "":
        return []
    try:
        result = json.loads(value)
    except (ValueError, TypeError):
        return [str(value)]
    return result if isinstance(result, list) else [result]


def normalize_row(row: dict) -> dict:
    clean = dict(row)
    for k in LIST_FIELDS:
        if k in clean:
            clean[k] = parse_list(clean[k])
    if "rubric_order" in clean:
        clean["rubric_order"] = int(clean["rubric_order"])
    for k in ("rubric_max_score", "max_points"):
        if k in clean:
            clean[k] = float(clean[k])
    return clean


def json_dump(path: Path, content: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
        f.write("\n")


def csv_dump(path: Path, rows: list[dict], preferred_headers: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    keys = list(preferred_headers or [])
    for row in rows:
        for key in row:
            if key not in keys:
                keys.append(key)
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else ("" if v is None else v) for k, v in row.items()})


def build_blueprint(data: dict[str, list[dict]]) -> dict:
    questions = {r["question_id"]: r for r in data["questions"]}
    slots = []
    for row in sorted(data["metadata"], key=lambda r: r["question_id"]):
        q = questions.get(row["question_id"], {})
        fields = (
            "question_id", "reference_question_ids", "subject", "topic", "subtopic", "concept_tags",
            "learning_objective", "question_type", "difficulty", "expected_methods", "variation_strategy",
        )
        record = {k: q.get(k, row.get(k, "")) if k not in ("expected_methods", "variation_strategy") else row.get(k, "") for k in fields}
        record["rubric_max_score"] = float(q.get("rubric_max_score", row.get("rubric_max_score", 0)))
        for field in LIST_FIELDS:
            if field in record:
                record[field] = parse_list(record[field])
        slots.append(record)
    return {
        "blueprint_version": "1.0",
        "source_note": "Inferred from a solutions-and-rubric reference PDF; not independently confirmed original questions.",
        "target_question_count": len(slots),
        "target_total_score": sum(s["rubric_max_score"] for s in slots),
        "topic_distribution": dict(Counter(s["topic"] for s in slots)),
        "difficulty_distribution": dict(Counter(s["difficulty"] for s in slots)),
        "slots": slots,
    }


def validate(data: dict[str, list[dict]], blueprint: dict) -> dict:
    errors: list[str] = []
    warnings: list[str] = [
        "Structural checks do not independently prove the mathematical validity of questions or solutions.",
        "Inherited validation_status=PASS must not be interpreted as external expert review.",
    ]
    all_ids = [s["question_id"] for s in blueprint["slots"]]
    if len(all_ids) != len(set(all_ids)):
        errors.append("Duplicate IDs in blueprint slots")
    if len(all_ids) != int(blueprint["target_question_count"]):
        errors.append("Blueprint slot count does not match target_question_count")
    id_set = set(all_ids)
    indexed = {}
    for table in ("questions", "solutions", "metadata"):
        rows = data[table]
        ids = [r.get("question_id", "") for r in rows]
        dup = sorted(k for k, n in Counter(ids).items() if n > 1)
        if dup:
            errors.append(f"Duplicate IDs in {table}: {dup}")
        if set(ids) != id_set:
            errors.append(f"ID mismatch in {table}: missing={sorted(id_set - set(ids))}, extra={sorted(set(ids)-id_set)}")
        required = {"questions": QUESTION_REQUIRED, "solutions": SOLUTION_REQUIRED, "metadata": META_REQUIRED}[table]
        for row in rows:
            for key in required:
                if not str(row.get(key, "")).strip():
                    errors.append(f"Missing {table}.{key} for {row.get('question_id', '?')}")
        indexed[table] = {r.get("question_id", ""): r for r in rows}
    rubric_ids = [r.get("criterion_id", "") for r in data["rubrics"]]
    if len(rubric_ids) != len(set(rubric_ids)):
        errors.append("Duplicate rubric criterion_id(s)")
    criterion_by_id = defaultdict(list)
    for row in data["rubrics"]:
        qid = row.get("question_id", "")
        if qid not in id_set:
            errors.append(f"Orphan rubric criterion {row.get('criterion_id')}: {qid}")
        criterion_by_id[qid].append(row)
        for key in RUBRIC_REQUIRED:
            if not str(row.get(key, "")).strip():
                errors.append(f"Missing rubrics.{key} for {row.get('criterion_id', '?')}")
        try:
            pts = Decimal(str(row.get("max_points", "0")))
            if pts <= 0:
                errors.append(f"Nonpositive points {row.get('criterion_id')}")
        except InvalidOperation:
            errors.append(f"Non-numeric max_points {row.get('criterion_id')}")
    for qid in all_ids:
        q, m = indexed["questions"].get(qid), indexed["metadata"].get(qid)
        if q is None or m is None:
            continue
        for key in ("topic", "subtopic", "difficulty", "rubric_max_score", "reference_question_ids", "concept_tags"):
            q_value = parse_list(q.get(key)) if key in LIST_FIELDS else str(q.get(key, ""))
            m_value = parse_list(m.get(key)) if key in LIST_FIELDS else str(m.get(key, ""))
            if q_value != m_value:
                errors.append(f"Question/metadata field mismatch {qid}.{key}")
        criteria = criterion_by_id[qid]
        if not criteria:
            errors.append(f"No rubric for {qid}")
        try:
            points = sum((Decimal(str(r["max_points"])) for r in criteria), Decimal("0"))
            qscore = Decimal(str(q["rubric_max_score"]))
            if points != qscore:
                errors.append(f"Rubric total mismatch {qid}: {points} != {qscore}")
            orders = sorted(int(r["rubric_order"]) for r in criteria)
            if orders != list(range(1, len(criteria)+1)):
                errors.append(f"Nonsequential rubric_order for {qid}: {orders}")
        except (InvalidOperation, ValueError, KeyError) as e:
            errors.append(f"Rubric format error {qid}: {e}")
    topics = dict(Counter(r.get("topic") for r in data["questions"]))
    diffs = dict(Counter(r.get("difficulty") for r in data["questions"]))
    if topics != blueprint["topic_distribution"]:
        errors.append(f"Topic distribution mismatch: {topics}")
    if diffs != blueprint["difficulty_distribution"]:
        errors.append(f"Difficulty distribution mismatch: {diffs}")
    slots = {r["question_id"]: r for r in blueprint["slots"]}
    if set(slots) != id_set:
        errors.append("Blueprint slot IDs do not match expected range")
    for q in data["questions"]:
        qid = q.get("question_id", "")
        slot = slots.get(qid)
        if slot:
            for field in ("topic", "difficulty", "question_type"):
                if q.get(field) != slot.get(field):
                    errors.append(f"Blueprint mismatch {qid}.{field}")
    try:
        total_score = sum(Decimal(str(x["rubric_max_score"])) for x in data["questions"])
        if total_score != Decimal(str(blueprint.get("target_total_score", 190))):
            errors.append(f"Unexpected overall score {total_score}")
    except (InvalidOperation, KeyError):
        errors.append("Invalid total score data")
        total_score = Decimal(0)
    return {
        "status": "PASS" if not errors else "FAIL",
        "validation_scope": "structural_integrity_only",
        "independent_mathematical_review": "NOT_PERFORMED",
        "expected_questions": len(all_ids),
        "questions": len(data["questions"]),
        "solutions": len(data["solutions"]),
        "rubric_criteria": len(data["rubrics"]),
        "metadata_records": len(data["metadata"]),
        "rubric_score_total": float(total_score),
        "topic_distribution": topics,
        "difficulty_distribution": diffs,
        "errors": errors,
        "warnings": warnings,
    }


def build_combined(data: dict[str, list[dict]]) -> list[dict]:
    solutions = {r["question_id"]: normalize_row(r) for r in data["solutions"]}
    metas = {r["question_id"]: normalize_row(r) for r in data["metadata"]}
    rubrics = defaultdict(list)
    for r in data["rubrics"]:
        rubrics[r["question_id"]].append(normalize_row(r))
    combined = []
    for q in sorted(data["questions"], key=lambda x: x["question_id"]):
        qid = q["question_id"]
        normalized = normalize_row(q)
        normalized.update(solutions[qid])
        # prefer question-level fields where both tables carry the same information
        for key, val in metas[qid].items():
            if key not in normalized:
                normalized[key] = val
        normalized["rubric_criteria"] = sorted(rubrics[qid], key=lambda x: x["rubric_order"])
        combined.append(normalized)
    return combined


def export_all(data: dict[str, list[dict]], dest: Path, report: dict) -> dict:
    dest.mkdir(parents=True, exist_ok=True)
    outputs = {}
    for table in TABLES:
        rows = [normalize_row(row) for row in data[table]]
        csv_dump(dest / f"{table}.csv", rows, list(data[table][0].keys()) if data[table] else None)
        json_dump(dest / f"{table}.json", rows)
        outputs[table] = len(rows)
    combined = build_combined(data)
    csv_dump(dest / "all_in_one.csv", combined)
    json_dump(dest / "all_in_one.json", combined)
    json_dump(dest / "validation_report.json", report)
    return outputs


def make_blind_dataset(data: dict[str, list[dict]], dest: Path) -> None:
    """Never write model solutions or final answers to this destination."""
    dest.mkdir(parents=True, exist_ok=True)
    questions = [normalize_row(q) for q in data["questions"]]
    rubrics = [normalize_row(r) for r in data["rubrics"]]
    json_dump(dest / "questions.json", questions)
    json_dump(dest / "rubrics.json", rubrics)
    csv_dump(dest / "questions.csv", questions)
    csv_dump(dest / "rubrics.csv", rubrics)
    joined = defaultdict(list)
    for rubric in rubrics:
        joined[rubric["question_id"]].append(rubric)
    payload = [{"question_id": q["question_id"], "question_text": q["question_text"], "rubric_max_score": q["rubric_max_score"], "rubric_criteria": joined[q["question_id"]]} for q in questions]
    json_dump(dest / "blind_generation_inputs.json", payload)


def make_review_dataset(data: dict[str, list[dict]], dest: Path) -> None:
    """Keep the gold answer only in a clearly distinct review-only directory."""
    dest.mkdir(parents=True, exist_ok=True)
    json_dump(dest / "review_inputs_WITH_SOLUTIONS.json", build_combined(data))


def source_digest(source: Path) -> dict[str, str]:
    return {f"{table}.csv": hashlib.sha256((source / f"{table}.csv").read_bytes()).hexdigest() for table in TABLES}
