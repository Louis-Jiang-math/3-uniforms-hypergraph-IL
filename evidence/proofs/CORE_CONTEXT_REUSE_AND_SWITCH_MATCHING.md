# Actual all-release cores, context reuse, and switch matchings

## 1. Setup

Let \(K\) be a finite strongly connected class of independent one-hole
transversals.  Assume:

1. every attempted vertex has exactly one blocker;
2. both old endpoints of that blocker are retained as legal release branches;
3. every such successor lies in \(K\);
4. no augmentation occurs inside \(K\).

For \(T\in K\), write \(B(T)\) for its missing block.  Let
\[
\Omega_K=\{T\cup\{x\}:T\in K,\ x\in B(T)\}.
\]
Every \(W\in\Omega_K\) contains exactly one edge, denoted \(e(W)\).  For a real
edge \(e\), define
\[
\Omega_e=\{W\in\Omega_K:e(W)=e\},
\qquad
c_e=|\Omega_e|.
\]

## 2. Triangle decomposition

If
\[
e(W)=\{x,y,z\},
\]
then exactly the three deletions
\[
W\setminus\{x\},\quad W\setminus\{y\},\quad W\setminus\{z\}
\]
are independent one-hole states in \(K\).  Deleting a vertex outside \(e(W)\)
leaves \(e(W)\) intact.

Consequently the state multigraph is \(2b\)-regular and decomposes into
triangles indexed by \(\Omega_K\).  Double-counting state-attempt pairs gives
\[
b|K|=3|\Omega_K|.
\]

## 3. Weighted context regularity

Let
\[
K_B=\{T\in K:B(T)=B\},
\qquad
N_B=|K_B|.
\]
For every \(v\in B\),
\[
\sum_{e\ni v}c_e=N_B.
\tag{3.1}
\]
Indeed, \(T\mapsto T\cup\{v\}\) is a bijection from \(K_B\) to the completions
whose unique edge contains \(v\).

Thus low degree does not prohibit all blockers; it forces context reuse:
\[
\max_{e\ni v}c_e\ge \frac{N_B}{d_H(v)}.
\]

## 4. Common-state multiplicities

For distinct edges \(e,f\), let \(m_{ef}\) be the number of one-hole states in
which two different attempted vertices have blockers \(e\) and \(f\).  Then
\[
\sum_{f\ne e}m_{ef}=3(b-1)c_e,
\tag{4.1}
\]
and
\[
m_{ef}\le\min(c_e,c_f).
\tag{4.2}
\]

For each \(e\)-completion there are three corner states, and in each corner
there are \(b-1\) other attempted vertices.  This proves (4.1).  A common state
determines at most one \(e\)-completion and at most one \(f\)-completion, proving
(4.2).

If \(A_K\) is the incompatibility graph on real edges, with \(ef\in E(A_K)\)
when \(m_{ef}>0\), then
\[
A_Kc\ge3(b-1)c
\]
and hence
\[
\rho(A_K)\ge3(b-1).
\]
Also
\[
d_{A_K}(e)\le3(b-1)\Delta(H),
\]
but this bound alone is too weak for the one-quarter threshold.

## 5. Fixed-pivot target following inside the core

Fix \(T\in K\) and \(p\in T\).  Choose independently and uniformly one target
vertex in every block other than \(B(p)\).  Follow the current hole, retaining
\(p\) whenever the unique blocker contains \(p\).

If the blocker is \(\{p,x_M,z\}\) and \(z\) is not the target of its block, the
number of matched target coordinates increases.  If \(z\) is that target, the
target contains a link edge of \(L_H(p)\).  Hence
\[
\Pr(\text{first forced off-pivot})
\ge
1-\frac{d_H(p)}{b^2}.
\tag{5.1}
\]

For disjoint core entrance cylinders of total mass \(M_K\), this target
postprocessing gives a disjoint second-stage forced-off-pivot mass
\(G_A^{\rm core}\) satisfying
\[
G_A^{\rm core}
\ge
\left(1-\frac{\Delta(H)}{b^2}\right)M_K.
\tag{5.2}
\]
This is a separate second-stage ledger and is not identified with the
clean-chart \(G_A\) of F-0051.

## 6. Pairwise incompatible real-edge families

Let \(\mathcal F\subseteq E(H)\) be pairwise incompatible and \(N=|\mathcal F|\).
For a block \(B\) and \(v\in B\), let
\[
d_B(v)=|\{e\in\mathcal F:v\in e\}|,
\qquad
s_B=\sum_{v\in B}d_B(v).
\]
The number of pairs certified incompatible in \(B\) is
\[
I_B=\sum_{\{u,v\}\subset B}d_B(u)d_B(v)
\le \frac{(b-1)\Delta(H)}2s_B.
\]
Every pair in \(\mathcal F\) is counted at least once, while
\[
\sum_Bs_B=3N.
\]
Therefore
\[
\binom N2\le\frac32(b-1)\Delta(H)N
\]
and
\[
N\le3(b-1)\Delta(H)+1.
\tag{6.1}
\]

If \(\mathcal F\) covers every complete transversal exactly once, then
\[
|\mathcal F|=b^3
\]
and (6.1) yields
\[
\Delta(H)\ge\frac{b^3-1}{3(b-1)}
=\frac{b^2+b+1}{3}.
\tag{6.2}
\]

