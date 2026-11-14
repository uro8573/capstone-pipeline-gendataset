#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 run_pipeline.py run
printf '\nPipeline complete. See output/\n'
