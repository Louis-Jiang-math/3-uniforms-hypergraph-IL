# FW-15 — Aggregate pair-cylinder entry

- **Status:** active supporting interface
- **Question:** Q-0015
- **DAG node:** G1c
- **Evidence:** `../../evidence/proofs/Q0015_AGGREGATE_PAIR_CYLINDER_RESET.md`

## 0. Purpose

This interface is an alternative sufficient route to the original per-source
configuration-flow entrance. It aggregates actual two-step failures into
normalized future cylinders while retaining actual blocker identities.

It does not change the status of Q-0002, and it does not close Q-0015.

## 1. Aggregate-cylinder contract

For actual roots \(R\), successful first coordinates \(r\), and actual second
blocks \(N(R,r)\), give \(R+r\) weight \(w_R/b\). If \(W_N\) is the resulting
cylinder root mass and \(E_N\) the further \(1/b\)-normalized failure mass, the
required exact identities are

\[
\mathcal B_k=b^2\sum_NE_N,
\qquad
\sum_NW_N\le A_{k-2}.
\]

This contract forbids sibling genealogy multiplication.

## 2. Pair-cylinder contract

For an actual pair \(p\), put

\[
\Gamma_N(p)=\sum_{S:p\subseteq S}a_S.
\]

Every failed second coordinate is attributed to an actual edge \(p+x\).
The same definition covers old-anchor and fresh/configurable blockers.

For every \(\eta\ge0\), either

\[
E_N\le(1+\eta)\frac{\Delta(H)}{b^2}W_N,
\]

or an actual edge \(p+x\) supports a coherent heavy root cylinder.

## 3. Exact active remainder

Set

\[
T_N=(1+\eta)\frac{W_N}{b^2}
\]

and

\[
\mathfrak H_k=
b\sum_N
\sum_{\substack{x\in N\\p+x\in E(H)}}
\bigl(\Gamma_N(p)-T_N\bigr)_+.
\]

Then

\[
\mathcal B_k
\le
(1+\eta)\Delta(H)A_{k-2}
+
\mathfrak H_k.
\]

The G1c task may therefore be stated as quantitative heavy-excess
dissipation: pay or telescope all \(\mathfrak H_k\), or output a reproducible
accepted structural exit.

## 4. Reset-compensation contract

A quotient may merge execution states only through a future-compatible
transition congruence. Tokens must preserve every datum affecting future
legality, including root projection, genealogy, blocker provenance and ledger
increments.

With accumulated blocker edges \(\mathcal E_t\), carrier support
\(\mathcal A_t\), and unused compatible token count \(U_t\), every transition
before quotient repetition strictly increases

\[
\bigl(|\mathcal E_t|,|\mathcal A_t|,-U_t\bigr)
\]

lexicographically.

The statement

\[
\text{no new edge}+\text{no new support}
\Longrightarrow
\text{immediate quotient}
\]

is invalid: one actual three-edge has three different hole orientations.

## 5. Aggregate closing criterion

For

\[
\Delta(H)\le\left(\frac14-\varepsilon\right)b^2,
\]

it is sufficient to find \(\eta,\rho\ge0\) satisfying

\[
(1+\eta)\left(\frac14-\varepsilon\right)+\rho<\frac14
\]

and prove, at every required depth or under a valid telescoping sum,

\[
\mathfrak H_k\le\rho b^2A_{k-2},
\]

unless an accepted structural exit occurs.

## 6. Active gap

The interface does not yet provide:

- a lossless weighted trajectory decomposition of all heavy excess;
- a quantitatively small future-compatible token budget;
- a proof that token repetition yields an accepted exact-future quotient;
- the required bound on \(\mathfrak H_k\).

Therefore G1c/Q-0015 remains active.
