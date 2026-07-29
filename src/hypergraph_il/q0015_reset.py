from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from itertools import combinations, product
from typing import Dict, List, Optional, Sequence, Tuple

from .models import Edge, Vertex, canonical_edge


@dataclass(frozen=True)
class OneHoleState:
    """An independent partial transversal with one empty block."""

    hole_block: int
    selected: frozenset[Vertex]


@dataclass(frozen=True)
class BlockingObligationState:
    """A tested hole vertex together with one actual blocker edge."""

    state: OneHoleState
    test_vertex: Vertex
    blocker_edge: Edge

    @property
    def carrier_pair(self) -> frozenset[Vertex]:
        return frozenset(self.blocker_edge - {self.test_vertex})


def all_transversal_edges(
    block_count: int,
    block_size: int,
) -> Tuple[Edge, ...]:
    """Return every triple using three distinct blocks."""

    if block_count < 3 or block_size <= 0:
        return ()
    edges: List[Edge] = []
    for block_triple in combinations(range(block_count), 3):
        for choices in product(range(block_size), repeat=3):
            edges.append(
                canonical_edge(
                    (block_triple[index], choices[index])
                    for index in range(3)
                )
            )
    return tuple(edges)


def build_one_hole_obligation_graph(
    block_count: int,
    block_size: int,
    edges: Sequence[Edge],
) -> Tuple[
    Tuple[BlockingObligationState, ...],
    Tuple[Tuple[int, ...], ...],
]:
    """Enumerate actual one-hole blocker states and legal hole moves."""

    edge_set = set(edges)
    states: List[OneHoleState] = []
    for hole_block in range(block_count):
        occupied_blocks = [
            block for block in range(block_count) if block != hole_block
        ]
        for choices in product(
            range(block_size),
            repeat=len(occupied_blocks),
        ):
            selected = frozenset(
                (occupied_blocks[index], choices[index])
                for index in range(len(occupied_blocks))
            )
            if not any(edge <= selected for edge in edge_set):
                states.append(OneHoleState(hole_block, selected))

    obligations: List[BlockingObligationState] = []
    obligations_by_state: Dict[OneHoleState, List[int]] = defaultdict(list)
    for state in states:
        for index in range(block_size):
            test_vertex = (state.hole_block, index)
            extended = frozenset(set(state.selected) | {test_vertex})
            for edge in edge_set:
                if test_vertex in edge and edge <= extended:
                    obligation_id = len(obligations)
                    obligations.append(
                        BlockingObligationState(
                            state=state,
                            test_vertex=test_vertex,
                            blocker_edge=edge,
                        )
                    )
                    obligations_by_state[state].append(obligation_id)

    adjacency: List[List[int]] = [[] for _ in obligations]
    for obligation_id, obligation in enumerate(obligations):
        for released_vertex in obligation.carrier_pair:
            new_selected = frozenset(
                (set(obligation.state.selected) - {released_vertex})
                | {obligation.test_vertex}
            )
            if any(edge <= new_selected for edge in edge_set):
                continue
            new_state = OneHoleState(released_vertex[0], new_selected)
            adjacency[obligation_id].extend(
                obligations_by_state.get(new_state, ())
            )

    return (
        tuple(obligations),
        tuple(tuple(neighbours) for neighbours in adjacency),
    )


def _resource_encoding(
    obligations: Sequence[BlockingObligationState],
) -> Tuple[
    Tuple[int, ...],
    Tuple[int, ...],
    Tuple[Tuple[Vertex, ...], ...],
]:
    edge_list = sorted(
        {obligation.blocker_edge for obligation in obligations},
        key=lambda edge: tuple(sorted(edge)),
    )
    vertex_list = sorted(
        {
            vertex
            for obligation in obligations
            for vertex in obligation.carrier_pair
        }
    )
    edge_id = {edge: index for index, edge in enumerate(edge_list)}
    vertex_id = {
        vertex: index for index, vertex in enumerate(vertex_list)
    }

    edge_bits: List[int] = []
    support_masks: List[int] = []
    carrier_keys: List[Tuple[Vertex, ...]] = []
    for obligation in obligations:
        edge_bits.append(1 << edge_id[obligation.blocker_edge])
        support_mask = 0
        for vertex in obligation.carrier_pair:
            support_mask |= 1 << vertex_id[vertex]
        support_masks.append(support_mask)
        carrier_keys.append(tuple(sorted(obligation.carrier_pair)))
    return tuple(edge_bits), tuple(support_masks), tuple(carrier_keys)


