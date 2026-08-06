# Closure of the finite switch-cube module and the root-excess reduction

## 0. Status and scope

This file closes the first two implementation stages selected in D-0012, with
precise scope labels.

1. **F-0071 is unconditional inside a finite unique-blocker all-release actual
   core.**  It gives a weighted natural actual-support defect and closes the
   finite normal-form core obligation of Q-0016.
2. **F-0072 is an exact no-copy reduction for any supplied faithful clean-cross
   atlas.**  It converts the canonical root excess of F-0070 into chart
   deficiency, F-0038 mismatch, fresh saturated leaves, and return/core mass.
   It does not claim that the chart deficiency or fresh leaves are already
   small.

The one-quarter theorem, Q-0017, and Q-0018 remain open.  No release descendant
receives a refreshed copy of the F-0070 root capacity.

---

## 1. Finite all-release core and literal switches

Let \(K\) be a finite strongly connected class of independent one-hole actual
transversals satisfying the hypotheses of F-0063:

- every attempted vertex has one blocker;
- both old-endpoint releases are retained;
- every release successor remains in \(K\);
- no augmentation occurs in \(K\).

Put

\[
\Omega_K=\{T\cup\{x\}:T\in K,\ x\in B(T)\}.
\]

Every \(W\in\Omega_K\) has one actual edge \(e(W)\).  If

\[
e(W)=\{u_1,u_2,u_3\},
\]

then, for \(u\in e(W)\) and \(x\in B(u)\setminus\{u\}\), define

\[
W^{u\to x}=(W\setminus\{u\})\cup\{x\},
\qquad
\pi_W(u,x)=e(W^{u\to x}).
\]

The switch is **literal** when

\[
\pi_W(u,x)=\bigl(e(W)\setminus\{u\}\bigr)\cup\{x\}.
\tag{1.1}
\]

Define the nonliteral density

\[
\beta_K=
\frac{
 |\{(W,u,x):(u,x)\text{ is nonliteral in }W\}|
}{3(b-1)|\Omega_K|}.
\tag{1.2}
\]

For a context-slot \((W,u,x)\), define the endpoint loss

\[
\ell(W,u,x)=
\left|
(e(W)\setminus\{u\})\setminus\pi_W(u,x)
\right|.
\]

A switch is literal exactly when \(\ell=0\).  Because the output edge contains
the inserted vertex \(x\), a nonliteral switch has \(\ell\in\{1,2\}\).  Set

\[
\delta_\square(K)=
\frac{1}{6(b-1)|\Omega_K|}
\sum_{W,u,x}\ell(W,u,x).
\tag{1.3}
\]

Then

\[
\boxed{\frac{\beta_K}{2}\le\delta_\square(K)\le\beta_K.}
\tag{1.4}
\]

---

## 2. Literal-prefix legality and terminal identity

### Lemma 2.1

Fix \(W\in\Omega_K\), write \(e(W)=\{u_1,u_2,u_3\}\), choose
\(x_i\in B(u_i)\setminus\{u_i\}\), and choose an order
\(\sigma\in S_3\).  If every switch in the ordered three-step instruction is
literal, then every intermediate deletion is an actual state of \(K\), and the
final completion has unique blocker

\[
\{x_1,x_2,x_3\}.
\tag{2.1}
\]

### Proof

After a literal switch \(u_i\to x_i\), the new unique blocker is obtained from
the current blocker by replacing \(u_i\) with \(x_i\).  Hence it retains the
two endpoints that have not yet been switched.  Deleting either retained
endpoint destroys the unique blocker, so by the triangle property in F-0063 it
is a legal one-hole state in \(K\).  Induction over the three positions gives
successive blockers

\[
\{x_{\sigma(1)},u_{\sigma(2)},u_{\sigma(3)}\},
\]

\[
\{x_{\sigma(1)},x_{\sigma(2)},u_{\sigma(3)}\},
\]

and finally \(\{x_1,x_2,x_3\}\). \(\square\)

Thus every all-literal instruction certifies an actual edge between the three
endpoint blocks of \(e(W)\).

---

## 3. First-nonliteral stopping map

