# Ten-minute quickstart

## 1. Mathematical target

For an equal-block partitioned 3-uniform hypergraph, prove

\[
\Delta(H)<\left(\frac14-o(1)\right)b^2
\Longrightarrow\text{an independent transversal exists}.
\]

The theorem is open.

## 2. Active node

The active node is **S1 / Q-0019**, global inverse-fiber decomposition.

## 3. Why \(1/4\) appears

Canonical maximal-matching repair deletes two old vertices per matching edge.
When the blocker-pair matching number is at most one, the record generating
function is \(1+\Delta z^2\), whose minimum growth is \(2\sqrt\Delta\). Thus
fork-free execution has threshold \(b^2/4\).

## 4. What remains

Below the threshold, no-IT executions must contain many disjoint-blocker forks.
Their total mass is useful only if repeated use of the same actual edge is
controlled. Two-coordinate replacement boxes give \(b^{-2}\) multiplicity,
but one-coordinate heavy pairs may migrate. Q-0019 must either charge the
migration to a valid exit or extract a future-complete fixed anchor.

## 5. Read in this order

1. `../HANDOFF_CURRENT.md`
2. `MAIN_PROOF_ROUTE.md`
3. `PROOF_DAG.md`
4. `../evidence/proofs/FORK_INVERSE_FIBER_ANCHOR_ROUTE.md`
5. `../evidence/audits/F0078_SCOPE_CORRECTION.md`
6. `../knowledge/QUESTIONS.md#Q-0019`
7. `../manuscript/independent_transversal_fork_route.tex`

## 6. Validation

```bash
python -m pip install -e ".[test]" --no-build-isolation
python -m compileall -q src enumerate tools tests
python -m pytest -q
python tools/check_repository.py
python tools/check_generated_artifacts.py
```
