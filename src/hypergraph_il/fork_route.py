from __future__ import annotations

from dataclasses import dataclass
from math import log, sqrt
from typing import Iterable, Mapping, Sequence

from .models import Edge, Hypergraph, Vertex

Pair = frozenset[Vertex]


def blocker_pairs(
    hypergraph: Hypergraph,
    state: Sequence[Vertex],
    attempted: Vertex,
) -> tuple[Pair, ...]:
    """Return the non-pivot pairs of all blockers created by ``attempted``.

    The input state must be independent and may contain at most one vertex from
    each block. Every blocker then necessarily contains ``attempted``.
    """
    if not hypergraph.is_independent(state):
        raise ValueError("state must be independent")
    blocks = [vertex[0] for vertex in state]
    if len(blocks) != len(set(blocks)):
        raise ValueError("state is not a partial transversal")
    if attempted[0] in set(blocks):
        raise ValueError("attempted vertex must lie in a missing block")

    pairs: list[Pair] = []
    for edge in hypergraph.blocking_edges(state, attempted):
        if attempted not in edge:
            raise AssertionError("an edge newly created from an independent state must contain the pivot")
        pair = frozenset(edge - {attempted})
        if len(pair) != 2:
            raise AssertionError("3-uniform blocker must leave a pair")
        pairs.append(pair)
    return tuple(sorted(pairs, key=lambda pair: tuple(sorted(pair))))


def canonical_maximal_matching(pairs: Iterable[Pair]) -> tuple[Pair, ...]:
    """Greedy maximal matching in canonical lexicographic order."""
    ordered = sorted(set(pairs), key=lambda pair: tuple(sorted(pair)))
    used: set[Vertex] = set()
    matching: list[Pair] = []
    for pair in ordered:
        if len(pair) != 2:
            raise ValueError("every blocker pair must contain exactly two vertices")
        if used.isdisjoint(pair):
            matching.append(pair)
            used.update(pair)
    return tuple(matching)


@dataclass(frozen=True)
class MatchingRepair:
    attempted: Vertex
    blocker_pairs: tuple[Pair, ...]
    matching: tuple[Pair, ...]
    removed: frozenset[Vertex]
    state_after: tuple[Vertex, ...]

    @property
    def rank(self) -> int:
        return len(self.matching)

    @property
    def fork_excess(self) -> int:
        return max(0, self.rank - 1)


def canonical_matching_repair(
    hypergraph: Hypergraph,
    state: Sequence[Vertex],
    attempted: Vertex,
) -> MatchingRepair:
    """Apply the canonical maximal-matching repair.

    Maximality guarantees that the removed endpoints meet every blocker pair,
    so the resulting partial transversal is independent.
    """
    pairs = blocker_pairs(hypergraph, state, attempted)
    matching = canonical_maximal_matching(pairs)
    removed = frozenset(vertex for pair in matching for vertex in pair)
    result = tuple(sorted((set(state) | {attempted}) - set(removed)))
    if not hypergraph.is_independent(result):
        raise AssertionError("maximal matching failed to hit every blocker")
    return MatchingRepair(
        attempted=attempted,
        blocker_pairs=pairs,
        matching=matching,
        removed=removed,
        state_after=result,
    )


def fork_free_growth_rate(max_degree: float) -> float:
    """Minimum of ``(1 + Delta z^2) / z`` for Delta >= 0."""
    if max_degree < 0:
        raise ValueError("max_degree must be nonnegative")
    return 2.0 * sqrt(max_degree)


def unrestricted_matching_growth_rate(max_degree: float) -> float:
    """Minimum of ``1 / (z(1-Delta z^2))`` for Delta >= 0."""
    if max_degree < 0:
        raise ValueError("max_degree must be nonnegative")
    return 1.5 * sqrt(3.0) * sqrt(max_degree)


@dataclass(frozen=True)
class ForkDensityParameters:
    epsilon: float
    A: float
    alpha: float


def fork_density_parameters(epsilon: float) -> ForkDensityParameters:
    """Return the explicit constants in the weighted fork-density count."""
    if not 0.0 < epsilon < 0.25:
        raise ValueError("epsilon must lie in (0, 1/4)")
    A = 0.5 * sqrt(1.0 - 4.0 * epsilon) * (2.0 - epsilon) / (1.0 - epsilon)
    if not 0.0 < A < 1.0:
        raise AssertionError("the fork-density contraction constant must lie in (0,1)")
    alpha = -log(A) / (2.0 * log(1.0 / epsilon))
    return ForkDensityParameters(epsilon=epsilon, A=A, alpha=alpha)


def replacement_fiber_multiplicities(
    outputs: Mapping[tuple[Vertex, Vertex], Edge],
) -> dict[tuple[Edge, int], int]:
    """Count replacement-box preimages by output edge and codimension class.

    The class is the number (0, 1, or 2) of replacement coordinates contained
    in the output edge. Mathematical applications with a private base edge
    should have no class-0 outputs; class 2 has multiplicity at most 1 and class
    1 at most the block size.
    """
    counts: dict[tuple[Edge, int], int] = {}
    for (u, v), edge in outputs.items():
        contained = int(u in edge) + int(v in edge)
        key = (edge, contained)
        counts[key] = counts.get(key, 0) + 1
    return counts
