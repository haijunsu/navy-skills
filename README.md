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

After adding the submodule, run the validation script to configure your AI agents (Claude, Gemini, Copilot, and OpenCode):

```bash
./<submodule-path>/scripts/rules_validation/validate_and_apply_rules.sh
```

This script dynamically detects your project root and the relative path to the rules, then creates or updates all agent config files (`CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `AGENTS.md`) with the correct rule paths.

Re-run it any time you add or rename rule files to keep all agent configs in sync.

### Updating Rules

To pull the latest rules into your project:

```bash
git submodule update --remote <submodule-path>
```

Then re-run the agent configuration script to apply any new or changed rules:

```bash
./<submodule-path>/scripts/rules_validation/validate_and_apply_rules.sh
```

### Syncing the Submodule

If you cloned the parent repo without `--recurse-submodules`, the `navy-skills` directory will be empty. Run these git commands manually from your **parent repo root**:

```bash
git pull
git submodule update --init --recursive
```

Then apply the rules:

```bash
./<submodule-path>/scripts/rules_validation/validate_and_apply_rules.sh
```

Once the submodule is initialized, you can use the sync script to pull future updates when the parent repo updates its submodule pointer:

```bash
./<submodule-path>/scripts/rules_validation/sync_submodule.sh
```

Then re-apply the rules if anything changed:

```bash
./<submodule-path>/scripts/rules_validation/validate_and_apply_rules.sh
```
