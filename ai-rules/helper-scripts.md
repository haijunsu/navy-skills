# Helper Scripts Rules

When a helper/utility script is needed (not part of the main application/skill):

- Follow the core language and environment rules in `stack.md`.
- Create a subfolder under `tools/` named after the tool (e.g. `tools/resize_images/`).
- Write the Python script inside that subfolder.
- Add a `run.sh` that activates the shared venv at `.venv/`, installs from the root `requirements.txt`, then runs the script.
- Add any new pip packages to the single `requirements.txt` in the project root.
- Add a `README.md` explaining what the tool does, options, and usage examples.
- Do not write throw-away scripts in `/tmp` or the frontend directory.
