# Root-only canonical excess and the actual switch-cube route

## 0. Status and purpose

This file records the initial supporting statements and the fixed proof route
selected in D-0012.  The two subsequent closure theorems are now proved in
`SWITCH_CUBE_AND_ROOT_EXCESS_CLOSURE.md`:

1. F-0071 closes the finite unique-blocker all-release switch-cube module;
2. F-0072 closes the exact root-excess clean-cross reduction;
3. fresh saturated-leaf and overflow conversion remain open in Q-0018.

The global forms of Q-0016, Q-0017, Q-0018, and the one-quarter theorem remain
open.
The final target remains the legal-interval master inequality

\[
\sum_{k\in I}\mathcal B_k
\le
(1+\eta)\Delta(H)S_I
-\mathsf{Gain}_I
+\mathsf{Boundary}_I,
\qquad
S_I=\sum_{k\in I}A_{k-2},
\]

with

\[
\mathsf{Boundary}_I/(b^2S_I)\to0.
\]

The central design rule is:

> Root two-step capacity pays only root two-step failure atoms.  Descendant
> release histories are used for structure, resource growth, and core
> extraction; they do not silently refresh the root capacity ledger.

## 1. All-release core notation

Use the setup of F-0063.  Thus \(K\) is a finite strongly connected actual
one-hole core in which every attempted vertex has one blocker, both releases
are retained, and no augmentation occurs.  For a completion \(W\), let
\(e(W)\) be its unique edge.  For a real edge \(e\), put

\[
\Omega_e=\{W:e(W)=e\},
\qquad
c_e=|\Omega_e|.
\]

Fix

\[
e=\{u_1,u_2,u_3\}.
\]

Its switch slots are

\[
S(e)=\{(u,x):u\in e,\ x\in B(u)\setminus\{u\}\}.
\]

For \(W\in\Omega_e\) and \(s=(u,x)\in S(e)\), define

\[
W^s=(W\setminus\{u\})\cup\{x\},
\qquad
\pi_W(s)=e(W^s).
\]

For a real edge \(f\), write

\[
n_s(f)=|\{W\in\Omega_e:\pi_W(s)=f\}|.
\]

F-0067 records

\[
m_{ef}=\sum_{s\in S(e)}n_s(f).
\tag{1.1}
\]

## 2. Global switch-slot uniqueness

### Lemma 2.1

For fixed real edges \(e,f\), at most one switch slot \(s\in S(e)\) satisfies
\(n_s(f)>0\).

### Proof

Suppose \(s=(u,x)\) and \(\pi_W(s)=f\) for some \(W\in\Omega_e\).  The edge
\(f\) must contain \(x\).  Otherwise

\[
f\subseteq W\setminus\{u\},
\]

but \(W\setminus\{u\}\) is an independent one-hole state by the triangle
property of F-0063.

Now suppose another slot \(t=(v,y)\) also produces \(f\) in some completion.
Then the same argument shows that \(f\) contains \(y\).

If \(B(u)=B(v)\), the stretched condition forbids the edge \(f\) from
containing the two distinct vertices \(x,y\) of that block, unless the slots
are identical.

If \(B(u)\ne B(v)\), then in every \(e\)-completion the coordinate in
\(B(v)\) is the endpoint \(v\) of \(e\).  Switching only \(u\) to \(x\)
leaves that coordinate equal to \(v\), so \(W^s\) does not contain
\(y\ne v\).  Hence \(f\), which contains \(y\), cannot be a subset of
\(W^s\), a contradiction.

Thus the producing slot is unique. \(\square\)

### Consequence

Equation (1.1) sharpens to

\[
\boxed{m_{ef}=n_{s(e,f)}(f)}
\tag{2.1}
\]

whenever \(m_{ef}>0\).  In particular, the abstract Latin-column migration
from A-0041 cannot occur in a one-step actual switch map: one real output edge
cannot move between switch slots as the completion context changes.

## 3. Perfect transitions and monodromy

Call \(e\to f\) a **perfect transition at multiplicity \(C\)** when

