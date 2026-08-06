# Current handoff

## Objective

Prove the asymptotic one-quarter threshold for independent transversals in
equal-block partitioned 3-uniform hypergraphs. The theorem remains open.

## Active route

- **Primary strategy:** fork--inverse-fiber--anchor.
- **Active DAG node:** `S1 / Q-0019`.
- **Supporting finite-state machinery:** F-0052, F-0053, F-0055 and the valid
  local part of F-0074/F-0078.
- **Former Route-B ledger strategy:** retained as supporting algebra, no longer
  the theorem-level closing mechanism.
- **Route A:** suspended.

The active chain is

\[
\boxed{
\begin{aligned}
&\text{finite actual-history LP / stopping exhaustion}\\
&\quad\longrightarrow\text{canonical maximal-matching repair}\\
&\quad\longrightarrow\text{positive disjoint-blocker fork density}\\
&\quad\longrightarrow\text{global inverse-fiber codimension decomposition}\\
&\quad\longrightarrow
\begin{cases}
\text{diffuse load: }\Delta(H)\ge(1/4-o(1))b^2,\\
\text{persistent anchor: }\Delta(H)\ge b^2.
\end{cases}
\end{aligned}}
\]

## What is rigorously available

### Finite history organization

For a supplied finite faithful actual-history digraph, F-0052 gives

\[
\text{strict potential}
\Longleftrightarrow
\text{acyclic reduced digraph}
\Longleftrightarrow
\text{no residual circulation}.
\]

This is an exhaustion and localization tool. It does not itself create a
negative term or a degree lower bound.

### Rank-two repair and the one-quarter constant

For an independent partial transversal \(S\) and attempted vertex \(x\), let
\(G_x(S)\) be the graph of blocker pairs. A canonical maximal matching
\(M_x(S)\) hits every blocker pair, so

\[
S'=(S\cup\{x\})\setminus V(M_x(S))
\]

is independent. If every matching has size at most one, the faithful record
generating function is

\[
1+\Delta z^2,
\qquad
\inf_{z>0}\frac{1+\Delta z^2}{z}=2\sqrt\Delta.
\]

Thus the fork-free branch has the exact threshold \(\Delta<b^2/4\). Under
\(\Delta\le(1/4-\varepsilon)b^2\), a no-IT execution must instead contain a
positive linear density of matching excess, each unit yielding two blocker
edges disjoint away from the pivot.

### Local inverse-fiber codimension

For a private transversal of an edge \(e=\{x,a,b\}\), replace \(a,b\) by
\((u,v)\) in their blocks. Every selected edge in the replacement target uses
at least one of \(u,v\). A fixed output edge has at most one preimage when it
uses both replacements, and at most \(b\) preimages when it uses exactly one.
This gives genuine \(b^{-2}\) and \(b^{-1}\) multiplicity bounds while
retaining the parent history.

The fork-rooted refill box F-0093 starts from the actual full matching repair
and refills every resulting hole against a product target. It gives an exact
augmentation/two-target-blocker dichotomy and at most \(3W/b^2\) received mass
on a fixed later output edge. F-0094 additionally protects the original pivot:
the terminal is then either a two-target edge through that pivot or a
three-target off-pivot edge; a fixed output in the latter class has mass at
most \(W/b^3\).

These estimates do not yet bound the source load \(\ell_x\). The independent
augmentation remains partial, and an off-pivot target edge on some target atoms
does not supply a complete proper-block no-IT subsystem.

### Direct macro-record audit

F-0095 tests the proposed bypass in which each refill output is recorded
directly as a nested entropy-compression macro. If matching excess is assigned
an independent mark \(y\), the exact infimum in the resulting weighted-tree
envelope is

\[
G(y)=\inf_{0<u<1/y}
\frac{1+(1-y)u}{\sqrt u(1-yu)}.
\]

Approaching the one-quarter threshold requires \(y=o_b(1)\). A new actual
three-edge output localized by one of its target endpoints gives only
\(y=\Delta/b^2\); even granting that factor independently to every excess unit
has self-consistent threshold \(0.211390706210804\ldots\). Repeating independent
boxes does not shrink the dispersed off-pivot output family. Therefore the
direct macro route is A-0051, not a replacement for the owner-preserving
transport/closure theorem.

### Persistent-anchor endgame

If a positive-mass class is future-complete for a fixed pivot \(p\), and every
unique blocker in every legal continuation contains \(p\), then target-following
shows that every full target outside the block of \(p\) contains a link edge of
\(p\). Double counting gives

\[
d_H(p)\ge b^2.
\]

This is an endgame theorem, not an anchor-extraction theorem.

## Exact remaining problem

For fork mass \(F_x\), define the edge load

\[
\ell_x(e)=\sum_f w_x(e,f),
\qquad
\ell_x^*=\max_{e\ni x}\ell_x(e).
\]

The elementary double count is

\[
2F_x\le d_H(x)\ell_x^*.
\]

The missing global theorem must prove a no-copy, history-preserving decomposition
that implies, schematically,

\[
\ell_x^*
\le
\frac{8+o_b(1)}{b^2}F_x
+\mathsf{Exit}_x
+\mathsf{Proper}_x
+\mathsf{Anchor}_x.
\]

The unresolved part is an owner-preserving transport from the refill outputs
back to the original fork edges. In the pivot-protected form this is precisely
the augmentation/three-target off-pivot mass: it must enter an independently
verified progress term, cover a complete proper-block subsystem, or leave a
future-complete class with the same fixed anchor. Local concentration does not
imply any of these global alternatives.

## F-0078 correction

Do not use F-0078 to assert any of the following:

1. \(G_\infty^W=0\) from global nonexistence of an independent transversal;
2. the physical token alone determines return versus fresh continuation;
3. a deterministic-policy return is an all-release F-0071 core;
4. fixed-instance exhaustion supplies a uniform finite-depth error bound.

The valid residue is the unfolded stopping identity together with F-0074's
local contraction.

## Do not reopen as main routes

- global signed re-entry or Hall transport without an independently verified
  negative term;
- waiting-time, Kraft or exact-certificate regeneration as a source of loss;
- first-owner compression or stationary matching;
- private-target external-coordinate concentration as link concentration;
- Hall deficiency alone as control of spread or blocker multiplicity.

## Required reading

1. `docs/MAIN_PROOF_ROUTE.md`
2. `evidence/proofs/FORK_INVERSE_FIBER_ANCHOR_ROUTE.md`
3. `evidence/audits/F0078_SCOPE_CORRECTION.md`
4. `knowledge/FACTS.md` entries F-0052, F-0058, F-0090--F-0095
5. `knowledge/QUESTIONS.md#Q-0019`
6. `knowledge/FAILURES.md#A-0051`
7. `evidence/analyses/FORK_MACRO_RECORD_ARITY_BARRIER.md`
8. `manuscript/independent_transversal_fork_route.tex`
