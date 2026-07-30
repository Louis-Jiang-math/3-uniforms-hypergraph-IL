# Route-B finite atlas, history-aware LP, and product-chart ledger

## 1. Scope and status

- **Role:** supporting proof package for `S1 / Q-0018`.
- **Status:** the finite-state and clean-chart statements below are proved in
  their stated scopes. They do not construct the required global execution from
  every target hypergraph and do not prove the one-quarter theorem.
- **Executable support:** `src/hypergraph_il/route_b_atlas.py`,
  `tests/test_route_b_atlas.py`, and
  `enumerate/route_b_lp_atlas_validation.py`.
- **Bounded evidence:**
  `evidence/experiments/route_b/baselines/route_b_lp_atlas_validation.json`.

Throughout, a faithful execution state retains actual selected vertices,
blocker-edge identity, attempted vertex, released endpoint, pivot, support,
genealogy/interface token, and the separate ledgers required by FW-60.

## 2. Competing blockers: exact release structure

Let `T` be an independent one-hole partial transversal and let `x` be inserted
in the missing block. Write

\[
\mathcal K(T,x)=\{e\in E(H):e\subseteq T\cup\{x\}\}.
\]

Every member of \(\mathcal K(T,x)\) contains \(x\), because otherwise it would
already lie in the independent set \(T\).

### Theorem 2.1 — common-release criterion

For an old selected vertex \(r\in T\),

\[
(T-r)+x\text{ is independent}
\quad\Longleftrightarrow\quad
r\in\bigcap_{e\in\mathcal K(T,x)}(e\setminus\{x\}).
\]

**Proof.** If some blocker \(e\) avoids \(r\), then
\(e\subseteq(T-r)+x\), so the released state is not independent. Conversely,
if every blocker contains \(r\) and the released state contains an edge \(f\),
then \(f\) contains \(x\) and belongs to \(\mathcal K(T,x)\), contradicting
that every blocker contains the deleted vertex \(r\). ∎

### Corollary 2.2 — release rank at most one

If \(|\mathcal K(T,x)|\ge2\), there is at most one legal single release.

**Proof.** If two old vertices \(r,p\) were both legal, every blocker would
contain the three vertices \(x,r,p\). Three-uniformity would force every
blocker to equal \(\{x,r,p\}\). ∎

Thus a live multi-blocker event has a unique common release \(r\) and all
blockers have the form

\[
\{x,r,p\},\qquad p\in P(T,x,r).
\]

If the common intersection is empty, the event is a genuine release deadlock.
The implementation function `legal_release_vertices` computes the exact
intersection and the tests cover both cases.

## 3. Fresh/return multiplicity

Fix a faithful support-interface token \(\sigma\) sufficient to determine the
complete blocker family, legal releases, successor, and retained labels. Fix an
actual attempted vertex and blocker incidence \((x,e)\).

Because Corollary 2.2 gives at most one release, a fixed triple
\((\sigma,x,e)\) determines at most one actual live transition. Along any
finite genealogy, partition occurrences of \((x,e)\) into:

1. the first occurrence of each distinct token \(\sigma\);
2. later occurrences of a token already seen.

If \(G_\Gamma(x,e)\) is the number of distinct tokens and
\(R_\Gamma(x,e)\) the number of repeated occurrences, then

\[
|\mathcal O_\Gamma(x,e)|=G_\Gamma(x,e)+R_\Gamma(x,e).
\]

This is an exact partition, not a capacity estimate. Repetition along one
branch produces a sound return cycle; repetition on incomparable branches is a
genealogy merge and must enter the information-loss/exact-future-core branch.
Consequently a bare incidence \((x,e)\) has no uniform capacity. The precise
resource is \((\sigma,x,e)\), with first occurrences paid by support progress
and repeats sent to return/core analysis.

## 4. Wide fans and heavy real pair fibers

Fix a live event with common pair \((x,r)\). For every remaining block \(C\),
let

\[
N_C(x,r)=\{p\in C:\{x,r,p\}\in E(H)\},\qquad d_C=|N_C(x,r)|.
\]

Let \(\Sigma\subseteq\prod_C S_C\) be the actual family of fresh external
supports for a fixed internal kernel, where \(S_C=\pi_C(\Sigma)\).

### Theorem 4.1 — rectangle or support-correlation witness

Either

\[
\Sigma=\prod_C S_C,
\]

or there is a finite actual witness

\[
z^*\in\prod_C S_C\setminus\Sigma.
\]

Every coordinate of \(z^*\) occurs in an actual support, but the coordinates
cannot be jointly realized. This is an `S`-type support-correlation witness.

### Theorem 4.2 — product-tail wide-fan bound

Assume \(\Sigma=\prod_C S_C\). Put
\(g_C=|S_C\cap N_C(x,r)|\). The number of supports containing at least three
pair-neighbors is

