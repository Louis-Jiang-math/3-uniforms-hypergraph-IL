# Enumeration and audit entry points

This directory contains CLI wrappers and schemas. Committed evidence lives under `evidence/experiments/`; ad-hoc run output defaults to `artifacts/runs/`, which is ignored by Git.

## Run

```bash
python enumerate/q0015_configuration_auditor.py --regressions-only --output-dir artifacts/runs/q0015
python enumerate/q0015_configuration_auditor.py --iterations 3 --time-limit 1 --output-dir artifacts/runs/q0015
```

Every output is written atomically and contains generator, command, parameters, source commit, result type, timestamp, and payload SHA-256.

## Regenerate the committed baseline

```bash
python tools/regenerate_baseline.py
python tools/check_generated_artifacts.py
```

The outer search is bounded and may return an iteration-limit or unresolved status. Such a result is not a proof or counterexample.
