# Finite-resource restart and exact exhaustion of fresh compatible mass

## 0. Status and scope

This file continues the fixed Route-B master inequality after F-0073/F-0074.
It proves two supporting statements.

1. **F-0075:** in a supplied faithful release-complete actual lift, new-edge and
   new-support outputs may be restarted rather than charged.  Since the actual
   edge and support universes are finite, and every pure-token continuation has
   pointwise ratio at most
   \[
   q_b=\frac{b\Delta(H)}{(b-1)^3},
   \]
   there is no persistent edge/support/pure-token remainder when \(q_b<1\).
2. **F-0076:** after the restart exhaustion and the existing return/core
   backend, the exact zero-defect branch has zero canonical root excess.

These statements do not prove that the remaining named exits or natural
actual-support defects are terminal contradictions or recurrence gain.  The
one-quarter theorem remains open.

---

## 1. Restart lift

Work in the F-0072 faithful clean atlas and the F-0073 first-token submeasure.
Every actual genealogy \(\gamma\) retains the resource sets

\[
\mathcal E(\gamma)\subseteq E(H),
\qquad
\mathcal A(\gamma)\subseteq V(H),
\]

consisting respectively of blocker edges and carrier-support vertices already
seen on that genealogy.  These are histories, not capacities: no descendant
receives a refreshed copy of the F-0070 root edge gate.

At a clean actual-cross first-token state apply the F-0073 priority
split.  At a pure-token state apply the F-0074 three-cylinder query.  The
outputs are treated as follows.

- `exit`, `splice`, and `return` are stopping outputs;
- on `edge`, append the certified actual blocker to \(\mathcal E\) and restart
  from the selected actual output state;
- on `support`, append the newly certified carrier-support vertices to
  \(\mathcal A\) and restart from the selected actual output state;
- on a pure child, keep the resource sets and recurse.

If the selected output state no longer lies in the supplied clean atlas, or its
actual labels no longer satisfy the actual-cross interface, record the
first actual atlas-boundary certificate and stop.  Thus restarting never
silently assumes clean-chart closure.

The six F-0074 orders remain finite actual-path queries.  Exactly one selected
certificate or child genealogy is retained, so restarting is no-copy.

---

## 2. Finite resource rank

Define the remaining resource rank

\[
R(\gamma)=|E(H)\setminus\mathcal E(\gamma)|
          +|V(H)\setminus\mathcal A(\gamma)|.
\tag{2.1}
\]

Every `edge` or `support` restart decreases \(R\) by at least one.  Hence every
root-to-leaf genealogy contains at most

\[
N_H:=|E(H)|+|V(H)|
\tag{2.2}
\]

resource restarts.

This is only a fixed-instance finiteness statement.  No polynomial or uniform
bound on \(N_H\) is claimed or needed for the exact infinite-depth exhaustion.

---

## 3. Polynomial-geometric remainder

Let \(U_L\) be the mass of samples that have not reached a stopping output
after \(L\) restart/query transitions.  A surviving path of length \(L\) has
at most \(N_H\) resource transitions.  Every other transition is a pure-token
child transition, whose total conditional mass is at most \(q_b\) by F-0074.

For a fixed set of \(r\) resource positions, the total mass of all paths with
those positions is at most \(q_b^{L-r}\) times the root mass: resource
transitions have total conditional mass at most one, while pure transitions
contribute at most \(q_b\).  Summing over the possible resource positions gives

\[
\boxed{
U_L\le
\Phi_I
\sum_{r=0}^{\min\{N_H,L\}}
\binom{L}{r}q_b^{L-r}.
}
\tag{3.1}
\]

For fixed finite \(H\) and \(q_b<1\), the right-hand side tends to zero.  For
example, for \(L\ge N_H\),

\[
U_L
\le
(N_H+1)L^{N_H}q_b^{L-N_H}\Phi_I
\longrightarrow0.
\tag{3.2}
\]

The estimate is deliberately not uniform in \(H\).  It is an exact
infinite-depth theorem for every fixed finite instance.

---

## 4. F-0075 — finite-resource restart exhaustion

Let

\[
G_L^{\rm exit},\quad
G_L^{\rm atlas},\quad
G_L^{\rm return},\quad
G_L^{\rm splice}
\]

be the cumulative first-stopping masses through transition \(L\).  Resource
outputs are not stopping masses: they update the genealogy and restart.

### Theorem 4.1

For every \(L\),

\[
\Phi_I
=
G_L^{\rm exit}+G_L^{\rm atlas}
+G_L^{\rm return}+G_L^{\rm splice}+U_L.
\tag{4.1}
\]

If \(q_b<1\), then

\[
\boxed{
\Phi_I
=
G_\infty^{\rm exit}+G_\infty^{\rm atlas}
+G_\infty^{\rm return}+G_\infty^{\rm splice}.
}
\tag{4.2}
\]

In particular there is no persistent new-edge, new-support, or pure-token
remainder.

