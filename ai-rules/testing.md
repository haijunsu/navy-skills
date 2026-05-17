# Testing Rules

## Python / pytest

- **Tooling**: Use **pytest** for all tests.
- Test method names must follow the pattern: `test_<function_under_test>_<purpose>` (e.g. `test_calculate_total_with_discount`).
- Mock and fixture data must be realistic and meaningful relative to the function being tested — no placeholder values like `foo`, `bar`, `123`, or `test`.
- No single-letter variable names anywhere in test code.

## Frontend / React (Jest + Testing Library)

- Run tests with: `CI=true npm test -- --testPathPattern=<ComponentName> --watchAll=false`
- For animation or transition behavior, use `@testing-library/user-event` to verify that the correct direction state or `custom` prop values are set — not just that callbacks fire with the right arguments.
  - **Why:** framer-motion mocks strip animation behavior, so verifying the triggering state (e.g. `direction` value) is the only way to confirm slide direction without manual browser inspection.
- Add `data-testid` attributes where needed to make CSS values testable via inline style.
