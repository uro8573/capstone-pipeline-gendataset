#!/usr/bin/env python3
"""CEDT Math II question generation and reproducible dataset build CLI."""
from __future__ import annotations
import argparse
import json
import shutil
import sys
import subprocess
from pathlib import Path

from pipeline.core import (
    TABLES, build_blueprint, export_all, json_dump, make_blind_dataset,
    make_review_dataset, read_sources, source_digest, validate,
)
from pipeline.prompting import write_packets

ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCE = ROOT / "input" / "source"
DEFAULT_OUTPUT = ROOT / "output"
DEFAULT_BLUEPRINT = ROOT / "config" / "blueprint.json"


def load_blueprint(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"Blueprint not found: {path} (run 'blueprint' first)")
    return json.loads(path.read_text(encoding="utf-8"))


def run(args) -> None:
    src = Path(args.source)
    dest = Path(args.output)
    data = read_sources(src)
    blueprint = load_blueprint(Path(args.blueprint))
    report = validate(data, blueprint)
    report["source_files_sha256"] = source_digest(src)
    json_dump(dest / "validation_report.json", report)
    print(f"Structural validation: {report['status']} | questions={report['questions']} | rubrics={report['rubric_criteria']} | errors={len(report['errors'])}")
    if report["errors"]:
        for error in report["errors"][:30]:
            print("  -", error)
        raise SystemExit(2)
    export_all(data, dest / "dataset", report)
    make_blind_dataset(data, dest / "blind_generation")
    make_review_dataset(data, dest / "review_only")
    prompts = write_packets(blueprint, data, dest / "prompts")
    manifest = {
        "pipeline_version": "1.0",
        "source_sha256": source_digest(src),
        "output_files": sorted(str(p.relative_to(dest)) for p in dest.rglob("*") if p.is_file()),
        "prompt_packets": prompts,
        "note": "Generation prompts are files for ChatGPT or another model; the pipeline does not silently invoke an API.",
    }
    json_dump(dest / "manifest.json", manifest)
    print("Dataset, blind generation inputs, gold-only review inputs, prompts, and manifest saved to:", dest)


def validate_only(args):
    report = validate(read_sources(Path(args.source)), load_blueprint(Path(args.blueprint)))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["errors"]:
        raise SystemExit(2)


def make_blueprint(args):
    data = read_sources(Path(args.source))
    bp = build_blueprint(data)
    target = Path(args.output)
    json_dump(target, bp)
    print(f"Wrote blueprint: {target} ({len(bp['slots'])} slots)")


def prompts_only(args):
    bp = load_blueprint(Path(args.blueprint))
    data = read_sources(Path(args.source))
    stages = (args.stage,) if args.stage != "all" else ("questions", "solutions", "rubrics", "review")
    counts = write_packets(bp, data, Path(args.output), stages=stages)
    print("Wrote prompt packets:", counts)


def extract_reference(args):
    """Plain text extraction only; equations/graphs must be checked against the PDF."""
    pdf = Path(args.pdf)
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    extracted = out / "reference_extracted.txt"
    try:
        subprocess.run(["pdftotext", "-layout", str(pdf), str(extracted)], check=True)
    except FileNotFoundError:
        raise SystemExit("pdftotext is not installed. Install Poppler tools or transcribe the reference manually.")
    prompt = (
        "ROLE: Reference exam analyst. Analyze the attached original PDF AND the extracted text. "
        "Review every question, record subject/topic/subtopic/concept tags, learning objective, "
        "question type, math methods and difficulty based on reasoning depth. "
        "Return a proposed blueprint for 30 questions with proportional topic and difficulty allocation. "
        "Do not pretend a solutions-and-rubrics file contains the complete original question wording. "
        "Explicitly flag uncertainties and damaged mathematical notation. "
        "Do not modify config/blueprint.json without review.\n\n"
        "SOURCE: input/reference/solutions_and_rubric_problems_1_8.pdf\n"
        "EXTRACTED TEXT: output/reference/reference_extracted.txt\n"
    )
    (out / "reference_analysis_prompt.md").write_text(prompt, encoding="utf-8")
    print(f"Reference text: {extracted}")
    print(f"Review prompt: {out / 'reference_analysis_prompt.md'}")
    print("WARNING: PDF text extraction may corrupt equations/diagrams. Compare with PDF visually.")


