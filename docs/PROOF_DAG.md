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
- **Input:** actual weighted fork occurrences with full owner/root/history
  provenance.
- **Required final output:** an exhaustive no-copy partition into a
  two-coordinate diffuse part, a valid exit part, a complete proper-block part,
  and a future-complete fixed-anchor part.
- **Current backend reduction:** F-0096 removes private support synchronization
  by common-parent exact rollback. F-0097 sends all rank-at-most-one pair
  continuation to the exact low grammar `(1+Delta z)^2`; the irreducible high
  case is rank two. F-0098 rules out a fixed protected-token count as the sharp
  high penalty. F-0099--F-0102 identify a bounded normal-Q4 zipper/support
  geometry, while F-0100 refutes strict endpoint persistence.
- **Current subproblem:** prove an owner-preserving rank-two recurrence in which
  normal continuation either exactly cancels a future obligation or consumes
  only finitely/subexponentially many source-static supports before a verified
  actual-edge reuse/core/exit term. The `[3]^4` support-packing number 12 is
  finite evidence for this mechanism, not yet the recurrence.
- **Quantitative requirement:** the eventual diffuse edge load is
  `O(F_x/b^2)` uniformly, or equivalently the high backend contributes only
  `o_b(1)` exponential weight / `O(1)` free events per source owner before a
  paid term.
- **Forbidden shortcuts:** a common descendant state is not a pair-obligation
  merge; a retryable rollback is not entropy loss; a bounded normal-window
  statistic is not a source charge; the endpoint tuple is not persistent.

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

Progress on S1 now requires at least one **real combinatorial compression**:

1. exact future-interface cancellation of one rank-two pair obligation;
2. an owner-weighted support-return/collision recurrence proving only
   `O(1)`/subexponentially many free normal high events per source occurrence;
3. a uniform actual-edge/codegree capacity paying first support reuse or
   escape;
4. a source-owned irreversible/telescoping coordinate that yields an
   `o_b(1)` high mark; or
5. an explicit counterexample satisfying the full actual-source hypotheses,
   which would refute the backend.

Further migration subtype names, state-only confluence, fixed protected-token
marks, unrooted window densities, or bounded finite enumeration without a
source interface do not count as theorem-level progress.