### Proof

At every query, the selected output cylinders and child cylinders are
measurable, disjoint, and exhaustive by F-0073/F-0074.  An edge/support child
strictly decreases (2.1); a pure child preserves it and has total conditional
mass at most \(q_b\).  Equation (4.1) follows by induction on \(L\), and (4.2)
follows from (3.1). \(\square\)

### Consequence for overflow

Within a supplied faithful lift, an unresolved branch cannot be justified only
by an ever-growing list of fresh edge/support/token labels.  Such a branch
would either consume infinitely many finite resources or eventually have only
pure-token transitions, both of which have zero mass by Theorem 4.1.  Any
remaining global overflow must therefore be an actual atlas/owner/reroot or
future-interface incompatibility, and must be retained in
\(G_\infty^{\rm atlas}\); it is no longer a token-universe remainder.

---

## 5. Return and finite-core backend

The `return` output retains the full sound token, both occurrences, the actual
states, blockers, supports, owners, and intervening genealogy.  It is therefore
an input to the F-0052 history-aware residual graph rather than a phase-only
cycle label.

Under the already stated F-0052/F-0057 normal-form hypotheses:

- certified \(W/M/A/N/S/\mathrm{reset}\) transitions are removed;
- the eventually-same-edge tail has zero mass;
- both unique-blocker releases are retained;
- every positive recurrent class is finite and all-release;

positive return mass enters a finite unique-blocker all-release actual core and
F-0071 gives

\[
G_\infty^{\rm return}
\le
\alpha_{b,\varepsilon}^{-1}
\operatorname{Def}_\square,
\tag{5.1}
\]

where

\[
\alpha_{b,\varepsilon}
=
\frac16\left[
1-\left(\frac14-\varepsilon\right)
\left(\frac b{b-1}\right)^3
\right]>0
\tag{5.2}
\]

for large \(b\).  If the normal-form hypotheses fail, the first actual failure
is retained as a named exit or atlas-boundary output.  This paragraph does not
construct the global normal form; it states the exact backend once supplied.

---

## 6. Defect-exhausted F-0072 inequality

Combine F-0072 with Theorem 4.1 and (5.1).  In the supplied faithful atlas and
normal-form scope,

\[
\boxed{
\begin{aligned}
\Xi_I\le{}&
\operatorname{ChartMis}_I
+2\mathcal D_I^\sharp
+G_\infty^{\rm exit}
+G_\infty^{\rm atlas}
+G_\infty^{\rm splice}\\
&+\alpha_{b,\varepsilon}^{-1}
\operatorname{Def}_\square
+\mathcal R_I^{\rm noncore}.
\end{aligned}
}
\tag{6.1}
\]

Here \(\mathcal R_I^{\rm noncore}\) denotes return/merge mass not yet covered by
the stated F-0052 normal form.  If the global residual normal form is supplied,
this term is absent.

The important change from F-0072 is that no first-edge, first-support, or pure
fresh-token term remains.  All such outputs are transient resources in the
restart execution.

---

## 7. F-0076 — exact zero-defect root closure

### Theorem 7.1

Assume the supplied faithful atlas and residual normal form, and suppose

\[
\operatorname{ChartMis}_I=0,
\qquad
\mathcal D_I^\sharp=0,
\]

\[
G_\infty^{\rm exit}=G_\infty^{\rm atlas}
=G_\infty^{\rm splice}=0,
\qquad
\operatorname{Def}_\square=0.
\tag{7.1}
\]

Then

\[
\boxed{\Xi_I=0.}
\tag{7.2}
\]

Consequently the root-only Round estimate is exact:

\[
\boxed{
\frac{\sum_{k\in I}\mathcal B_k}{b^2S_I}
\le
(1+\eta)\frac{\Delta(H)}{b^2}.
}
\tag{7.3}
\]

### Proof

F-0075 exhausts the fresh mass into the four stopping categories.  The return
category is zero by F-0071 and (7.1).  F-0072 then has no remaining right-hand
excess term, proving (7.2).  F-0070 gives (7.3). \(\square\)

Thus the exact zero-defect algebraic branch is closed.  What remains for the
one-quarter theorem is not a fresh-resource persistence problem; it is the
actual terminal/gain consequence of the finite list in (6.1), plus construction
of the faithful global atlas and residual normal form.

---

## 8. Nonclaims and remaining theorem-level obligation

F-0075/F-0076 do **not** show that

\[
\operatorname{ChartMis}_I,
\quad \mathcal D_I^\sharp,
\quad G_\infty^{\rm exit},
\quad G_\infty^{\rm atlas},
\quad G_\infty^{\rm splice},
\quad \operatorname{Def}_\square
\]

are small or contradictory in every low-degree instance.  They only reduce the
fresh/overflow side to this finite actual list and close its common zero set.
The remaining global theorem must convert each positive-density item into an
accepted structural terminal, a genuine negative term in the fixed master
inequality, or a negligible interval boundary.
