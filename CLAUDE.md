# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

`navy-skills` is a Python repository for AI skills, owned by Haijun (Navy) Su. The project is in its early stages — no source code or tooling configuration exists yet beyond a standard Python `.gitignore` and MIT license.

## Language & Tooling

The repository is configured for **Python** (evidenced by the `.gitignore`, which covers pytest, ruff, mypy, venv, and common Python packaging tools). When code is added, follow these conventions inferred from the ignored paths:

- **Linting/formatting**: Ruff (`.ruff_cache/` is gitignored)
- **Type checking**: mypy or pytype (`.mypy_cache/`, `.pyre/`, `.pytype/` are gitignored)
- **Testing**: pytest (`.pytest_cache/` is gitignored)
- **Virtual environments**: `.venv/` or `venv/` (gitignored — do not commit)

Once a `pyproject.toml`, `setup.py`, or equivalent is added, update this file with the actual build/lint/test commands.
