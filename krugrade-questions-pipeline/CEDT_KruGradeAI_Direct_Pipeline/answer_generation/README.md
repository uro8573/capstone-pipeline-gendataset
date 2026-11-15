# KruGradeAI — FULL / PARTIAL / WRONG response pipeline

Generates **5 responses per question** by default: FULL, low/middle/high PARTIAL, and WRONG. A separate solution-aware call scores the actual work. Labels are derived from scores: FULL = maximum, WRONG = zero, PARTIAL = strictly between. All labels remain synthetic and unreviewed by humans.

## Balanced generation and training export

`--mode balanced --count 5` is the default. Larger counts repeat the five-slot cycle;
use multiples of five for equal slot counts. PARTIAL bands are fractions of maximum:
LOW (0, 1/3), MID [1/3, 2/3), HIGH [2/3, 1). Targets never enter the grading prompt.
`--mode partial` retains the previous all-PARTIAL mode.

```powershell
python -X utf8 pipeline/run.py --input ../question_generation/output/university_math_1000/dataset/all_in_one.csv --out output/balanced --mode balanced --count 5 --resume
```

- `new_samples.csv`: all generated responses with actual scores and actual types.
- `new_partial_samples.csv`: PARTIAL subset only; use `new_samples.csv` for all types.
- `generation_review_queue.csv`: target-band mismatches, preserving the actual score.
- `validation_report.json`: actual bands, distinct score vectors, failures and mismatches.

No score is forced and no retry loop silently fills missing bands. Some rubrics cannot
produce all three PARTIAL bands. Inspect coverage before expanding a run. Use a fresh
output folder for this version; resume uses a new cache key. Generation alone does
not qualify a row for training: run the sibling evaluation pipeline with
`--answers <path/to/new_samples.csv>`. Its `training_candidates.csv` contains only rows
whose question and answer both passed AI review, with complete core fields, matching
scores and no target mismatch. Candidates still require your chosen label-validation
process. Optional fields and fields not applicable to FULL/WRONG can be empty.

## Direct CEDT Question Pipeline input (no adapter)

The native `question_generation/output/dataset/all_in_one.csv` is accepted **as-is**.
There is no conversion/adapter step, no renaming of columns and no need to add
student-answer fields manually. The answer pipeline reads the source
`rubric_criteria` JSON array (`max_points`, `full_credit`, `partial_credit`,
`common_mistakes`) **directly** and appends answer-specific columns only in its
exported files. The source question CSV remains untouched.

```bash
python pipeline/run.py --input ../question_generation/output/dataset/all_in_one.csv --dry-run
python pipeline/run.py --input ../question_generation/output/dataset/all_in_one.csv --out output/cedt_pilot --count 5 --max-questions 2
python pipeline/run.py --input ../question_generation/output/dataset/all_in_one.csv --out output/cedt_full --count 5 --resume
```

A question-only input yields `new_samples.csv` (all new answers) and
`expanded_dataset.csv` (30 original question rows with blank answer fields plus
new answer rows). Evaluate `new_samples.csv` before selecting training candidates.

When CEDT `partial_credit` is prose rather than a structured scoring-anchor
list, the model grades against that text but numeric anchor membership cannot
be fully checked deterministically. The local validator still verifies totals
and 0 < score < maximum. Human review is recommended.

## Prerequisites

- Python 3.10+ (standard library only)
- Codex CLI installed and authenticated (`codex login`), with sufficient account quota. See [Codex non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode).
- Input CSV with question, rubric, and solution columns (answer fields optional). Use the **original dataset** rather than previously auto-generated additions if you want exactly five new samples per question.

## Quick start (Windows PowerShell)

```powershell
# In the project directory; copy your CSV into input/ or use an absolute path
codex login
python pipeline/run.py --input "input/kru_grade_ai_optimization_expanded.csv" --dry-run
python pipeline/run.py --input "input/kru_grade_ai_optimization_expanded.csv" --out output/optimization --count 5 --max-questions 2
# Run every question after inspecting the pilot:
python pipeline/run.py --input "input/kru_grade_ai_optimization_expanded.csv" --out output/optimization --count 5 --resume
```

macOS/Linux: substitute `python3` for `python` if necessary.

## Outputs

- `output/<subject>/new_partial_samples.csv`: only newly generated rows
- `output/<subject>/expanded_dataset.csv`: original rows followed by successful new rows
- `output/<subject>/validation_report.json`: per-question status and diversity counts
- `output/<subject>/manifest.json`: input hash and requested count
- `output/<subject>/stages/`: resumable per-question generation and grading JSON (do not treat as verified labels)

## Pipeline steps

1. **Load & audit.** Read UTF-8 CSV and check question-level consistency and rubric maximums.
2. **Generation (blind).** Send question, criteria, guide and requested response slots to Codex with `--output-schema`; **do not send the official solution**.
3. **Independent scoring stage.** Send the already-generated answers, official solution and rubric to a separate Codex call, producing per-criterion scores and feedback.
4. **Deterministic checks.** Check count, duplicate text, distinct pattern labels, criterion order, score limits and explicit anchors. Classify by actual score; record target-band mismatches. In `--mode partial`, require `0 < score < max`. Failed questions are excluded and reported; completed stages can be resumed.
5. **Export.** Preserve original columns, write new IDs, `missed_concepts` JSON arrays, original question difficulty descriptions, `adjudication_status=not_required` and `label_review_status=unreviewed` when those columns exist.

## Operational notes

- **Cost**: 2 Codex CLI invocations per question; 47 questions require 94 calls absent retries. These consume Codex quota and may take time.
- Codex structured output schema is used as an output contract, but cannot guarantee mathematical correctness or semantic diversity. Checks catch *structural* problems, not independent grading accuracy. Review samples and scores before using as ground truth.
- This runner uses `--sandbox read-only` and sends context in stdin. It does not ask Codex to modify files.
- `--resume` reuses stage outputs only when the input file's SHA256 matches; do not change input midway. A failed grading attempt can be inspected in `stages/` and rerun by deleting that question's grading JSON. If the source file changes, use a fresh output directory.
- Student response diversity is currently guarded by exact normalized text and `error_pattern` uniqueness. A human or a semantic-review extension should inspect near-duplicates.
- Existing metadata conventions differ. The pipeline preserves row schema and most question metadata, but clears review-only fields; for specialized fields validate downstream needs. An LLM-generated score is **provisional**, even when the local checks pass.
- If `solution` is empty, the grading call cannot reliably cross-check with the official reference; do not use that dataset for validated labels until solutions are supplied.

## Running tests

```bash
python -m unittest discover -s tests -v
```
