# Fork macro-record arity barrier

## Status and purpose

This note audits the proposed replacement of the output-to-source transport in
`S1 / Q-0019` by a source-owned nested-refill macro record.  It proves a no-go
statement for the **direct** version: attach target coordinates to every fork,
record the first later actual output edge, and use its target codimension as a
fork penalty in the matching-record generating function.

The audit does not rule out a macro code with an additional source-determined
edge identity, an irreversible fourth coordinate, or a new uniform
future-closure invariant.  It shows that F-0093/F-0094 alone do not supply such
an invariant.

## 1. Exact marked matching growth

Give each unit of matching excess the optimistic multiplicative penalty
\(y\in[0,1)\).  The node polynomial is

\[
  \Phi_y(z)
  =1+\sum_{r\ge1}y^{r-1}\Delta^r z^{2r}
  =1+\frac{\Delta z^2}{1-y\Delta z^2}.
\]

Writing \(u=\Delta z^2\), the exact infimum in the corresponding
simply-generated-tree envelope is

\[
  G(y)
  :=\inf_{0<u<1/y}
  \frac{1+(1-y)u}{\sqrt u(1-yu)}.
\]

For \(y=0\), \(G(0)=2\).  For \(0<y<1\), the unique minimizing point is

\[
  u_y=
  \frac{\sqrt{1+8y}-1-2y}{2y(1-y)},
\]

and \(G(y)>2\).  Thus, if \(c=\Delta/b^2\), a marked-record contradiction
requires

\[
  \sqrt c\,G(y)<1.
  \tag{1.1}
\]

In particular, along any sequence \(c\to1/4\), condition (1.1) forces
\(y\to0\).  A fixed positive penalty factor, even one strictly below one,
cannot recover the asymptotic one-quarter threshold.

## 2. What a directly recorded three-edge pays

Consider a deterministic auxiliary target refinement on \(n\) blocks.  A
fixed off-pivot F-0094 output edge containing three target coordinates has at
most \(b^{n-3}\) target preimages.  This pointwise \(b^{-3}\) statement is not
yet a degree-coded record weight.

To bound the number of possible actual output edges by \(\Delta\), the decoder
must know one actual endpoint of the edge.  If no endpoint is fixed by the
source parent, locating that endpoint costs one target coordinate, or
equivalently stores that coordinate in the output state.  Even granting fixed
block roles and ignoring constant role factors, the best direct count is

\[
  b\Delta\,b^{n-3}
  =\frac{\Delta}{b^2}b^n.
  \tag{2.1}
\]

The same normalized factor occurs for a two-target link edge through the
already fixed source pivot: there are at most \(d_H(x)\le\Delta\) edge labels
and \(b^{n-2}\) preimages.  Hence a new actual edge recorded only through the
maximum-degree bound gives, optimistically,

\[
  y_{\rm direct}=\frac{\Delta}{b^2}=c,
  \tag{2.2}
\]

per independently usable fork mark.  The third target coordinate in an
off-pivot edge is the current record node or the endpoint needed to localize
the \(\Delta\)-sized edge list; it is not a free extra child in the matching
record tree.

If the output edge could instead be reconstructed from the original source
label without paying a new \(\Delta\) choice, (2.1) would improve.  That is
precisely an output-to-source incidence theorem, not a consequence of the
local refill box.

## 3. The best-case direct threshold is below one quarter

Give the direct macro route the favorable assumption that every one of the
\((r-1)_+\) excess units of a rank-\(r\) repair independently receives the
factor (2.2).  Substituting \(y=c\) into (1.1), the limiting equality

\[
  \sqrt c\,G(c)=1
\]

has a unique solution in \((0,1/4)\),

\[
  c_0=0.211390706210804\ldots.
\]

Eliminating the minimizing variable \(u_c\) gives

\[
  4c_0^4-12c_0^3+4c_0^2-24c_0+5=0.
\]

Consequently the direct degree-coded macro mark does not make the standard
weighted-tree envelope contract at one quarter, even under the optimistic
independent marking above.  Its self-consistent constant in this envelope is
strictly below \(1/4\).  A smaller actual record language would require an
additional dependence between macro outputs; such a dependence is not present
in the independent-mark substitution itself.

## 4. Why independent repetition does not repair the count

Repeating the same auxiliary refill box \(k\) times makes the all-link
subfamily at most \((d_H(x)/b^2)^k\), but it does not make the complete output
family that small.  In a no-IT full-block parent every target tuple has some
terminal output.  The off-pivot outputs fill the complement, and their actual
edge identities and stopping contexts must remain in a faithful record.

For a deterministic output map \(\varphi\), the exact partition

\[
  b^n=\sum_c|\varphi^{-1}(c)|
\]

is unchanged by tensoring independent copies.  Pointwise fiber bounds become
an entropy loss only after the number or total capacity of admissible
certificates is bounded.  F-0094 bounds the source-pivot link certificates but
does not bound the globally dispersed off-pivot certificate family.

Alternatively, one may follow the actual state after the first off-pivot
repair and repeat there.  The attempted endpoint, pivot and output edge can
then migrate.  Proving that this recursion either dissipates uniformly or
retains one fixed source anchor is exactly the owner-preserving future
transport/closure obligation of Q-0019.  Restarting at the old parent without
recording the intervening outputs discards genuine target information;
recording them restores the count above.

Two existing regression mechanisms show why neither omission is harmless.
The diagonal dispersed-incidence model of A-0024 lets successive off-pivot
outputs use disjoint actual vertices and edges, so the number of output
contexts grows without creating a high-degree anchor.  The live pair-fan
two-cycle of A-0050 lets actual-successor mass return reversibly between a
small set of edges, so recurrence alone is not dissipation or all-release
closure.  These models have not been promoted to low-degree no-IT
counterexamples; they refute only the local/interface inference used by the
direct macro count.

## 5. Conclusion and retry conditions

The direct nested-refill macro does not bypass Q-0019.  It either

1. records each new actual output edge, yielding only the constant-scale
   factor \(\Delta/b^2\) and a best-case threshold \(c_0<1/4\); or
2. repeats through actual successors, in which case source ownership and
   fixed-anchor future closure must still be proved.

A genuinely new macro route must provide at least one of the following:

- an output edge determined by the existing source record without a fresh
  \(\Delta\)-choice;
- an additional irreversible coordinate beyond the two children already paid
  for by a three-edge repair;
- a uniform source-owned stopping modulus whose residual is
  \(o_b(1)\), not merely zero for each fixed instance;
- an all-successor fixed-anchor closure theorem.

Without one of these additions, calling the F-0094 \(b^{-3}\) pointwise fiber
an \(o(1)\) macro-record penalty double-counts the current target coordinate
and loses faithful actual-edge identity.