An ordered three-switch instruction consists of

- a root \(W\in\Omega_K\);
- an order \(\sigma\in S_3\);
- targets \(x_i\in B(u_i)\setminus\{u_i\}\).

There are \(6(b-1)^3\) instructions per root.  If an instruction is not
all-literal, assign it to its first nonliteral **current context-slot**
\((V,u,x)\).

### Lemma 3.1 — bounded first-defect multiplicity

A fixed nonliteral current context-slot is the first nonliteral step of at most

\[
\boxed{6(b-1)^2}
\tag{3.1}
\]

ordered instructions, counted over all roots.

### Proof

Fix the current completion \(V\), the current endpoint \(u\in e(V)\), and the
target \(x\in B(u)\setminus\{u\}\).

- **Position 1.**  The root is \(V\).  The two remaining targets are arbitrary,
  and their order has two choices.  This gives at most
  \(2(b-1)^2\) instructions.
- **Position 2.**  One of the two other current edge endpoints is the vertex
  inserted at the first literal step.  Choose which one in two ways, recover
  its root endpoint in at most \(b-1\) ways, and choose the final target in at
  most \(b-1\) ways.  This gives at most \(2(b-1)^2\).
- **Position 3.**  The two other current edge endpoints were inserted in the
  first two literal steps.  Choose their order in two ways and recover their
  two root endpoints in at most \((b-1)^2\) ways.  This gives at most
  \(2(b-1)^2\).

Summing the three positions proves (3.1).  The bound is sharp in the ambient
three-coordinate overwrite cube; `tests/test_route_b_closure.py` exhaustively
checks it for \(b=2,3,4\). \(\square\)

The stopping map is defined from actual intermediate completions, so it is
measurable on the finite core and is preserved by faithful splitting of an
entrance cylinder.

---

## 4. F-0071 — actual switch-cube defect theorem

### Theorem 4.1

For every finite core \(K\) above,

\[
\boxed{
\Delta(H)\ge
(1-3\beta_K)_+\frac{(b-1)^3}{b}.
}
\tag{4.1}
\]

### Proof

The total number of ordered instructions is

\[
6|\Omega_K|(b-1)^3.
\]

There are \(3(b-1)|\Omega_K|\beta_K\) nonliteral context-slots.  By Lemma 3.1,
the number of bad instructions is at most

\[
3(b-1)|\Omega_K|\beta_K\cdot6(b-1)^2
=18|\Omega_K|\beta_K(b-1)^3.
\]

Hence the total number of all-literal instructions is at least

\[
6|\Omega_K|(1-3\beta_K)(b-1)^3.
\]

If the right-hand side is positive, some root \(W\) supports at least

\[
6(1-3\beta_K)(b-1)^3
\]

all-literal instructions.  By Lemma 2.1, each ends at the actual edge
\(\{x_1,x_2,x_3\}\).  A fixed target triple is produced by at most the six
orders, so the three endpoint blocks of \(e(W)\) contain at least

\[
E=(1-3\beta_K)(b-1)^3
\]

distinct actual edges.  These edges have \(3E\) incidences among \(3b\)
vertices, so one vertex has degree at least \(E/b\).  This is (4.1).  If
\(1-3\beta_K\le0\), the positive-part statement is immediate. \(\square\)

### Corollary 4.2 — low degree forces a positive natural defect

If

\[
\Delta(H)\le\left(\frac14-\varepsilon\right)b^2,
\]

then

\[
\beta_K\ge
\frac13\left[
1-\left(\frac14-\varepsilon\right)
\left(\frac b{b-1}\right)^3
\right]
\tag{4.2}
\]

and

\[
\boxed{
\delta_\square(K)\ge
\frac16\left[
1-\left(\frac14-\varepsilon\right)
\left(\frac b{b-1}\right)^3
\right]
=\frac18+\frac\varepsilon6-O_\varepsilon(b^{-1}).
}
\tag{4.3}
\]

### Weighted entrance-cylinder form

Suppose disjoint no-copy entrance cylinders enter finite cores \(K\) with
masses \(\mu_K\).  Append an independent uniform completion of \(K\), a
uniform endpoint, and a uniform replacement in its endpoint block.  The event
that the resulting actual switch is nonliteral has mass

