# Q-0015 aggregate pair-cylinder reduction and reset compensation

## Scope lock

```text
Task:
  Register and verify the aggregate Q-0015 reduction, exact heavy-pair excess,
  and the corrected reset-compensation theorem.
Mode:
  status-promotion for supporting facts; Q-0015 remains active.
Base version:
  local repository HEAD 1da38011d28643eb8a3d35aa727d5fb206aacf41.
Target:
  G1c / Q-0015.
Inputs:
  NC-1 and TS-1 from the current local repository; F-0001, F-0005, F-0032,
  F-0033, F-0036.
Outputs:
  exact aggregate normalization; unified pair-cylinder bound; explicit
  heavy-excess remainder; future-compatible orientation-budget theorem;
  bounded-exhaustive refutation of immediate reset closure.
Allowed paths:
  src/, tests/, enumerate/, evidence/, knowledge/, docs/, README.md,
  HANDOFF_CURRENT.md.
Forbidden paths:
  sources/raw/, history/, old/, unrelated implementation.
Expected status change:
  supporting facts and refutations are promoted; Q-0015 remains open.
Acceptance criteria:
  preserve real edge, root projection, genealogy, blocker provenance and
  separate ledgers; distinguish formal proof, conditional criterion and bounded
  computation.
Required checks:
  compileall; full pytest; repository checker; generated-artifact checker;
  Q-0015 regression CLI; reset-compensation artifact generation and validation.
Non-goals:
  no heavy-excess dissipation theorem; no Q-0015/Q-0016/Q-0017 closure; no
  one-quarter theorem.
```

## 1. Existing local inputs

The local repository already proves two inputs.

1. A no-configuration obligation can be retyped, with unchanged mass and no
   ledger charge, as an actual blocker surviving after the inserted vertex is
   released.
2. For a monotone block-success profile, the exact imbalance identity and
   endpoint temporal estimate give a genealogy-internal Lyapunov bound.

See
`../experiments/q0015/reports/q0015_external_old_anchor_temporal_stability.md`
and `../../tests/test_q0015_old_anchor.py`.

Neither input by itself controls all two-step failure mass.

## 2. Exact aggregate normalization

Let \(\mathscr R\) be actual reachable independent roots, with weights
\(w_R\ge0\), and let

\[
W=\sum_{R\in\mathscr R}w_R.
\]

For each root \(R\), let \(G_R\) be the successful vertices in the actual first
future block. For \(r\in G_R\), let \(N(R,r)\) be the actual second future
block, put \(S_{R,r}=R+r\), and define

\[
D(R,r)=\{x\in N(R,r):S_{R,r}+x\text{ is not independent}\}.
\]

The raw two-step failure mass is

\[
\mathcal B=
\sum_Rw_R\sum_{r\in G_R}|D(R,r)|.
\tag{1}
\]

For each actual second block \(N\), set

\[
\mathscr S_N=\{(R,r):r\in G_R,\ N(R,r)=N\},
\qquad
a_{R,r}=\frac{w_R}{b},
\]

and define

\[
W_N=\sum_{(R,r)\in\mathscr S_N}a_{R,r},
\qquad
E_N=\frac1b\sum_{(R,r)\in\mathscr S_N}a_{R,r}|D(R,r)|.
\]

### Theorem 1 — aggregate-cylinder identity

\[
\boxed{\mathcal B=b^2\sum_NE_N}
\tag{2}
\]

and

\[
\boxed{
\sum_NW_N
=\frac1b\sum_Rw_R|G_R|
\le W.
}
\tag{3}
\]

### Proof

Substitution gives

\[
b^2\sum_NE_N
=
\sum_N\sum_{(R,r)\in\mathscr S_N}w_R|D(R,r)|
=
\mathcal B.
\]

Likewise,

\[
\sum_NW_N
=
\frac1b\sum_Rw_R|G_R|
\le
\sum_Rw_R.
\]

Thus successful \(r\)-genealogies are normalized coordinates, not copied root
mass. \(\square\)

## 3. Unified old/fresh pair-cylinder bound

Fix a cylinder \(N\). For a real pair \(p\), define

\[
\Gamma_N(p)
=
\sum_{\substack{(R,r)\in\mathscr S_N\\p\subseteq R+r}}
a_{R,r}.
\tag{4}
\]

