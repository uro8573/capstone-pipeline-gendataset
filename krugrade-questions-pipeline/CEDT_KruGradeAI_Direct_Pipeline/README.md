# CEDT Question Generation → KruGradeAI Answer Generation (Direct)

The included **original** `question_generation/` project exports
`output/dataset/all_in_one.csv`. The **updated** `answer_generation/`
project accepts that CSV directly. **No adapter, join, or manual column editing.**

## Prerequisites
- Python 3.10+
- Codex CLI installed and authenticated (`codex login`) for actual AI generation

## Quick start (at the root of this extracted ZIP)

Dry run for all **30** existing generated questions; no Codex calls:

```bash
python run_end_to_end.py --dry-run
```

Pilot for 2 questions, 5 PARTIAL answers each:

```bash
python run_end_to_end.py --max-questions 2 --count 5 --out output/pilot
```

Full set (30 × 5 = 150 new PARTIAL answers, if generation and scoring pass):

```bash
python run_end_to_end.py --count 5 --out output/full --resume
```

Re-export questions from the original question pipeline first (optional):

```bash
python run_end_to_end.py --rebuild-questions --dry-run
```

To point to another native Question Pipeline output:

```bash
python run_end_to_end.py --question-csv "/path/to/all_in_one.csv" --dry-run
```

## Input contract

- Source of truth: `question_generation/output/dataset/all_in_one.csv`
- Required columns: `question_id`, `question_text`, `solution`, `rubric_criteria`, `rubric_max_score`
- Native rubric keys read directly: `criterion_id`, `max_points`, `criterion`, `full_credit`, `partial_credit`, `common_mistakes`
- **Not required on input**: `rubric_scoring_guide`, `answer_text`, `sample_type`, `expected_score`, `rubric_analysis`, `response_id`
- Additional original fields (topic, concept tags, difficulty, etc.) are kept unchanged.
- No extra adapter file is created; the Answer Generator works with native rubric objects in-memory.

## Export

- `output/full/new_partial_samples.csv`: only successful generated student answers
- `output/full/expanded_dataset.csv`: original question-only rows plus generated answers; original rows have blank answer fields
- `output/full/validation_report.json`: per-question successes and failures
- `output/full/stages/`: JSON for the separate blind generation and solution-aware grading calls

The blind-generation prompt excludes official solutions, and the grading prompt introduces them only afterward. This is a boundary in the model input, not a formal security guarantee. AI-graded scores are **provisional**, and mathematical correctness/semantic diversity require independent review. Native CEDT `partial_credit` text may imply numeric anchors; these are not guessed, so the deterministic validator cannot guarantee every nuanced scoring increment is valid.

Run tests:

```bash
python -m unittest discover -s answer_generation/tests -v
```
