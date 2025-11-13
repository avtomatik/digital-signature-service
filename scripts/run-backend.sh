#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# Script to run Digital Signature Service backend via uv
# -----------------------------------------------------------------------------

# Exit immediately if a command fails
set -e

# Move to backend folder
cd "$(dirname "$0")/../backend"

# Activate uv's environment and run uvicorn
uv run --active uvicorn app.main:app --reload
