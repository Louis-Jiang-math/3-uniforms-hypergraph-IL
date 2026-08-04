# Project-specific agent instructions

The reusable write protocol is [`agent.md`](agent.md). Read it before mutating any file.
This file contains only rules specific to this repository.

## Authoritative state

Read in this order:

1. `HANDOFF_CURRENT.md`
2. `docs/MAIN_PROOF_ROUTE.md`
3. `docs/PROJECT_STATE.yaml`
4. `docs/PROOF_DAG.md`
5. `knowledge/DECISIONS.md`
6. `knowledge/FACTS.md`
7. `knowledge/FAILURES.md`
8. `knowledge/QUESTIONS.md`
9. the relevant file under `docs/framework/`
10. relevant code, tests, and evidence

Raw conversations under `sources/raw/` and legacy frameworks under `history/` are
historical sources, not canonical status.

## Current mathematical status

- The one-quarter theorem is open.
- The active proof strategy is **Route B: critical stability**.
- The single active proof node is `S1 / Q-0018`: faithful global
  Round-or-Core entrance and natural defect.
- D-0012 fixes the implementation route: root-only canonical excess (F-0070),
  actual switch-cube core defect (Q-0016 candidate), F-0041 fresh-leaf resource
  split, then actual three-cylinder regeneration and F-0042.
- `Q-0017` is the zero-defect global normal-form problem.
- `Q-0016` is the actual-support Core Endgame problem.
- F-0055 closes only the exact execution-tree/pathwise finite interface. The
  current genuine closure map is the root-excess clean-chart reduction,
  fresh-leaf/overflow conversion, and the actual switch-cube Core Endgame. Critical-profile and
  heavy-pair work are subcontracts of the first item; the existing stability
  algebra remains conditional on faithful zero- or vanishing-loss input.
- Route A (`Q-0002/Q-0015`, near-lossless charging and aggregate heavy-excess
  dissipation) is suspended as a main route. Its formal modules remain usable as
  supporting lemmas and regression infrastructure.
- `F-0034` and `F-0042` remain conditional sufficient criteria; they do not
  reactivate Route A.
- No theorem or question is closed by this strategy change.

## Route-B anti-drift rules

Do not:

1. refresh a root two-step actual-edge capacity along release descendants;
2. require all residual mass to acquire an independent charging entitlement;
3. treat \(1/4\) as a theorem of \(100\%\) residual conversion;
4. redefine a defect so that the desired terminal structure is true by definition;
5. promote a new Hall cut, token, quotient candidate, or obstruction name to main
   progress unless it yields an exact zero-defect classification, a strict
   monotone quantity, a real \(1/4\) link, an IT, or a complete-block contradiction;
6. treat local same-pivot windows as a global single-pivot cylinder;
7. treat reversible genealogy or phase consistency as product support;
8. treat splice as a free repeatable closure operation.

Reactivating Route A requires an explicit decision in `knowledge/DECISIONS.md`
and synchronized changes to the handoff, project state, proof DAG, questions, and
repository checker.

## Project-specific integrity rules

The implementation and mathematics must distinguish:

1. root/configuration budget;
2. projection-sensitive slot capacity;
3. global real-edge capacity.

Do not merge execution states solely because their current traces or compressed
signatures agree. Preserve real-edge identity, root projection, genealogy,
blocker provenance, and ledger usage.

Do not infer complete real support from projected support, phase data, monodromy,
or partial support. Do not use finite computation as a general proof.

## Writable areas

- `src/`, `tests/`, `tools/`, `enumerate/`: implementation and verification;
- `knowledge/`: canonical registries;
- `docs/framework/`: normative mathematical interfaces;
- `evidence/`: proofs, audits, experiment reports, baselines, and certificates;
- `HANDOFF_CURRENT.md`: current snapshot, updated last;
- `sources/raw/` and `history/`: read-only except for adding new immutable source
  material or migration indexes.

Compatibility stubs at repository root must remain short and must point to their
canonical location.

## Required validation

For any implementation or canonical-document change, run:

```bash
python -m compileall -q src enumerate tools tests
python -m pytest -q
python tools/check_repository.py
python tools/check_generated_artifacts.py
python enumerate/q0015_configuration_auditor.py --regressions-only --output-dir artifacts/runs/q0015
python enumerate/q4_splice_pay_cylinder_validation.py
```

Do not commit or push automatically.
