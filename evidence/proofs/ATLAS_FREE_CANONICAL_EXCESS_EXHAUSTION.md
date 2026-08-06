# Atlas-free physical exhaustion of the canonical root excess

## 0. Status and purpose

F-0070 already realizes the canonical excess as an actual no-copy submeasure
\(\nu_I\) of the two-step root-failure Palm space.  Each atom retains an
actual full completion, its complete blocker family, its immutable owner and
its pre-root genealogy.  This file observes that the F-0073--F-0075 physical
postprocessing can be run directly on \(\nu_I\); a product chart is not needed
for the exact structural exhaustion.

The result does not prove a terminal or recurrence consequence for the final
stopping categories.  It removes the global clean-atlas construction from the
**common-zero-set** closure of the root excess.

---

## 1. Canonical excess atoms are physical completion atoms

Let \(y=(k,R,r,x)\) be an F-0070 root atom.  Then

\[
W(y)=R\cup\{r,x\}
\]

is a full transversal of the first \(k\) actual blocks, and it is not
independent.  Its complete blocker family is

\[
\mathcal K(W)=\{e\in E(H):e\subseteq W\}.
\]

The canonical excess density \(\alpha_{\kappa(y)}\) only scales the mass of the
same actual atom; it does not alter \(W\), \(\mathcal K(W)\), owner, support or
genealogy.  Thus \(\nu_I\) is a legitimate starting measure for physical
postprocessing.

At a root or later completion:

1. if the blocker family has size at least two, output the complete actual
   multi-blocker/deadlock record `M`;
2. if the blocker is unique, enter the release-complete unique-blocker kernel;
3. if an attempted completion is independent, output augmentation `W`.

No chart, pivot inheritance or profile threshold is used.

---

## 2. Explicit finite physical token

For the unique-blocker kernel retain separately the complete unfolded
genealogy, but define the transition token

\[
\sigma=(\operatorname{owner},W,e,\mathcal E,\mathcal A),
\tag{2.1}
\]

where

- \(W\) is the current actual completion;
- \(e\) is its unique blocker;
- \(\mathcal E\subseteq E(H)\) is the set of actual blocker edges already seen
  on this genealogy;
- \(\mathcal A\subseteq V(H)\) is the set of actual vertices appearing in the
  retained carrier supports.

The fixed order on the six three-cylinder queries and all finite tie-breaking
rules are part of the kernel definition.  Therefore (2.1) determines the
complete next-query law, all actual stopping certificates, the selected child
state, and the resource increments.  It is a transition congruence for this
physical postprocessor.  For fixed finite \(H\) and finite interval \(I\), the
token universe is finite.

Genealogy is not discarded: two nodes with the same token remain distinct in
the unfolded tree.  Equality of tokens is used only to certify a sound return.

---

## 3. Direct priority split on \(\nu_I\)

For a unique-blocker excess atom apply the F-0073 priority split using its
actual pre-root history:

- a new actual blocker edge;
- an old edge with new support vertices;
- a first occurrence of the physical token (2.1);
- a repeated token, recorded as sound return.

For first-token atoms apply the F-0074 release-complete three-cylinder query.
The proof of its pointwise continuation bound uses only the actual completion,
unique blocker and complete release paths.  Hence

\[
q_b=\frac{b\Delta(H)}{(b-1)^3}
\tag{3.1}
\]

is valid without a clean chart.

On edge/support outputs, update \(\mathcal E\) or \(\mathcal A\) and restart
from the selected actual completion.  On a pure child, recurse.  Stop on
augmentation, multi-blocker/deadlock, sound return, or the specified
three-cylinder splice record.

Every query uses independent finite coordinates and retains exactly one first
certificate or one canonical child genealogy.  Thus this is a measurable
no-copy stopping forest over \(\nu_I\).

---

## 4. Finite-resource remainder

Let

\[
N_H=|E(H)|+|V(H)|.
\]

Every edge/support restart adds an element to \(\mathcal E\) or \(\mathcal A\),
so a genealogy has at most \(N_H\) such restarts.  All other unresolved
transitions are pure children and contribute conditional mass at most \(q_b\).
If \(U_L^\Xi\) is unresolved excess mass after \(L\) transitions, the F-0075
argument gives

\[
\boxed{
U_L^\Xi\le
\Xi_I\sum_{r=0}^{\min\{N_H,L\}}\binom Lr q_b^{L-r}.
}
\tag{4.1}
\]

For fixed finite \(H\) and \(q_b<1\), this tends to zero.

---

## 5. F-0078 — atlas-free canonical-excess exhaustion

Let

\[
G_L^W,\quad G_L^M,\quad G_L^{\rm return},\quad G_L^{\rm splice}
\]

be the cumulative first-stopping masses through depth \(L\), where \(W\)
includes augmentation and \(M\) retains the complete multi-blocker/deadlock
record.

### Theorem 5.1

For every \(L\),

\[
\Xi_I=
G_L^W+G_L^M+G_L^{\rm return}+G_L^{\rm splice}+U_L^\Xi.
\tag{5.1}
\]

If \(q_b<1\), then

\[
\boxed{
\Xi_I=
G_\infty^W+G_\infty^M
+G_\infty^{\rm return}+G_\infty^{\rm splice}.
}
\tag{5.2}
\]

In particular there is no chart-mismatch, profile-rounding, first-edge,
first-support or pure-token remainder in the physical exhaustion of the
canonical excess.

### Proof

The root multi/unique split and every later F-0073/F-0074 split are measurable,
disjoint and exhaustive.  Resource restarts strictly decrease the finite rank
\(N_H-|\mathcal E|-|\mathcal A|\), while every remaining child has total
conditional mass at most \(q_b\).  Induction gives (5.1), and (4.1) gives
(5.2). \(\square\)

---

## 6. Return backend and improved zero-set closure

A return output retains both occurrences of the exact token (2.1), the actual
states, blockers, resource sets, owners and intervening genealogy.  Under the
F-0052 residual normal-form hypotheses it enters a finite actual recurrent
class.  If that class is unique-blocker and all-release, F-0071 gives

\[
G_\infty^{\rm return}
\le
\alpha_{b,\varepsilon}^{-1}\operatorname{Def}_\square.
\tag{6.1}
\]

If the normal form fails, retain the first actual multi-blocker or release
incompatibility in \(G_\infty^M\); do not erase it.

Consequently, in a no-IT instance, if

\[
G_\infty^M=G_\infty^{\rm splice}
=\operatorname{Def}_\square=0,
\]

and the stated residual normal form holds, then

\[
\boxed{\Xi_I=0}
\]

without any global clean atlas or profile-deficit assumption.  F-0070 then
gives the exact root Round estimate.

---

## 7. What remains

F-0078 is an exact structural exhaustion, not the final stability theorem.  It
leaves only the actual consequences of:

1. positive multi-blocker/deadlock mass;
2. positive three-cylinder splice mass;
3. positive return/core switch-square defect;
4. failure of the residual normal form.

The main theorem still requires these positive-density outputs to yield an
accepted structural contradiction, a genuine negative term in the fixed
interval master inequality, or a negligible legal boundary.
