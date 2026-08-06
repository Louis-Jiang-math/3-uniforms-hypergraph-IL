# Fresh saturated leaves: exact resource split and pure-token three-cylinder stopping line

## 0. Scope lock

```text
Task:
  Advance stage C of D-0012 from the closed F-0071/F-0072 interfaces.
Mode:
  status-promotion for two supporting theorems; the one-quarter theorem and
  global Q-0017/Q-0018 remain open.
Base version:
  stage-A/B closure snapshot supplied in this task.
Target:
  The fresh compatible mass Phi_I in F-0072.
Inputs:
  F-0041, F-0048, F-0049, F-0061, F-0070, F-0071, F-0072, FW-60.
Outputs:
  (i) an exact no-copy priority split of Phi_I;
  (ii) a release-complete three-slot stopping theorem eliminating a persistent
       pure-fresh-token remainder;
  (iii) explicit remaining edge/support/global-atlas obligations.
Allowed paths:
  src/, tests/, evidence/, knowledge/, docs/, README.md,
  HANDOFF_CURRENT.md, AGENTS.md.
Forbidden paths:
  sources/raw/, history/, old/, unrelated implementation.
Expected status change:
  promote the exact fresh split and the conditional pure-token stopping theorem;
  do not close Q-0017, Q-0018, S1, or the main theorem.
Acceptance criteria:
  preserve actual owner, root projection, complete blocker family, actual edge,
  carrier support, full genealogy, and separate ledgers; no descendant receives
  F-0070 root capacity; the stopping cylinders are disjoint and the remainder
  has a pointwise geometric bound.
Required checks:
  compileall; full pytest; repository checker; generated-artifact checker;
  Q-0015 regression CLI; Q4 splice validation.
Non-goals:
  no bounded multiplicity theorem for first-certifying edges; no claim that a
  Cartesian support family is already a terminal; no global atlas construction;
  no overflow conversion; no one-quarter theorem.
```

## 1. Input measure and a correction to the previous route notation

Work in the supplied faithful clean atlas of F-0072.  Let \(\Phi_I\) be the
submeasure assigned to actual-cross ordered cross cells whose faithful
support-interface token is seen for the first time in its actual genealogy.
Every atom retains

\[
(\operatorname{owner},\operatorname{root},\sigma,x,e,p,\Gamma),
\]

where \(e\) is the selected actual blocker, \(p\) is its carrier support,
\(\sigma\) is the complete future-compatible token, and \(\Gamma\) is the
complete genealogy/ledger record.

Because \(\Phi_I\) is already the **first-token** part of F-0072, a repeated
sound token is not a fourth part of its initial priority split.  Repeated tokens
belong to \(\mathcal R_I\).  Thus the notation

\[
\Phi_I^{\rm edge}+\Phi_I^{\rm support}
+\Phi_I^{\rm token}+\Phi_I^{\rm repeat}
\]

was redundant at the entrance.  The correct split has an immediate named-exit
part and three resource parts.

## 2. F-0073 — exact fresh compatible priority split

For a \(\Phi_I\)-atom \(\omega\), let

\[
\mathcal E_{<\omega},\qquad
\mathcal A_{<\omega},\qquad
\mathcal V_{<\omega}
\]

be the actual blocker edges, accumulated carrier-support vertices, and faithful
tokens seen strictly before \(\omega\) on its genealogy.

First route every atom whose complete blocker family or chart label gives a
certified \(M/A/N/S/\mathrm{reset}\) event to \(\Phi_I^{\rm exit}\).  On the
remaining unique-blocker clean atoms use the priority order

\[
\begin{array}{lll}
\text{edge} &:& e(\omega)\notin\mathcal E_{<\omega},\\
\text{support} &:& e(\omega)\in\mathcal E_{<\omega}
  \text{ and }p(\omega)\nsubseteq\mathcal A_{<\omega},\\
\text{pure token} &:& e(\omega)\in\mathcal E_{<\omega},\quad
  p(\omega)\subseteq\mathcal A_{<\omega}.
\end{array}
\tag{2.1}
\]

The token in the last line is necessarily unvisited because \(\omega\in\Phi_I\).
Denote the corresponding submeasures by
\(\Phi_I^{\rm edge}\), \(\Phi_I^{\rm support}\), and
\(\Phi_I^{\rm token}\).

### Theorem 2.1

\[
\boxed{
\Phi_I=
\Phi_I^{\rm exit}
+\Phi_I^{\rm edge}
+\Phi_I^{\rm support}
+\Phi_I^{\rm token}.
}
\tag{2.2}
\]

The equality is an exact disjoint equality of measures and is covariant under
faithful refinement.

### Proof