def ingest(args):
    stage = args.stage
    input_path = Path(args.file)
    if not input_path.is_file():
        raise SystemExit(f"Missing candidate file: {input_path}")
    content = json.loads(input_path.read_text(encoding="utf-8"))
    rows = content if isinstance(content, list) else [content]
    if not rows or any(not isinstance(r, dict) for r in rows):
        raise SystemExit("Candidate JSON must be an object or list of objects")
    working = Path(args.working)
    if not working.exists():
        shutil.copytree(Path(args.source), working)
    from pipeline.core import read_csv, csv_dump
    src = working / f"{stage}.csv"
    old = read_csv(src)
    incoming_ids = {r.get("question_id", "") for r in rows}
    if "" in incoming_ids:
        raise SystemExit("Every candidate row needs question_id")
    if stage == "rubrics":
        if any("criterion_id" not in r or not r["criterion_id"] for r in rows):
            raise SystemExit("Rubric candidate requires criterion_id for each row")
        if args.replace_question_rubrics:
            old = [r for r in old if r.get("question_id", "") not in incoming_ids]
        existing = {r["criterion_id"]: r for r in old}
        for r in rows:
            if r["criterion_id"] in existing and not args.replace:
                raise SystemExit(f"Criterion {r['criterion_id']} already exists; pass --replace")
            existing[r["criterion_id"]] = {**existing.get(r["criterion_id"], {}), **r}
        updated = list(existing.values())
    else:
        existing = {r["question_id"]: r for r in old}
        for r in rows:
            qid = r["question_id"]
            if qid in existing and not args.replace:
                raise SystemExit(f"Question {qid} already exists; pass --replace")
            existing[qid] = {**existing.get(qid, {}), **r}
        updated = list(existing.values())
    csv_dump(src, sorted(updated, key=lambda x: (x.get("question_id", ""), str(x.get("rubric_order", "")))))
    print(f"Staged {len(rows)} {stage} row(s) into {src}.")
    print("Next: run --source", working, "to re-check all structural constraints.")


def main():
    parser = argparse.ArgumentParser(description="CEDT Exam Generation Pipeline (stdlib only)")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("blueprint", help="derive 30 generation slots from current approved metadata")
    p.add_argument("--source", default=str(DEFAULT_SOURCE))
    p.add_argument("--output", default=str(DEFAULT_BLUEPRINT))
    p.set_defaults(func=make_blueprint)
    p = sub.add_parser("validate", help="validate source CSVs without writing new datasets")
    p.add_argument("--source", default=str(DEFAULT_SOURCE))
    p.add_argument("--blueprint", default=str(DEFAULT_BLUEPRINT))
    p.set_defaults(func=validate_only)
    p = sub.add_parser("run", help="validate, export, create prompts and isolated blind/review inputs")
    p.add_argument("--source", default=str(DEFAULT_SOURCE))
    p.add_argument("--blueprint", default=str(DEFAULT_BLUEPRINT))
    p.add_argument("--output", default=str(DEFAULT_OUTPUT))
    p.set_defaults(func=run)
    p = sub.add_parser("prompts", help="create stage-specific generation/solution/rubric/review prompts")
    p.add_argument("--stage", choices=("all", "questions", "solutions", "rubrics", "review"), default="all")
    p.add_argument("--source", default=str(DEFAULT_SOURCE))
    p.add_argument("--blueprint", default=str(DEFAULT_BLUEPRINT))
    p.add_argument("--output", default=str(DEFAULT_OUTPUT / "prompts"))
    p.set_defaults(func=prompts_only)
    p = sub.add_parser("reference", help="extract PDF text and create a human-review reference analysis prompt")
    p.add_argument("--pdf", default=str(ROOT / "input" / "reference" / "solutions_and_rubric_problems_1_8.pdf"))
    p.add_argument("--output", default=str(DEFAULT_OUTPUT / "reference"))
    p.set_defaults(func=extract_reference)
    p = sub.add_parser("ingest", help="stage a new candidate JSON for replacement or update; never alters original source")
    p.add_argument("--stage", choices=TABLES, required=True)
    p.add_argument("--file", required=True)
    p.add_argument("--source", default=str(DEFAULT_SOURCE))
    p.add_argument("--working", default=str(ROOT / "input" / "working"))
    p.add_argument("--replace", action="store_true")
    p.add_argument("--replace-question-rubrics", action="store_true", help="for rubric ingest, replace all prior criteria for affected question IDs")
    p.set_defaults(func=ingest)
    args = parser.parse_args()
    try:
        args.func(args)
    except FileNotFoundError as e:
        parser.exit(2, f"Input file missing: {e}\n")


if __name__ == "__main__":
    main()
