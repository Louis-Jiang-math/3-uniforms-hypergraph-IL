# Main proof route

## 1. Status and target

The target is

\[
\Delta(H)<\left(\frac14-o(1)\right)b^2
\Longrightarrow H\text{ has an independent transversal}.
\]

The theorem is open. The primary route is no longer a global terminal-absorption
extension of the root-excess ledger. The active route isolates the mechanism
that naturally yields the constant \(1/4\): canonical rank-two repair.

## 2. Fixed route

\[
\boxed{
\begin{aligned}
&\text{A. finite actual-history organization}\\
&\quad\downarrow\\
&\text{B. canonical maximal-matching repair}\\
&\quad\downarrow\\
&\text{C. disjoint-blocker fork density}\\
&\quad\downarrow\\
&\text{D. global inverse-fiber codimension decomposition}\\
&\quad\downarrow\\
&\text{E. diffuse degree bound or persistent-anchor endgame.}
\end{aligned}}
\]

Only stage D is active at theorem level.

## 3. Stage A: finite actual-history organization

The role of LP and stopping arguments is limited but important. On any supplied
finite faithful history digraph, F-0052 gives the standard equivalence among a
strict potential, acyclicity after named exits are deleted, and absence of a
nonzero residual circulation. Bottom strongly connected components localize
nonterminating behavior.

This stage must retain enough history to determine every legal transition. A
state label that omits the visited set cannot decide whether a successor is a
return. The finite quotient is therefore an input to the argument, not a free
consequence of the physical state alone.

No claim in this stage converts circulation into degree concentration.

## 4. Stage B: canonical maximal-matching repair

Let \(S\) be an independent partial transversal and let \(x\) lie in a missing
block. Define

\[
G_x(S)=\{\{u,v\}\subseteq S:\{x,u,v\}\in E(H)\}.
\]

Choose a maximal matching \(M_x(S)\) by a fixed deterministic order and set

\[
S'=(S\cup\{x\})\setminus V(M_x(S)).
\]

Every blocker pair meets \(V(M_x(S))\), so \(S'\) is independent. If the
matching size is \(r\), the height change is \(1-2r\).

The crucial distinction is

\[
\text{many blockers with matching number one}
\quad\text{versus}\quad
\nu(G_x(S))\ge2.
\]

Only the second case creates a disjoint-blocker fork.

## 5. Stage C: the source of the one-quarter constant

When every repair has matching size zero or one, the faithful record generating
function is

\[
\Phi_0(z)=1+\Delta z^2.
\]

Hence

\[
\inf_{z>0}\frac{\Phi_0(z)}z=2\sqrt\Delta.
\]

The reconstruction count therefore yields the fork-free implication

\[
\Delta<\frac{b^2}{4}\Longrightarrow\text{an independent transversal exists}.
\]

If \(\Delta\le(1/4-\varepsilon)b^2\) and there is no independent transversal,
a weighted version of the same generating function shows that almost every
long execution contains a positive linear density of matching excess. Each
excess unit supplies two actual blocker edges

\[
\{x,u_1,v_1\},\qquad \{x,u_2,v_2\}
\]

with disjoint non-pivot endpoints.

This stage explains the constant \(1/4\) without tuning a final error term.

## 6. Stage D: global inverse-fiber codimension decomposition

For weighted fork occurrences with pivot \(x\), put

\[
F_x=\sum_{\{e,f\}}w_x(e,f),
\qquad
\ell_x(e)=\sum_f w_x(e,f),
\qquad
\ell_x^*=\max_{e\ni x}\ell_x(e).
\]

Then

\[
2F_x=\sum_{e\ni x}\ell_x(e)
\le d_H(x)\ell_x^*.
\]

Thus the diffuse branch closes if

\[
\ell_x^*\le\frac{8+o_b(1)}{b^2}F_x.
\]

F-0092 supplies the local codimension mechanism. For a private transversal of
\(e=\{x,a,b\}\), vary the two non-pivot coordinates. A fixed output edge has
at most one preimage when it uses both new coordinates, and at most \(b\)
preimages when it uses exactly one. The two-coordinate part therefore has the
required \(b^{-2}\) loss.

The theorem-level obstruction is the one-coordinate part. Its heavy auxiliary
vertex or pair may vary from row to row, from source edge to source edge, and
from one future transition to the next. The active theorem Q-0019 must prove a
history-preserving partition into

\[
\text{two-coordinate diffuse}
\sqcup
\text{valid exit}
\sqcup
\text{proper-block subsystem}
\sqcup
\text{future-complete fixed anchor}.
\]

The partition must be exhaustive, no-copy, and quantitatively uniform.

## 7. Stage E: persistent-anchor endgame

Suppose a class is future-complete for a fixed vertex \(p\), every state is an
independent one-hole transversal, and every legal continuation has a unique
blocker containing \(p\). For any full target outside the block of \(p\),
follow target coordinates while preserving \(p\). Either the process finds a
link edge of \(p\) inside the target, or the number of matched target
coordinates increases. Hence every target contains a link edge of \(p\).

There are \(b^{m-1}\) targets and each link edge belongs to \(b^{m-3}\) of
them, so

\[
d_H(p)b^{m-3}\ge b^{m-1},
\qquad d_H(p)\ge b^2.
\]

This closes an already persistent anchor. It does not extract one from a
single heavy inverse fiber.

## 8. Corrected scope of the physical stopping route

The local stopping forest can be retained in fully unfolded history space, but
four former conclusions are disallowed.

1. The mass \(G_\infty^W\) of independent partial completions cannot be deleted
   merely because the full instance has no independent transversal.
2. The label consisting of current completion, blocker and seen resources does
   not determine return status unless visited history is included.
3. A cycle under a selected release policy is not automatically closed under
   every legal release.
4. A tail estimate depending on \(|E(H)|+|V(H)|\) is fixed-instance, not a
   uniform asymptotic gap.

Consequently F-0078 is not the theorem-level zero-set closure and does not
reduce the proof to a finite named terminal list.

## 9. Supporting modules retained from earlier routes

The following remain valid within their stated hypotheses:

- root-only normalization and exact algebraic stability identities;
- finite all-release switch-cube estimates;
- local three-cylinder contraction;
- canonical full-target repair;
- finite actual-history LP and future-signature constructions.

They may be used to construct or audit the decomposition in stage D. They may
not replace it.

## 10. Rejected closing mechanisms

The following do not create the required degree bound by themselves:

- global signed re-entry or Hall deficiency without a verified original
  negative term;
- waiting-time or Kraft coding of reversible histories;
- exact blocker-pattern regeneration;
- first-owner compression;
- stationary perfect matching;
- private-target external-coordinate concentration;
- recurrence of a live pair-fan;
- local high inverse multiplicity without future persistence.

## 11. Acceptance criterion for Q-0019

A solution must provide an explicit measurable/finite decomposition of actual
fork occurrences satisfying all of the following:

1. parent occurrence, owner, root and actual edge identities are retained;
2. no occurrence is copied or silently merged;
3. the diffuse part has a uniform \(O(b^{-2})\) inverse multiplicity;
4. every removed part is paired with an independently established exit or a
   complete proper-block subsystem;
5. every anchor part is closed under all legal relevant successors with the
   same anchor;
6. the constants are uniform over the number of blocks and the size of the
   finite history graph.

Once these conditions hold, the fork double count and F-0058 close the two
branches at the required scale.
