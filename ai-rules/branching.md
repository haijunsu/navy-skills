# Branching Rules

- Never commit or work directly on `main` or `develop` branches.
- Before starting any work, check the current branch with `git branch`.
- Always create feature branches from `develop`: `git checkout develop && git checkout -b feature/<name>`.
- Feature branches always merge to `develop` via PR, unless the user explicitly asks to merge elsewhere.
- Branch names must be descriptive (e.g. `feature/portfolio-redesign`, `feature/gothic-background`).
- Never `git push` or `gh pr create` automatically. Always stop after committing and ask the user before pushing or opening a PR.
