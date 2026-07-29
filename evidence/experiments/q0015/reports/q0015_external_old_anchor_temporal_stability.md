# Q-0015 external-old-anchor temporal stability and saturated-core route

## Scope lock

```text
Task:
  Record and machine-check the current external-old-anchor progress.
Mode:
  implementation without status-promotion.
Base version:
  cfadd24b52546d4d5800c4a3c5a75a2add86f928.
Target:
  G1c / Q-0015 named E exits.
Allowed paths:
  src/, tests/, evidence/experiments/q0015/.
Forbidden paths:
  knowledge/, docs/PROOF_DAG.md, docs/PROJECT_STATE.yaml,
  HANDOFF_CURRENT.md, sources/raw/, history/.
Expected status change:
  none.
Acceptance:
  proved statements receive tests; conditional statements preserve their
  entrance assumptions; the three ledgers remain distinct.
Non-goals:
  no general configuration entrance, no non-tree core closure, no closure of
  Q-0015 or the one-quarter theorem.
```

No canonical status was promoted.

## Result classification

| ID | Statement | Status in this report |
|---|---|---|
| NC-1 | no-configuration retypes to a surviving old-anchor blocker | proved-formal for the current execution contract |
| TS-1 | exact profile stability and endpoint temporal stability | proved-formal abstract profile theorem |
| OA-1 | fixed-root genealogy-demand identity | supporting, under full-candidate-mass execution |
| SL-1 | local residual-ledger cut or saturated backward core | supporting/conditional |
| NT-1 | saturated near-tree core forces the one-quarter degree scale | proved-conditional |
| Closure | non-tree saturated-core decomposition and termination | open |

## NC-1: no-configuration reduction

Let `R` be an actual independent root trace, `r` a successful inserted
vertex, and `x` a later failed attempt. The current execution enumerator
constructs a configuration only after the released trace `R+x` passes a full
independence test. Hence an empty configuration set is equivalent to a real
edge surviving in `R+x`.

Since `R` is independent, a surviving edge contains `x`; since `r` was
released, it excludes `r`. Therefore each such obligation can be retyped,
with unchanged mass, as `external-old-anchor-blocker`. The retyping itself
charges no root-budget, slot, or global-real-edge capacity.

The regression separates the original first blocker
`{0_0,2_0,3_0}` from the blocker `{0_0,1_0,3_0}` that survives release.

## TS-1: exact profile stability

For a profile `a=(a_1,...,a_n)` in `[0,1]^n`, define

\[
F(a)=\frac1{n(n-1)}\sum_{i\ne j}a_i(1-a_j).
\]

Write

\[
A=\sum_i a_i,\qquad Q=n-2A,\qquad
P=\sum_i a_i(1-a_i).
\]

Then

\[
\frac{n}{4(n-1)}-F(a)
=
\frac{Q^2}{4n(n-1)}
+
\frac{P}{n(n-1)}.
\tag{1}
\]

The exact cube maximum is

\[
F_{\max}(n)=
\frac{\lfloor n^2/4\rfloor}{n(n-1)}.
\tag{2}
\]

If `delta=F_max(n)-F(a)` and `chi(n)` is the parity indicator, then

\[
|Q|\le B(n,\delta)
:=
\sqrt{4n(n-1)\delta+\chi(n)}.
\tag{3}
\]

Thus near equality simultaneously controls imbalance and polarization.

Now let `I_{t+1}=I_t\setminus{M_t}` and assume every surviving profile
coordinate can only decrease. Put
\(\alpha_t=a_{M_t}^{(t)}\) and let \(D_t\ge0\) be the total decrease of the
surviving coordinates. Then

\[
Q_{t+1}-Q_t=2\alpha_t-1+2D_t.
\tag{4}
\]

Consequently, for any interval `[s,u]`,

\[
\sum_{t=s}^{u-1}(2\alpha_t-1)
\le
B(n_s,\delta_s)+B(n_u,\delta_u).
\tag{TS-1}
\]

