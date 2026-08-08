# Independent transversals in partitioned 3-uniform hypergraphs

This repository studies the independent-transversal threshold for equal-block
partitioned 3-uniform hypergraphs, with the target implication

\[
\Delta(H)<\left(\frac14-o(1)\right)b^2
\Longrightarrow H\text{ has an independent transversal.}
\]

## Current status

The one-quarter theorem is **open**. The active proof node is now
**S1 / Q-0019**, the global inverse-fiber decomposition problem. The primary
research route is

\[
\boxed{
\text{finite actual-history exhaustion}
\to
\text{rank-two repair and fork density}
\to
\text{inverse-fiber codimension}
\to
\text{persistent-anchor target-following}.
}
\]

The roles are deliberately separated:

- finite-state LP and physical stopping organize transient histories, recurrent
  classes, and named exits;
- canonical maximal-matching repair is the mechanism that produces the
  one-quarter constant;
- inverse-fiber estimates address repeated use of a small set of actual edges;
- fixed-pivot target-following closes a genuinely future-complete anchored
  class by proving \(d_H(p)\ge b^2\).

The precise unresolved bridge is global: every residual disjoint-blocker fork
occurrence must be assigned, without duplicating mass and with its actual
history retained, to a two-coordinate diffuse fiber, an already paid exit, a
proper-block subsystem, or a future-complete fixed-anchor class. Local
replacement-box estimates do not by themselves provide this assignment.

The current S1 subfrontier is more specific than the original one-coordinate
migration formulation. Common-parent parallel rollback removes private support
reset; the low pair grammar has critical growth `4\Delta`; the irreducible
high case is a rank-two `(2,0)/(0,2)` core. Bounded normal-Q4 computation now
exhibits a unique eight-edge zipper and finite support-packing structure, but a
state-level splice is not yet a faithful merger of two future obligations.
See `evidence/proofs/Q0019_RANK_TWO_ROLLBACK_ZIPPER_ROUTE.md`.

## Scope correction for F-0078

F-0074's local three-cylinder contraction and the fixed-instance stopping
identity remain useful. The stronger interpretation formerly attached to
F-0078 is not valid:

- a partial independent completion is not a global independent transversal;
- the proposed physical token is not a transition congruence when return status
  depends on the visited history;
- a return under one deterministic release policy does not imply an all-release
  recurrent core;
- fixed-instance exhaustion does not give a uniform asymptotic stopping depth.

F-0078 is therefore retained only as a local, history-unfolded stopping
statement, not as a zero-set closure theorem or as the final backend.

## Verified central modules

- **F-0052:** finite actual-history potential / recurrent-core equivalence;
- **F-0058:** fixed-pivot target-following, conditional on future-complete
  persistence, gives \(d_H(p)\ge b^2\);
- **F-0090:** canonical full-target repair reaches either the target or an
  actual target-supported edge;
- **F-0091:** canonical maximal-matching repair is independent; the fork-free
  record growth is \(2\sqrt{\Delta}\), and low-degree no-IT executions carry
  positive density of disjoint-blocker forks;
- **F-0092:** a private-edge two-coordinate replacement box gives global
  \(b^{-2}\) multiplicity for outputs using both replacement coordinates and
  \(b^{-1}\) multiplicity for outputs using exactly one.

## Start here

1. [`HANDOFF_CURRENT.md`](HANDOFF_CURRENT.md)
2. [`docs/MAIN_PROOF_ROUTE.md`](docs/MAIN_PROOF_ROUTE.md)
3. [`docs/PROOF_DAG.md`](docs/PROOF_DAG.md)
4. [`manuscript/independent_transversal_fork_route.tex`](manuscript/independent_transversal_fork_route.tex)
5. [`evidence/proofs/FORK_INVERSE_FIBER_ANCHOR_ROUTE.md`](evidence/proofs/FORK_INVERSE_FIBER_ANCHOR_ROUTE.md)
6. [`evidence/proofs/Q0019_RANK_TWO_ROLLBACK_ZIPPER_ROUTE.md`](evidence/proofs/Q0019_RANK_TWO_ROLLBACK_ZIPPER_ROUTE.md)
7. [`evidence/analyses/Q0019_COMBINATORIAL_COMPRESSION_AUDIT_2026_08_08.md`](evidence/analyses/Q0019_COMBINATORIAL_COMPRESSION_AUDIT_2026_08_08.md)
8. [`evidence/audits/F0078_SCOPE_CORRECTION.md`](evidence/audits/F0078_SCOPE_CORRECTION.md)
9. [`knowledge/QUESTIONS.md`](knowledge/QUESTIONS.md)
10. [`knowledge/FAILURES.md`](knowledge/FAILURES.md)

## Install and validate

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install -e ".[test]" --no-build-isolation
python -m compileall -q src enumerate tools tests
python -m pytest -q
python tools/check_repository.py
python tools/check_generated_artifacts.py
```

## Source baseline

The public source baseline is commit
`cfadd24b52546d4d5800c4a3c5a75a2add86f928` dated 2026-07-28. The present
archive is a research-state update built on that baseline; it does not claim a
new public upstream commit.
