# Q-0019 rank-two normal-zipper validation

- **Generator:** `enumerate/q0019_rank_two_zipper_validation.py`
- **Command:** `python enumerate/q0019_rank_two_zipper_validation.py`
- **Artifact:** `evidence/experiments/q0019_rank_two/baselines/q0019_rank_two_zipper_validation.json`
- **Result type:** bounded exhaustive computation plus exact finite MILP
- **Scope:** all coordinate perfect matchings of binary `Q4`, all normal rooted one-hole states/release pairs, and all embedded normal supports in `[3]^4`.

## Binary normal geometry

The generator reproduces the existing finite baseline:

- 272 coordinate perfect matchings;
- 8 normal matchings;
- 192 rooted independent one-hole states;
- 768 two-branch release pairs, classified as

  \[
  C=192,\qquad S=384,\qquad R=192.
  \]

It strengthens the structural readout:

1. every normal root has two completion blockers intersecting in exactly one actual coordinate-value `q`;
2. the four release choices are determined by whether each branch retains or releases `q`: retain/retain is `C`, the two mixed choices are `S`, and release/release is `R`;
3. every `S` pair has exactly one eight-edge bridge order and exactly seven edge-disjoint cuts of that same bridge;
4. the eight blocker triples form one cyclic `8_3` support; the endpoint/first-inward incidence has one unoriented type;
5. the source endpoint pair determines the normal support uniquely in the binary window.

The antipodal zipper does **not** preserve the endpoint tuple. In all 192 rooted cases it keeps the same eight-edge support, moves the endpoint pair from bridge positions `(0,7)` to `(3,4)`, shares no endpoint actual edge with the old pair, and changes the common coordinate-value. Hence strict endpoint persistence is refuted while support persistence survives in this finite model.

## Normal-support overlap in a fixed binary window

Across the eight normal supports:

- all 32 possible blocker triples occur, each in exactly two normal supports;
- two distinct supports intersect in either 0 or 2 actual blocker triples;
- the overlap-2 graph is exactly `K_{4,4}`.

Consequently a fixed binary window contains at most four pairwise actual-edge-disjoint normal supports. This is a finite support-packing statement, not a global source-capacity theorem.

## Embedded ternary supports

Embedding every normal binary support into all `3^4=81` binary subwindows of `[3]^4` gives 648 distinct supports on 108 possible blocker triples. The full `S_4 x S_3^4` block/value action has orbit size 648 on a fixed support, so the support family is transitive.

An exact set-packing MILP then gives:

- a feasible packing of 12 pairwise actual-edge-disjoint normal supports;
- infeasibility of a packing of 13 supports after fixing one support, which is valid by the verified transitivity.

Thus the finite packing number is exactly

\[
\nu_{\mathrm{normal}}([3]^4)=12.
\]

One optimal packing covers 96 of the 108 blocker triples and leaves 12, three in each omitted direction. This is bounded evidence for an `O(1)` free-normal-support principle inside a source-static ternary box; it is not an asymptotic charging theorem.

## Codimension-one incidence certificate

For every normal splice bridge `H_0,...,H_7`, let

\[
e_1=H_0,\quad e_2=H_7,\quad f_1=H_1,\quad f_2=H_6.
\]

The endpoint pair exposes 5 of the 8 binary coordinate-value vertices. Adding the two first-inward edges exposes 7 of 8; adding the central completion exposes all 8. Uniformly in the complete `b`-ary completion model, the corresponding raw completion counts are

\[
(b-1)^3,\qquad b-1,\qquad 1.
\]

The remaining factor `b-1` is **not** automatically a valid `1/b` record saving: one still has to prove that the last value is source-owned or is exposed by an already-paid faithful future event.

## Interpretation

The computation supports replacing strict endpoint persistence by a weaker source-static support notion. It also supplies a finite packing obstruction to arbitrarily many fresh normal zippers inside a fixed ternary four-buffer. Neither statement proves `P^2 -> P`: confluence of two histories at the same state does not imply equality of owner/root/stack/provenance future obligations.
