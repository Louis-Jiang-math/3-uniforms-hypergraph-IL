# Current handoff

## Objective

Prove

\[
\Delta(H)<\left(\frac14-o(1)\right)b^2
\Longrightarrow H\text{ has an independent transversal}.
\]

The theorem remains open. The theorem-level strategy remains
**fork--inverse-fiber--anchor**, and the only active theorem-level node is
`S1 / Q-0019`.

## Current state

- **Active node:** `S1 / Q-0019` — global inverse-fiber/source-load decomposition.
- **Current S1 subfrontier:** rank-two rollback/support-return.
- **Recently completed reductions:** common-parent minimal-bad reduction and
  exact rollback (F-0096); low pair grammar `L(z)=(1+Delta z)^2` (F-0097);
  protected-token first-use audit and fixed-token limitation (F-0098).
- **New bounded geometry:** normal-Q4 shared-`q` switch, unique eight-edge
  zipper, antipodal endpoint migration, fixed-window `K4,4` support geometry,
  exact `[3]^4` normal-support packing number 12, and codimension-one endpoint/
  first-inward incidence certificate (F-0099--F-0103).
- **Current blocker:** turn those finite support facts into an owner/root/open-
  child preserving recurrence on actual rank-two source occurrences. In
  particular, prove exact future-obligation cancellation or bounded free
  support return followed by an independently payable actual-edge collision.

The one-quarter theorem, Q-0019, and supporting Q-0016--Q-0018 are all open.
Route A remains suspended.

## Reliable inputs

### Fork density and local inverse fibers

F-0091 supplies the canonical maximal-matching repair and the source of the
one-quarter constant. Below `(1/4-epsilon)b^2`, a no-IT faithful long execution
contains positive density of matching excess/disjoint-blocker forks.

F-0092--F-0094 provide genuine local `b^{-2}`/`b^{-3}` inverse-fiber estimates
on later outputs, but they do not by themselves control the original source
fork load. F-0095 proves that directly recording a new degree-indexed descendant
edge gives only a constant-scale mark and cannot recover the sharp threshold.

### Common-parent rollback

For four singleton repairs defined from one independent parent,

\[
R_I(Q)=\left(R\setminus\bigcup_{i\in I}D_i(q_i)\right)\cup\{q_i:i\in I\},
\]

an inclusion-minimal bad set has size 2 or 3. Rolling back one whole branch
returns exactly to `R_{I\setminus{t}}`, already independent by minimality. This
closes the earlier support-synchronization problem without assuming equal
private deletion sets.

Rollback does **not** permanently remove the hole obligation; the block may be
sampled again.

### Pair grammar

In the faithful low pair grammar,

\[
L(z)=(1+\Delta z)^2,
\qquad
\inf_{z>0}\frac{L(z)}z=4\Delta.
\]

Thus only a node with matching rank at least two on one side needs additional
control. The irreducible high geometry is the first two canonical matching
edges, i.e. a `(2,0)` or `(0,2)` core, provided the remaining children are left
untouched.

Protected tokens can be recovered when their first deletion occurs through an
already-recorded canonical matching edge. If `N` tokens are born and `2C` are
deleted by `C` such matching edges, the corresponding token factor is

\[
\Delta^C/b^N.
\]

But a fixed number of tokens per high node gives only a constant factor near
`Delta=b^2/4`, not the required `o_b(1)` mark.

### Normal-Q4 zipper geometry

The bounded exhaustive generator
`enumerate/q0019_rank_two_zipper_validation.py` gives:

- 272 coordinate perfect matchings, 8 normal;
- 192 rooted normal one-hole states;
- `C/S/R = 192/384/192` for the four two-branch releases;
- the category is determined by whether the shared actual coordinate-value `q`
  is retained on both sides, released on both sides, or mixed;
- every `S` pair has one eight-edge bridge order and seven cuts of that same
  bridge;
- the bridge is a cyclic `8_3` support;
- strict endpoint persistence is false: the endpoint pair moves from bridge
  seam `(0,7)` to `(3,4)` and `q` changes, while the whole eight-edge support
  remains unchanged in the binary window;
- the eight fixed-window normal supports have overlap-2 graph `K4,4`;
- all 648 embedded normal supports in `[3]^4` form one block/value automorphism
  orbit and have exact pairwise edge-disjoint packing number 12;