\[
\sum_{\substack{J\subseteq\mathcal C\\|J|\ge3}}
\prod_{C\in J}g_C\prod_{C\notin J}(|S_C|-g_C).
\]

Every actual wide fan is counted by this expression, hence its fresh-support
count is at most that value.

**Proof.** Partition the product support by the exact set of coordinates that
fall in \(S_C\cap N_C(x,r)\). The displayed summands count disjoint classes. A
wide fan needs at least three distinct pivot blocks. ∎

For five total blocks there are exactly three remaining blocks, and therefore

\[
F_{x,r}\le d_1d_2d_3
\le\left(\frac{d(x,r)}3\right)^3,
\quad d(x,r)=d_1+d_2+d_3.
\]

Summing over release vertices and using

\[
\sum_r d(x,r)=2\deg_H(x)
\]

gives

\[
F_x\le\frac1{27}\sum_r d(x,r)^3
\le\frac{2}{27}D_x^2\deg_H(x),
\qquad D_x=\max_r d(x,r).
\]

Thus large normalized fan mass forces a linear-size actual pair fiber. It does
not by itself prove a \(b^2/4\) vertex degree.

## 5. Exact critical deficit

For \(a=(a_1,\ldots,a_n)\in[0,1]^n\), define

\[
F_n(a)=\frac1{n(n-1)}\sum_{i\ne j}a_i(1-a_j).
\]

Writing \(S=\sum_i a_i\) and
\(P=\sum_i a_i(1-a_i)\), direct expansion gives

\[
\frac{n}{4(n-1)}-F_n(a)
=
\frac{(n-2S)^2}{4n(n-1)}+\frac{P}{n(n-1)}.
\]

This is F-0038. The implementation independently checks the identity through
`critical_deficit` and `cross_mass`.

If the deficit is at most \(\delta\), then

\[
\left|S-\frac n2\right|\le\sqrt{\delta n(n-1)},
\qquad
P\le\delta n(n-1).
\]

For any \(0<\varepsilon\le1/2\), the number of coordinates in
\([\varepsilon,1-\varepsilon]\) is at most

\[
\frac{\delta n(n-1)}{\varepsilon(1-\varepsilon)}.
\]

These are exact algebraic stability conclusions. Translating deficit into
execution progress needs the chart ledger below.

## 6. Clean product-chart ledger

Fix a finite faithful product chart with no reroot inside the chart and no
uncertified `S` or cross-anchor `A` transition. Let \(G\) be the finite external
future-compatible state graph and let \(\rho\) be a strict topological rank on
its SCC condensation.

Use the faithful genealogy unfolding. At a node \(u\) of mass \(m(u)\), split
each of the \(n\) candidate directions into a continuation part of relative
mass \(a_i(u)\) and a first-stop/first-exit part of relative mass
\(1-a_i(u)\). A successor remaining in the same external SCC is not counted as
transient progress; it enters the recurrent-module ledger. Every transient
successor therefore increases \(\rho\) by at least one.

Let \(C(u)\) be total transient continuation mass and \(L(u)\) first-stop or
first-exit mass. The critical deficit admits a nonnegative decomposition

\[
m(u)D(a(u))=D^+(u)+D^-(u),
\qquad D^+(u)\le C(u),\quad D^-(u)\le L(u).
\]

To verify this, split indices at \(a_i=1/2\). The nonbinary term
\(a_i(1-a_i)\) is bounded by \(a_i\) on the low side and by \(1-a_i\) on the
high side. The imbalance term is paid by the majority side; if
\(S\ge n/2\),

\[
\frac{m(S-n/2)^2}{n(n-1)}
\le C(u)-\frac{m(u)}2,
\]

and the opposite case is symmetric.

First-stop genealogy cylinders are pairwise disjoint: incomparable nodes have
disjoint parent cylinders, while a sample stopped at an ancestor cannot reach a
descendant. Hence, summing over the chart,

\[
\sum_u m(u)D(a(u))
\le G_{\rm rank}+G_{\rm leaf}+G_S+G_A+G_C+G_{\rm reset}.
\]

This theorem controls execution mass. It does not yet give a bounded-multiplicity
map from rank/leaf mass to distinct original hypergraph edges.

## 7. History-aware LP and residual core

