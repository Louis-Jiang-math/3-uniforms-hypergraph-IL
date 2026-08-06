import pytest

from hypergraph_il.route_b_closure import (
    half_profile_rounding_ratio,
    rounding_free_cross_reduction,
)


def test_rounding_free_cross_identity():
    assert rounding_free_cross_reduction(0.2, 0.3, 0.1) == pytest.approx(0.6)


def test_rounding_free_cross_rejects_negative_mass():
    with pytest.raises(ValueError):
        rounding_free_cross_reduction(-0.1, 0.2, 0.3)


@pytest.mark.parametrize("n", [2, 3, 4, 8, 20])
def test_half_profile_rounding_loss_is_dimension_dependent(n):
    assert half_profile_rounding_ratio(n) == pytest.approx(n - 1)
