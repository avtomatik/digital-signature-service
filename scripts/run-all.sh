#!/usr/bin/env bash
set -e

trap 'kill 0' SIGINT

./scripts/run-backend.sh &
./scripts/run-frontend.sh &

wait