The certified-exit test is evaluated first and is determined by retained actual
data.  On its complement, either the current actual edge is new or old.  If it
is old, either the carrier support adds a new vertex or it does not.  These are
mutually exclusive and exhaustive alternatives.  In the last alternative the
current token cannot have appeared before, by the definition of \(\Phi_I\).
Faithful refinement only splits an atom with all labels unchanged, so its class
in (2.1) is unchanged.  No atom is copied. \(\square\)

This is the measure-level form of F-0041 appropriate after the F-0049
first/return partition.  Sound repetition is not lost: it remains in
\(\mathcal R_I\), and it can also occur later as a stopping output of the
pure-token postprocessing below.

## 3. Pure-token actual execution kernel

Take an atom in \(\Phi_I^{\rm token}\).  Its current full completion \(W\) has
a unique actual blocker

\[
e(W)=\{u_1,u_2,u_3\}.
\]

If this fails, the atom was already in \(\Phi_I^{\rm exit}\).  Extend the atom
by three independent uniform coordinates

\[
x_i\in B(u_i)\setminus\{u_i\},\qquad i=1,2,3.
\tag{3.1}
\]

For an order \((i,j,k)\in S_3\), start from \(W\setminus\{u_i\}\), insert
\(x_i\), and inspect the **complete** blocker family.

At every intermediate attempt use the following stopping priority.

1. If the attempt gives augmentation/survivor, a multi-blocker family, or a
   certified \(A/N/S/\mathrm{reset}\) event, stop in `exit`.
2. If its actual blocker edge is first-certifying on the genealogy, stop in
   `edge`.
3. If its carrier support adds a new support vertex, stop in `support`.
4. If its faithful token has appeared before, stop in `return`.
5. Otherwise the successor is again a pure fresh-token state.

When the blocker is unique, F-0061 makes both old-endpoint releases legal.  The
chosen order may continue precisely when the next requested old endpoint lies
in the current unique blocker.  If it does not, record the current blocker and
the requested but absent endpoint.

The first two switches of an order are called a **pure prefix** when they stay
in case 5.  A terminal coordinate \(k\) is **purely reachable** when one of the
two orders ending in \(k\) has a pure prefix and reaches the final completion.

## 4. Terminal identity and canonical stopping categories

### Lemma 4.1 — terminal identity

If all three terminal coordinates are purely reachable and the final completion
has a unique blocker, then that blocker is

\[
\boxed{\{x_1,x_2,x_3\}.}
\tag{4.1}
\]

### Proof

For each \(k\), choose a pure-prefix order ending in \(k\).  Its final attempt
adds \(x_k\) to an independent one-hole state, so the final unique blocker
contains \(x_k\).  All orders reach the same actual completion.  The blocker is
a three-edge containing all three \(x_i\), hence equals (4.1). \(\square\)

For each target triple, inspect the six orders in one fixed global order.  An
inspected order is a finite **actual legal path query**: every intermediate
completion, complete blocker family, requested release, and faithful token is
retained.  If the first retained output is `exit`, `edge`, `support`, or
`return`, the postprocessor selects that least order and outputs its finite
actual path as the certificate.  Thus the certificate is not an abstract
counterfactual label; it is one deterministically selected legal path in the
release-complete lift.

If no inspected order has a resource/named-exit output, assign the target triple
as follows:

- `splice defect`, if some terminal is not purely reachable; choose the least
  such terminal and record both orders ending there together with their first
  missing-endpoint blockers;
- `child`, if all terminals are purely reachable, the final blocker is unique,
  and the final state is again pure fresh token along at least one pure order.
  Choose the least such pure order as the **canonical child genealogy**;
- otherwise assign the final state to its own first category among `exit`,
  `edge`, `support`, and `return` along the least pure order reaching it.

Exactly one selected path or one splice record is retained.  The other order
queries are discarded after classification, so neither mass nor a resource
ledger is copied.  In particular, freshness/return for a child is evaluated
relative to its canonical child genealogy, not relative to a quotient current
state.

The splice-defect record contains only actual data:

\[
(W,e(W),x_1,x_2,x_3,k,
  \text{the two terminal-}k\text{ orders},
  \text{first-failure blockers and missing endpoints}).
\tag{4.2}
\]

It is therefore a specified actual-support defect in the sense of FW-60, not
“whatever remains”.

## 5. Pointwise continuation bound

Let \(\mathcal C(W)\) be the target triples assigned to `child`.  By Lemma 4.1,
for every \(\mathbf x\in\mathcal C(W)\),

\[
\{x_1,x_2,x_3\}\in E(H).
\]

Different triples give different actual edges between the three endpoint
blocks.  Hence, pointwise for every root completion,

\[
|\mathcal C(W)|
\le |E_H(B(u_1),B(u_2),B(u_3))|
\le b\Delta(H).
\tag{5.1}
\]

Since the target box has size \((b-1)^3\), the pure-token continuation ratio is
at most

\[
\boxed{
q_b=\frac{b\Delta(H)}{(b-1)^3}.
}
\tag{5.2}
\]

