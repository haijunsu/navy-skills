# Workflow Rules

- Always start in plan mode. Before writing any code, produce a design plan that covers architecture, data flow, and key decisions.
- Present the plan to the user and wait for explicit approval before generating any code.
- If requirements change mid-task, return to plan mode and re-seek approval before proceeding.

## When to Follow This Workflow

This workflow is required for all substantive work: feature requests, bug fixes, and new tools. Follow it whenever you are asked to implement, fix, or build something non-trivial.

## File Naming Prefixes

Requirements, plans, solutions, checklists, and summaries must use a meaningful name with one of these prefixes based on work type:

| Work type             | Prefix  | Example                 |
| --------------------- | ------- | ----------------------- |
| Feature / requirement | `req-`  | `req-dark-mode.md`      |
| Bug fix               | `bug-`  | `bug-login-redirect.md` |
| New tool / script     | `tool-` | `tool-image-resize.md`  |

Never use numeric IDs like `fr-1.md` or `req-001.md`. Names must describe the work, not number it.

## Implementation Procedure

Follow these steps before writing any code:

1. Ensure a requirements file exists at `docs/requirements/<prefix>-<name>.md`. Create it if the user has not already provided one.
2. Read all affected components to understand their current state.
3. Write `docs/solutions/<prefix>-<name>-solutions.md` — one section per solution; each section has: **Addresses** (requirement name), **Current state**, **Solution**, **Files touched**. Use inline bold labels, not sub-headings, to avoid duplicate heading lint errors.
4. Write `docs/plan/<prefix>-<name>-plan.md` — numbered phases; each phase header includes `**Req:** <requirement-name> | **Solution:** <solution-name> | **File:** path`; include a step table and a short test description.
5. Write `docs/checklists/<prefix>-<name>-checklist.md` — one checkbox per step, per acceptance criterion, and a `Human approve Phase N` item at the end of each phase.
6. Present a summary to the user and **wait for approval** before touching any code.
7. Implement one phase at a time:
   a. Make the code change
   b. Write unit tests covering the changed behavior (add `data-testid` attributes where needed to make CSS values testable via inline style)
   c. Run tests with `CI=true npm test -- --testPathPattern=<ComponentName> --watchAll=false`
   d. Only mark Verify items `[x]` after tests pass — never pre-check them
   e. Add a `Human approve Phase N` checkbox — only mark it when the user explicitly approves
8. After tests pass (before asking for human approval), immediately write/update `docs/summaries/<prefix>-<name>-summary.md`:
   - Set status to "Complete — pending human approval"
   - List every changed file and what changed
   - List the test file and each test with its result
   - Commit the summary, then present it to the user and ask for approval
9. When the user approves, update the summary: set status to Complete, log approval with date, commit.
10. **Never create a PR until the summary is written, approved, and committed.** The summary commit must appear in the PR diff.

**File naming convention:** always suffix with `-solutions`, `-plan`, `-checklist`, `-summary` so files in different folders have distinct names.
