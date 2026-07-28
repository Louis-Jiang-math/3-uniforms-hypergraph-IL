# Independent transversals in partitioned 3-uniform hypergraphs

This repository studies the independent-transversal threshold for equal-block
partitioned 3-uniform hypergraphs, with the target implication

\[
\Delta(H)<\left(\frac14-o(1)\right)b^2
\Longrightarrow H\text{ has an independent transversal.}
\]

## Current status

The one-quarter theorem is **open**. The only active main-proof node is:

> **G1c / Q-0015 — quantitative control of named E exits.**

The current logical path is

\[
\text{configuration entrance}
\to \text{persistent-blocker normal form}
\to \text{causal regeneration}
\to \text{terminal counting}
\to \frac14.
\]

A formal future-complete lift is available after an actual Q-0015 root obstacle
has already been constructed, but it does not provide the general entrance or
downstream concentration theorem.

## Ten-minute start

1. [`docs/QUICKSTART_10_MINUTES.md`](docs/QUICKSTART_10_MINUTES.md)
2. [`HANDOFF_CURRENT.md`](HANDOFF_CURRENT.md)
3. [`docs/PROOF_DAG.md`](docs/PROOF_DAG.md)
4. [`AGENTS.md`](AGENTS.md)
5. [`agent.md`](agent.md)
6. [`knowledge/FACTS.md`](knowledge/FACTS.md)
7. [`knowledge/FAILURES.md`](knowledge/FAILURES.md)
8. [`knowledge/QUESTIONS.md`](knowledge/QUESTIONS.md)

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
```

## Source baseline

The public source baseline is commit
`cfadd24b52546d4d5800c4a3c5a75a2add86f928` dated 2026-07-28.
See [`docs/BASELINE.md`](docs/BASELINE.md).
