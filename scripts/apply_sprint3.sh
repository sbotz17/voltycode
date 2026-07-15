#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BACKEND_DIR="$REPO_ROOT/apps/backend"

cd "$BACKEND_DIR"

if [[ ! -d ".venv" ]]; then
  python3 -m venv .venv
fi

source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -e "$REPO_ROOT/packages/voltycore"
python -m pip install -r requirements.txt

ruff check . "$REPO_ROOT/packages/voltycore" --fix
ruff check . "$REPO_ROOT/packages/voltycore"
pytest -q "$REPO_ROOT/packages/voltycore/tests" tests

echo "Sprint 3 applicato con successo."