- `(e_1,e_2;q;f_1,f_2)` exposes 7 of the 8 binary coordinate-value vertices,
  leaving one complementary `b`-ary value in the complete-universe model.

These are bounded support facts. They are not an asymptotic source charge and
do not prove `P^2 -> P`.

## Provisional findings retained for reconstruction

The supplied conversations also reported several potentially useful finite
results whose generators/certificates are not present in the current patch and
therefore are **not promoted** to canonical facts:

- a ternary axis-line exact-cover MILP with at most `16/81` normal binary boxes
  and center-star extremizers;
- a complete nonnormal-Q4 cancellable-face classification with rooted diagonal
  exceptions;
- a rooted-bad edge-weight profile `(1,3,3,1)` yielding a degree-based
  inequality of the form `3B <= 4 Delta (b-1)^2`.

If these are reused, first reconstruct and commit their generators/certificates.
The unrooted `16/81` density must not be treated as a source survival
probability; the supplied conversation already produced a rooted diagonal
codebook obstruction to that shortcut.

## Do not repeat

The following mechanisms have been audited and rejected as theorem-closing
shortcuts:

1. descendant output codimension automatically bounds the original source row;
2. a local heavy coordinate automatically becomes a future-complete anchor;
3. a retained/frozen pair child supplies an additional `1/b` or `1/b^2` mark;
4. a minimal triple's third target is automatically irreversible;
5. fixed support implies a fixed pair fiber;
6. fresh transition rank or fresh Shannon information automatically telescopes
   across changing supports;
7. rollback `4 -> 2` is automatically a `b^{-2}` entropy saving;
8. full protected-pair coverage forces quadratic degree;
9. normal-window density is automatically a source contraction;
10. the endpoint tuple `(e_1,e_2;q)` is fixed under the normal zipper;
11. two histories reaching one actual state are automatically one future
    obligation.

The repository-level reason is the same in each case: no-copy source provenance
or a real capacity/telescoping quantity is missing.

## Open questions

1. **Source-owned support universe.** Starting from one actual high rank-two
   source occurrence, can every no-paid normal continuation be kept inside one
   bounded source-static ternary support universe, or does first escape itself
   expose an independently payable actual edge/support?
2. **Exact future merge.** At the unique `4+4` normal zipper midpoint, are the
   two open pair boundaries future-congruent with owner/root/stack/provenance
   preserved, so that one obligation really disappears?
3. **Owner-weighted support return.** If exact merge fails, can F-0101's finite
   support packing be lifted to a recurrence saying each source owner has only
   `O(1)` free normal high events before actual-edge reuse/core?
4. **Codimension-one completion.** Can the final complementary value left by
   `(e_1,e_2;q;f_1,f_2)` be recovered from an already-paid future event, rather
   than recorded as a new free `b`-ary label?

## Immediate next actions

1. Build an actual rank-two **ternary support-migration graph** whose node label
   retains owner, root, source four-buffer, current normal support, open pair
   obligations, and actual-edge history.
2. Exhaust/verify its bounded transitions: same-box support move, first support
   escape, exact-future merge, or actual-edge reuse. A new subtype is useful
   only if it reduces mass/capacity/return potential.
3. Derive the owner-weighted recurrence. Success means either an `o_b(1)` high
   mark or only `O(1)` free high events per source owner before a verified paid
   term. Without this recurrence, do not promote Q-0019.
4. Separately reconstruct the conversation-reported `16/81`, cancellable-face,
   and rooted `(1,3,3,1)` generators if those finite lemmas are to be used.

## Required reading

1. `docs/MAIN_PROOF_ROUTE.md`
2. `knowledge/QUESTIONS.md#q-0019--global-inverse-fiber-decomposition-for-fork-mass`
3. `evidence/proofs/FORK_INVERSE_FIBER_ANCHOR_ROUTE.md`
4. `evidence/proofs/Q0019_RANK_TWO_ROLLBACK_ZIPPER_ROUTE.md`
5. `evidence/analyses/FORK_MACRO_RECORD_ARITY_BARRIER.md`
6. `evidence/analyses/Q0019_COMBINATORIAL_COMPRESSION_AUDIT_2026_08_08.md`
7. `evidence/experiments/q0019_rank_two/reports/q0019_rank_two_zipper_validation.md`
8. `knowledge/FAILURES.md` entries A-0051--A-0058
9. `knowledge/DECISIONS.md` entries D-0013--D-0014
