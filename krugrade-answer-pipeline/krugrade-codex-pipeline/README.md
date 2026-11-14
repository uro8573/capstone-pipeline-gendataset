# KruGradeAI — PARTIAL sample pipeline for Codex CLI

Generates **5 new PARTIAL student answers per question** (configurable), scores them with a **second, solution-aware Codex call**, and creates schema-compatible CSV files. Works with Statistics, Signals and Optimization input formats (rubrics remain subject-specific). Does not claim independent validation.

## Prerequisites

- Python 3.10+ (standard library only)
- Codex CLI installed and authenticated (`codex login`), with sufficient account quota. See [Codex non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode).
- Input CSV with question, rubric and existing response columns. Use the **original dataset** rather than previously auto-generated additions if you want exactly five new samples per question.

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
2. **Generation (blind).** Send question, criteria, guide and existing PARTIAL response patterns to Codex with `--output-schema`; **do not send the official solution**.
3. **Independent scoring stage.** Send the already-generated answers, official solution and rubric to a separate Codex call, producing per-criterion scores and feedback.
4. **Deterministic checks.** Check answer count, duplicate exact text, distinct error pattern labels, criterion ID order, score limits and explicit scoring anchors, and strict partial total (`0 < score < max`). Failed questions are excluded and reported; completed stages can be resumed.
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