\[
c_e=c_f=m_{ef}=C>0.
\]

By Lemma 2.1 there is one slot \(s(e,f)=(u,x)\) with

\[
n_{s(e,f)}(f)=C.
\]

Consequently every \(W\in\Omega_e\) has \(\pi_W(s(e,f))=f\), and

\[
\theta_{ef}:\Omega_e\to\Omega_f,
\qquad
\theta_{ef}(W)=W-u+x,
\tag{3.1}
\]

is a bijection.  It is injective because the inverse coordinate replacement
is determined, and the two fibers have the same size.  The relation is
symmetric: \(m_{ef}=m_{fe}\), and the reverse perfect transition uses the
inverse coordinate replacement.

### Lemma 3.1 — perfect monodromy is trivial

For a directed cycle of perfect transitions

\[
e_0\to e_1\to\cdots\to e_\ell=e_0,
\]

the composite

\[
\Theta=\theta_{e_{\ell-1}e_\ell}\circ\cdots\circ\theta_{e_0e_1}
:\Omega_{e_0}\to\Omega_{e_0}
\]

is the identity.

### Proof

Each factor overwrites one block coordinate by a fixed vertex.  Therefore the
composite, viewed on the ambient product of blocks, overwrites every touched
coordinate by its final fixed value and leaves the other coordinates
unchanged.  Applying the same composite again makes no further change, so

\[
\Theta^2=\Theta.
\]

The map \(\Theta\) is also a bijection, being a composite of bijections.  A
bijective idempotent map is the identity. \(\square\)

### Corollary 3.2 — sheet decomposition

In a connected component of the undirected perfect-transition graph whose edge
fibers all have size \(C\), transport from one base fiber is path-independent.
Indeed, two paths followed by the reverse of one another form a closed perfect
walk, whose monodromy is the identity by Lemma 3.1.  The lifted completion graph
therefore decomposes into \(C\) disjoint sheets, one for each base completion.
In particular, if the lifted graph over such a component is connected, then
\(C=1\).

This is a supporting structural reduction only.  A nonperfect boundary may be
an almost-perfect partial matching, so the corollary does not itself yield the
one-quarter loss.

## 4. Root-only canonical excess

Fix a finite legal interval \(I\) and set

\[
S_I=\sum_{k\in I}A_{k-2}>0.
\]

Use the actual two-step failure decomposition of F-0039.  In its Palm
normalization, a root failure atom has mass

\[
\frac{w_{k,R}}{S_Ib^2}
\]

and has a nonempty complete blocker family \(C(y)\).  Every edge in \(C(y)\)
contains the root second-coordinate vertex and hence meets its root future
block \(N(y)\).

Fix one global order on actual edges and select the canonical root blocker

\[
\kappa(y)=\min C(y).
\]

Define the root load

\[
L_I(e)=\mu_I\{y:\kappa(y)=e\}.
\]

Then the normalized root failure mass is exactly

\[
M_I=\sum_eL_I(e)
=
\frac{\sum_{k\in I}\mathcal B_k}{b^2S_I}.
\tag{4.1}
\]

For \(\eta\ge0\), define one root-only actual-edge capacity

\[
c_I(e)=
\frac{1+\eta}{S_Ib^3}
\sum_{\substack{k\in I,N\\e\cap N\ne\varnothing}}W_{k,N}.
\tag{4.2}
\]

Since a block has at most \(b\Delta(H)\) incident actual edges and
\(\sum_NW_{k,N}\le A_{k-2}\),

\[
\sum_ec_I(e)
\le
(1+\eta)\frac{\Delta(H)}{b^2}.
\tag{4.3}
\]

Define the canonical root excess

\[
\Xi_I=\sum_e\bigl(L_I(e)-c_I(e)\bigr)_+.
\tag{4.4}
\]

Termwise,

\[
L_I(e)\le c_I(e)+\bigl(L_I(e)-c_I(e)\bigr)_+.
\]

Summing and using (4.1)--(4.3) gives

\[
\boxed{
\frac{\sum_{k\in I}\mathcal B_k}{b^2S_I}
\le
(1+\eta)\frac{\Delta(H)}{b^2}+\Xi_I.
}
\tag{4.5}
\]

