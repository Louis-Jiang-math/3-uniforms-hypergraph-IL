# Independent transversals in partitioned 3-uniform hypergraphs

This repository studies the independent-transversal threshold for equal-block
partitioned 3-uniform hypergraphs, with the target implication

\[
\Delta(H)<\left(\frac14-o(1)\right)b^2
\Longrightarrow H\text{ has an independent transversal.}
\]

## Current status

The one-quarter theorem is **open**. The active proof strategy is now:

> **Route B — critical stability.**

The single active node is:

> **S1 / Q-0018 — faithful global execution and natural defect decomposition.**

The current logical path is

\[
\text{faithful execution object}
\to \text{zero-defect global normal form}
\to \text{reversible-core saturation}
\to \text{terminal }1/4\text{ structure}
\to \varepsilon\text{-stability}.
\]

Route A—the near-lossless configuration/escape-flow and aggregate
heavy-excess-dissipation program—is temporarily suspended as a main route.
Its proved modules remain available as supporting tools:

- future-complete lift;
- no-configuration retyping;
- old-anchor temporal Lyapunov;
- aggregate pair-cylinder normalization;
- pair-flat/heavy-excess orthogonalization;
- future-compatible orientation accounting;
- conditional recurrence criteria.

The strategy change does **not** close Q-0015, Q-0016, Q-0017, or the
one-quarter theorem. It changes what counts as main progress: the project now
seeks an exact zero-defect structure theorem and a quantitative stability
upgrade, rather than a unit-by-unit charging of all residual mass.

## Ten-minute start

1. [`docs/QUICKSTART_10_MINUTES.md`](docs/QUICKSTART_10_MINUTES.md)
2. [`HANDOFF_CURRENT.md`](HANDOFF_CURRENT.md)
3. [`docs/PROOF_DAG.md`](docs/PROOF_DAG.md)
4. [`docs/framework/FW-60_CRITICAL_STABILITY_ROUTE.md`](docs/framework/FW-60_CRITICAL_STABILITY_ROUTE.md)
5. [`AGENTS.md`](AGENTS.md)
6. [`agent.md`](agent.md)
7. [`knowledge/DECISIONS.md`](knowledge/DECISIONS.md)
8. [`knowledge/FACTS.md`](knowledge/FACTS.md)
9. [`knowledge/FAILURES.md`](knowledge/FAILURES.md)
10. [`knowledge/QUESTIONS.md`](knowledge/QUESTIONS.md)

## Protocol split

- `agent.md`: short mandatory write protocol;
- `WORKFLOW.md`: detailed explanations, templates, and examples;
- `AGENTS.md`: project-specific mathematical and repository constraints.

Agents should read the short protocol on every write task and load the detailed
workflow only when its templates or explanations are needed.

## Information architecture

- `knowledge/`: canonical facts, failures, questions, decisions, and definitions;
- `docs/framework/`: normative mathematical interfaces;
- `evidence/`: audits, experiment baselines, reports, proofs, and certificates;
- `src/`, `tests/`, `tools/`, `enumerate/`: executable proof-engineering infrastructure;
- `sources/raw/`: immutable source conversations and manifests;
- `history/`: superseded and monolithic documents;
- `HANDOFF_CURRENT.md`: clean current snapshot, not a changelog.

## Install and validate

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install -e ".[test]" --no-build-isolation
python -m compileall -q src enumerate tools tests
python -m pytest -q
python tools/check_repository.py
python tools/check_generated_artifacts.py
python enumerate/q0015_configuration_auditor.py \
  --regressions-only \
  --generated-at 2026-07-28T00:00:00Z \
  --output-dir artifacts/runs/q0015
python enumerate/q4_splice_pay_cylinder_validation.py
```

## Source baseline

The public source baseline is commit
`cfadd24b52546d4d5800c4a3c5a75a2add86f928` dated 2026-07-28.
See [`docs/BASELINE.md`](docs/BASELINE.md).
