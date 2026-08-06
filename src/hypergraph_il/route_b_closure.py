from __future__ import annotations

from itertools import permutations, product
from typing import Mapping, Sequence


def canonical_excess(
    loads: Mapping[object, float],
    capacities: Mapping[object, float],
) -> float:
    """Return the positive-part excess of a no-copy canonical edge partition."""

    keys = set(loads) | set(capacities)
    if any(loads.get(key, 0.0) < 0.0 for key in keys):
        raise ValueError("loads must be nonnegative")
    if any(capacities.get(key, 0.0) < 0.0 for key in keys):
        raise ValueError("capacities must be nonnegative")
    return sum(max(loads.get(key, 0.0) - capacities.get(key, 0.0), 0.0) for key in keys)


def critical_deficit(profile: Sequence[float]) -> float:
    """Return the F-0038 critical deficit."""

    n = len(profile)
    if n < 2:
        raise ValueError("profile must contain at least two coordinates")
    if any(value < 0.0 or value > 1.0 for value in profile):
        raise ValueError("profile entries must lie in [0, 1]")
    total = sum(profile)
    nonbinary = sum(value * (1.0 - value) for value in profile)
    return (
        (n - 2.0 * total) ** 2 / (4.0 * n * (n - 1))
        + nonbinary / (n * (n - 1))
    )


def rounded_cross_mismatch(profile: Sequence[float]) -> float:
    """Return normalized ordered-cross mass incompatible with rounded 1->0 routing."""

    n = len(profile)
    if n < 2:
        raise ValueError("profile must contain at least two coordinates")
    if any(value < 0.0 or value > 1.0 for value in profile):
        raise ValueError("profile entries must lie in [0, 1]")
    rounded = tuple(value >= 0.5 for value in profile)
    return sum(
        profile[i] * (1.0 - profile[j])
        for i in range(n)
        for j in range(n)
        if i != j and not (rounded[i] and not rounded[j])
    ) / (n * (n - 1))


def switch_cube_bad_preimage_bound(block_size: int) -> int:
    """Maximum instructions assigned to one first-nonliteral context-slot."""

    if block_size < 2:
        raise ValueError("block size must be at least two")
    return 6 * (block_size - 1) ** 2


def switch_cube_degree_lower_bound(block_size: int, nonliteral_density: float) -> float:
    """Return the F-0071 lower bound for maximum degree."""

    if block_size < 2:
        raise ValueError("block size must be at least two")
    if nonliteral_density < 0.0 or nonliteral_density > 1.0:
        raise ValueError("density must lie in [0, 1]")
    return max(1.0 - 3.0 * nonliteral_density, 0.0) * (block_size - 1) ** 3 / block_size


def enumerate_literal_prefix_preimages(
    block_size: int,
    context: tuple[int, int, int],
    slot_block: int,
    target: int,
    position: int,
) -> int:
    """Brute-force the purely combinatorial preimage count used in F-0071.

    Prior steps are treated as literal coordinate overwrites.  The function is
    for regression tests; the proof uses the direct reconstruction argument.
    """

    if block_size < 2:
        raise ValueError("block size must be at least two")
    if len(context) != 3 or any(value not in range(block_size) for value in context):
        raise ValueError("context must be a three-coordinate block tuple")
    if slot_block not in range(3):
        raise ValueError("slot_block must be 0, 1, or 2")
    if target not in range(block_size) or target == context[slot_block]:
        raise ValueError("target must differ from the current slot endpoint")
    if position not in (1, 2, 3):
        raise ValueError("position must be 1, 2, or 3")

    count = 0
    for root in product(range(block_size), repeat=3):
        for targets in product(range(block_size), repeat=3):
            if any(targets[index] == root[index] for index in range(3)):
                continue
            for order in permutations(range(3)):
                current = list(root)
                for step, coordinate in enumerate(order, start=1):
                    if (
                        step == position
                        and tuple(current) == context
                        and coordinate == slot_block
                        and targets[coordinate] == target
                    ):
                        count += 1
                    current[coordinate] = targets[coordinate]
    return count


def classify_fresh_compatible_atom(
    *,
    certified_exit: bool,
    edge_is_new: bool,
    support_is_new: bool,
    token_is_new: bool,
) -> str:
    """Return the F-0073 priority class of one compatible fresh atom.

    The function mirrors the measure-theoretic priority split.  A genuinely
    fresh atom must have ``token_is_new=True`` unless it is routed to a named
    exit before the resource classification is evaluated.
    """

    if certified_exit:
        return "exit"
    if not token_is_new:
        raise ValueError("F-0073 applies only to first-token atoms")
    if edge_is_new:
        return "edge"
    if support_is_new:
        return "support"
    return "token"


def three_slot_continuation_ratio(block_size: int, maximum_degree: float) -> float:
    """Return the F-0074 pointwise pure-token continuation ratio."""

    if block_size < 2:
        raise ValueError("block size must be at least two")
    if maximum_degree < 0.0:
        raise ValueError("maximum degree must be nonnegative")
    return block_size * maximum_degree / (block_size - 1) ** 3


def three_slot_remainder_bound(
    initial_mass: float,
    block_size: int,
    maximum_degree: float,
    generations: int,
) -> float:
    """Return the geometric remainder bound in F-0074."""

    if initial_mass < 0.0:
        raise ValueError("initial mass must be nonnegative")
    if generations < 0:
        raise ValueError("generations must be nonnegative")
    ratio = three_slot_continuation_ratio(block_size, maximum_degree)
    return initial_mass * ratio**generations


def finite_resource_remainder_bound(
    initial_mass: float,
    continuation_ratio: float,
    resource_budget: int,
    transitions: int,
) -> float:
    """Return the F-0075 polynomial-geometric unresolved-mass bound."""

    from math import comb

    if initial_mass < 0.0:
        raise ValueError("initial_mass must be nonnegative")
    if continuation_ratio < 0.0 or continuation_ratio > 1.0:
        raise ValueError("continuation_ratio must lie in [0, 1]")
    if resource_budget < 0:
        raise ValueError("resource_budget must be nonnegative")
    if transitions < 0:
        raise ValueError("transitions must be nonnegative")
    return initial_mass * sum(
        comb(transitions, r) * continuation_ratio ** (transitions - r)
        for r in range(min(resource_budget, transitions) + 1)
    )


def switch_defect_core_factor(
    block_size: int,
    epsilon: float,
) -> float:
    """Return the F-0071 defect density factor alpha_{b,epsilon}."""

    if block_size < 2:
        raise ValueError("block_size must be at least two")
    if epsilon < 0.0 or epsilon >= 0.25:
        raise ValueError("epsilon must lie in [0, 1/4)")
    return (
        1.0
        - (0.25 - epsilon) * (block_size / (block_size - 1.0)) ** 3
    ) / 6.0


def rounding_free_cross_reduction(chart_mis: float, first_mass: float, return_mass: float) -> float:
    """Exact mass identity for the rounding-free assigned actual-cross split."""
    values = (chart_mis, first_mass, return_mass)
    if any(value < 0 for value in values):
        raise ValueError("cross masses must be nonnegative")
    return sum(values)


def half_profile_rounding_ratio(n: int) -> float:
    """Mismatch/deficit ratio for a_i=1/2 under deterministic threshold rounding."""
    if n < 2:
        raise ValueError("n must be at least 2")
    mismatch = 0.25
    deficit = 1.0 / (4.0 * (n - 1))
    return mismatch / deficit
