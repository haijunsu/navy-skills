# Tech Stack & Tooling Rules

The repository is primarily a **Python** project focused on AI skills.

## Core Language
- **Python**: All core logic and helper scripts must be written in Python.

## Tooling
- **Linting & Formatting**: [Ruff](https://github.com/astral-sh/ruff).
- **Type Checking**: [mypy](https://github.com/python/mypy) or [pytype](https://github.com/google/pytype).
- **Testing**: [pytest](https://github.com/pytest-dev/pytest).

## Environment Management
- **Virtual Environment**: Use `.venv/` or `venv/` at the project root.
- **Shared Venv**: One virtual environment for the entire project. Do not create per-folder venvs.
- **Gitignore**: Ensure `.venv/` and tool caches (`.ruff_cache/`, `.pytest_cache/`, `.mypy_cache/`, etc.) are always in the root `.gitignore`.
- **Dependencies**: Add all pip packages to the single `requirements.txt` in the project root.
