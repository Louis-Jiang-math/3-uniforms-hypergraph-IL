# Faithful Round-or-Core on an exact execution tree

- **Status:** proved-conditional supporting theorem.
- **Role:** finite/exact interface for `S1 / Q-0018`.
- **Input scope:** an exact finitely branching actual execution tree with a
  measurable no-copy cylinder decomposition, a first-owner stopping line,
  complete actual blocker-edge candidate sets, and separately verified root and
  projection-slot budgets.
- **Output:** an exact finite-depth dynamic max-flow/min-cut formula, a pathwise
  realization of every feasible flow by disjoint actual sample mass, and a
  `Round / named exit / same-edge R / recurrent core / overflow` alternative.
- **Nonclaims:** no construction of the required execution tree from every target
  hypergraph; no proof of root/slot budgets; no overflow conversion; no
  classification of recurrent actual-support cores; no one-quarter theorem.

## 1. Exact execution-tree interface

Let `(Omega, mu)` be a finite measure space. We may replace it by the atomless
extension

\[
(\Omega\times[0,1],\mu\otimes\lambda)
\]

when a measurable set must be split by an arbitrary real amount.

Let `T` be a finitely branching rooted forest with a finite root antichain
`I`. Thus every finite-depth truncation has finitely many nodes. Every node `u`
has a measurable actual-history cylinder
`Omega_u`. If `v` is a child of `u`, then

\[
\Omega_v\subseteq\Omega_u.
\]

For each node `u`, the child cylinders and named-exit cylinders are pairwise
disjoint and satisfy

\[
\Omega_u
=
\bigsqcup_{v\in\operatorname{Ch}(u)}\Omega_v
\sqcup
\bigsqcup_{\xi\in\operatorname{Exit}(u)}\Omega_{u,\xi}.
\tag{1.1}
\]

A named exit may be an augmentation, a release deadlock, or an independently
certified `W/M/A/N/S/reset` module. A non-exit history has an actual successor.

The roots partition the entrance mass:

\[
\Omega_{\mathrm{ent}}=\bigsqcup_{i\in I}\Omega_i,
\qquad
M:=\mu(\Omega_{\mathrm{ent}})<\infty.
\tag{1.2}
\]

Every node stores the complete actual state data needed by the faithful
execution contract, including actual blocker-edge identity, root projection,
pivot/release data, support, and genealogy. Its actual candidate edge set is

\[
\Gamma(u)\subseteq E(H).
\]

The interface requires `Gamma(u)` to be constant on `Omega_u`; otherwise the
node must first be faithfully refined.

Each entrance root has a unique preassigned owner

\[
\operatorname{own}(i)=(r(i),s(i),\sigma(i)),
\]

and all descendants inherit this owner. The root/configuration and
projection-sensitive slot inequalities are external hypotheses:

\[
\sum_{i:r(i)=r}\mu(\Omega_i)\le C_R(r),
\qquad
\sum_{i:s(i)=s}\mu(\Omega_i)\le C_S(s).
\tag{1.3}
\]

The present network never changes an owner, so it cannot create new root or slot
mass.

Finally, every actual edge `e` has an externally supplied global capacity
`c(e) >= 0`.

## 2. First-owner stopping line

Suppose the forest is obtained from a larger actual execution by taking, for
each sample, the first failure obligation not already absorbed by a named exit.
Then the first-obligation nodes form an antichain.

### Lemma 2.1 — no-copy first ownership

The first-owner cylinders are pairwise disjoint. Any faithful refinement only
splits them, and therefore

\[
\sum_{i\in I}\mu(\Omega_i)=M.
\tag{2.1}
\]

No sample receives two root or slot budgets.

### Proof

Two first-obligation nodes cannot be comparable: a descendant of a first
obligation is not first. Incomparable execution-tree cylinders are disjoint.
Refinement replaces a cylinder by a disjoint measurable partition and hence
preserves its total measure. ∎

