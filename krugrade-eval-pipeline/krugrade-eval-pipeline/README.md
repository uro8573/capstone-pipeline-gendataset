# KruGradeAI — Generated Exam & Student Answer Evaluation Pipeline

Two-phase evaluation **with Codex CLI**: audit generated questions, solutions and rubrics; independently re-grade generated student answers and compare to dataset labels. Supports the Statistics, Signals and Optimization CSV variants used by KruGradeAI. Standard library Python 3.10+ only.

## Setup

1. Install Codex CLI and authenticate (`codex login`).
2. Place files in `input/` (or provide absolute paths).
3. Run a small pilot before full evaluation.

```bash
# Only deterministic checks, with no Codex charges:
python pipeline/evaluate.py --questions input/generated_questions.csv --answers input/generated_student_answers.csv --dry-run --out output/pilot

# Codex quality assessment for two questions, up to five student answers each:
python pipeline/evaluate.py --questions input/generated_questions.csv --answers input/generated_student_answers.csv --references input/original_questions.csv --max-questions 2 --max-answers 5 --out output/pilot_ai

# Whole dataset, resume completed model stages:
python pipeline/evaluate.py --questions input/generated_questions.csv --answers input/generated_student_answers.csv --references input/original_questions.csv --out output/full --resume
```

If questions and answers are **combined in one CSV** (as in KruGradeAI Statistics/Signals/Optimization datasets), simply omit `--answers`:

```bash
python pipeline/evaluate.py --questions input/kru_grade_ai_optimization_expanded_plus_235_partial.csv --max-questions 2 --max-answers 5 --out output/optimization_pilot
```

For **question-only datasets**, omit `--answers`; answer report contains zero rows. For originality checks, use `--references` with the source/reference exam questions. Without it, originality is **not verified**. The optional `--max-answers` limits each selected question for piloting, not total answers.

## Evaluation dimensions

**Question quality:** structural completeness; question consistency across rows; solvability and ambiguity; independent verification of official solution; rubric coverage/fairness; topic and difficulty fit; and reference-question text similarity. In Codex mode, the model assigns 0–4 for clarity, solvability, solution correctness, rubric alignment and originality, and gives pass/review/fail with issues. Numeric similarity is merely triage; mathematical originality and correctness still need review.

**Student answer quality:** required fields; expected_score versus sum of existing criterion scores; individual scoring anchors (if provided); sample_type PARTIAL score boundaries; duplicate response IDs and exact duplicate answers within a question. Codex mode re-grades **without being shown `expected_score`**, assigns per-criterion scores and evidence, assesses student authenticity, and flags mismatches and non-substantive errors. Score differences are flagged, not automatically corrected.

## Outputs

- `question_evaluation.csv` — per-question checks and model review
- `answer_evaluation.csv` — independent rubric vectors, score disagreements, evidence, quality indicators
- `review_queue.csv` — flagged questions/responses for human inspection
- `summary.json` — counts and limitations
- `manifest.json` — input checksums
- `training_candidates.csv` — original response columns, restricted to AI-pass questions and answers with complete core fields, matching total/criterion scores, and no generation-target mismatch. Dry-run exports no candidates. Human review status is preserved; these are provisional candidates, not verified gold labels.
- `stages/*.json` — resumable raw Codex judgments

**No input CSV is modified.** Treat AI judgments as provisional; manually adjudicate mathematical mistakes and score disagreements before training/evaluating a grader. Do not equate model `pass` with verified ground truth.

## Practical requirements/limitations

- Codex must be installed and logged in for full evaluation. `--dry-run` needs no Codex and checks only structural, scoring and exact-text issues, **not math correctness**.
- `--resume` checks input hashes and batch size; use the same output directory and unchanged inputs.
- Each selected question makes one Codex question review call and one answer call per batch of up to 8 responses, unless resumed.
- Existing `rubric_criteria` should contain JSON array with `criterion_id` and `max_score`, `max_points`, or `points`. `rubric_analysis` should contain `awarded_score` per criterion. If absent, those checks will flag the record, not fail silently.
- Native question-generation CSVs can supply scoring guidance inside every criterion as nonempty `full_credit` and `partial_credit` strings. The evaluator uses these directly when `rubric_scoring_guide` is absent; incomplete guidance still requires review. This does not convert prose rules into validated numeric scoring anchors.
- If the official `solution` is absent, independent answer grading is skipped; report it as missing instead of guessing.
- Long problems/reference sets may exceed context; choose small batches or trim irrelevant references when necessary.
- A second, independent judge or human expert is recommended for high-stakes use.
- WRONG now means zero awarded points; partially correct work is PARTIAL. Authentic student mistakes alone should not trigger a quality-review verdict. Scoring uncertainty, inconsistent labels and inauthentic responses still require review. Use a new output directory for evaluation version 2; older cached judgments cannot be resumed.

## Run tests

```bash
python -m unittest discover -s tests -v
```
