# Copilot Instructions

This workspace contains scripts for the game **The Farmer Was Replaced**. The
game does not run a full Python interpreter — it uses its own interpreter
that accepts Python-like syntax with a reduced/altered feature set. Treat
this as the target language for all code in this repo, not standard Python.

The scripts cannot be tested using regular Python interpreters, they must only be
run within the game's interpreter.

## Missing features (do not use)

- No list methods other than `append`, `pop`, `remove`.
- No dict methods other than `pop`.
- No set methods other than `add`, `remove`.
- No methods on strings or numbers.
- No classes.
- No lambdas.
- No `int(x)` — use `x // 1` to floor instead.
- No `async`/`await`.
- No named arguments.
- No `*args` / `**kwargs`.
- No list comprehensions.
- No ternary operator (`a if condition else b`).
- If a missing built-in is needed, implement an equivalent function locally.

## Behavior differences from real Python

- All numbers are floats, not ints; arithmetic can produce inexact results.
- Default parameter values bind at call time, not at function definition time.
- `a, b += tuple` creates a new tuple appended at the end, not element-wise addition.
- List indices are rounded, so `lst[1.2]` is valid and equivalent to `lst[1]`.
- `range()` supports fractional bounds/step, e.g. `range(0, 1, 0.1)`.
- Method-call syntax `x.foo(y)` is supported as sugar for `foo(x, y)`.
- `print(x)` prints to in-game smoke, not stdout; use `quick_print(x)` to write to `output.txt`.

## Style rules

- Follow the repository's `.editorconfig` file.
- Use literal tab characters for indentation; never use spaces for indentation.
- Treat one tab as four spaces for display and alignment.
- Preserve the existing indentation and formatting style when editing code.
- Keep changes focused on the requested behavior and avoid unrelated refactoring.
- Preserve existing public names and calling conventions unless the task explicitly requires a change.
- Add comments only when they explain non-obvious behavior.
