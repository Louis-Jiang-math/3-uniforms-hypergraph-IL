# Fork-rooted refill box

## Status and role

This note proves a local, actual-history-preserving input lemma for
`S1 / Q-0019`.  It replaces the static private-transversal box by a product
refinement rooted at the actual canonical matching repair.  It does **not**
prove the global inverse-fiber decomposition: the diffuse output load obtained
below is load on the first later blocker edge, not the original fork-edge load
\(\ell_x\).

## 1. Input

Let \(H\) be a partitioned three-uniform hypergraph with block size \(b\).
Fix an actual parent occurrence consisting of

\[
  \omega=(h,\operatorname{owner},\operatorname{root},S,x,M),
\]

where

- \(S\) is an independent partial transversal;
- \(x\) lies in a block missed by \(S\);
- \(M\) is a canonically chosen maximal matching in the blocker-link graph
  \(G_x(S)\);
- the complete parent history, owner, root, actual blocker family and actual
  matching-edge identities are retained in \(\omega\).

Write

\[
  R_0=(S\cup\{x\})\setminus V(M).
\]

By maximality of \(M\), every blocker pair meets \(V(M)\), so \(R_0\) is an
independent partial transversal.  Let \(\mathcal J\) be the set of blocks met
by \(S\), together with the block of \(x\).  Thus

\[
  |\mathcal J|=|S|+1.
\]

Attach a full coordinate refinement

\[
  Q=(q_B)_{B\in\mathcal J}\in\prod_{B\in\mathcal J}B.
\]

This is an auxiliary no-copy refinement: an atom of parent weight \(w(\omega)\)
is split into \(b^{|\mathcal J|}\) atoms of weight
\(w(\omega)b^{-|\mathcal J|}\).  The parent fields are never discarded.

## 2. Refill process

Maintain an independent partial transversal \(R\), a set \(I\subseteq
\mathcal J\) of blocks whose target coordinate has already been installed,
and the current set of holes in \(\mathcal J\).  Initially

\[
  R=R_0,\qquad I=\varnothing.
\]

The holes are precisely the blocks of \(V(M)\).  Repeat the following using a
fixed order on blocks, vertices and actual edges.

1. Let \(B\) be the first current hole and attempt \(q_B\).
2. If \(R\cup\{q_B\}\) is independent, install \(q_B\), put \(B\) into
   \(I\), and continue.
3. Otherwise every blocker contains \(q_B\), because \(R\) was independent.
   If some actual blocker contains a vertex \(q_C\) with \(C\in I\), stop at
   the first such actual blocker \(g\), retaining the stopping block and the
   complete history.
4. If no blocker contains an already installed target coordinate, both
   non-attempted endpoints of every blocker are inherited vertices of
   \(S\cup\{x\}\).  Choose the canonical maximal matching \(N\) in the
   complete blocker-link graph, set
   \[
     R\leftarrow(R\cup\{q_B\})\setminus V(N),
   \]
   put \(B\) into \(I\), and continue.  The new state is independent by the
   canonical matching-repair lemma.

In step 4 no installed target coordinate is deleted: the continuation
hypothesis says that every blocker pair consists entirely of inherited
vertices, hence so does \(V(N)\).  Consequently \(I\) strictly increases at
every iteration and is never decreased.  The process therefore makes at most
\(|\mathcal J|\) attempts.

## 3. Exact dichotomy

### Lemma 3.1 — augmentation or two-coordinate blocker

For every parent occurrence \(\omega\) and every target tuple \(Q\), the
refill process has exactly one of the following outcomes.

1. **Augmentation.**  The process has no hole left.  Its final state is an
   independent partial transversal meeting every block of \(\mathcal J\), and
   hence has size \(|S|+1\).
2. **Two-coordinate blocker.**  The process stops at an actual edge \(g\)
   containing the current target coordinate \(q_B\) and at least one earlier
   installed target coordinate \(q_C\).  Thus \(g\) contains target
   coordinates from at least two distinct blocks.

#### Proof

Independence is preserved at a successful insertion and by every canonical
matching repair.  Each iteration installs the target coordinate of one new
block, and continuation repairs delete only inherited vertices in as-yet
uninstalled blocks.  Hence no block is processed twice and the process
terminates.

If it terminates without the stopping event, every hole has been filled.
There is then exactly one selected vertex in every block of \(\mathcal J\),
and the maintained independence gives outcome 1.  Otherwise step 3 supplies
an actual blocker containing the current installed coordinate and an earlier
one, which is outcome 2.  The alternatives are disjoint by the first-stopping
rule.  \(\square\)

## 4. Uniform inverse multiplicity

At a stopping event choose, by the fixed block order, the first previously
installed target block \(C\) appearing in \(g\), and record the unordered
witness pair

\[
  P=\{B,C\}
\]

