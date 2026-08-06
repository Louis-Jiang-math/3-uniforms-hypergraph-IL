from __future__ import annotations

from itertools import product
import math

from hypergraph_il.route_b_closure import (
    canonical_excess,
    critical_deficit,
    enumerate_literal_prefix_preimages,
    rounded_cross_mismatch,
    switch_cube_bad_preimage_bound,
    switch_cube_degree_lower_bound,
)


def test_canonical_excess_is_exact_positive_part_remainder() -> None:
    loads = {"e0": 0.4, "e1": 0.35, "e2": 0.25}
    capacities = {"e0": 0.3, "e1": 0.5, "e2": 0.1}
    excess = canonical_excess(loads, capacities)
    assert math.isclose(excess, 0.25)
    assert sum(loads.values()) <= sum(capacities.values()) + excess + 1e-12


def test_rounded_cross_mismatch_bound_exhaustive_grid() -> None:
    grid = (0.0, 0.25, 0.5, 0.75, 1.0)
    for n in range(2, 7):
        for profile in product(grid, repeat=n):
            mismatch = rounded_cross_mismatch(profile)
            bound = 2.0 * (n - 1) * critical_deficit(profile)
            assert mismatch <= bound + 1e-12


def test_switch_cube_first_bad_preimage_bound_is_sharp() -> None:
    for block_size in (2, 3, 4):
        context = (0, 0, 0)
        for position in (1, 2, 3):
            count = enumerate_literal_prefix_preimages(
                block_size,
                context,
                slot_block=0,
                target=1,
                position=position,
            )
            assert count == 2 * (block_size - 1) ** 2
        assert 3 * count == switch_cube_bad_preimage_bound(block_size)


def test_switch_cube_degree_bound_uses_positive_part() -> None:
    assert math.isclose(switch_cube_degree_lower_bound(5, 0.0), 64 / 5)
    assert switch_cube_degree_lower_bound(5, 1 / 3) == 0.0
    assert switch_cube_degree_lower_bound(5, 0.9) == 0.0
