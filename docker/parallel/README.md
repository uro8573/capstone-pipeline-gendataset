# Five-worker dataset run

The host `parallel_dataset.py` exporter and five Docker workers replace the
sequential full-dataset runner. Do not run the old runner concurrently.

Each worker owns every fifth slot of the selected plan. The original plan has
1,000 questions (200 per worker); the 200-question subset has 40 per worker.
Per-question stages already completed by the original runner are reused.
Each question continues through balanced response generation and independent
evaluation without waiting for all questions to finish. Isolated job snapshots
keep downstream resume hashes stable. Only the host exports the shared question
dataset and reserves identities in its existing duplicate registry; responses
for rejected duplicate questions are excluded from the merged data.

Run from the repository root with Docker Desktop running. The local, ignored
`.env.workers` contains `CODEX_AUTH_FILE` (a path, never the token contents),
`KRUGRADE_MODEL`, and `KRUGRADE_REASONING`. The auth file is mounted read-only and
copied into each container's private Codex home. Credentials are not in the image.

```powershell
python -X utf8 parallel_dataset.py prepare
docker compose --env-file .env.workers -f docker-compose.workers.yml build worker0
docker compose --env-file .env.workers -f docker-compose.workers.yml up -d --no-build
python -X utf8 parallel_dataset.py supervise
```

The supervisor must remain running on the host for continuous exports. It can
also be launched as a hidden background process. Worker and supervisor locks
prevent duplicate instances from writing the same jobs.

Outputs are in `output/parallel_dataset/`:

For live, worker-colored logs, open `watch_workers.cmd` from the repository root
or run `python -X utf8 watch_workers.py`. W0 is cyan, W1 green, W2 yellow,
W3 magenta, and W4 blue; errors are red and retain their worker ID. The read-only
viewer polls once per second, shows saved stages and tails per-job logs. It is
not model-token streaming. Closing it does not stop the workers. For raw container
logs use `docker compose --env-file .env.workers -f docker-compose.workers.yml logs -f`.

- `status.json`, `worker-0.json` through `worker-4.json`: progress and errors.
- `new_samples.csv`: completed responses belonging to globally accepted questions.
- `training_candidates.csv`: original row fields for AI-reviewed provisional candidates.
- `train.csv`, `validation.csv`, `test.csv`: candidates preserving family splits.
- `review_queue.csv`: answer flags, data failures, and rejected duplicate questions.
- `jobs/<question_id>/`: immutable question input, model stages, logs and evaluation.

All candidate labels remain unreviewed by humans. Empty optional fields are
allowed; correct FULL responses can use `not_applicable` for error location.
Coverage can be below target after review and duplicate filtering.

To stop after current questions, create the `output/parallel_dataset/STOP` file.
For an immediate stop, use `docker compose --env-file .env.workers -f
docker-compose.workers.yml stop`. Wait for the supervisor to exit after a graceful
stop; after a forced stop, inspect the worker statuses before resuming.

Once the cause of a model/auth/quota failure is resolved and workers have stopped:

```powershell
python -X utf8 parallel_dataset.py resume
docker compose --env-file .env.workers -f docker-compose.workers.yml up -d --no-build
python -X utf8 parallel_dataset.py supervise
```

Use `resume --refresh-code` only for an intentional code deployment with workers
stopped; it records the previous/new code fingerprints and preserves the plan.
Terminal data-validation failures are preserved for review instead of silently
retried; authentication/provider failures stop workers after their current job.
Use `python -X utf8 parallel_dataset.py collect` for a one-time host export when
the supervisor is not running. Do not run the collector inside a container: the
host's original absolute output path is part of the cross-run registry identity.

To reduce the run to 200 questions, request a graceful stop and wait for workers
and the supervisor to exit, then run `python -X utf8 parallel_dataset.py reduce-to-200`.
Start Compose and the supervisor again. Selection keeps 20 questions per topic,
whole two-question families and their original splits (160 train / 20 validation /
20 test before filtering), prioritizing questions already started. It never
rewrites original IDs or discards existing stages. `selection.json` preserves the
subset across future resumes. Reducing fails explicitly if started families
cannot fit those quotas. All subsequent merged outputs use only selected IDs.
