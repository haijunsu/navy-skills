# Project Structure Rules

Every project must contain the following top-level folders:

| Folder       | Contents                                                              |
|--------------|-----------------------------------------------------------------------|
| `skills/`    | Individual AI skill implementations                                   |
| `ai-rules/`  | Sharable AI behavior and coding rules                                 |
| `docs/`      | Project requirements and design specifications                        |
| `scripts/`   | Operational scripts (e.g. `setup.sh`, `start.sh`, `test.sh`)          |
| `tools/`     | Internal helper/utility scripts                                       |
| `data/`      | Local data storage (git-ignored)                                      |
| `logs/`      | Execution logs (git-ignored)                                          |
| `ai_reports/`| AI operation summaries and reports (git-ignored)                      |

Within each folder, follow the industry-standard layout for the language in use (e.g. `src/` layout for Python packages).

AI must organise files inside `ai_reports/` into date-based subfolders (`YYYY-MM-DD/`) so reports are easy to locate over time.

## Environment Variables

Maintain a `.env.example` file at the project root documenting all available environment variables with placeholder values. Never commit a populated `.env` file.
