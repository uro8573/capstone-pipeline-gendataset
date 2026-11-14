# Pipeline at a glance

- **Stage 0: Reference** — PDF → extraction + reference analysis prompt; human verifies notation and conceptual coverage.
- **Stage 1: Blueprint** — locked 30 slots describing topic, concepts, learning objective, difficulty, variation strategy, points.
- **Stage 2: Question generation** — 30 prompts with **no existing solutions**. Optional ChatGPT/human authors question JSON.
- **Stage 3: Independent solving** — 30 solution prompts with questions only. No gold solution provided.
- **Stage 4: Rubric design** — 30 rubric prompts using question + solution; explicit partial-credit conditions.
- **Stage 5: Mathematical review** — 30 review prompts; human/independent model verifies math, rubric, originality.
- **Stage 6: Structural QA** — Python checks IDs, cross-table keys, rubric point sums and blueprint coverage.
- **Stage 7: Export** — CSV/JSON outputs, isolated blind-input and review-only packages, SHA256 provenance.

One command builds all reproducible outputs from the current 30-question dataset:

```bash
python run_pipeline.py run
```

Test with:

```bash
python -m unittest discover -s tests -v
```

**Reference limitation:** uploaded reference is a solutions-and-rubric PDF, so exact original question wording may not be recoverable. **Mathematical correctness limitation:** automated structural checks do not independently prove mathematical truth.
