from __future__ import annotations

from dataclasses import dataclass
from math import prod
from typing import Hashable, Iterable, Mapping, Sequence

import networkx as nx

Vertex = Hashable
Edge = frozenset[Vertex]


@dataclass(frozen=True)
class HistoryTransition:
    """A faithful finite transition used by the reduced history audit."""

    transition_id: Hashable
    source: Hashable
    target: Hashable
    blocker_edge: Hashable
    certified: bool = False


def legal_release_vertices(
    blockers: Iterable[Edge],
    attempted_vertex: Vertex,
) -> frozenset[Vertex]:
    """Return the old endpoints whose deletion destroys every blocker.

    The caller supplies the complete blocker family after inserting
    ``attempted_vertex`` into an independent one-hole state. Every blocker must
    contain the attempted vertex. A release is legal exactly when it belongs to
    every blocker.
    """

    blocker_list = tuple(blockers)
    if not blocker_list:
        return frozenset()
    if any(attempted_vertex not in edge for edge in blocker_list):
        raise ValueError("every blocker must contain the attempted vertex")
    old_endpoint_sets = [set(edge) - {attempted_vertex} for edge in blocker_list]
    return frozenset(set.intersection(*old_endpoint_sets))


def wide_fan_product_bound(fiber_sizes: Sequence[int]) -> int:
    """Product-space count of supports with at least three good coordinates.

    Each coordinate has ``d_i`` good choices and one is counting only the
    all-good choices in the five-block case (three remaining coordinates).
    The general Poisson-binomial form additionally needs ambient coordinate
    sizes; this helper is the exact five-block form used in the audit.
    """

    if len(fiber_sizes) != 3:
        raise ValueError("the exact product helper expects three remaining blocks")
    if any(value < 0 for value in fiber_sizes):
        raise ValueError("fiber sizes must be nonnegative")
    return prod(fiber_sizes)


def critical_deficit(profile: Sequence[float]) -> float:
    """Return the exact F-0038 critical deficit for a finite profile."""

    n = len(profile)
    if n < 2:
        raise ValueError("profile must contain at least two coordinates")
    if any(value < 0.0 or value > 1.0 for value in profile):
        raise ValueError("profile entries must lie in [0, 1]")
    total = sum(profile)
    imbalance = n - 2.0 * total
    nonbinary = sum(value * (1.0 - value) for value in profile)
    return (
        imbalance * imbalance / (4.0 * n * (n - 1))
        + nonbinary / (n * (n - 1))
    )


def cross_mass(profile: Sequence[float]) -> float:
    """Return the ordered continuation/termination cross mass."""

    n = len(profile)
    if n < 2:
        raise ValueError("profile must contain at least two coordinates")
    if any(value < 0.0 or value > 1.0 for value in profile):
        raise ValueError("profile entries must lie in [0, 1]")
    return sum(
        profile[i] * (1.0 - profile[j])
        for i in range(n)
        for j in range(n)
        if i != j
    ) / (n * (n - 1))


def reduced_history_graph(
    transitions: Iterable[HistoryTransition],
) -> nx.DiGraph:
    """Build the residual edge-history graph.

    Certified transitions are removed. The remaining vertices are actual
    transitions. Consecutive moves are adjacent only when the target/source
    states agree and the actual blocker-edge identities differ. Thus a local
    same-edge release oscillation is not a residual cycle.
    """

    active = tuple(transition for transition in transitions if not transition.certified)
    graph = nx.DiGraph()
    graph.add_nodes_from(transition.transition_id for transition in active)
    by_source: dict[Hashable, list[HistoryTransition]] = {}
    for transition in active:
        by_source.setdefault(transition.source, []).append(transition)
    for left in active:
        for right in by_source.get(left.target, []):
            if left.blocker_edge != right.blocker_edge:
                graph.add_edge(left.transition_id, right.transition_id)
    return graph


def has_residual_cycle(transitions: Iterable[HistoryTransition]) -> bool:
    """Return whether an uncertified multi-edge residual circulation exists."""

    return not nx.is_directed_acyclic_graph(reduced_history_graph(transitions))


def stable_partition(
    signatures_k: Mapping[Hashable, Hashable],
    signatures_k1: Mapping[Hashable, Hashable],
) -> bool:
    """Check whether depth-k equality already determines depth-(k+1) equality."""

    if signatures_k.keys() != signatures_k1.keys():
        raise ValueError("signature maps must have the same domain")
    grouped: dict[Hashable, Hashable] = {}
    for state, signature in signatures_k.items():
        next_signature = signatures_k1[state]
        previous = grouped.setdefault(signature, next_signature)
        if previous != next_signature:
            return False
    return True