## 3. The depth-`L` dynamic routing network

Fix a finite depth `L`, and let `T_L` be the nodes at distance at most `L` from
`I`. Construct a directed network `N_L` with source `s`, sink `t`, one node for
every `u in T_L`, and one gate `g_e` for every actual edge appearing in a
candidate set.

The capacities are:

1. entrance arcs
   \[
   s\to i,
   \qquad
   \operatorname{cap}(s,i)=\mu(\Omega_i);
   \tag{3.1}
   \]
2. actual continuation arcs
   \[
   u\to v,
   \qquad
   \operatorname{cap}(u,v)=\mu(\Omega_v)
   \quad(v\in\operatorname{Ch}(u)\cap T_L);
   \tag{3.2}
   \]
3. candidate certification arcs
   \[
   u\to g_e
   \quad(e\in\Gamma(u))
   \tag{3.3}
   \]
   with a common capacity `B` larger than
   \[
   M+\sum_e c(e);
   \]
4. global actual-edge gates
   \[
   g_e\to t,
   \qquad
   \operatorname{cap}(g_e,t)=c(e);
   \tag{3.4}
   \]
5. named-exit arcs
   \[
   u\to t,
   \qquad
   \operatorname{cap}(u,t)
   =q(u):=\sum_{\xi\in\operatorname{Exit}(u)}
     \mu(\Omega_{u,\xi}).
   \tag{3.5}
   \]

Nodes on the depth frontier have no continuation arcs beyond depth `L`.
Let `F_L` be the maximum flow value.

For `U subseteq T_L`, define

\[
\mu_{\mathrm{in}}(U)
=
\sum_{i\in I\cap U}\mu(\Omega_i),
\tag{3.6}
\]

\[
\kappa_L^+(U)
=
\sum_{\substack{u\in U,\ v\notin U\\u\to v\text{ continuation}}}
\mu(\Omega_v),
\tag{3.7}
\]

\[
q(U)=\sum_{u\in U}q(u),
\qquad
\Gamma(U)=\bigcup_{u\in U}\Gamma(u),
\tag{3.8}
\]

and

\[
d_L(U)
=
\mu_{\mathrm{in}}(U)
-
\kappa_L^+(U)
-
q(U)
-
\sum_{e\in\Gamma(U)}c(e).
\tag{3.9}
\]

## 4. Exact finite-depth Round-or-Cut

### Theorem 4.1

For every finite depth `L`,

\[
\boxed{
M-F_L=
\max_{U\subseteq T_L} d_L(U)_+.
}
\tag{4.1}
\]

Thus, for every `eta in [0,1)`, either

\[
F_L\ge(1-\eta)M,
\tag{4.2}
\]

or there is an explicit dynamic Hall cut `U` satisfying

\[
d_L(U)>\eta M.
\tag{4.3}
\]

### Proof

Consider a finite-capacity `s-t` cut and let `U` be the execution nodes on the
source side. Since `B` exceeds the capacity of the cut consisting of all
entrance arcs, no minimum cut crosses an arc `u -> g_e`. Hence every gate in
`Gamma(U)` is also on the source side.

For fixed `U`, the least-capacity cut with these execution nodes on the source
side contains exactly:

- the entrance arcs to roots outside `U`, of total capacity
  \[
  M-\mu_{\mathrm{in}}(U);
  \]
- continuation arcs leaving `U`, of total capacity `kappa_L^+(U)`;
- named-exit arcs from `U`, of total capacity `q(U)`;
- gate arcs `g_e -> t` for `e in Gamma(U)`, of total capacity
  \[
  \sum_{e\in\Gamma(U)}c(e).
  \]

Its capacity is therefore

\[
M-d_L(U).
\]

Minimizing over `U` and applying max-flow/min-cut gives (4.1). Equations
(4.2)--(4.3) are immediate. ∎

The cut is not itself a new structural defect. It records the exact amount by
which entrance demand exceeds all currently exposed continuation, named-exit,
and actual-edge capacities.

