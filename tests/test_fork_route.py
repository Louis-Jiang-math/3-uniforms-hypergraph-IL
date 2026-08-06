from __future__ import annotations

import math

from hypergraph_il.fork_route import (
    canonical_matching_repair,
    fork_density_parameters,
    fork_free_growth_rate,
    replacement_fiber_multiplicities,
    unrestricted_matching_growth_rate,
)
from hypergraph_il.models import Hypergraph, canonical_edge


def test_matching_number_one_hits_many_overlapping_blockers() -> None:
    x = (0, 0)
    a, b, c = (1, 0), (2, 0), (3, 0)
    hypergraph = Hypergraph.build(
        m=4,
        b=2,
        edges=[{x, a, b}, {x, a, c}],
    )
    repair = canonical_matching_repair(hypergraph, [a, b, c], x)
    assert repair.rank == 1
    assert repair.fork_excess == 0
    assert hypergraph.is_independent(repair.state_after)
    assert x in repair.state_after


def test_disjoint_blockers_create_fork_excess() -> None:
    x = (0, 0)
    a, b, c, d = (1, 0), (2, 0), (3, 0), (4, 0)
    hypergraph = Hypergraph.build(
        m=5,
        b=2,
        edges=[{x, a, b}, {x, c, d}],
    )
    repair = canonical_matching_repair(hypergraph, [a, b, c, d], x)
    assert repair.rank == 2
    assert repair.fork_excess == 1
    assert repair.state_after == (x,)


def test_growth_constants_recover_one_quarter_and_four_twenty_sevenths() -> None:
    b = 100.0
    assert math.isclose(fork_free_growth_rate(b * b / 4.0), b)
    assert math.isclose(unrestricted_matching_growth_rate(4.0 * b * b / 27.0), b)


def test_fork_density_parameters_are_positive() -> None:
    for epsilon in (0.001, 0.01, 0.05, 0.2):
        parameters = fork_density_parameters(epsilon)
        assert 0.0 < parameters.A < 1.0
        assert parameters.alpha > 0.0


def test_replacement_box_fiber_classes() -> None:
    u0, u1 = (1, 0), (1, 1)
    v0, v1 = (2, 0), (2, 1)
    p, q = (3, 0), (4, 0)
    outputs = {
        (u0, v0): canonical_edge({u0, v0, p}),
        (u0, v1): canonical_edge({u0, p, q}),
        (u1, v0): canonical_edge({u1, p, q}),
        (u1, v1): canonical_edge({u1, v1, q}),
    }
    counts = replacement_fiber_multiplicities(outputs)
    assert max(count for (edge, cls), count in counts.items() if cls == 2) == 1
    assert max(count for (edge, cls), count in counts.items() if cls == 1) <= 2
