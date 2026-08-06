# F-0078 scope correction

## Status

F-0078 is downgraded from a zero-set closure interpretation to a
fixed-instance, history-unfolded stopping statement. F-0074's local
three-cylinder contraction is unaffected.

## 1. The omitted partial-completion term

The stopping identity has the form

\[
\Xi_I
=
G_\infty^W+G_\infty^M+G_\infty^{\mathrm{return}}
+G_\infty^{\mathrm{splice}}.
\]

Here \(W\) is an independent completion on the currently exposed proper set of
blocks. Global nonexistence of an independent transversal does not imply
\(G_\infty^W=0\). In a block-minimal counterexample, independent transversals
on proper block sets are expected.

Therefore no common-zero-set statement may delete \(G_\infty^W\) without a
separate extension, telescoping, or signed-progress argument.

## 2. The physical token is not a transition congruence

A label consisting of owner, current completion, blocker and seen resource
sets does not determine whether the next label is a fresh child or a return.
That classification depends on the set of labels visited earlier in the same
history. Two histories can reach the same physical label with different
visited sets and classify the same successor differently.

A faithful finite state may include the visited set and any other
history-dependent data, but then finiteness is a fixed-instance construction,
not the claimed history-free quotient.

## 3. Policy return is weaker than all-release closure

A repeated state along one deterministic release policy gives a policy cycle.
F-0071 requires closure under every legal release successor in a unique-blocker
normal form. The unused release branch may lead to an independent completion,
a multi-blocker state, a splice, a new resource, or a new state. Hence

\[
\text{policy return}\not\Rightarrow\text{all-release core}.
\]

## 4. Fixed-instance exhaustion is not uniform

Bounds of the form

\[
U_L\le \Xi_I\sum_{r=0}^{N_H}\binom Lr q_b^{L-r},
\qquad N_H=|E(H)|+|V(H)|,
\]

vanish for each fixed finite hypergraph when \(q_b<1\). They do not provide a
single depth \(L\) or a uniform normalized gap over all instances, because
\(N_H\) is unbounded. The order of quantifiers required by an asymptotic
recurrence is different.

## 5. Retained conclusion

One may run the local stopping process in fully unfolded history space and
retain the exact terminal identity. This is useful front-end organization. It
neither creates a negative term nor replaces the active global inverse-fiber
decomposition Q-0019.
