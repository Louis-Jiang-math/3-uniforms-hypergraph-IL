# Q-0015 aggregate heavy-excess update

```text
Base commit:
  1da38011d28643eb8a3d35aa727d5fb206aacf41
Write mode:
  status-promotion for supporting facts; no question closure
Task:
  Integrate the current local no-configuration/temporal results with the new
  aggregate pair-cylinder, heavy-excess and reset-orientation results.
Target DAG node:
  G1c / Q-0015
Allowed paths:
  src/, tests/, enumerate/, evidence/, knowledge/, docs/, README.md,
  HANDOFF_CURRENT.md
Forbidden paths:
  sources/raw/, history/, old/, unrelated implementation
Claim status sought:
  proved-formal supporting facts; refuted-bounded-exhaustive immediate-reset
  claim; confirmed-conditional aggregate closing criterion
Acceptance criterion:
  preserve real identities and separate ledgers; executable counterexample;
  full required repository checks pass; Q-0015 remains active
Required validations:
  compileall; full pytest; repository checker; generated-artifact checker;
  Q-0015 regression CLI; reset artifact generation and hash validation
Final status:
  validated
```

## Non-goals

- no proof that the heavy-pair excess is sufficiently small;
- no polynomial orientation-token bound;
- no Q-0015, Q-0016, Q-0017 or one-quarter closure;
- no modification of raw or historical sources.


## Validation result

```text
python -m compileall -q src enumerate tools tests
  passed
python -m pytest -q
  24 passed
python tools/check_repository.py
  passed
python tools/check_generated_artifacts.py
  passed
python enumerate/q0015_configuration_auditor.py --regressions-only ...
  passed; payload ef02bf6446618026052c1a107913e4d015e3c8f3b48a59441a72afa09429a8ad
python enumerate/q0015_reset_compensation.py ...
  passed; exhaustive 255/256 counterexamples;
  payload 854f2a0560c78505691253a5d33cc0b4031107711bc77b6dd22b826f5a0a7248
git diff --check
  passed
```

No canonical question was closed. Supporting facts F-0037–F-0042 and failures
A-0027–A-0028 were promoted at their stated evidence strength.
