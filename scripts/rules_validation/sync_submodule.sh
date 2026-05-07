#!/usr/bin/env bash
set -euo pipefail

# Find the top-level git repo root, even when run from inside a submodule.
ROOT=$(git rev-parse --show-superproject-working-tree 2>/dev/null)
if [[ -z "$ROOT" ]]; then
  ROOT=$(git rev-parse --show-toplevel)
fi

cd "$ROOT"
git pull
git submodule update --init --recursive
