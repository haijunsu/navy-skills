#!/usr/bin/env bash
set -euo pipefail

# Run from the parent repo root to pull latest and sync the navy-skills submodule.
git pull
git submodule update --init --recursive
