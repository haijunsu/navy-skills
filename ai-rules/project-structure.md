# Project Structure Rules

Every project must contain the following top-level folders:

| Folder      | Contents                                                              |
|-------------|-----------------------------------------------------------------------|
| `backend/`  | FastAPI app, Ollama chat loop, PropertyReach client, tests            |
| `frontend/` | Single-page chat UI (`index.html`)                                    |
| `docs/`     | Project requirements and API spec                                     |
| `scripts/`  | `setup.sh`, `start.sh`, `test.sh`                                     |
| `data/`     | SQLite DB for quota tracking (git-ignored)                            |
| `logs/`     | Conversation logs (git-ignored)                                       |

Within each folder, follow the industry-standard layout for the language in use (e.g. `src/` layout for Python packages, feature-based structure for React frontends).

## Environment Variables

Maintain a `.env.example` file at the project root documenting all available environment variables with placeholder values. Never commit a populated `.env` file.
