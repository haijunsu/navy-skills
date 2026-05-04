# Helper Scripts Rules

When a helper/utility script is needed (not part of the app itself):

- Use Python, not Node.js or shell one-liners.
- Create a subfolder under `tools/` named after the tool (e.g. `tools/resize_images/`).
- Write the Python script inside that subfolder.
- Add a `run.sh` that activates the shared venv at `.venv/`, installs from the root `requirements.txt`, then runs the script.
- Add any new pip packages to the single `requirements.txt` in the project root — never per-tool requirements files.
- Add a `README.md` explaining what the tool does, options, and usage examples.
- The shared venv lives at `.venv/` — one venv for the entire project, never create additional venvs.
- `.venv/` must be in the root `.gitignore`.
- Do not write throw-away scripts in `/tmp` or the frontend directory.