\[
\operatorname{Def}_{\rm nl}=\sum_K\mu_K\beta_K,
\]

and the endpoint-loss observable has mass

\[
\operatorname{Def}_\square=\sum_K\mu_K\delta_\square(K).
\]

This postprocessing splits entrance mass but never copies it.  Refining an
entrance cylinder only splits the corresponding coefficient \(\mu_K\), so both
defects are covariant under faithful refinement and genealogy expansion.
Under the degree hypothesis,

\[
\boxed{
\operatorname{Def}_\square
\ge
\frac16\left[
1-\left(\frac14-\varepsilon\right)
\left(\frac b{b-1}\right)^3
\right]M_{\rm core},
}
\tag{4.4}
\]

where \(M_{\rm core}=\sum_K\mu_K\).

Thus zero switch-square defect excludes positive finite-core mass, and near-zero
defect controls that mass linearly.  This is the natural actual-support defect
outcome accepted by FW-60/Q-0016 for finite unique-blocker all-release cores.

---

## 5. Canonical root-excess submeasure

Fix a finite legal interval \(I\), put

\[
S_I=\sum_{k\in I}A_{k-2}>0,
\]

and use the F-0039 Palm root-failure measure \(\mu_I\).  Select one canonical
root blocker \(\kappa(y)\) from the complete blocker family of each root atom.
Let

\[
Y_e=\{y:\kappa(y)=e\},
\qquad
L_I(e)=\mu_I(Y_e),
\]

and use the F-0070 root-only capacity \(c_I(e)\).  Define

\[
\alpha_e=
\begin{cases}
\dfrac{(L_I(e)-c_I(e))_+}{L_I(e)},&L_I(e)>0,\\[6pt]
0,&L_I(e)=0.
\end{cases}
\]

The measure

\[
\nu_I(A)=\sum_e\alpha_e\mu_I(A\cap Y_e)
\tag{5.1}
\]

is a canonical no-copy submeasure of the root failure measure, and

\[
\nu_I(\Omega)=\Xi_I.
\tag{5.2}
\]

This density form avoids any unnecessary atomless subset choice and is
covariant under faithful refinement of root cylinders.

---

## 6. Faithful clean-cross assignment

Let a finite faithful clean-chart atlas be supplied in the scope of F-0051.  A
chart node \(u\) has

- multiplicity scale \(m(u)\);
- \(n(u)\ge2\) ordered directions;
- continuation profile \(a(u)=(a_1,\ldots,a_n)\);
- actual owner, root projection, support, blocker, and genealogy labels.

Its ordered cross cell \((u,i,j)\), \(i\ne j\), has capacity

\[
q(u,i,j)=
\frac{m(u)}{n(u)(n(u)-1)}a_i(u)(1-a_j(u)).
\tag{6.1}
\]

A root-excess atom may be assigned to a cell only when its actual owner, root
projection, support interface, canonical blocker, and ordered continuation/stop
directions agree with that cell.  Run the finite bipartite max-flow from the
excess submeasure \(\nu_I\) to these cells with capacities (6.1).  The flow is
realized on a no-copy refinement exactly as in F-0055/F-0043.

Define

\[
\operatorname{ChartMis}_I
=
\Xi_I-F_I^{\rm chart},
\tag{6.2}
\]

where \(F_I^{\rm chart}\) is the maximum faithfully assigned chart mass.  This
is an exact chart-interface Hall deficiency.  It is not declared small or
called a terminal by definition.

For each chart, round

\[
\beta_i=\mathbf 1_{\{a_i\ge1/2\}}.
\]

A cell is **critical-compatible** when \((\beta_i,\beta_j)=(1,0)\).

### Lemma 6.1 — incompatible cross capacity

For every chart node \(u\), the total capacity of incompatible cells is at most

\[
2m(u)(n(u)-1)D_{n(u)}(a(u)).
\tag{6.3}
\]

### Proof

An incompatible ordered pair has either \(\beta_i=0\) or \(\beta_j=1\).  Hence
its normalized mass is bounded by the union estimate

