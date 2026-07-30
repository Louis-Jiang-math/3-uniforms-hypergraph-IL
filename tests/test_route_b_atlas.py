from __future__ import annotations

import math

from hypergraph_il.route_b_atlas import (
    HistoryTransition,
    critical_deficit,
    cross_mass,
    has_residual_cycle,
    legal_release_vertices,
    stable_partition,
    wide_fan_product_bound,
)


def test_competing_blockers_have_at_most_one_legal_release() -> None:
    x, r, p, q = "x", "r", "p", "q"
    blockers = (frozenset({x, r, p}), frozenset({x, r, q}))
    assert legal_release_vertices(blockers, x) == frozenset({r})


def test_deadlock_has_no_common_release() -> None:
    x, a, b, c, d = "x", "a", "b", "c", "d"
    blockers = (frozenset({x, a, b}), frozenset({x, c, d}))
    assert legal_release_vertices(blockers, x) == frozenset()


def test_wide_fan_five_block_bound() -> None:
    assert wide_fan_product_bound((2, 3, 4)) == 24


def test_critical_deficit_identity() -> None:
    profile = (0.0, 0.25, 0.75, 1.0)
    n = len(profile)
    lhs = n / (4 * (n - 1)) - cross_mass(profile)
    assert math.isclose(lhs, critical_deficit(profile), abs_tol=1e-12)


def test_same_edge_release_cycle_is_removed() -> None:
    transitions = (
        HistoryTransition("a", "s0", "s1", "e"),
        HistoryTransition("b", "s1", "s0", "e"),
    )
    assert not has_residual_cycle(transitions)


def test_multi_edge_cycle_survives() -> None:
    transitions = (
        HistoryTransition("a", "s0", "s1", "e0"),
        HistoryTransition("b", "s1", "s0", "e1"),
    )
    assert has_residual_cycle(transitions)


def test_certified_transition_breaks_residual_cycle() -> None:
    transitions = (
        HistoryTransition("a", "s0", "s1", "e0", certified=True),
        HistoryTransition("b", "s1", "s0", "e1"),
    )
    assert not has_residual_cycle(transitions)


def test_partition_stability() -> None:
    signatures_k = {"u": 0, "v": 0, "w": 1}
    assert stable_partition(signatures_k, {"u": "a", "v": "a", "w": "b"})
    assert not stable_partition(signatures_k, {"u": "a", "v": "c", "w": "b"})


def test_four_tool_dynamic_deadlock_counterexample() -> None:
    from collections import deque
    from itertools import product

    edges = tuple(
        frozenset(edge)
        for edge in [
            ((0, 0), (1, 0), (4, 1)),
            ((0, 0), (1, 1), (4, 1)),
            ((0, 0), (2, 1), (4, 0)),
            ((0, 0), (3, 0), (4, 0)),
            ((0, 1), (1, 1), (4, 0)),
            ((0, 1), (2, 0), (4, 1)),
            ((0, 1), (3, 1), (4, 0)),
            ((1, 0), (3, 0), (4, 0)),
            ((2, 0), (3, 1), (4, 0)),
            ((2, 1), (3, 0), (4, 1)),
            ((2, 1), (3, 1), (4, 1)),
        ]
    )

    def vertices(state):
        return {(block, value) for block, value in enumerate(state) if value is not None}

    def independent(state):
        selected = vertices(state)
        return not any(edge <= selected for edge in edges)

    states = []
    for missing in range(5):
        for values in product((0, 1), repeat=4):
            iterator = iter(values)
            state = tuple(None if block == missing else next(iterator) for block in range(5))
            if independent(state):
                states.append(state)
    state_set = set(states)

    def successors(state):
        missing = state.index(None)
        output = set()
        for attempted_value in (0, 1):
            full_values = list(state)
            full_values[missing] = attempted_value
            full = {(block, value) for block, value in enumerate(full_values)}
            attempted = (missing, attempted_value)
            blockers = [edge for edge in edges if edge <= full]
            for blocker in blockers:
                for released in blocker - {attempted}:
                    target = list(full_values)
                    target[released[0]] = None
                    target_state = tuple(target)
                    if target_state in state_set:
                        output.add(target_state)
        return output

    start = (1, 1, 0, 1, None)
    queue = deque([start])
    reached = {start}
    while queue:
        state = queue.popleft()
        for target in successors(state):
            if target not in reached:
                reached.add(target)
                queue.append(target)

    masks = set()
    for state in reached:
        if state.index(None) != 4:
            continue
        mask = sum((state[block] != start[block]) << block for block in range(4))
        masks.add(mask)
    assert masks == set(range(15))

    deadlock = (0, 0, 1, 0, None)
    assert deadlock in state_set
    assert successors(deadlock) == set()