Let \(\tau:s\to s'\) range over a finite faithful quotient's actual
transitions, with actual blocker identity \(e(\tau)\). Remove transitions with
certified `W/M/A/N` witnesses. Form the reduced history graph whose vertices are
the remaining transitions and whose arcs are

\[
\tau\rightsquigarrow\sigma
\quad\Longleftrightarrow\quad
\operatorname{head}(\tau)=\operatorname{tail}(\sigma)
\text{ and }e(\tau)\ne e(\sigma).
\]

The edge inequality excludes the local same-edge release oscillation `R`.

### Theorem 7.1 — finite potential-or-core equivalence

The following are equivalent:

1. there is a potential \(h\) with
   \[
   h(\sigma)-h(\tau)\ge1
   \]
   on every reduced-history arc;
2. the reduced history graph is acyclic;
3. there is no uncertified multi-edge residual circulation.

**Proof.** A strict potential cannot sum positively around a cycle. Conversely,
a finite DAG has a strict topological rank. ∎

The resource-priced LP version adds nonnegative witness terms to certified
transitions. If it is infeasible after all certified modules are exposed, its
dual supports a genuine residual circulation preserving actual blocker-edge
history. The code tests that a same-edge two-cycle is removed, a two-edge cycle
survives, and a certified transition breaks the residual cycle.

## 8. Finite signature atlas and overflow

For a finitely branching faithful execution, define

\[
\sigma_0(u)=d(u),
\]

and recursively

\[
\sigma_{k+1}(u)=
\left(d(u),\left\{\!\left\{(\lambda(u,v),\sigma_k(v)):u\to v\right\}\!\right\},
\operatorname{stop}(u)\right).
\]

For fixed \(k\), there are finitely many signatures whenever the current-data
and one-step-label alphabets are finite and branching is bounded.

If equality of \(\sigma_K\) already determines equality of
\(\sigma_{K+1}\), the induced finite partition is a future-compatible
congruence. Equality of the \((K+1)\)-signature gives a same-label matching of
all legal successors whose \(K\)-signatures agree. The partition then remains
stable at every deeper level.

Therefore:

- **finite completion:** a stable signature level gives a finite faithful atlas;
- **overflow:** if no level stabilizes, finite future interfaces keep strictly
  refining. Compatible overflow signatures have an inverse-limit exact-future
  object by König's lemma.

Repeated exact types give a return/recurrent object. Nonrepetition gives
unbounded interface complexity. Deriving a concrete `W/S/A` consequence from
that complexity remains an open overflow-structure problem.

## 9. Fixed-rank local realizability is not automatic

The repository also retains an executable five-block binary counterexample to
automatic 3-local realizability. The eleven real edges are listed in
`tests/test_route_b_atlas.py::test_four_tool_dynamic_deadlock_counterexample`.
From the base one-hole state `(1,1,0,1,*)`, every proper subset of the four
coordinate changes is reachable by an actual blocker-release path, but the
all-four target `(0,0,1,0,*)` is a release deadlock. The test exhausts the finite
one-hole transition graph and obtains exactly the return masks
`{0,1,...,14}`. Thus three-uniformity does not imply that every dynamic
incompatibility has a binary or ternary witness.

## 10. Bounded computation and interpretation

The committed generated artifact records:

- all 50,528 edge-minimal four-block binary star-forest covers;
- 50,524 block-minimal covers, split into 50,256 `M`, 260 nonnormal `N`, and 8
  normal \(Q_4\) models;
- all 272 coordinate perfect matchings, all 8 normal matchings, 192 normal
  one-hole states, and 768 release policies with the existing `384/192/192`
  classification;
- fixed-seed bounded \(b=3\) searches in which raw same-edge release kernels are
  removed by the `R` history reduction and no new reduced residual core is
  found in the committed sample.

These are computational observations only. The generator, command, parameters,
seeds, platform, Python version, result type, and payload SHA-256 are embedded
in the artifact.

## 11. Remaining closure gaps and reliability assessment

The finite LP/chart work leaves three logically separate gaps.

### Gap A — critical-profile identification

**Expected form.** In a clean chart, identify \(F_n(a)\) with the normalized
actual pair-cylinder cross mass; any mismatch must yield an explicit
`W/M/A/N/S/R/reset` witness.

**Reliability estimate:** high. Existing clean-chart computations show no
independent mismatch, and most remaining work is faithful normalization and
chart-interface bookkeeping. This is not yet proved globally.

### Gap B — heavy-pair aggregation

**Direct form judged unreliable.** A single linear pair codegree
\(d_H(x,r)\ge\alpha b\) does not imply
\(\Delta(H)\ge(1/4-o(1))b^2\). The proved wide-fan theorem stops at a real heavy
pair fiber.

**Expected reliable form.** Positive heavy-pair load must either concentrate
many fibers at a common actual vertex, generate distinct real-edge growth, or
form an `S/A` pair-codebook/recurrent core.

**Reliability estimate:** medium for the global dichotomy, low for a direct
heavy-pair-to-\(1/4\) implication.

### Gap C — residual-core saturation

**Expected form.** Classify residual actual-support cores into finite rigid
normal/codebook templates and prove a density, augmentation, complete-block, or
accepted-defect consequence for each.

**Reliability estimate:** high that residual cores are rigid; low-to-medium that
all such cores can be eliminated or forced into a single-pivot/product form.
Normal \(Q_4\), fixed-light-anchor, and diagonal-codebook tests rule out those
strong shortcuts.

No gap is closed by the bounded computations, and the one-quarter theorem,
Q-0018, Q-0017, and Q-0016 remain open.
