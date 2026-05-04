# navy-skills

My AI skills and sharable rules.

## AI Rules Submodule

The `ai-rules/` directory contains sharable AI behavior and coding rules designed to be used across multiple projects via Git submodules.

### Installation

To add these rules to your project:

```bash
git submodule add git@github.com:haijunsu/navy-skills.git ai-rules
```

### Agent Configuration

After adding the submodule, configure your AI agents to use these rules.

#### Claude Code
Create or update `CLAUDE.md` in your project root to point to the submodule:

```markdown
# CLAUDE.md
Rules for this repository are managed in the `ai-rules/` submodule.
```

#### Gemini CLI
Create or update `GEMINI.md` in your project root. Gemini CLI automatically discovers instructions in `GEMINI.md` files.

```markdown
# Project Instructions
This project adheres to the standards defined in the `ai-rules/` submodule.

## Rule Index
- [Tech Stack](ai-rules/stack.md)
- [Code Style](ai-rules/code-style.md)
- [Workflow](ai-rules/workflow.md)
```

#### GitHub Copilot CLI / Chat
For GitHub Copilot, create `.github/copilot-instructions.md` in your project root:

```markdown
# Copilot Instructions
Follow the project standards and workflows defined in the `ai-rules/` directory:
- Tech Stack: ai-rules/stack.md
- Code Style: ai-rules/code-style.md
- Workflow: ai-rules/workflow.md
```

#### OpenCode
Create or update `AGENTS.md` in your project root:

```markdown
# AGENTS.md
Rules for this repository are managed in the `ai-rules/` submodule.
Refer to the rules in:
- [ai-rules/stack.md](ai-rules/stack.md)
- [ai-rules/code-style.md](ai-rules/code-style.md)
- [ai-rules/workflow.md](ai-rules/workflow.md)
```

### Updating Rules

To pull the latest rules into your project:

```bash
git submodule update --remote ai-rules
```