\[
\frac1n\sum_i|a_i-\beta_i|.
\]

Since

\[
|a_i-\beta_i|=\min(a_i,1-a_i)\le2a_i(1-a_i)
\]

and F-0038 gives

\[
\sum_i a_i(1-a_i)\le n(n-1)D_n(a),
\]

multiplication by \(m(u)\) gives (6.3). \(\square\)

Define

\[
\mathcal D_I^\sharp
=
\sum_um(u)(n(u)-1)D_{n(u)}(a(u)).
\tag{6.4}
\]

Therefore the mass assigned to incompatible cells is at most
\(2\mathcal D_I^\sharp\).

---

## 7. F-0072 — exact root-excess clean-cross reduction

On the mass assigned to critical-compatible cells, retain the actual
support-interface token \((\sigma,x,e)\) and full genealogy.  Use the F-0049 /
F-0041 first-occurrence partition:

- \(\Phi_I\): first occurrence of the compatible token;
- \(\mathcal R_I\): return, merge, repeated token, cycle, or recurrent-core
  occurrence.

The two sets are measurable, disjoint, and exhaustive on the compatible
assigned mass.

### Theorem 7.1

For every finite legal interval and every supplied faithful clean-chart atlas,

\[
\boxed{
\Xi_I
\le
\operatorname{ChartMis}_I
+2\mathcal D_I^\sharp
+\Phi_I+\mathcal R_I.
}
\tag{7.1}
\]

Consequently,

\[
\boxed{
\frac{\sum_{k\in I}\mathcal B_k}{b^2S_I}
\le
(1+\eta)\frac{\Delta(H)}{b^2}
+
\operatorname{ChartMis}_I
+2\mathcal D_I^\sharp
+\Phi_I+\mathcal R_I.
}
\tag{7.2}
\]

### Proof

The excess submeasure has mass \(\Xi_I\).  Its unassigned mass is exactly
\(\operatorname{ChartMis}_I\).  Assigned incompatible mass is at most the sum
of incompatible cell capacities, which is at most
\(2\mathcal D_I^\sharp\) by Lemma 6.1.  Assigned compatible mass is exactly the
disjoint sum \(\Phi_I+\mathcal R_I\).  This proves (7.1).  Combining with
F-0070 gives (7.2). \(\square\)

### Covariance and no-copy statement

- Root refinement pulls back \(\nu_I\) and splits its mass without changing
  (5.2).
- Chart refinement splits cells and their capacities; a feasible assignment
  splits with them, so no sample is copied.
- The candidate relation preserves actual owner, root, support, blocker, and
  ordered directions.
- The fresh/return partition is evaluated after assignment on the original
  faithful genealogy, not on a phase-only quotient.

Thus (7.1) is an exact typed interface, not a relabeling of the unresolved
mass.

---

## 8. What is now closed and what remains

### Closed

1. The finite unique-blocker all-release core has a constant-density natural
   actual-support defect below the one-quarter degree threshold (F-0071).
2. The root-only canonical excess has the exact no-copy clean-cross reduction
   (F-0072), once a faithful F-0051 atlas is supplied.

### Still open

1. Constructing the global faithful atlas from every target instance and
   proving that \(\operatorname{ChartMis}_I\) has an accepted actual
   consequence.
2. Paying \(\mathcal D_I^\sharp\) with the full negative F-0038/F-0051 ledger,
   rather than treating it as a positive error.
3. F-0073/F-0074 now give the exact entrance split and eliminate the persistent
   pure-token remainder.  The remaining fresh-forest work is the actual
   consequence of first-certifying edge/support outputs and return/core delivery.
4. Converting overflow outside finite complete interfaces into the F-0074 output
   taxonomy or an actual core.

The final target remains the fixed interval master inequality.  F-0071 and
F-0072 remove the finite-core candidate theorem and the algebraic root-excess
reduction from the list of open stages.  F-0073/F-0074, proved separately in
`FRESH_LEAF_THREE_CYLINDER_CLOSURE.md`, remove the persistent pure-token branch;
the remaining global fresh-forest work is edge/support/return consequence and
overflow conversion.