If every removed block satisfies \(\alpha_t\ge1-\tau\), this gives

\[
(u-s)(1-2\tau)
\le
B(n_s,\delta_s)+B(n_u,\delta_u).
\]

Only the two endpoint deficits are required. Additional profile drift makes
the imbalance grow faster and cannot prolong a near-critical interval.

## OA-1: fixed-root old-anchor demand

For an actual root `R`, let each remaining block have size `b`, root mass
`w`, and

\[
g_M=|G_M(R)|=ba_M,\qquad A=\sum_Ma_M.
\]

For a blocked vertex \(x\in N\), all successful insertions from blocks
\(M\ne N\) create old-anchor genealogy demand

\[
\lambda_R(x)=w\sum_{M\ne N}g_M=wb(A-a_N).
\tag{5}
\]

Summing over all blocked vertices gives the exact demand identity

\[
\operatorname{Dem}_R
=
wb^2n(n-1)F(a).
\tag{6}
\]

This is demand, not permission to reuse real-edge capacity.

Fix a previously valid global residual real-edge ledger
\(c_{\rm res}(e)\). The relevant neighborhood for \(x\) is

\[
\mathcal E_R(x)
=
\{e\in E(H):e\subseteq R\cup\{x\}\}.
\]

Different \(x\)-fibers are edge-disjoint inside this fixed root. Hence the
local unmet demand is

\[
\operatorname{Def}_R
=
\sum_x
\left[
\lambda_R(x)-
\sum_{e\in\mathcal E_R(x)}c_{\rm res}(e)
\right]_+.
\tag{7}
\]

This identity is not a cross-root allocation theorem. The same real edge
cannot be reallocated at another root or genealogy.

## Saturated backward core

If the local deficit in (7) is small while demand is near the maximum degree
capacity, most blocked vertices must have almost all available degree in
edges of the form

\[
\{u,v,x\},\qquad u,v\in R.
\]

This is the saturated backward-link core interface. It is a structural output
of a fixed residual ledger, not a canonical closure theorem.

Along one successful genealogy, every blocked vertex in a consumed block has
a backward witness edge. Different consumed blocks give distinct third
vertices. Combining this with TS-1 gives a real backward-edge scaffold when
many successes come from non-good blocks.

## NT-1: conditional near-tree one-quarter consequence

For a saturated vertex \(x\), suppose a median-source obligation network can
be formed in one common real testing space. Let \(\Pi_x\) be the minimum
obligation mass deleted so that the remainder is a faithful rooted forest
with:

1. fixed historical anchor \(x\);
2. no history merge or recoverable cycle;
3. distinct first-certifying real edges;
4. every certifying edge containing \(x\);
5. use only of unconsumed global real-edge capacity.

The earlier median source has
\(\lfloor b^2/4\rfloor+O(b)\) obligations. Faithful tree injection then gives

\[
d_H(x)+\Pi_x
\ge
\left\lfloor\frac{b^2}{4}\right\rfloor-O(b).
\tag{NT-1}
\]

Therefore, below \((1/4-\eta)b^2\), a saturated core must have
\(\Pi_x\ge\eta b^2-o(b^2)\) for typical \(x\).

NT-1 is conditional. The general saturated core has not yet been shown to
supply the common testing space, faithful first-edge injection, disjoint
stopping-time capacity, or a terminating treatment of every non-tree defect.

## Remaining closure problem

A non-tree saturated-core decomposition must convert main-order defect into
at least one of:

1. distinct regenerated real edges;
2. a global reuse Hall cut;
3. concentration on a controlled anchor set;
4. a strictly smaller saturated subcore with a decreasing potential;
5. a reproducible countermodel.

The decomposition must preserve root projection, genealogy, blocker
provenance, and global real-edge identity. It must not merge root budget,
slot capacity, and global real-edge capacity. Until this closure is proved,
Q-0015, G1c, and the one-quarter theorem remain open.
