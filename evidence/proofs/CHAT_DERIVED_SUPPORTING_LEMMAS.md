# Supporting execution lemmas

## 1. Finite complete-state stabilization

Let \(\mathcal T\) be an unfolded actual execution tree and let \(q(u)\) be a
finite label attached to each node.  Assume that \(q(u)\) determines the complete
one-step labeled successor multiset, including actual support, attempted vertex,
complete blocker family, legal releases, successor support, owner fields, and
all ledger increments.

If the depth-zero future signature is defined by
\[
\sigma_0(u)=q(u),
\]
then there is a finite function \(\Psi\) such that
\[
\sigma_1(u)=\Psi(q(u)).
\]
Consequently,
\[
\sigma_0(u)=\sigma_0(v)
\Longrightarrow
\sigma_1(u)=\sigma_1(v).
\]
The finite future-signature hierarchy therefore stabilizes at depth \(0\).
This is conditional: constructing such a complete finite state for the global
execution is a separate obligation.

## 2. Release-complete no-copy refinement

Let \(T\) be an independent one-hole transversal and let \(x\) lie in its
missing block.  Suppose the complete blocker family is
\[
\mathcal K(T,x)=\{\{x,a,b\}\}.
\]
Then both
\[
(T\setminus\{a\})\cup\{x\},
\qquad
(T\setminus\{b\})\cup\{x\}
\]
are independent.

Indeed, any edge appearing after either deletion would already belong to
\(\mathcal K(T,x)\), while deletion destroys its unique member.  Hence a parent
cylinder can be partitioned by an independent binary coordinate into the two
legal release children.  The operation splits mass and does not copy it.
Discarding one branch is a policy choice, not future completeness.

## 3. Eventually-same-edge tails under uniform hole sampling

Fix a real edge \(e\).  Assume that at each nonterminal one-hole state the
attempted vertex is uniform in the missing block of size \(b\).  Conditional on
the past, at most one attempted vertex can make \(e\) the next blocker, since
\(e\) has at most one vertex in that block.  Therefore
\[
\Pr(\text{the next \(m\) blockers are all \(e\)}\mid\mathcal F_t)
\le b^{-m}.
\]
Letting \(m\to\infty\) shows that the event “from time \(t\) onward every blocker
is \(e\)” has probability zero.  A finite union over real edges and a countable
union over \(t\) still have measure zero.

This statement requires uniform positive hole-vertex sampling; it is not a
property of an arbitrary faithful execution.

## 4. Fixed-pivot target-following

Let \(T\) be an independent one-hole transversal, let \(p\in T\), and exclude
the block \(B(p)\) from the active blocks.  Choose a target vertex \(x_C\in C\)
for every active block \(C\).  Starting at the current missing block \(M\),
attempt \(x_M\).

Stop if one of the following occurs:

1. \(T\cup\{x_M\}\) is independent;
2. the complete blocker family is not a single edge with a legal common release;
3. the unique blocker does not contain \(p\).

Otherwise the blocker is
\[
\{p,x_M,z\}.
\]
Release \(z\), retain \(p\), and move the hole to \(B(z)\).

If \(z=x_{B(z)}\), then the target contains the link edge
\[
\{x_M,x_{B(z)}\}\in E(L_H(p)).
\]
If \(z\neq x_{B(z)}\), the move inserts one new target coordinate and deletes a
nontarget coordinate, so the number of matched target blocks strictly
increases.  Thus the process stops after at most the number of active blocks.

It follows that every target transversal either contains an edge of \(L_H(p)\)
or produces one of the three stopping events above.

If a future-complete class permits only ordinary fixed-pivot moves and has no
other stopping event, every target contains a link edge.  A uniform target
contains each fixed link edge with probability \(b^{-2}\), hence
\[
1\le \frac{|E(L_H(p))|}{b^2}
=\frac{d_H(p)}{b^2},
\]
and therefore
\[
d_H(p)\ge b^2.
\]

More generally, for a uniform target,
\[
\Pr(\text{forced off-pivot or another stopping event})
\ge 1-\frac{d_H(p)}{b^2}.
\]
This target-coordinate refinement is no-copy, but it is a second-stage
postprocessing of a core cylinder; it is not literally the clean-chart
\(G_A\) variable of F-0051.

## 5. Literal one-coordinate splice closure

Let
\[
X\subseteq \prod_{i=1}^m A_i
\]
be nonempty.  Suppose that for all \(x,y\in X\) and every coordinate \(i\), the
tuple obtained from \(x\) by replacing \(x_i\) with \(y_i\) also belongs to
\(X\).  Then
\[
X=\prod_{i=1}^m \operatorname{proj}_i(X).
\]

To prove this, fix \(x^{(0)}\in X\) and arbitrary
\(a_i\in\operatorname{proj}_i(X)\).  For each \(i\), choose \(y^{(i)}\in X\)
with \(y^{(i)}_i=a_i\).  Successively replace coordinate \(i\) of the current
tuple by \(a_i\).  Closure keeps every intermediate tuple in \(X\), and the final
tuple is \((a_1,\ldots,a_m)\).

The hypothesis is literal actual-support closure.  Phase consistency,
reversibility, or projected surjectivity does not imply it.

## 6. Clean-epoch temporal contraction

Let a monotone clean epoch have continuation profile
\[
a^{(t)}=(a^{(t)}_1,\ldots,a^{(t)}_{n_t}),
\]
and define
\[
Q_t=n_t-2\sum_i a^{(t)}_i.
\]
If coordinate \(M_t\) is removed with value
\(\alpha_t=a^{(t)}_{M_t}\), and the total decrease of the surviving coordinates
is \(D_t\ge0\), then
\[
Q_{t+1}-Q_t=2\alpha_t-1+2D_t.
\]
Hence, for \(s<u\),
\[
\sum_{t=s}^{u-1}(2\alpha_t-1)\le |Q_s|+|Q_u|.
\]

The exact critical-profile identity bounds
\[
|Q_t|\le
B(n_t,\delta_t)
=
\sqrt{4n_t(n_t-1)\delta_t+\chi(n_t)}.
\]
For \(0<\tau<1/2\), if
\[
J=|\{t\in[s,u):\alpha_t<1-\tau\}|,
\]
then
\[
J\ge
\frac{(1-2\tau)(u-s)-B(n_s,\delta_s)-B(n_u,\delta_u)}
{2(1-\tau)}.
\]
If surviving mass satisfies \(m_{t+1}\le\alpha_t m_t\), then
\[
m_u\le
m_s(1-\tau)^J.
\]

Consequently, in a finite-transition-type execution, any family of histories
that avoids terminal events and finite recurrent classes and does not repeat a
complete transition type has surviving mass tending to zero: before repetition,
the number of regenerations is bounded by the finite actual resource/type
alphabet, while total clean length must diverge.

This is a conditional transient theorem.  It does not classify the recurrent
part.
