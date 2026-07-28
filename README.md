# Independent transversals in partitioned 3-uniform hypergraphs

This repository studies the independent-transversal threshold for equal-block partitioned 3-uniform hypergraphs, with the target implication

\[
\Delta(H)<\left(rac14-o(1)
ight)b^2
\Longrightarrow H	ext{ has an independent transversal.}
\]

## Current status

The one-quarter theorem is **open**. The only active main-proof node is:

> **G1c / Q-0015 — quantitative control of named E exits.**

The current logical path is

\[
	ext{configuration entrance}
	o 	ext{persistent-blocker normal form}
	o 	ext{causal regeneration}
	o 	ext{terminal counting}
	o rac14.
\]

A formal future-complete lift is available after an actual Q-0015 root obstacle has already been constructed, but it does not provide the general entrance or downstream concentration theorem.

## Ten-minute start

1. [`docs/QUICKSTART_10_MINUTES.md`](docs/QUICKSTART_10_MINUTES.md)
2. [`HANDOFF_CURRENT.md`](HANDOFF_CURRENT.md)
3. [`docs/PROOF_DAG.md`](docs/PROOF_DAG.md)
4. [`AGENTS.md`](AGENTS.md)
5. [`knowledge/FACTS.md`](knowledge/FACTS.md)
6. [`knowledge/FAILURES.md`](knowledge/FAILURES.md)
7. [`knowledge/QUESTIONS.md`](knowledge/QUESTIONS.md)

## Information architecture

- `agent.md`: reusable repository-write protocol;
- `AGENTS.md`: project-specific constraints;
- `knowledge/`: canonical facts, failures, questions, decisions, and definitions;
- `docs/framework/`: normative mathematical interfaces;
- `evidence/`: audits, experiment baselines, reports, proofs, and certificates;
- `src/`, `tests/`, `tools/`, `enumerate/`: executable proof-engineering infrastructure;
- `sources/raw/`: immutable source conversations and manifests;
- `history/`: superseded and monolithic documents;
- `HANDOFF_CURRENT.md`: clean current snapshot, not a changelog.

## Install and validate

```bash
python -m pip install -r requirements.txt
python -m pip install -e . --no-build-isolation
python -m compileall -q src enumerate tools tests
python -m pytest -q
python tools/check_repository.py
python tools/check_generated_artifacts.py
python enumerate/q0015_configuration_auditor.py --regressions-only --output-dir artifacts/runs/q0015
```

## Source baseline

The public source baseline is commit `cfadd24b52546d4d5800c4a3c5a75a2add86f928` dated 2026-07-28. See [`docs/BASELINE.md`](docs/BASELINE.md).
