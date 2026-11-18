# Run protocol

1. Record the baseline SHA once with `git rev-parse HEAD`. Use a clean worktree from that exact SHA for every harness × exercise × repetition. Example: `git worktree add -b runs/pi/01/r1 ../hb-pi-01 BASELINE_SHA`. Preinstall the same Python and development dependency in each environment.
2. Start a fresh session in that worktree. Keep model/version, reasoning level, permissions, network, plugins, hardware and timeout fixed where supported. Record differences. If models differ, label the comparison harness + model. Rotate harness order across repetitions. One pass per harness is a pilot; use three or more for timing comparisons.
3. Copy benchmark/run.json outside the worktree. Paste only the selected prompt verbatim. Start wall time at submission. Stop when the harness declares completion, fails, or reaches the preselected timeout. Include tool waits and human response time. Log every blocking question or approval, including unanswered requests. Record unsolicited operator help separately and retain exact replies. Never give another harness's solution as a hint.
4. Commit the resulting code and tests on the run branch, even if incomplete. Capture its SHA. Keep main at baseline. For review, publish the branch and attach the completed run record and sanitized transcript or usage evidence separately. Remove tokens and private paths before sharing in this public repo.
5. Independently rerun the commands below on the solution SHA. Use both baseline and agent-added tests. The startup hook measures subprocess CLI tests too (POSIX shell, active virtual environment). Use a temporary directory with no spaces for the hook.

```sh
hook=$(mktemp -d)
echo 'import coverage; coverage.process_startup()' > "$hook/sitecustomize.py"
export COVERAGE_PROCESS_START="$PWD/.coveragerc"
export PYTHONPATH="$hook:$PWD${PYTHONPATH:+:$PYTHONPATH}"
export COVERAGE_FILE="$PWD/.coverage"
python -m unittest discover -s tests -v
unset COVERAGE_PROCESS_START
python -m coverage combine
python -m coverage report -m
python -m coverage json -o /tmp/hb-coverage.json
```

Use a clean worktree to avoid old coverage shards. Record test exit status even on failure. Read totals.covered_lines / totals.num_statements and totals.covered_branches / totals.num_branches from the JSON. Record counts, not combined coverage.py percentage. Zero denominator means unavailable. Inspect per-file gaps. Compare coverage within the same exercise.

## Measurements
- Time: wall seconds and human wait seconds. Keep failures and timeouts in results.
- Human interventions: count blocking requests by category (permission or clarification), plus unsolicited assists. Where possible, distinguish harness UI approvals from model questions.
- Cost: record provider-reported billed amount, currency, tokens by type and premium requests when available. Subscription usage with no per-run price is unknown. Keep estimates separate with rate source and date. Use null for unavailable values and zero only for measured zero.
- Quality: reviewer scores four dimensions from 0–2 each. Correctness: 0 core behavior fails, 1 partial contract, 2 all stated examples and boundaries pass independent checks. Compatibility: 0 baseline broken, 1 partial regression or scope drift, 2 baseline and scope preserved. Test strength: 0 absent or ineffective, 1 happy path only or gaps, 2 meaningful normal and edge/regression assertions. Maintainability: 0 fragile or opaque, 1 workable with specific issues, 2 clear idiomatic code meeting resource/lifecycle requirements. Record evidence and total /8. Report contract failures explicitly even if total is high.
- Review procedure: blind harness names during scoring if practical. Rerun the same independent cases against every solution for an exercise. Apply those checks separately from submitted-suite coverage. Summarize completion rate plus median elapsed time, requests and known cost per exercise. Keep unknown costs visible.
