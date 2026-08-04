# Current Handoff

## Objective

Prove the independent-transversal threshold at \(1/4-o(1)\). The theorem
remains open.

## Current strategy and status

- **Primary strategy:** Route B — critical stability.
- **Active DAG node:** `S1 / Q-0018` — faithful global Round-or-Core entrance
  and natural defect.
- **Implementation route:** D-0012 and `docs/MAIN_PROOF_ROUTE.md`.
- **Route A status:** suspended as a main route; its exact identities, Hall
  tools, and F-0042 backend remain supporting modules.
- **Open:** Q-0016, Q-0017, Q-0018, S1--S5, and the one-quarter theorem.

No theorem or open question is closed by the 2026-08-04 route clarification.

## Fixed final target

For a legal finite interval \(I\), write

\[
S_I=\sum_{k\in I}A_{k-2}.
\]

The final target is

\[
\sum_{k\in I}\mathcal B_k
\le
(1+\eta)\Delta(H)S_I
-\mathsf{Gain}_I
+\mathsf{Boundary}_I,
\]

with

\[
\mathsf{Boundary}_I/(b^2S_I)\to0.
\]

F-0042/Q-0007 is the conditional backend once the normalized additive loss is
below

\[
\varepsilon-\eta(1/4-\varepsilon).
\]

Do not rename a local subterm as a new final objective.

## Fixed implementation route

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

### Stage A — root-only recurrence entrance

F-0070 is verified. On a finite legal interval,

\[
\frac{\sum_{k\in I}\mathcal B_k}{b^2S_I}
\le
(1+\eta)\frac{\Delta(H)}{b^2}+\Xi_I.
\]

The capacity in F-0070 belongs only to original two-step failure roots. A
blocker appearing after a release does not receive another copy of the root
capacity merely because it lies in the same genealogy.

The open Q-0018 chart interface is

\[
\Xi_I
\le
\operatorname{ChartMis}_I
+2\mathcal D_I^\sharp
+\Phi_I
+\mathcal R_I,
\]

in the same interval normalization and with root, slot, and actual-edge types
kept separate.

### Stage B — actual finite cores

F-0063--F-0067 give the finite unique-blocker all-release core and its
completion-switch matching.

New verified supporting facts:

1. **F-0068 — global switch-slot uniqueness.** For fixed actual edges \(e,f\),
   the output \(f\) can arise from at most one switch slot of \(e\), uniformly
   over all completion contexts. Thus the abstract Latin-column migration of
   A-0041 cannot occur in a one-step actual switch map.
2. **F-0069 — perfect-transition monodromy.** Perfect transition cycles have
   identity monodromy and perfect components split into completion sheets.

These facts do not close Q-0016. The fixed candidate theorem is the **actual
switch-cube defect**: on ordered three-coordinate switches, preserve every
intermediate actual support, assign each bad instruction to its first
nonliteral context-slot, and prove bounded multiplicity. A successful proof
gives a natural positive actual-support defect for every positive-mass finite
core, which is an accepted Route-B Q-0016 outcome.

### Stage C — fresh saturated leaves

After the root-excess reduction, use the F-0041 no-copy priority split

\[
\Phi_I=
\Phi_I^{\rm edge}
+\Phi_I^{\rm support}
+\Phi_I^{\rm token}
+\Phi_I^{\rm repeat}.
\]

Fixed destinations:

- repeat \(\to\) actual recurrent core \(\to\) switch-cube defect;
- support \(\to\) actual \(S\) witness or hereditary coordinate expansion and
  a complete-block/product terminal;
- edge \(\to\) first-certifying actual-edge growth with owner-preserving
  bounded multiplicity;
- token \(\to\) the remaining actual three-cylinder critical regeneration
  theorem.

Finite token-universe exhaustion for each fixed instance is qualitative and is
not a substitute for the required interval-level conversion.

## Verified supporting facts added in this patch

### F-0068 — global switch-slot uniqueness

For fixed \(e,f\), if \(\pi_W(u,x)=f\), then \(f\) must contain the new vertex
\(x\). Two different slots would force \(f\) either to contain two vertices
from one block or to contain a replacement vertex absent from the other
switched completion. Hence the producing slot is unique.

### F-0069 — trivial perfect monodromy

A perfect transition is a fixed coordinate overwrite bijection between equal
completion fibers. A cycle of such maps is idempotent on the ambient product
and bijective on the fiber, hence is the identity. Perfect components therefore
split into sheets.

### F-0070 — root-only canonical excess

For canonical root load \(L_I(e)\), root-only capacity \(c_I(e)\), and

\[
\Xi_I=\sum_e(L_I(e)-c_I(e))_+,
\]

one has the exact degree-term-plus-excess bound above and

\[
\sum_ec_I(e)
\le
(1+\eta)\frac{\Delta(H)}{b^2}.
\]

This fact does not control \(\Xi_I\).

## Current genuine gaps

### E1 / Q-0018 — root-excess clean-chart compatibility

Prove the reduction of \(\Xi_I\) to actual chart mismatch, F-0038 deficit,
fresh saturated leaves, and repeat/core mass. Verify the exact correspondence
between the Palm roots, F-0051 clean charts, and F-0042 recurrence units.

### E2 / Q-0018 — fresh forest and overflow conversion

Prove the F-0041 edge/support/token/repeat conversion with first-owner and
three-ledger multiplicities. The pure token branch must become actual
three-cylinder regeneration, not merely a finite-state exhaustion statement.
Unbounded exact-future interfaces must produce the same named structures,
resource growth, or a positive-mass actual core.

### E3 / Q-0016 — actual switch-cube defect

Prove intermediate-state legality, terminal-edge identity, first-nonliteral
measurability, bounded instruction multiplicity, weighted entrance-cylinder
covariance, and the required model regressions. Alternatively construct a real
countermodel satisfying all F-0063 core hypotheses.

## Immediate next actions

1. Formalize the weighted actual switch-cube defect theorem and its
   first-nonliteral assignment.
2. Prove the root-excess chart reduction in the exact F-0070 interval units.
3. Split fresh saturated leaves by F-0041 and isolate the pure three-cylinder
   token statement.
4. Keep all tests against normal \(Q_4\), differing-pivot, fixed-anchor,
   diagonal-codebook, and product/near-\(1/4\) models.

## Anti-drift rules

Do not:

- refresh root capacity along release descendants;
- treat a static core edge set as the actual support/genealogy object;
- infer capacity slack from abstract Latin dispersion;
- infer uniform loss from fixed-instance token finiteness;
- require a positive natural core defect to acquire a separate root charging
  entitlement;
- promote the candidate switch-cube inequality before its actual-support proof
  and weighted interface are complete.

## Required reading

1. `AGENTS.md` and `agent.md`
2. `docs/MAIN_PROOF_ROUTE.md`
3. `docs/PROJECT_STATE.yaml`
4. `docs/PROOF_DAG.md`
5. `knowledge/DECISIONS.md#D-0012`
6. `knowledge/FACTS.md#F-0068` through `#F-0070`
7. `knowledge/FAILURES.md#A-0041` through `#A-0043`
8. `knowledge/QUESTIONS.md#Q-0016` through `#Q-0018`
9. `evidence/proofs/ROOT_ONLY_EXCESS_SWITCH_CUBE_ROUTE.md`
10. `docs/framework/FW-60_CRITICAL_STABILITY_ROUTE.md`
