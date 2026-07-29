# Current Handoff

## Objective

Prove the independent-transversal threshold at \(1/4-o(1)\). The theorem remains open.

## Current state

- **Active node:** `G1c / Q-0015` — E-exit and aggregate heavy-excess control.
- **Formal local progress:** F-0037–F-0042 give no-configuration retyping, the old-anchor temporal Lyapunov theorem, exact aggregate normalization, a unified old/fresh pair-cylinder bound, the explicit heavy-pair excess \(\mathfrak H_k\), and future-compatible orientation-budget reset compensation.
- **Current blocker:** no theorem yet dissipates all \(\mathfrak H_k\) with sufficient strength, or converts all repeated sound tokens into accepted exact-future quotients while preserving genealogy and the separate ledgers.
- **Downstream status:** Q-0017 and Q-0016 remain open. The aggregate route may replace per-source flow only after it produces a uniform \(c_\varepsilon<1/4\) recurrence.

## Reliable inputs

- `knowledge/FACTS.md`: especially F-0029–F-0042;
- `docs/framework/FW-10_CONFIGURATION_ENTRY.md`;
- `docs/framework/FW-15_AGGREGATE_PAIR_CYLINDER.md`;
- `docs/framework/FW-30_PIVOT_SWITCH_ESCAPE.md`;
- `docs/framework/FW-40_FUTURE_COMPLETE_LIFT.md`;
- `evidence/proofs/Q0015_AGGREGATE_PAIR_CYLINDER_RESET.md`;
- `evidence/experiments/q0015/reports/q0015_external_old_anchor_temporal_stability.md`;
- `evidence/experiments/q0015/reports/q0015_reset_compensation_attack.md`;
- Q-0015 implementation and regression evidence under `src/`, `tests/`, `enumerate/`, and `evidence/experiments/q0015/`.

## Do not repeat

- Do not assume a common preassigned pivot.
- Do not merge distinct projections or genealogies by current trace alone.
- Do not replace root budget, slot capacity, and real-edge capacity by one resource.
- Do not close Q-0015 after controlling only one named E subclass.
- Do not treat the existence of one heavy pair as control of the full positive excess.
- Do not infer immediate quotient closure from “no new edge and no new support”; A-0028 requires an orientation budget.
- Do not use finiteness of the exact token space as a quantitative bound; it may be exponential.

## Open questions

1. **Q-0015:** prove quantitative heavy-pair dissipation for the full \(\mathfrak H_k\), or prove the original near-lossless configuration/escape flow.
2. **Q-0017:** derive a persistent-blocker critical normal form from a real near-lossless entrance.
3. **Q-0016:** prove causal regeneration or concentration without preinstalling a charging right.

## Immediate next actions

1. Construct a mass-preserving decomposition of \(\mathfrak H_k\) into labelled carrier trajectories.
2. Find a future-compatible orientation signature with a polynomial or linear weighted budget, or pay every new token using an independent real resource.
3. Prove that repeated sound tokens produce an accepted exact-future quotient or complete-block closure; then test whether F-0042 reaches \(c_\varepsilon<1/4\).

## Required reading

1. `AGENTS.md`
2. `agent.md`
3. `docs/PROOF_DAG.md`
4. `knowledge/FAILURES.md`
5. `knowledge/QUESTIONS.md#Q-0015`
6. `docs/framework/FW-15_AGGREGATE_PAIR_CYLINDER.md`
7. `evidence/proofs/Q0015_AGGREGATE_PAIR_CYLINDER_RESET.md`

## Integrity warnings

- Raw conversations contain intermediate claims later corrected; use canonical registries for status.
- The bounded \(m=3,b=2\) reset enumeration refutes only immediate closure; it does not prove a general quantitative token bound.
- Q-0015, Q-0016, Q-0017, and the one-quarter theorem remain open.
