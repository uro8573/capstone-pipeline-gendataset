# University mathematics dataset generation

`generate_dataset.py` builds NEW questions, solutions and rubrics using four separate
model calls per question. Existing seed CSVs are never modified. Python standard
library only. This is question generation, not model training or student-response
generation. All scores/solutions are synthetic and unreviewed by humans.

## Default configuration

`config/generation.university_math.json`: 1,000 questions across 10 university-level
topics, 100 each. Each topic has 20 Easy, 50 Medium and 30 Hard questions and six
question formats. Two slots sharing a family stay in the same split. Planned split:
800 train, 100 validation, 100 synthetic test. This is not an independent real-world
test benchmark. Mathematical families and text checks cannot guarantee no semantic
overlap; independently review close variants before use.

Edit topics/count/subtopics, difficulty_weights, question_types, variation_strategies,
points_by_difficulty, variants_per_family, split_weights, language and seed.
`model: null` uses the CLI configuration; set a model ID available to your account
to pin the model for reproducibility. No API key is read by this runner. Codex CLI
must be installed/authenticated; generation consumes its quota. The default full
run needs 4,000 model calls before retries, so inspect a pilot first.

## Commands (from this directory)

```powershell
# Offline: materialize the blueprint, plan.csv and 1,000 question prompt packets
python generate_dataset.py plan --out output/university_math_1000

# Generate two questions, solve, build rubrics, review, validate and export
python generate_dataset.py generate --out output/university_math_1000 --limit 2

# Continue another batch; valid existing stages are automatically resumed
python generate_dataset.py generate --out output/university_math_1000 --limit 20

# Explicitly process every remaining question
python generate_dataset.py generate --out output/university_math_1000 --all

# Rebuild exports without model calls
python generate_dataset.py export --out output/university_math_1000
```

Use `--config path/to/config.json` to select a different config. Use a new output
directory after changing config. On Windows, if Python cannot launch the shell
shim, pass `--codex-bin codex.exe` pointing to a native Codex executable.

## Outputs and review

- `manifest.json`, `blueprint.json`, `plan.csv`: frozen configuration and family splits.
- `prompts/`: question-only prompt packets.
- `stages/<id>/`: hash-checked question, solution, rubric and AI review records.
- `dataset/all_in_one.csv`: provisional questions with solutions and rubric metadata;
  directly accepted by the sibling `answer_generation/pipeline/run.py`.
- `splits/train`, `splits/validation`, `splits/test`: same schema, split by family.
- `review_queue.csv`: incomplete, invalid, flagged or possible duplicate questions.
- `summary.json`: actual coverage; fewer than 1,000 rows can be exported.

Only structurally valid questions with model PASS and no reported issues are
exported. These still have `label_review_status=unreviewed`. Other results stay in
the review queue and raw stages. Exact/near text similarity is checked across
splits; semantic uniqueness is NOT proven. A model error/timeout/quota failure
stops further calls and preserves completed stages. When a generated question
matches the registry, the generator asks for a replacement up to five times and
includes the matched question in its retry prompt. If every attempt still matches,
generation stops for that slot instead of exporting a duplicate.
To retry a failed review, archive/remove that question's review stage first, then
generate again. Review-stage failures are not automatically rewritten into a PASS.

Training a grader additionally requires student answers at varied score levels and
reviewed labels. The sibling answer generator now defaults to FULL/PARTIAL/WRONG
with low/mid/high PARTIAL targets; actual grading may leave coverage gaps. Preserve
question family and split fields in all downstream responses.

Tests: `python -B -m unittest discover -s tests -v` (offline, mocked model calls).

## Cross-run duplicate registry

Every `generate`/`export` command now checks a persistent SQLite registry, by default
`output/question_registry.sqlite3` under this question-generation project. Different
output folders share this default automatically. `plan` never registers questions.
No embeddings, paid API calls or external services are used for duplicate checks.

Checks run immediately after each question is generated, before the solution,
rubric and review stages. Unique questions are reserved in SQLite at that point,
so sequential runs and parallel workers sharing the registry see one another's
questions. The checks also run again before accepting export rows:

1. Unicode/whitespace/case normalization and exact-text comparison.
2. Numeric-constant masking: likely variants differing only in numeric values.
3. Near-text similarity using `near_duplicate_threshold` (default 0.90).

Matches cause a replacement generation attempt; if the retry limit is exhausted,
the slot is marked failed and is not exported. Nothing rewrites or deletes the old
question. Re-exporting the same output with the same config and question
text/split/family does not flag the question against itself. Changing those fields
under an existing identity produces `identity_conflict`.

### Import questions generated before this feature

Import every historical dataset you want new runs checked against. CSV requires
`question_id` and `question_text`; optional `split` and `family_id` preserve their
provenance. Missing split is recorded as `unknown`. Use one stable `--dataset-id`
for each historical dataset. Re-importing it is idempotent. The import command
prints accepted records and flagged matches; `accepted` includes unchanged records
already imported. Invalid input aborts/rolls back the import.

```powershell
python -B -m pipeline.question_registry --input output/dataset/all_in_one.csv --registry output/question_registry.sqlite3 --dataset-id original_signals_30
```

### Repeated generation rounds

For a genuinely new round, copy the config and change `dataset_id` and `seed` (and
optionally topic counts). Give it a new output folder but keep the SAME registry:

```powershell
python generate_dataset.py generate --config config/math_round2.json --out output/math_round2 --registry output/question_registry.sqlite3 --limit 20
```

Use `--registry` with an absolute path to share the registry across separate project
copies. Separate registry files do NOT check one another. Keep and back up the
registry: removing/replacing it removes cross-run history. The database and generated
outputs are intentionally excluded from Git; teammates must share/import historical
CSV data or use the same registry. SQLite serializes write transactions; a run waits
up to 30 seconds for another generator/exporter, then fails explicitly rather than
bypassing checks. Resume generation after the other writer finishes.

Question reservations commit as soon as a unique question is generated, even if a
later solution, rubric or review stage fails. This keeps other workers from generating
the same question. Export remains transactional for its own writes. Output CSV files
themselves are not a single atomic transaction: if interrupted,
rerun `export` successfully before consuming them. Historical reservations are kept
conservatively even if a later review rejects an older question. Do not reset the
registry to force a flagged question into a different split.

These are duplicate-screening heuristics, not a mathematical-equivalence proof.
Numeric variants may be legitimate exercises but are held for review; variable
renaming, translations and substantially reworded equivalents can escape detection.
There is no automatic adjudication/override, and the five-attempt retry cap may leave
a slot incomplete. Review semantic families before building a benchmark; synthetic
test is not a substitute for an independent human-verified real dataset.
