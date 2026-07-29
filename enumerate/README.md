# Enumeration and audit entry points

This directory contains CLI wrappers and schemas. Committed evidence lives under `evidence/experiments/`; ad-hoc run output defaults to `artifacts/runs/`, which is ignored by Git.

## Run

```bash
python enumerate/q0015_configuration_auditor.py --regressions-only --output-dir artifacts/runs/q0015
python enumerate/q0015_configuration_auditor.py --iterations 3 --time-limit 1 --output-dir artifacts/runs/q0015
python enumerate/q0015_reset_compensation.py --output artifacts/runs/q0015/reset_compensation_results.json
```

Every output is written atomically and contains generator, command, parameters, source commit, result type, timestamp, and payload SHA-256.

The reset-compensation command performs a bounded exhaustive check of all
\(2^8\) transversal-edge subsets on three blocks of size two. Its result is a
finite counterexample certificate, not a general positive theorem.

## Regenerate the committed baseline

```bash
python tools/regenerate_baseline.py
python tools/check_generated_artifacts.py
```

The outer search is bounded and may return an iteration-limit or unresolved status. Such a result is not a proof or counterexample.
