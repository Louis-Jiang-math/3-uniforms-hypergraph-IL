# Fork--inverse-fiber--anchor route

## Purpose

This note records the strongest currently justified route to the one-quarter
threshold. It separates the source of the constant, the repeated-edge problem,
and the rigid endgame.

## 1. Canonical maximal-matching repair

For an independent partial transversal \(S\) and an attempted vertex \(x\),
let

\[
G_x(S)=\{\{u,v\}\subseteq S:\{x,u,v\}\in E(H)\}.
\]

Choose a maximal matching \(M\) in this graph. Every edge of \(G_x(S)\) meets
\(V(M)\); otherwise it could be added to the matching. Consequently

\[
(S\cup\{x\})\setminus V(M)
\]

is independent. If \(|M|=1\), every blocker is removed by deleting two old
vertices even when the blocker family itself is large. The obstruction to
rank-two repair is therefore \(\nu(G_x(S))\ge2\), not merely the existence of
multiple blockers.

## 2. Entropy dichotomy

In the fork-free case the two record types have height changes \(+1\) and
\(-1\), with at most \(\Delta\) edge labels in the latter case. The node
polynomial is

\[
\Phi_0(z)=1+\Delta z^2,
\]

and

\[
\inf_{z>0}\Phi_0(z)/z=2\sqrt\Delta.
\]

Thus faithful reconstruction gives the exact one-quarter threshold in the
fork-free class. Marking matching excess by \(y\in(0,1)\) gives

\[
\Phi_y(z)=1+\frac{\Delta z^2}{1-y\Delta z^2}.
\]

At \(z=\Delta^{-1/2}\), this is

\[
\sqrt\Delta\frac{2-y}{1-y}.
\]

For every fixed \(\varepsilon>0\), choosing \(y=\varepsilon\) yields a positive
constant \(\alpha_\varepsilon\) such that, under
\(\Delta\le(1/4-\varepsilon)b^2\), records with fewer than
\(\alpha_\varepsilon T\) excess units have exponential growth strictly below
\(b^T\). Hence no-IT long executions carry positive fork density.

## 3. Fork load double counting

For weighted fork pairs at pivot \(x\),

\[
2F_x=\sum_{e\ni x}\ell_x(e)
\le d_H(x)\ell_x^*.
\]

A uniform estimate

\[
\ell_x^*\le(8+o_b(1))F_x/b^2
\]

would yield the desired degree lower bound. The entire backend problem is the
control of \(\ell_x^*\).

## 4. Two-coordinate replacement boxes

Let \(H\) be edge-minimal without an independent transversal. For an edge
\(e=\{x,a,b\}\), choose a full transversal \(W_e\) containing no edge other
than \(e\). Replace \(a,b\) by \(u,v\) in their blocks and select an edge
\(g_e(u,v)\) of the resulting target.

Any such edge contains \(u\) or \(v\); otherwise it would already be a second
edge of \(W_e\). A fixed output edge has at most one preimage if it contains
both \(u,v\), and at most \(b\) if it contains exactly one. After retaining the
parent occurrence, these become global weighted multiplicity bounds
\(b^{-2}\) and \(b^{-1}\).

The remaining one-coordinate output has the form \(\{u,p,q\}\). The pair
\(\{p,q\}\) can depend on the row, source edge, and later transition. A local
box can be fully covered by such row-dependent pairs while maximum degree is
only linear in \(b\). Thus no local codimension argument can force persistence.

## 5. Persistent-anchor endgame

Assume a future-complete residual class has a fixed pivot \(p\), every state is
an independent one-hole transversal, and every unique blocker in every legal
continuation contains \(p\). Follow an arbitrary target outside the block of
\(p\). Each nonterminating step either finds a link edge of \(p\) in the target
or increases the number of target coordinates already installed. Therefore
every target contains a link edge. Counting targets gives \(d_H(p)\ge b^2\).

This theorem disposes of a fixed persistent anchor, not a migrating local heavy
pair.

## 6. Active theorem

The global inverse-fiber decomposition must turn every actual fork occurrence
into exactly one of:

- a two-coordinate diffuse occurrence;
- a transition with an independently valid signed or structural exit;
- a complete proper-block subsystem;
- a future-complete occurrence in a fixed-anchor class.

It must retain the actual parent, owner, root, edges and legal future moves.
The constants must be uniform. The only unresolved mass is the first loss or
migration of the heavy coordinate/pair.

## 7. Why this route is preferred

- It is the only route whose local counting naturally produces \(1/4\).
- It treats high inverse multiplicity as rigidity rather than assuming it is
  bounded.
- It does not require every terminal to manufacture a negative root-ledger
  term.
- Its zero-loss branch has a recognizable endgame, namely a fixed-pivot link
  covering all targets.

LP, root normalization, finite stopping and stability identities remain useful
front-end tools, but they are not substitutes for the global decomposition.
