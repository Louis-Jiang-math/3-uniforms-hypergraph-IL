# Project-specific agent instructions

The reusable write protocol is [`agent.md`](agent.md). Read it before mutating any file.
This file contains only rules specific to this repository.

## Authoritative state

Read in this order:

1. `HANDOFF_CURRENT.md`
2. `docs/PROJECT_STATE.yaml`
3. `docs/PROOF_DAG.md`
4. `knowledge/FACTS.md`
5. `knowledge/FAILURES.md`
6. `knowledge/QUESTIONS.md`
7. the relevant file under `docs/framework/`
8. relevant code, tests, and evidence

Raw conversations under `sources/raw/` and legacy frameworks under `history/` are historical sources, not canonical status.

## Current mathematical status

- The one-quarter theorem is open.
- The single active proof node is `G1c / Q-0015`: quantitative control of named E exits.
- Q-0016 and Q-0017 are open.
- Future-complete lift is a formal supporting result, not a general entrance theorem.
- AMCG is a specification, not a theorem that every target instance supplies such an interface.
- Ordinary transition capping is not an accepted proof of the `11/27` normal form.

## Project-specific integrity rules

The implementation and mathematics must distinguish:

1. root/configuration budget;
2. projection-sensitive slot capacity;
3. global real-edge capacity.

Do not merge execution states solely because their current traces or compressed signatures agree. Preserve real-edge identity, root projection, genealogy, blocker provenance, and ledger usage.

Do not infer complete real support from projected support, phase data, monodromy, or partial support. Do not use finite computation as a general proof.

## Writable areas

- `src/`, `tests/`, `tools/`, `enumerate/`: implementation and verification;
- `knowledge/`: canonical registries;
- `docs/framework/`: normative mathematical interfaces;
- `evidence/`: proofs, audits, experiment reports, baselines, and certificates;
- `HANDOFF_CURRENT.md`: current snapshot, updated last;
- `sources/raw/` and `history/`: read-only except for adding new immutable source material or migration indexes.

Compatibility stubs at repository root must remain short and must point to their canonical location.

## Required validation

For any implementation or canonical-document change, run:

```bash
python -m compileall -q src enumerate tools tests
python -m pytest -q
python tools/check_repository.py
python tools/check_generated_artifacts.py
python enumerate/q0015_configuration_auditor.py --regressions-only --output-dir artifacts/runs/q0015
```

Do not commit or push automatically.
