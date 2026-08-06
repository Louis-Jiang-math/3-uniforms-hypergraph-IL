# Proof DAG

## 1. Active dependency graph

\[
\begin{array}{c}
R0\ \text{basic hypergraph and execution definitions}\\
\downarrow\\
R1\ \text{finite actual-history organization (F-0052/F-0053/F-0055)}\\
\downarrow\\
R2\ \text{canonical target and matching repair (F-0090/F-0091)}\\
\downarrow\\
R3\ \text{positive disjoint-blocker fork density}\\
\downarrow\\
\boxed{S1\ \text{global inverse-fiber decomposition (Q-0019) [ACTIVE]}}\\
\swarrow\qquad\searrow\\
S2a\ \text{diffuse }b^{-2}\text{ load}\qquad
S2b\ \text{future-complete fixed anchor}\\
\downarrow\qquad\downarrow\\
\Delta(H)\ge(1/4-o(1))b^2\qquad \Delta(H)\ge b^2\\
\searrow\qquad\swarrow\\
M0\ \text{one-quarter theorem.}
\end{array}
\]

## 2. Node contracts

### R1 — finite actual-history organization

- **Status:** verified supporting.
- **Output:** transient / bottom-SCC / named-exit localization in a supplied
  finite faithful history graph.
- **Nonoutput:** no automatic negative term, degree concentration, or
  all-release closure.

### R2 — canonical repair

- **Status:** verified supporting.
- **Output:** F-0090 full-target repair and F-0091 maximal-matching repair.
- **Key invariant:** all blockers created by adding the pivot are hit by the
  selected maximal matching.

### R3 — fork density

- **Status:** verified under the faithful execution-log reconstruction used in
  F-0091.
- **Output:** below \((1/4-\varepsilon)b^2\), no-IT long executions have positive
  linear density of disjoint-blocker fork excess.

### S1 — global inverse-fiber decomposition

- **Status:** active.
- **Question:** Q-0019.
- **Input:** actual weighted fork occurrences with full provenance.
- **Required output:** an exhaustive no-copy partition into a two-coordinate
  diffuse part, a valid exit part, a complete proper-block part, and a
  future-complete fixed-anchor part.
- **Quantitative requirement:** the diffuse edge load is
  \(O(F_x/b^2)\), uniformly in the number of contexts and histories.
- **Forbidden shortcut:** local heavy coordinates may not be called persistent
  without closure under every relevant legal successor.

### S2a — diffuse branch

- **Status:** conditional on S1.
- **Backend:** F-0092 plus
  \(2F_x\le d_H(x)\ell_x^*\).
- **Output:** \(d_H(x)\ge(1/4-o(1))b^2\).

### S2b — anchored branch

- **Status:** conditional on S1; endgame verified by F-0058.
- **Output:** \(d_H(p)\ge b^2\).

### M0 — one-quarter theorem

- **Status:** blocked by S1.
- **Acceptance criterion:** an unconditional, uniform, actual-object proof.

## 3. Supporting but inactive branches

- Q-0016--Q-0018 and the former Route-B chart/root-excess route remain open as
  supporting frameworks, not as the active closing chain.
- F-0042 is a conditional recurrence backend and may be reused only if a valid
  global input is supplied.
- Route A remains suspended.

## 4. Progress rule

Progress on S1 requires one of:

1. a proof of anchor persistence from first loss of an external coordinate;
2. a uniform charging of anchor migration to already valid exits;
3. an explicit counterexample satisfying all global no-IT and minimality
   hypotheses, which would refute the route;
4. a stronger global product-space covering theorem that directly yields the
   same diffuse/anchor dichotomy.

New terminal names, local box estimates, or finite-instance enumerations do not
change the active node by themselves.