## 7. Completion–switch maps

Fix
\[
e=\{u_1,u_2,u_3\}
\]
with \(C=c_e>0\).  Define the switch slots
\[
S(e)=
\{(u,x):u\in e,\ x\in B(u)\setminus\{u\}\},
\qquad
k=|S(e)|=3(b-1).
\]
For \(W\in\Omega_e\) and \(s=(u,x)\), let
\[
W^s=(W\setminus\{u\})\cup\{x\},
\qquad
\pi_W(s)=e(W^s).
\]

### Lemma 7.1

Each \(\pi_W:S(e)\to E(H)\) is injective.

If two different slots in the same block had the same output edge, that edge
would contain two vertices from one block.  If they were in different blocks,
the output edge for the first switch would contain the new vertex of the second
switch, which is absent from the first switched completion.  Both are
impossible.

Define
\[
n_s(f)=|\{W\in\Omega_e:\pi_W(s)=f\}|,
\qquad
p_s(f)=\frac{n_s(f)}C.
\]
Then
\[
m_{ef}=\sum_{s\in S(e)}n_s(f).
\tag{7.1}
\]

If \(e\) has maximum context multiplicity,
\[
C=\max_g c_g,
\]
then
\[
\sum_f p_s(f)=1
\quad\text{and}\quad
\sum_s p_s(f)=\frac{m_{ef}}C\le\frac{c_f}C\le1.
\tag{7.2}
\]
Thus \(P_e=(p_s(f))\) is a fractional matching saturated on the slot side.

## 8. Maximal-reuse synchronization–dispersion theorem

For \(W,W'\in\Omega_e\), define
\[
d_e(W,W')
=
|\{s\in S(e):\pi_W(s)\ne\pi_{W'}(s)\}|.
\]
For every \(0<\delta<1\), exactly one of the following holds.

### Synchronization

There is \(W_0\in\Omega_e\) such that
\[
\sum_{W\in\Omega_e}d_e(W,W_0)\le\delta Ck.
\tag{8.1}
\]
Writing \(f_s=\pi_{W_0}(s)\), there are
\[
S_0\subseteq S(e),\qquad \Omega_0\subseteq\Omega_e
\]
with
\[
|S_0|\ge(1-\sqrt\delta)k,
\qquad
|\Omega_0|\ge(1-\sqrt\delta)C,
\]
such that
\[
n_s(f_s)\ge(1-\sqrt\delta)C
\quad(s\in S_0),
\]
and every \(W\in\Omega_0\) agrees with \(W_0\) on at least
\((1-\sqrt\delta)k\) slots.  The edges \(f_s\) are pairwise different, and
\[
(1-\sqrt\delta)C\le m_{ef_s}\le c_{f_s}\le C.
\tag{8.2}
\]

This follows by applying Markov's inequality to the exceptional
context–slot pairs in (8.1), and by injectivity of \(\pi_{W_0}\).

### Dispersion

For every \(W_0\in\Omega_e\),
\[
\sum_Wd_e(W,W_0)>\delta Ck.
\]
Averaging \(W_0\) gives
\[
\frac1{C^2}\sum_{W,W'}d_e(W,W')>\delta k.
\tag{8.3}
\]
For each slot, two independent contexts agree with probability
\(\sum_f p_s(f)^2\), so
\[
\sum_s\left(1-\sum_fp_s(f)^2\right)>\delta k.
\tag{8.4}
\]
Since for any probability vector \(q\),
\[
1-\max q_i\ge\frac12\left(1-\sum_iq_i^2\right),
\]
we obtain
\[
\sum_s\left(C-\max_fn_s(f)\right)
>
\frac\delta2Ck.
\tag{8.5}
\]

Thus a positive proportion of context–slot pairs lie outside the modal output
of their slot.

## 9. Exact synchronization

If the synchronization defect is zero, all maps \(\pi_W\) are the same
injection \(\pi_e\).  For \(s=(u,x)\), let \(f_s=\pi_e(s)\).  Then
\[
m_{ef_s}=c_e=c_{f_s},
\]
and
\[
f_s\setminus\{x\}\subseteq
\bigcap_{W\in\Omega_e}W.
\]
Moreover,
\[
W\longmapsto W^s
\]
is a bijection \(\Omega_e\to\Omega_{f_s}\).

If every maximum-multiplicity edge is exactly synchronized, the graph joining
\(e\) to \(f\) when \(m_{ef}=C\) is \(3(b-1)\)-regular.

These conclusions are strong, but they do not imply product support without an
actual coordinate-expansion theorem.

## 10. Latin-square saturation obstruction

The dispersion estimate does not by itself create unused real-edge capacity.
Let contexts, slots, and labels all be \(\mathbb Z_q\), and define
\[
\pi_t(s)=s+t\pmod q.
\]
Every \(\pi_t\) is a bijection, and
\[
n_s(f)=1
\]
for every \(s,f\).  Thus the switch maps are maximally dispersed, while every
label column has total load
\[
\sum_sn_s(f)=q=C.
\]

This abstract array satisfies all fractional-matching and column-saturation
identities above.  It need not be realizable by an actual recurrent hypergraph,
but it proves that matrix dispersion alone cannot imply capacity slack.  Any
completion of Q-0016 must use actual edge endpoints, support transport, and
no-IT/block-minimal structure.
