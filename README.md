# navy-skills

My AI skills and sharable rules.

## AI Rules Submodule

The `ai-rules/` directory (or any directory name you choose) contains sharable AI behavior and coding rules designed to be used across multiple projects via Git submodules.

### Installation

To add these rules to your project:

```bash
git submodule add git@github.com:haijunsu/navy-skills.git <submodule-name>
```

### Agent Configuration

After adding the submodule, you can automatically configure your AI agents:

```bash
./<submodule-name>/scripts/rules_validation/validate_and_apply_rules.sh
```

The script will automatically detect the submodule name and the project root, and it will create or update the following configuration files:

#### Claude Code (`CLAUDE.md`)
Points Claude to the submodule for rules.

#### Gemini CLI (`GEMINI.md`)
Adheres to the standards and provides a rule index.

#### GitHub Copilot (`.github/copilot-instructions.md`)
Follows the project standards and workflows.

#### OpenCode (`AGENTS.md`)
References the rules for consistency across agents.

### Manual Configuration

If you prefer to configure agents manually, follow these templates (replacing `<submodule-name>` with your chosen directory):

#### Claude Code
Create or update `CLAUDE.md`:

```markdown
# CLAUDE.md
Rules for this repository are managed in the `<submodule-name>/` submodule.
```

#### Gemini CLI
Create or update `GEMINI.md`:

```markdown
# Project Instructions
This project adheres to the standards defined in the `<submodule-name>/` submodule.

## Rule Index
- [Tech Stack](<submodule-name>/stack.md)
- [Code Style](<submodule-name>/code-style.md)
- [Workflow](<submodule-name>/workflow.md)
```

#### GitHub Copilot CLI / Chat
Create `.github/copilot-instructions.md`:

```markdown
# Copilot Instructions
Follow the project standards and workflows defined in the `<submodule-name>/` directory:
- Tech Stack: <submodule-name>/stack.md
- Code Style: <submodule-name>/code-style.md
- Workflow: <submodule-name>/workflow.md
```

#### OpenCode
Create or update `AGENTS.md`:

```markdown
# AGENTS.md
Rules for this repository are managed in the `<submodule-name>/` submodule.
Refer to the rules in:
- [<submodule-name>/stack.md](<submodule-name>/stack.md)
- [<submodule-name>/code-style.md](<submodule-name>/code-style.md)
- [<submodule-name>/workflow.md](<submodule-name>/workflow.md)
```

### Updating Rules

To pull the latest rules into your project:

```bash
git submodule update --remote <submodule-name>
```
