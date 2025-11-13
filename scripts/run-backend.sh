#!/usr/bin/env bash
set -e
cd "$(dirname "$0")/../backend"

if [[ "$1" == "test" ]]; then
    uv run python -m pytest -v tests/
else
    uv run --active uvicorn app.main:app --reload
fi
