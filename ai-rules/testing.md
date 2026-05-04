# Testing Rules

- **Tooling**: Use **pytest** for all tests.
- Test method names must follow the pattern: `test_<function_under_test>_<purpose>` (e.g. `test_calculate_total_with_discount`).
- Mock and fixture data must be realistic and meaningful relative to the function being tested — no placeholder values like `foo`, `bar`, `123`, or `test`.
- No single-letter variable names anywhere in test code.
