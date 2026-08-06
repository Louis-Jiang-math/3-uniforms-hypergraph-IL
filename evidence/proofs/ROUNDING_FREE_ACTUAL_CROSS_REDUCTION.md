# Rounding-free actual-cross reduction

## 0. Purpose

F-0072 used the deterministic threshold

\[
\beta_i=\mathbf 1_{\{a_i\ge1/2\}}
\]

and paid the assigned cells not satisfying \((\beta_i,\beta_j)=(1,0)\) by
\(2\mathcal D_I^\sharp\).  That rounding is not needed for the genealogy
argument and its loss cannot be absorbed by a dimension-free multiple of the
F-0038 deficit.  This file removes it.

The root-only capacity and canonical excess of F-0070 are unchanged.

---

## 1. Why deterministic rounding cannot be the final interface

Take a chart with

\[
a_1=\cdots=a_n=\frac12.
\]

Then

\[
F_n(a)=\frac14,
\qquad
D_n(a)=\frac{n}{4(n-1)}-\frac14=\frac1{4(n-1)}.
\]

Under the convention \(\beta_i=1\) at equality, no ordered cell is
threshold-compatible, so its incompatible cross mass is \(1/4\).  Hence

\[
\frac{\Lambda_{\rm incompatible}}{D_n(a)}=n-1.
\]

Thus no dimension-free estimate
\(\Lambda_{\rm incompatible}\le C D_n(a)\) is possible.  This is an artifact
of deterministic profile rounding, not an actual execution obstruction.

---

## 2. Every chart cell is already an actual binary cross

Keep the F-0072 faithful clean atlas and exact no-copy max-flow.  A chart node
\(u\) has ordered cell capacities

\[
q(u,i,j)=\frac{m(u)}{n(u)(n(u)-1)}a_i(u)(1-a_j(u)).
\]

The candidate relation only allows an excess atom into \((u,i,j)\) when the
retained actual data certify:

- direction \(i\) is the actual continuation side;
- direction \(j\) is the actual first-stop/failure side;
- owner, root projection, actual blocker, support interface and genealogy
  agree.

Consequently an assigned atom is already a binary continuation--stop cross at
the atom level.  No profile-level threshold bit is required.

Let \(F_I^{\rm chart}\) be the maximum assigned mass and retain

\[
\operatorname{ChartMis}_I=\Xi_I-F_I^{\rm chart}.
\]

On **all** assigned cross atoms retain the complete faithful token
\((\sigma,x,e)\) and the full genealogy.  F-0049 gives the exact first/return
partition:

- \(\Phi_I^\times\): first occurrence of the token;
- \(\mathcal R_I^\times\): return, merge, repeated token, cycle or recurrent
  occurrence.

These sets are measurable, disjoint and exhaustive on the assigned mass.
Therefore

\[
\boxed{
\Xi_I=
\operatorname{ChartMis}_I+\Phi_I^\times+\mathcal R_I^\times.
}
\tag{2.1}
\]

This is an equality, not merely an upper bound.

---

## 3. F-0077 — rounding-free root-excess reduction

Combining (2.1) with F-0070 gives

\[
\boxed{
\frac{\sum_{k\in I}\mathcal B_k}{b^2S_I}
\le
(1+\eta)\frac{\Delta(H)}{b^2}
+\operatorname{ChartMis}_I
+\Phi_I^\times+\mathcal R_I^\times.
}
\tag{3.1}
\]

No positive F-0038 mismatch term occurs.

### No-copy and covariance

The max-flow assignment is the same faithful cell refinement as in F-0072.
The first/return decision is evaluated on the retained actual genealogy.
Refining a root or chart cylinder only splits its assigned mass and does not
change its continuation/stop directions or token history.  Hence all three
terms in (2.1) are covariant and no-copy.

---

## 4. Compatibility with F-0073--F-0075

The proofs of F-0073, F-0074 and F-0075 use only:

1. a first-token actual atom;
2. the complete blocker family;
3. actual edge and carrier-support history;
4. the faithful token and genealogy;
5. release-complete actual path queries.

They never use the threshold bits \(\beta_i\).  Therefore their statements
hold verbatim with \(\Phi_I^\times\) in place of the old
rounded-compatible \(\Phi_I\).

Within the supplied faithful lift, F-0075 yields

\[
\Phi_I^\times
=
G_\infty^{\rm exit}
+G_\infty^{\rm atlas}
+G_\infty^{\rm return}
+G_\infty^{\rm splice}.
\tag{4.1}
\]

Under the supplied residual normal form and F-0071,

\[
G_\infty^{\rm return}
\le
\alpha_{b,\varepsilon}^{-1}\operatorname{Def}_\square.
\]

Consequently

\[
\boxed{
\begin{aligned}
\Xi_I\le{}&
\operatorname{ChartMis}_I
+G_\infty^{\rm exit}
+G_\infty^{\rm atlas}
+G_\infty^{\rm splice}\\
&+\alpha_{b,\varepsilon}^{-1}\operatorname{Def}_\square
+(\mathcal R_I^\times)^{\rm noncore}.
\end{aligned}
}
\tag{4.2}
\]

The profile-deficit term has disappeared from the terminal list.

---

## 5. Improved common-zero-set closure

Given the faithful atlas and residual normal form, if

\[
\operatorname{ChartMis}_I=0,
\quad
G_\infty^{\rm exit}=G_\infty^{\rm atlas}
=G_\infty^{\rm splice}=0,
\quad
\operatorname{Def}_\square=0,
\]

then

\[
\boxed{\Xi_I=0}
\]

without assuming \(\mathcal D_I^\sharp=0\).  Thus profile polarization or
imbalance is not an independent obstruction in the exact root-excess
exhaustion.

F-0038 and F-0051 remain useful for other temporal/stability arguments, but
must not be charged as a positive rounding error in the fixed master
inequality.

---

## 6. Remaining theorem-level list

After F-0077 the finite list is:

1. \(\operatorname{ChartMis}_I\) / actual atlas-boundary;
2. named actual stopping outputs;
3. the specified three-cylinder splice defect;
4. F-0071 switch-square defect;
5. return/merge outside the supplied residual normal form;
6. construction of the faithful global atlas and residual normal form.

The F-0038 profile term is no longer on the positive side of the master
inequality.
