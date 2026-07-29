# Route-B reorientation audit

## 1. Scope lock

```text
Task: reorient the main proof strategy from Route A to Route B
Mode: proposal + status-promotion of strategy only
Base version: local repository commit b56fe56d3fd7d4bf09c9b48113f50890d727aba7; historical source baseline cfadd24
Target: faithful execution, exact zero-defect structure, and stability
Inputs: F-0036–F-0042, failure registry, current Proof DAG, bounded Q4 experiments
Outputs: exact supporting lemmas, bounded observations, and revised contracts
Allowed paths: canonical state/docs/registries, evidence, enumerate, checker
Forbidden paths: raw conversations, history, unrelated implementation
Expected status change: active strategy/node only; no mathematical question closed
Non-goals: prove Q-0016/Q-0017/Q-0018 or the one-quarter theorem
```

## 2. Exact local Hall-deficiency orthogonalization

Fix one future cylinder. Let \(Y\) be its finite failure atoms, with masses
\(\mu_y\ge0\). Let \(C(y)\) be the set of actual blocker keys available to \(y\).
Give each blocker key capacity \(\tau\).

Construct the network

\[
s\to y\to e\to t
\]

with capacities \(\mu_y,\infty,\tau\). Let \(M=\sum_y\mu_y\) and let
\(\delta=M-\operatorname{maxflow}\).

### Theorem 2.1

\[
\delta=
\max_{U\subseteq Y}
\left(
\sum_{y\in U}\mu_y-\tau|C(U)|
\right)_+.
\]

#### Proof

A finite cut is determined by a set \(U\) of atom nodes on the source side. All
blocker neighbors \(C(U)\) must also lie on the source side because
\(y\to e\) has infinite capacity. Its capacity is

\[
M-\sum_{y\in U}\mu_y+\tau|C(U)|.
\]

Minimizing and subtracting from \(M\) gives the formula. \(\square\)

Let

\[
L_e=\sum_{y:e\in C(y)}\mu_y.
\]

### Theorem 2.2

\[
\delta\le\sum_e(L_e-\tau)_+.
\]

#### Proof

For every \(U\),

\[
\sum_{y\in U}\mu_y
\le \sum_{e\in C(U)}L_e.
\]

Hence

\[
\sum_{y\in U}\mu_y-\tau|C(U)|
\le
\sum_{e\in C(U)}(L_e-\tau)
\le
\sum_e(L_e-\tau)_+.
\]

Take the positive part and maximize over \(U\). \(\square\)

This is a local orthogonalization theorem. It does not grant later trajectories
a global real-edge charging entitlement.

## 3. Same-load alternating exchange theorem

Fix a feasible local maximum blocker assignment \(q_{a\ell}\). Put

\[
r_a=m_a-\sum_\ell q_{a\ell},
\qquad
\lambda_\ell=\sum_a q_{a\ell}.
\]

Build the alternating network with:

\[
s\to a\quad(r_a),\qquad
a\to\ell\quad(\infty),\qquad
\ell\to a\quad(q_{a\ell}),
\]

and attach every atom \(a\) to its actual reachable global resource network.

### Theorem 3.1

Every flow \(\phi\) in the alternating network determines

\[
q'_{a\ell}
=
q_{a\ell}
+\phi(a,\ell)-\phi(\ell,a)
\]

such that:

1. \(q'_{a\ell}\ge0\);
2. \(\sum_aq'_{a\ell}=\lambda_\ell\) for every blocker \(\ell\);
3. \(q'\) is therefore another local maximum assignment;
4. the amount sent from atom \(a\) into the global resource network is the
   corresponding residual mass after the exchange, modulo any unsent source
   residual.

Conversely, every such same-load reassignment and resource flow induces an
alternating flow.

#### Proof

The reverse capacity gives
\(\phi(\ell,a)\le q_{a\ell}\), proving nonnegativity. Flow conservation at
\(\ell\) gives

\[
\sum_a\phi(a,\ell)=\sum_a\phi(\ell,a),
\]

so each \(\lambda_\ell\) is preserved. Atom conservation gives the residual
identity. Reversing the calculation constructs the converse flow. \(\square\)

### Caveat

The theorem is deliberately stated for the same blocker-load vector. The
bounded experiments found no dependence on the initially chosen maximum flow,
but that stronger arbitrary-maximum equivalence is not promoted here.

## 4. Conditional splice-density count

Fix four actual blocks of size \(b\). Sample uniformly from all choices of two
vertices in each block and from \(q\) policies.

Suppose every policy marked “splice” has a certificate containing at least
\(s\) distinct actual hyperedges, each supported on three selected window
vertices.

### Theorem 4.1

The marked fraction is at most

\[
\frac{32}{3s}\frac{\Delta(H)}{b^2}.
\]

#### Proof

A fixed actual edge is contained in at most

\[
q(b-1)^3\binom b2
\]

policies: choose the second vertex in each of its three blocks and choose the
two vertices in the omitted block.

If \(E_4\) is the set of actual edges inside the four blocks, then

\[
3|E_4|
\le 4b\Delta(H).
\]

Double-counting certificate-edge incidences and dividing by
\(q\binom b2^4\) yields the stated bound. \(\square\)

This theorem is conditional on the existence of the specified actual
\(s\)-edge certificates. It is a window-density bound, not a charging theorem.

## 5. Bounded exhaustive \(Q_4\) result

Generator:

```text
enumerate/q4_splice_pay_cylinder_validation.py
```

The computation exhausts:

- 272 coordinate perfect matchings of \(Q_4\);
- all 8 normal matchings;
- 192 normal independent one-hole states;
- 768 future-complete release policies.

Results:

\[
384\text{ edge-disjoint splice candidates},
\quad
192\text{ unavoidable-reuse policies},
\quad
192\text{ local same-pivot policies}.
\]

Every edge-disjoint splice candidate uses all eight real edges.

Status: bounded exhaustive observation. It does not prove a general global
classification.

## 6. Refuted candidate lemmas

### 6.1 Common-base diamond

False as stated. Complete reversibility and ordinary single-defect behavior do
not create an actual independent common base. An internal old-anchor edge may
already block the missing corner.

### 6.2 Free repeated splice

False in the bounded normal model. A minimum edge-disjoint splice may use every
real edge in the model.

### 6.3 Complete charging as the meaning of \(1/4\)

Not established and no longer adopted as the main strategy. The recurrence
criterion F-0042 is sufficient, not known necessary. Large residual mass may
belong to a rigid critical structure.

## 7. Route-B target and nonclaims

The proposed exact target is

\[
\text{binary regeneration forest}
+
\text{reversible exact-future cores}.
\]

This audit does not prove that target. It records why a pure-tree theorem is too
strong and why the reversible cores must be classified on actual support.

No canonical mathematical question is closed by this audit.