This single definition covers both:

- \(p\subseteq R\), an old-anchor pair;
- \(p=\{r,u\}\), a fresh/configurable pair.

Indeed \(S_{R,r}\) is independent. Every blocker in \(S_{R,r}+x\) must contain
\(x\), and hence is a real edge \(p+x\) with \(p\subseteq S_{R,r}\).

### Theorem 2 — pair-flat or coherent heavy cylinder

For every \(\eta\ge0\), either

\[
\boxed{
E_N\le(1+\eta)\frac{\Delta(H)}{b^2}W_N,
}
\tag{5}
\]

or there are a real pair \(p\) and \(x\in N\) such that

\[
p+x\in E(H),
\qquad
\boxed{
\Gamma_N(p)>(1+\eta)\frac{W_N}{b^2}.
}
\tag{6}
\]

In the second branch, every extended source counted by \(\Gamma_N(p)\) is
blocked at \(x\) by the same actual edge \(p+x\).

### Proof

For every failed triple \((R,r,x)\),

\[
1
\le
\sum_{\substack{p\subseteq R+r,\ |p|=2\\p+x\in E(H)}}1.
\]

Multiply by \(a_{R,r}/b\) and sum:

\[
E_N
\le
\frac1b
\sum_{\substack{x\in N\\p+x\in E(H)}}\Gamma_N(p).
\tag{7}
\]

If (6) fails, each summand is at most
\((1+\eta)W_N/b^2\). The number of real edges in the sum is at most

\[
\sum_{x\in N}d_H(x)\le b\Delta(H).
\]

This proves (5). \(\square\)

## 4. Exact unresolved heavy excess

Put

\[
T_N=(1+\eta)\frac{W_N}{b^2}
\]

and define

\[
X_N=
\frac1b
\sum_{\substack{x\in N\\p+x\in E(H)}}
\bigl(\Gamma_N(p)-T_N\bigr)_+.
\tag{8}
\]

Splitting every \(\Gamma_N(p)\) into its capped part and positive excess in
(7) gives

\[
\boxed{
E_N
\le
(1+\eta)\frac{\Delta(H)}{b^2}W_N+X_N.
}
\tag{9}
\]

Therefore

\[
\boxed{
\mathcal B
\le
(1+\eta)\Delta(H)W+\mathfrak H,
}
\tag{10}
\]

where the exact unresolved term is

\[
\boxed{
\mathfrak H
=
b^2\sum_NX_N
=
b\sum_N
\sum_{\substack{x\in N\\p+x\in E(H)}}
\left(
\Gamma_N(p)-(1+\eta)\frac{W_N}{b^2}
\right)_+.
}
\tag{11}
\]

A single heavy-pair witness does not control (11). Q-0015 needs a
mass-preserving treatment of the entire positive part.

### Conditional aggregate closing criterion

Assume

\[
\Delta(H)\le\left(\frac14-\varepsilon\right)b^2.
\]

If there are \(\eta,\rho\ge0\) such that

\[
(1+\eta)\left(\frac14-\varepsilon\right)+\rho<\frac14
\tag{12}
\]

and, at each required depth or after a valid cross-depth telescoping sum,

\[
\mathfrak H_k\le\rho b^2A_{k-2}
\tag{13}
\]

unless an accepted structural exit occurs, then F-0005 gives a second-order
recurrence with coefficient strictly below \(1/4\). The characteristic-root
induction then keeps every transversal-counting mass positive and yields an IT.

This is a proved sufficient reduction, not a proof of (13).

## 5. Future-compatible orientation tokens

Let \(\mathfrak X\) be a finite set of fully labelled execution states. A state
must retain all continuation-relevant data, including the one-hole partial
transversal, test vertex, actual blocker edge, root projection, genealogy and
ledger state.

A finite map

\[
\theta:\mathfrak X\to\Omega
\]

is **future-compatible** if token equality is a transition congruence:

1. current outputs and ledger demands agree;
2. legal successors correspond in both directions through equal tokens;
3. corresponding transitions have identical real-edge, support and ledger
   increments.

The identity on full labelled states is future-compatible, although its token
space can be large.

Along a trajectory \(\xi_0\to\cdots\to\xi_t\), define

