# KruGradeAI Codex pipeline — agent instructions

- Never edit the original input CSV. Keep the exact input header order in exported CSVs.
- Generation is blind: NEVER pass `solution`, `canonical_solution`, `answer`, or `canonical_answer` to the generation model.
- Evaluate the finished student answers separately using the solution and rubric; do not force a planned score.
- Synthesize authentic student math, not meta-explanations of rubric omissions.
- Use the supplied rubric score anchors when present. Do not create unsupported fractional awards.
- Do not mark synthetic labels as human-reviewed or independently verified.
- Preserve `difficulty_reason` from the original question; `missed_concepts` remains a JSON array of short labels.
- If checks fail, report failures instead of fabricating rows or silently assigning desired scores.
- The CLI runner is `python pipeline/run.py ...`; keep `--dry-run` and resumability functional.