## 5. Pathwise realization and no-copy rounding

The network flow is fractional, but the execution tree supplies enough
measurable structure to realize it by disjoint actual sample mass.

### Theorem 5.1 — pathwise realization

Every feasible flow `f` in `N_L` can be represented on the atomless extension of
`Omega` by measurable sets with the following properties.

For every execution node `u`, there is a set `R_u subseteq Omega_u` whose
measure is the total flow entering `u`. The set `R_u` is partitioned into:

- sets `R_{u,v} subseteq Omega_v` of measure `f(u,v)` for continuation arcs;
- named-exit subsets of total measure `f(u,t)` contained in the actual exit
  cylinders at `u`;
- sets `R_{u,e}` of measure `f(u,g_e)` assigned to actual edge `e`.

All sets assigned to different source-to-sink paths are disjoint. Consequently:

1. each actual sample is assigned at most once;
2. each assigned sample follows one actual continuation history before it is
   certified by one actual edge or one named exit;
3. each actual edge receives total mass at most `c(e)`;
4. root and slot ownership are inherited and never duplicated.

### Proof

Proceed upward from depth `L`.

Assume the required sets have been constructed for all children of `u`. For a
child `v`, the realized set `R_v` has measure `f(u,v)` and lies inside
`Omega_v`. Different child cylinders are disjoint by (1.1), so the child sets
are disjoint.

Choose first, inside the union of the named-exit cylinders at `u`, a measurable
set of measure `f(u,t)`. This is possible because `f(u,t) <= q(u)`. Then choose
pairwise disjoint measurable subsets for the edge flows `f(u,g_e)` from the
remaining part of `Omega_u`.

Flow conservation gives

\[
\sum_v f(u,v)+f(u,t)+\sum_e f(u,g_e)
=
\text{flow entering }u
\le \mu(\Omega_u).
\]

Therefore enough measure remains. The atomless extension permits every required
real-valued split. Define `R_u` as the union of the child, exit, and edge pieces.
Its measure equals the incoming flow.

At an entrance root, the same construction uses the source flow `f(s,i)`. The
resulting root sets are disjoint by (1.2). Induction completes the realization.
The actual-edge capacity statement follows from the gate constraint
`f(g_e,t) <= c(e)`. ∎

### Corollary 5.2

If `F_L >= (1-eta)M`, then at least `(1-eta)M` entrance mass has a no-copy
pathwise assignment to actual edges or named exits. If the capacities are
integer multiples of a common atom size, the standard integral max-flow theorem
gives an integral assignment after rescaling.

Algorithmic reverse arcs in a max-flow residual graph are not used as actual
blocker-release transitions. They only compute the final forward assignment.

## 6. Infinite depth: Round, unresolved histories, and overflow

The networks are nested in the sense that every depth-`L` flow remains feasible
at depth `L+1`. Hence

\[
F_1\le F_2\le\cdots\le M.
\tag{6.1}
\]

Let

\[
F_\infty=\lim_{L\to\infty}F_L.
\]

### Round branch

If `F_infty = M`, then for every `eta > 0` some finite depth satisfies

\[
F_L\ge(1-\eta)M,
\]

and Corollary 5.2 gives a faithful near-lossless Round assignment.

### Unresolved-history branch

Let `E_L` be the union of all actual samples that reach a named exit by depth
`L`. The exit cylinders are disjoint actual cylinders, so their mass can be
routed along the unique continuation paths to their dedicated exit arcs.
Therefore

\[
F_L\ge\mu(E_L).
\tag{6.2}
\]

The sets `E_L` increase with `L`. If

\[
\delta:=M-F_\infty>0,
\]

then (6.2) and continuity from below give

\[
\mu\left(
\Omega_{\mathrm{ent}}\setminus\bigcup_L E_L
\right)
\ge\delta.
\tag{6.3}
\]

