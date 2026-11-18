# Repository instructions

## Scope
Applies throughout the repository. Complete only the assigned exercise. Other prompts describe independent trials.

## Layout
- `telemetry/` contains production code. `__main__.py` is the CLI.
- `tests/` contains unittest tests. `examples/` contains a small input fixture.
- `exercises/` defines task contracts. `benchmark/` is operator-owned.

## Implementation
Target Python 3.12. Keep runtime dependencies in the standard library. Preserve existing public APIs and CLI behavior except where the assigned prompt changes them. Add focused tests for normal and boundary cases. Keep existing baseline tests intact.

## Verification and handoff
Run `python -m unittest discover -s tests -v` from the root. Run the relevant CLI example for CLI changes. Report files changed, tests run, results and unresolved issues. Leave run records, rubric, prompts and coverage settings to the operator.
