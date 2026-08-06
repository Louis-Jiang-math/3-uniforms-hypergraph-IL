from __future__ import annotations

import math

import pytest

from hypergraph_il.route_b_closure import (
    classify_fresh_compatible_atom,
    three_slot_continuation_ratio,
    three_slot_remainder_bound,
)


def test_f0073_priority_split() -> None:
    assert classify_fresh_compatible_atom(
        certified_exit=True,
        edge_is_new=True,
        support_is_new=True,
        token_is_new=False,
    ) == "exit"
    assert classify_fresh_compatible_atom(
        certified_exit=False,
        edge_is_new=True,
        support_is_new=True,
        token_is_new=True,
    ) == "edge"
    assert classify_fresh_compatible_atom(
        certified_exit=False,
        edge_is_new=False,
        support_is_new=True,
        token_is_new=True,
    ) == "support"
    assert classify_fresh_compatible_atom(
        certified_exit=False,
        edge_is_new=False,
        support_is_new=False,
        token_is_new=True,
    ) == "token"


def test_f0073_rejects_repeat_inside_phi() -> None:
    with pytest.raises(ValueError, match="first-token"):
        classify_fresh_compatible_atom(
            certified_exit=False,
            edge_is_new=False,
            support_is_new=False,
            token_is_new=False,
        )


def test_f0074_continuation_ratio_and_remainder() -> None:
    block_size = 101
    epsilon = 0.03
    maximum_degree = (0.25 - epsilon) * block_size**2
    ratio = three_slot_continuation_ratio(block_size, maximum_degree)
    assert ratio < 0.25 - epsilon / 2

    initial_mass = 0.8
    for generations in range(6):
        expected = initial_mass * ratio**generations
        assert math.isclose(
            three_slot_remainder_bound(
                initial_mass,
                block_size,
                maximum_degree,
                generations,
            ),
            expected,
        )


def test_f0074_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        three_slot_continuation_ratio(1, 0.0)
    with pytest.raises(ValueError):
        three_slot_continuation_ratio(2, -1.0)
    with pytest.raises(ValueError):
        three_slot_remainder_bound(-0.1, 3, 1.0, 1)
    with pytest.raises(ValueError):
        three_slot_remainder_bound(0.1, 3, 1.0, -1)
