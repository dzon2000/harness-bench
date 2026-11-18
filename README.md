# Harness Bench
Compare coding agents on a small industrial telemetry project. Every exercise starts from the same commit. A reading has a machine ID, an integer event time in Unix seconds and a numeric value.

## Quick start
Use Python 3.12, from the checkout root.

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python -m telemetry examples/readings.csv
```

The CLI prints the most recent value per machine as JSON. The runtime and unit tests use only the standard library. Coverage measurement uses coverage.py.

## Exercises
Copy the entire contents of ONE prompt into a fresh agent session.

| Prompt | Work type |
|---|---|
| [01. Out-of-order readings](exercises/01-ordering.md) | Diagnose and fix a regression |
| [02. Threshold alarms](exercises/02-alarms.md) | Implement stateful domain logic |
| [03. Stream the CSV reader](exercises/03-stream.md) | Refactor while preserving an API |
| [04. SQLite history](exercises/04-history.md) | Add transactional persistence |
| [05. Window report](exercises/05-report.md) | Deliver an end-to-end CLI feature |

Use the [run protocol and review rubric](benchmark/PROTOCOL.md) and [run record](benchmark/run.json).