This is an exact no-copy root normalization.  It makes no assertion that a
blocker arising later in a release genealogy is entitled to capacity (4.2).
Such descendants belong to the structural/resource/core analysis below.

## 5. F-0071 — actual switch-cube defect

The candidate theorem stated in the original route is now proved in
`SWITCH_CUBE_AND_ROOT_EXCESS_CLOSURE.md` §§1–4.  For nonliteral context-slot
density \(\beta_K\),

\[
\Delta(H)\ge(1-3\beta_K)_+\frac{(b-1)^3}{b}.
\]

The proof establishes intermediate-state legality, terminal edge identity, and
the first-nonliteral preimage bound \(6(b-1)^2\).  Its weighted endpoint-loss
defect is no-copy and covariant under faithful entrance refinement.

## 6. F-0072 — root-excess clean-cross reduction

The intended reduction is now an exact chart-interface theorem.  Define the
canonical excess submeasure from F-0070 and assign it by a no-copy max-flow to
faithful F-0051 ordered clean-cross cells.  The unassigned mass is the exact
chart Hall deficiency \(\operatorname{ChartMis}_I\).  The rounded-incompatible
cell capacity is at most \(2\mathcal D_I^\sharp\), and the compatible assigned
mass splits by F-0049/F-0041 into first and return parts.  Thus

\[
\boxed{
\Xi_I\le
\operatorname{ChartMis}_I+2\mathcal D_I^\sharp+\Phi_I+\mathcal R_I.
}
\]

See `SWITCH_CUBE_AND_ROOT_EXCESS_CLOSURE.md` §§5–7.  The theorem does not make
any right-hand term small.  The remaining Q-0018 work is the actual consequence
of chart deficiency, the negative-margin integration, and the conversion of
fresh saturated leaves and overflow.

Apply the F-0041 priority split

\[
\Phi_I=
\Phi_I^{\rm edge}+\Phi_I^{\rm support}+\Phi_I^{\rm token}
+\Phi_I^{\rm repeat}.
\]

Repeat goes to F-0071; support, edge, and token retain the destinations fixed in
D-0012.

## 7. Remaining global theorem: three-cylinder regeneration

The remaining theorem must be stated on actual missing-terminal cylinders, not
as an abstract bound on the size of a token universe.

For each saturated critical leaf, the three-coordinate switch cube has one
terminal-complete branch and three first-missing-coordinate cylinders.  The
required statement is that each missing-coordinate cylinder yields at least one
of:

1. a first-certifying actual edge;
2. an actual support inconsistency or named \(S/A/N/reset\) witness;
3. sound repetition and hence an actual recurrent core;
4. a genuine clean-chart continuation child with a telescoping rank/leaf
   potential change.

The terminal-complete branch is controlled by actual degree, while the other
three cylinders regenerate the F-0038/F-0051 ledger.  Proving this statement
with the root/slot/real-edge types kept separate is the remaining new global
mathematics on the selected route.

## 8. Route summary

The selected sequence is:

\[
\boxed{
\begin{aligned}
&\text{root two-step failures}
  \xrightarrow{\text{F-0070}}
  \text{degree term}+\Xi_I,\\
&\Xi_I
  \xrightarrow{\text{F-0072}}
  \text{profile mismatch}+\Phi_I+\mathcal R_I,\\
&\mathcal R_I
  \xrightarrow{\text{F-0071}}
  \text{natural core defect},\\
&\Phi_I
  \xrightarrow{\text{F-0073}}
  \text{exit/edge/support/pure-token outcomes},\\
&\Phi_I^{\rm token}
  \xrightarrow{\text{F-0074}}
  \text{exit/edge/support/return/splice stopping outputs},\\
&\text{master inequality}
  \xrightarrow{\text{F-0042}}
  \text{IT}.
\end{aligned}
}
\]

No descendant blocker is paid from the root capacity merely because it appears
in the same release history, and no positive natural core defect is required to
acquire an independent charging entitlement.