\[
\mathcal E_t=\{e(\xi_i):0\le i\le t\},
\qquad
\mathcal A_t=\bigcup_{i=0}^tp(\xi_i),
\]

where \(p(\xi_i)\) is the carrier pair. Let

\[
\Omega(\mathcal E,\mathcal A)
=
\{\theta(\xi):e(\xi)\in\mathcal E,\ p(\xi)\subseteq\mathcal A\},
\]

\[
V_t=\{\theta(\xi_i):0\le i\le t\},
\qquad
U_t=
|\Omega(\mathcal E_t,\mathcal A_t)\setminus V_t|.
\tag{14}
\]

### Theorem 3 — reset compensation

For every legal transition \(\xi_t\to\xi_{t+1}\), at least one occurs:

1. \(e(\xi_{t+1})\notin\mathcal E_t\);
2. \(p(\xi_{t+1})\nsubseteq\mathcal A_t\);
3. the two resource sets are unchanged and \(U_{t+1}=U_t-1\);
4. \(\theta(\xi_{t+1})=\theta(\xi_j)\) for some \(j\le t\), giving a directed
   cycle in the sound quotient graph.

Equivalently,

\[
\boxed{
\text{no new edge}
+
\text{no new support}
+
\text{no token consumption}
\Longrightarrow
\text{sound quotient repetition}.
}
\tag{15}
\]

### Proof

If the next edge or carrier support is new, cases 1 or 2 hold. Otherwise
\(\mathcal E_{t+1}=\mathcal E_t\) and
\(\mathcal A_{t+1}=\mathcal A_t\), so the compatible token set is unchanged.

If the next token is unvisited, exactly one token leaves the unused set and
\(U_{t+1}=U_t-1\). If it is already visited, case 4 holds. Future
compatibility makes this a sound quotient cycle, rather than an invalid merge
by current trace alone. \(\square\)

Hence

\[
\bigl(|\mathcal E_t|,|\mathcal A_t|,-U_t\bigr)
\]

strictly increases lexicographically before quotient repetition. On an
interval with fixed \(\mathcal E_*,\mathcal A_*\) and no quotient repetition,
there are at most

\[
|\Omega(\mathcal E_*,\mathcal A_*)|-1
\]

transitions.

## 6. Immediate reset closure is false

The stronger statement

\[
\text{no new edge}+\text{no new support}
\Longrightarrow
\text{immediate repetition of the full labelled state}
\]

is false.

Take three blocks of size two and the single edge

\[
e=\{0_0,1_0,2_0\}.
\]

There are three successive blocker states with hole blocks \(0,1,2\), all
using \(e\), and carrier pairs

\[
\{1_0,2_0\},
\qquad
\{0_0,2_0\},
\qquad
\{0_0,1_0\}.
\]

The transition to the third state introduces neither a new edge nor a new
carrier endpoint, but reaches a new fully labelled state. A further move
repeats the first orientation.

The executable test checks all \(2^8=256\) transversal-edge subsets on three
blocks of size two. Exactly 255 instances, every nonempty instance, contain an
immediate counterexample. This is an exhaustive bounded refutation, not a
general positive theorem.

## 7. Q-0015 status

The local repository now has formal proofs or tests for:

- no-configuration retyping;
- exact profile and temporal stability;
- aggregate normalization;
- the unified old/fresh pair-flat bound;
- the exact heavy-excess remainder;
- future-compatible orientation-budget reset compensation;
- a bounded-exhaustive refutation of immediate reset closure.

Q-0015 remains open. The aggregate route still needs:

1. a mass-preserving decomposition of all \(\mathfrak H_k\) into labelled
   carrier trajectories;
2. a quantitatively small future-compatible token space, or an independent
   payment for new tokens;
3. a proof that repeated sound tokens yield an accepted exact-future quotient,
   complete-block closure or another approved structural exit;
4. a bound of the form (13), or an equivalent telescoping estimate.

The original per-source near-lossless configuration/escape flow remains a
sufficient route. It is not logically necessary if the aggregate criterion is
proved.

## 8. Nonclaims

This document does not prove:

- a sufficient bound on \(\mathfrak H_k\);
- a polynomial or linear bound on exact orientation tokens;
- that every quotient cycle gives a smaller complete-block no-IT instance;
- Q-0015, Q-0016, Q-0017 or the one-quarter theorem.
