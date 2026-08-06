from __future__ import annotations

import math

import pytest

from hypergraph_il.route_b_closure import (
    finite_resource_remainder_bound,
    switch_defect_core_factor,
)


def test_zero_resource_budget_is_geometric() -> None:
    assert finite_resource_remainder_bound(3.0, 0.2, 0, 4) == pytest.approx(3.0 * 0.2**4)


def test_remainder_matches_binomial_truncation() -> None:
    value = finite_resource_remainder_bound(2.0, 0.25, 2, 5)
    expected = 2.0 * sum(math.comb(5, r) * 0.25 ** (5 - r) for r in range(3))
    assert value == pytest.approx(expected)


def test_fixed_resource_remainder_tends_to_zero() -> None:
    values = [finite_resource_remainder_bound(1.0, 0.3, 4, length) for length in (20, 40, 80)]
    assert values[2] < values[1] < values[0]
    assert values[2] < 1e-30


def test_resource_budget_at_least_length_gives_trivial_binomial_bound() -> None:
    value = finite_resource_remainder_bound(1.0, 0.4, 10, 3)
    assert value == pytest.approx((1.0 + 0.4) ** 3)


def test_switch_defect_factor_positive_below_quarter() -> None:
    assert switch_defect_core_factor(1000, 0.01) > 0.12


def test_input_validation() -> None:
    with pytest.raises(ValueError):
        finite_resource_remainder_bound(-1.0, 0.2, 1, 1)
    with pytest.raises(ValueError):
        finite_resource_remainder_bound(1.0, 1.2, 1, 1)
    with pytest.raises(ValueError):
        switch_defect_core_factor(1, 0.01)