Thus positive actual mass follows an infinite history containing no named exit.
This conclusion uses actual execution paths, not residual reverse arcs.

## 7. Stable finite atlas: actual recurrent Core

Assume the future-signature hierarchy stabilizes and gives a finite faithful
quotient `Q` preserving current actual data, all same-label legal successors,
actual blocker-edge identity, and ledger increments.

Project the positive-mass infinite non-exit histories from (6.3) to `Q`. The SCC
condensation of `Q` is a finite DAG, so every infinite projected history is
eventually contained in one recurrent SCC.

Classify each such history by its recurrent transition set. If the history is
eventually supported on a single actual blocker-edge identity `e`, it is a
same-edge release oscillation `R_e`. Since `Q` and the set of actual edge labels
appearing in it are finite, either some `R_e` class has positive mass, or the
histories not eventually confined to one edge identity have positive mass.

For a history in the latter class, the transitions occurring infinitely often
form a strongly connected recurrent subgraph and use at least two actual
blocker-edge identities. There are only finitely many recurrent transition
subgraphs of `Q`; hence one actual multi-edge recurrent subgraph supports
positive history mass. After certified modules and same-edge `R` components are
removed, this is an actual multi-edge recurrent core in the sense of F-0052.

Hence the stable-atlas branch has the exact alternative

\[
\boxed{
\text{near-lossless Round}
\ \vee
\text{positive named exit}
\ \vee
R
\ \vee
\text{positive-mass actual multi-edge recurrent core}.
}
\tag{7.1}
\]

If the future signatures do not stabilize, F-0053 requires the unresolved
branch to remain an explicit exact-future overflow object. No finite quotient
may silently merge it.

## 8. Faithful Round-or-Core-or-Overflow theorem

### Theorem 8.1

Under the exact execution-tree hypotheses of Section 1, for every `eta > 0` at
least one of the following holds:

1. **Round:** at some finite depth, at least `(1-eta)M` entrance mass is
   pathwise assigned without duplication to named exits or globally capacitated
   actual edges;
2. **Exit:** positive actual mass reaches an independently certified named exit;
3. **R:** positive actual mass lies in a same-edge release-oscillation component;
4. **Core:** after stable finite future completion and same-edge `R` reduction,
   positive actual mass lies in an actual multi-edge recurrent core;
5. **Overflow:** future signatures never stabilize and the unresolved branch is
   retained as an inverse-limit exact-future overflow object.

### Proof

If `F_infty=M`, use the Round branch of Section 6. Otherwise (6.3) gives positive
mass of infinite non-exit histories. Apply F-0053. Stable signatures give the
`R` or Core alternative of Section 7; nonstabilization gives Overflow. Named exits are
already separated by the execution-tree partition. ∎

## 9. What remains global

Theorem 8.1 closes the finite/exact network part only. A proof for the original
hypergraph still needs:

### E1 — global faithful entrance and Round compatibility

Construct the exact execution tree from every target block-minimal no-IT
instance; prove conservative first ownership, complete candidate blocker sets,
the root/slot budgets, and that the resulting actual-edge Round estimate is the
quantity needed by the existing F-0038/F-0051/F-0042 stability backend.
Critical-profile identification and heavy-pair aggregation are subcontracts of
this entrance/Round backend, not separate final endgames.

### E2 — overflow conversion

Show that unbounded exact-future interface growth yields a named actual
`W/M/A/N/S/reset` consequence, actual resource growth, or a positive-mass
actual recurrent core. F-0053 alone only preserves overflow.

### E3 — actual-support Core Endgame

For every positive-mass actual recurrent core, prove augmentation, a real
near-one-quarter pivot link, a complete real-block no-IT subinstance, or a
strictly positive natural defect. This is Q-0016.

The F-0038 stability identity, the conditional clean-chart ledger F-0051, and
the conditional recurrence criterion F-0042 remain available once E1 supplies
their faithful global input with zero or vanishing loss. They are not promoted
here to an unconditional stability theorem.
