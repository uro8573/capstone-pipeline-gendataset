FROM node:22-bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends python3 ca-certificates git \
    && rm -rf /var/lib/apt/lists/* \
    && npm install -g @openai/codex@0.169.0
WORKDIR /workspace
ENV PYTHONUTF8=1 PYTHONUNBUFFERED=1 CODEX_HOME=/root/.codex
ENTRYPOINT ["python3", "-B", "parallel_dataset.py", "worker"]