This bound is pointwise and needs no stationary distribution, uniform context
multiplicity, or token-universe estimate.

## 6. F-0074 — pure-token three-cylinder stopping theorem

Apply the construction recursively only to `child` cylinders.  Genealogy
identity is retained even when two children have the same current state.  Let
\(R_L\) be the total pure-token mass surviving after \(L\) generations, and let

\[
G_L^{\rm exit},\ G_L^{\rm edge},\ G_L^{\rm support},\
G_L^{\rm return},\ G_L^{\rm splice}
\]

be the cumulative first-stopping masses through generation \(L\).

### Theorem 6.1

For every \(L\ge0\),

\[
\Phi_I^{\rm token}
=
G_L^{\rm exit}+G_L^{\rm edge}+G_L^{\rm support}
+G_L^{\rm return}+G_L^{\rm splice}+R_L,
\tag{6.1}
\]

and

\[
\boxed{R_L\le q_b^L\Phi_I^{\rm token}.}
\tag{6.2}
\]

If \(q_b<1\), then the stopping cylinders exhaust the pure-token mass:

\[
\boxed{
\Phi_I^{\rm token}
=
G_\infty^{\rm exit}+G_\infty^{\rm edge}
+G_\infty^{\rm support}+G_\infty^{\rm return}
+G_\infty^{\rm splice}.
}
\tag{6.3}
\]

### Proof

At one generation, the fixed target box and deterministic priority rule form a
finite measurable partition.  Parent cylinders are split by independent target
coordinates, so children and first-stopping cylinders are pairwise disjoint and
have total parent mass.  The `child` part of each parent is at most \(q_b\) times
its mass by (5.1).  Induction gives (6.1) and (6.2).  If \(q_b<1\), then
\(R_L\to0\), and monotone convergence of the cumulative stopping masses gives
(6.3). \(\square\)

Under

\[
\Delta(H)\le(1/4-\varepsilon)b^2,
\]

\[
q_b\le(1/4-\varepsilon)\left(\frac b{b-1}\right)^3<1
\]

for all sufficiently large \(b\); indeed one may take
\(q_b\le1/4-\varepsilon/2\).

### Refinement covariance

Faithful refinement keeps all data in (4.2) unchanged and only splits its
mass.  Terminal reachability, first stopping category, child identity, and
stopping generation pull back exactly.  Thus the five stopping measures and
\(R_L\) are covariant and no-copy.

### Independent defect consequence

If all four non-defect outputs in (6.3) have zero mass, then

\[
G_\infty^{\rm splice}=\Phi_I^{\rm token}.
\]

If in addition the splice defect is zero, then
\(\Phi_I^{\rm token}=0\).  More quantitatively, (6.2) is a separate geometric
dissipation theorem for the specified defect stopping line.  This supplies the
zero-set/dissipation requirement of FW-60 without assigning root edge capacity
to any descendant.

## 7. Consequence for the F-0072 right-hand side

Combining F-0073 and F-0074, for \(q_b<1\) the fresh term has the exact
postprocessed decomposition

\[
\boxed{
\begin{aligned}
\Phi_I={}&\Phi_I^{\rm exit}+\Phi_I^{\rm edge}
+\Phi_I^{\rm support}\\
&+G_\infty^{\rm exit}+G_\infty^{\rm edge}
+G_\infty^{\rm support}+G_\infty^{\rm return}
+G_\infty^{\rm splice}.
\end{aligned}
}
\tag{7.1}
\]

There is no persistent pure-token or token-universe remainder.  All output
cylinders retain actual owner, support, blocker, and genealogy labels.

This does **not** assert that edge/support/exit outputs are already paid in the
master recurrence.  It removes only the pure-token obstruction and sends
return mass to the existing \(\mathcal R_I\)/core backend.

## 8. Exact remaining stage-C obligations

After F-0073/F-0074, stage C no longer contains a pure-token theorem.  The
remaining global work is:

1. **edge output:** prove owner-preserving bounded multiplicity or another
   accepted actual consequence for
   \(\Phi_I^{\rm edge}+G_\infty^{\rm edge}\);
2. **support output:** prove that
   \(\Phi_I^{\rm support}+G_\infty^{\rm support}\) yields an actual specified
   \(S\)-correlation or hereditary coordinate expansion with a terminal
   consequence;
3. **return output:** deliver \(G_\infty^{\rm return}\) and the pre-existing
   \(\mathcal R_I\) to a faithful recurrent core and then F-0071, or another
   accepted terminal;
4. **named exits and atlas deficiency:** give actual consequences for
   \(\Phi_I^{\rm exit}+G_\infty^{\rm exit}\) and
   \(\operatorname{ChartMis}_I\);
5. **profile margin and overflow:** retain the negative F-0038/F-0051 margin and
   convert unbounded interfaces.

The fixed interval master inequality and F-0042 remain the final target.
