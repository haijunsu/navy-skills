# navy-skills

My AI skills and sharable rules.

## AI Rules Submodule

The `ai-rules/` directory contains sharable AI behavior and coding rules designed to be used across multiple projects via Git submodules.

### Installation

To add these rules to your project:

```bash
git submodule add git@github.com:haijunsu/navy-skills.git <submodule-path>
```

### Agent Configuration

After adding the submodule, you can automatically configure your AI agents (Claude, Gemini, Copilot, and OpenCode) to use these rules:

```bash
./<submodule-path>/scripts/rules_validation/validate_and_apply_rules.sh
```

The script dynamically detects your project root and the relative path to the rules, ensuring that all agent configuration files (`CLAUDE.md`, `GEMINI.md`, etc.) are created or updated with the correct paths.

### Updating Rules

To pull the latest rules into your project:

```bash
git submodule update --remote <submodule-path>
```
