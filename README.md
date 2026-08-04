# Independent transversals in partitioned 3-uniform hypergraphs

This repository studies the independent-transversal threshold for equal-block
partitioned 3-uniform hypergraphs, with the target implication

\[
\Delta(H)<\left(\frac14-o(1)\right)b^2
\Longrightarrow H\text{ has an independent transversal.}
\]

## Current status

The one-quarter theorem is **open**. The active proof strategy is:

> **Route B — critical stability.**

The single active DAG node remains:

> **S1 / Q-0018 — faithful global Round-or-Core entrance and natural defect.**

D-0012 now fixes the implementation sequence:

\[
\boxed{
\text{root-only canonical excess}
\to
\text{actual switch-cube core defect}
\to
\text{fresh saturated-leaf conversion}
\to
\text{F-0042}.
}
\]

The authoritative route map is
[`docs/MAIN_PROOF_ROUTE.md`](docs/MAIN_PROOF_ROUTE.md).

Recent verified supporting progress is:

- F-0068: for fixed actual edges \(e,f\), the output \(f\) can arise from at
  most one switch slot of \(e\), uniformly over completion contexts;
- F-0069: perfect switch-transition cycles have trivial monodromy and split
  into completion sheets;
- F-0070: original two-step failure roots admit an exact root-only canonical
  excess normalization
  \[
  \frac{\sum_{k\in I}\mathcal B_k}{b^2S_I}
  \le
  (1+\eta)\frac{\Delta(H)}{b^2}+\Xi_I.
  \]

These facts do **not** close Q-0016 or Q-0018. The current open mathematical
steps are:

1. prove the Q-0016 actual switch-cube defect theorem on finite all-release
   cores, keeping all intermediate actual supports and a bounded first-
   nonliteral assignment;
2. reduce the root excess \(\Xi_I\) to clean-chart mismatch, F-0038 deficit,
   fresh saturated leaves, and repeat/core mass in the same interval units;
3. split fresh leaves by F-0041 into edge/support/token/repeat outcomes and
   prove the actual three-cylinder regeneration theorem for the pure token
   branch;
4. convert any remaining unbounded exact-future interface growth into those
   actual outcomes or a positive-mass core.

Root two-step capacity is not refreshed along release descendants. Descendant
blockers are structural/resource/core data, not new copies of the recurrence
capacity. Route A remains suspended as a main route, although its exact mass
identities, Hall tools, and F-0042 backend remain available as supporting
modules.

No open question or theorem is closed by this route clarification.

## Ten-minute start

1. [`docs/QUICKSTART_10_MINUTES.md`](docs/QUICKSTART_10_MINUTES.md)
2. [`HANDOFF_CURRENT.md`](HANDOFF_CURRENT.md)
3. [`docs/MAIN_PROOF_ROUTE.md`](docs/MAIN_PROOF_ROUTE.md)
4. [`docs/PROOF_DAG.md`](docs/PROOF_DAG.md)
5. [`docs/framework/FW-60_CRITICAL_STABILITY_ROUTE.md`](docs/framework/FW-60_CRITICAL_STABILITY_ROUTE.md)
6. [`AGENTS.md`](AGENTS.md)
7. [`agent.md`](agent.md)
8. [`knowledge/DECISIONS.md`](knowledge/DECISIONS.md)
9. [`knowledge/FACTS.md`](knowledge/FACTS.md)
10. [`knowledge/FAILURES.md`](knowledge/FAILURES.md)
11. [`knowledge/QUESTIONS.md`](knowledge/QUESTIONS.md)

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