together with the actual output edge \(g\).  For a fixed parent \(\omega\) and
a fixed certificate \((P,g)\), the two target coordinates in the blocks of
\(P\) are fixed by the actual vertices of \(g\).  Therefore

\[
  \#\{Q:\text{the output certificate is }(P,g)\}
  \le b^{|\mathcal J|-2}.
\]

After the uniform product refinement, the output mass of a fixed certificate
\((P,g)\) from parent \(\omega\) is at most

\[
  \frac{w(\omega)}{b^2}.
\]

Now let \(\Omega\) be any weighted family of parent occurrences, retaining
their histories, and put \(W=\sum_{\omega\in\Omega}w(\omega)\).  Summing the
pointwise estimate over the disjoint parent atoms gives

\[
  L(P,g)\le \frac{W}{b^2}.
\]

An actual three-edge has at most three unordered pairs of coordinate blocks,
so after the witness pair is forgotten its total received diffuse load
satisfies

\[
  L(g)\le \frac{3W}{b^2}.
\]

This constant is independent of the number of blocks, the matching rank, the
number of parent histories and the size of a finite history graph.  Actual
edge identities are not merged in establishing the estimate: it is first
proved separately on every parent atom and only then summed for the same
actual output edge.

## 5. Pivot-protected refinement

There is a second canonical refill rule that retains the original pivot and
sharpens the description of the unresolved output.  Initially \(x\in R_0\).
At every stage protect

\[
  P_x=\{x\}\cup\{q_C:C\in I\}.
\]

After attempting \(q_B\), inspect the complete blocker family.  If some
blocker has both non-attempted endpoints in \(P_x\), stop at the first such
actual edge.  Otherwise every blocker pair meets the deletable inherited set
\(R\setminus P_x\).  Choose a canonical inclusion-minimal subset of
\(R\setminus P_x\) hitting all blocker pairs, delete it, install \(q_B\), and
continue.  Such a hitting set exists because the whole deletable inherited
set hits every pair.  This repair preserves independence and never deletes
\(x\) or an installed target coordinate, so the same strictly increasing
installed-block argument proves termination.

### Lemma 5.1 — protected-pivot trichotomy

For every parent \(\omega\) and target tuple \(Q\), the pivot-protected process
has exactly one of the following outcomes.

1. an independent augmentation of size \(|S|+1\) that still contains \(x\);
2. an actual link edge \(g=\{x,q_B,q_C\}\) containing \(x\) and two target
   coordinates;
3. an actual off-pivot edge \(g=\{q_B,q_C,q_D\}\) consisting of three target
   coordinates.

Indeed, the two old endpoints of a stopping blocker lie in \(P_x\).  If one is
\(x\), the other is an earlier installed target coordinate.  If neither is
\(x\), both are earlier installed target coordinates.  These are outcomes 2
and 3.  If there is no stopping blocker, all holes are eventually filled and
the protected pivot remains selected, giving outcome 1.

For a weighted parent family of total mass \(W\), a fixed link output through
\(x\) receives at most \(W/b^2\), while a fixed off-pivot target edge receives
at most \(W/b^3\).  Consequently the total link-output mass is at most

\[
  \frac{d_H(x)}{b^2}W.
\]

This is a genuine source-pivot-preserving estimate.  It does not make outcomes
1 or 3 into accepted global exits: an augmentation is still only a larger
partial transversal, and one off-pivot target edge does not imply that the
complete non-pivot block system has no independent transversal.

## 6. What remains open

The estimate above concerns the later output edge \(g\).  The active load in
Q-0019 is instead

\[
  \ell_x(e)=\sum_f w_x(e,f)
\]

on the original fork edges through the original pivot \(x\).  The refill map
does not ensure that \(g\) contains \(x\), and it does not give an injective
actual repair from \(g\) back to the original source edge.  Consequently

\[
  L(g)=O(W/b^2)
  \quad\not\Rightarrow\quad
  \ell_x^*=O(F_x/b^2).
\]

At the level of the proved marginals this nonimplication is exact.  A single
source row of mass \(W\) may be split without copying among \(b^2\) distinct
certificate columns, each of mass \(W/b^2\).  Every certificate bound in
Section 4 then holds, while the original row load is still \(W\).  This is an
interface table, not a claimed counterexample realizable by a block-minimal
no-IT hypergraph; it shows that an additional incidence or future-closure
theorem is logically necessary.

The unresolved theorem is a mass-transport statement: either transport the
diffuse certificate back to the original fork load without duplicating
capacity, or show that repeated failure of such transport yields a
future-complete fixed anchor.  In the protected version, the same obligation
is concentrated in the independent-augmentation and off-pivot target-edge
outcomes.  Neither is by itself a global independent transversal, a complete
proper-block subsystem, or a paid exit.  Treating the stopping edge as a new
owner, forgetting the parent occurrence, or calling pivot migration a terminal
would repeat A-0044 and A-0048--A-0050.