def find_immediate_reset_counterexample(
    obligations: Sequence[BlockingObligationState],
    adjacency: Sequence[Sequence[int]],
    max_depth: int = 8,
) -> Optional[Tuple[int, ...]]:
    """Find a resource-free carrier reset entering a new labelled state."""

    if max_depth < 2:
        raise ValueError("max_depth must be at least two")
    if not obligations:
        return None
    if len(adjacency) != len(obligations):
        raise ValueError("adjacency must have one row per obligation")

    edge_bits, support_masks, carrier_keys = _resource_encoding(
        obligations
    )
    queue = deque()
    seen_augmented_states = set()

    for start in range(len(obligations)):
        augmented = (
            start,
            edge_bits[start],
            support_masks[start],
            1 << start,
        )
        queue.append((*augmented, (start,)))
        seen_augmented_states.add(augmented)

    while queue:
        current, seen_edges, seen_support, visited, path = queue.popleft()
        if len(path) >= max_depth:
            continue

        for next_id in adjacency[current]:
            if not (0 <= next_id < len(obligations)):
                raise ValueError(
                    "adjacency contains an invalid obligation id"
                )
            next_was_visited = bool(visited & (1 << next_id))
            resource_free_reset = (
                carrier_keys[current] != carrier_keys[next_id]
                and bool(seen_edges & edge_bits[next_id])
                and (support_masks[next_id] & ~seen_support) == 0
            )
            if resource_free_reset and not next_was_visited:
                return path + (next_id,)
            if next_was_visited:
                continue

            next_augmented = (
                next_id,
                seen_edges | edge_bits[next_id],
                seen_support | support_masks[next_id],
                visited | (1 << next_id),
            )
            if next_augmented in seen_augmented_states:
                continue
            seen_augmented_states.add(next_augmented)
            queue.append((*next_augmented, path + (next_id,)))

    return None


def _serialize_edge(edge: Edge) -> List[List[int]]:
    return [list(vertex) for vertex in sorted(edge)]


def _serialize_obligation(
    obligation: BlockingObligationState,
) -> Dict:
    return {
        "hole_block": obligation.state.hole_block,
        "selected": [
            list(vertex) for vertex in sorted(obligation.state.selected)
        ],
        "test_vertex": list(obligation.test_vertex),
        "blocker_edge": _serialize_edge(obligation.blocker_edge),
        "carrier_pair": _serialize_edge(obligation.carrier_pair),
    }


def minimal_reset_counterexample() -> Dict:
    """Return the exact one-edge, three-block orientation counterexample."""

    edges = (canonical_edge(((0, 0), (1, 0), (2, 0))),)
    obligations, adjacency = build_one_hole_obligation_graph(3, 2, edges)
    path = find_immediate_reset_counterexample(
        obligations,
        adjacency,
    )
    if path is None:
        raise AssertionError(
            "the canonical reset counterexample was not found"
        )
    return {
        "block_count": 3,
        "block_size": 2,
        "edges": [_serialize_edge(edge) for edge in edges],
        "path": [
            _serialize_obligation(obligations[obligation_id])
            for obligation_id in path
        ],
        "path_length": len(path),
    }


def exhaustive_reset_compensation_summary() -> Dict:
    """Test all 2^8 edge subsets for three blocks of size two."""

    candidates = all_transversal_edges(3, 2)
    counterexamples = 0
    for mask in range(1 << len(candidates)):
        edges = tuple(
            candidates[index]
            for index in range(len(candidates))
            if mask & (1 << index)
        )
        obligations, adjacency = build_one_hole_obligation_graph(
            3,
            2,
            edges,
        )
        if find_immediate_reset_counterexample(
            obligations,
            adjacency,
        ) is not None:
            counterexamples += 1

    total = 1 << len(candidates)
    return {
        "tested_hypergraphs": total,
        "counterexamples": counterexamples,
        "non_counterexamples": total - counterexamples,
    }


def run_reset_compensation_experiment() -> Dict:
    """Return the deterministic bounded-exhaustive reset experiment."""

    return {
        "schema_version": "q0015-reset-compensation-v1",
        "claim_attacked": (
            "no new blocker edge and no new carrier support imply immediate "
            "repetition of a full labelled blocker state"
        ),
        "minimal_counterexample": minimal_reset_counterexample(),
        "exhaustive_m3_b2": exhaustive_reset_compensation_summary(),
        "interpretation": (
            "Immediate reset closure is false. The sound replacement uses a "
            "future-compatible orientation budget: a resource-free reset "
            "either visits a new token or repeats a quotient token."
        ),
    }
