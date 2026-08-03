# Harmonic degree-budget compression and its strict limitation

## 1. Exact local compression

Fix an independent state \(S\) and a missing block \(B\).  For each failed
vertex \(x\in B\), choose a blocker
\[
e_x=\{x,y_x,z_x\}
\]
attaining the harmonic minimum.  Define
\[
c_{S,B}(y)=
\sum_{\substack{x\in F(S,B)\\y\in e_x}}
\frac1{d_H(y)+d_H(r_x(y))},
\]
where \(r_x(y)\) is the other old endpoint of \(e_x\).

Then the harmonic failure term equals
\[
\sum_{y\in S}c_{S,B}(y)\gamma_{S\setminus\{y\}},
\]
and
\[
0\le c_{S,B}(y)\le1,
\qquad
\sum_{y\in S}d_H(y)c_{S,B}(y)=|F(S,B)|.
\]

The first bound follows because the chosen blockers containing \(y\) are
different real edges, so there are at most \(d_H(y)\) summands, each at most
\(1/d_H(y)\).  Each failed vertex contributes
\[
\frac{d_H(y_x)}{d_H(y_x)+d_H(z_x)}
+
\frac{d_H(z_x)}{d_H(y_x)+d_H(z_x)}
=1
\]
to the weighted sum.

## 2. The degree-budget polytope is a strict relaxation

Take three blocks
\[
B_i=\{p_i,q_i\},\qquad i=1,2,3,
\]
and all eight cross-block triples.  Then \(b=2\), every vertex has degree \(4\),
and there is no independent transversal.

For a rank-two state \(S=\{u,v\}\), both vertices of the remaining block fail
and their unique blockers are \(\{u,v,x\}\).  The true harmonic failure term is
\[
2\,\frac{\gamma_u+\gamma_v}{4+4}
=
\frac{\gamma_u+\gamma_v}{4}.
\]
The projected degree-budget constraints retain only
\[
4c_u+4c_v=2,
\qquad\text{equivalently}\qquad
c_u+c_v=\frac12,
\]
and therefore incorrectly allow \((c_u,c_v)=(1/2,0)\).

Define a projected dual assignment by
\[
\alpha_{p_i}=1,\quad \gamma_{p_i}=0,
\qquad
\alpha_{q_i}=0,\quad \gamma_{q_i}=2,
\]
and at rank two set
\[
\alpha_{p_ip_j}=0,
\]
while every pair containing at least one \(q\)-vertex has
\[
\alpha_{uv}=1,\qquad \gamma_{uv}=0.
\]
The root and singleton projected inequalities hold with equality.  For the pair
\(p_iq_j\), the relaxed choice
\[
c_{q_j}=\frac12,\qquad c_{p_i}=0
\]
gives
\[
\alpha_{p_iq_j}=1=\frac12\gamma_{q_j}.
\]
Thus the degree-budget relaxation is feasible.

The true harmonic inequality at the same pair would require
\[
1=\alpha_{p_iq_j}
\le
\frac{\gamma_{p_i}+\gamma_{q_j}}4
=
\frac12,
\]
a contradiction.

Therefore the exact compression lemma is valid, but replacing its
actually-generated coefficients by arbitrary points of the degree-budget
polytope loses the old-endpoint pairing and is not sound.
