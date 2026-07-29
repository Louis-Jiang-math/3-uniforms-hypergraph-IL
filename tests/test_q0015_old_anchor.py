from itertools import permutations, product

import pytest

from hypergraph_il.execution import build_root_groups
from hypergraph_il.models import Hypergraph
from hypergraph_il.q0015 import (
    eight_edge_model,
    no_configuration_exit_certificate,
    old_anchor_profile_maximum,
    old_anchor_profile_score,
    old_anchor_profile_summary,
    old_anchor_temporal_certificate,
)


def mixed_blocker_no_configuration_model() -> Hypergraph:
    return Hypergraph.build(
        4,
        2,
        [
            ((0, 0), (2, 0), (3, 0)),
            ((0, 0), (1, 0), (3, 0)),
        ],
    )


def test_no_configuration_retypes_to_surviving_old_anchor() -> None:
    hg = mixed_blocker_no_configuration_model()
    group = next(
        group
        for group in build_root_groups(hg, (0, 1, 2, 3))
        if group.root_record.trace == ((0, 0), (1, 0))
        and group.success_block == 2
        and group.failure_block == 3
    )
    obligation = next(
        obligation
        for obligation in group.obligations
        if obligation.inserted_vertex == (2, 0)
        and obligation.attempted_vertex == (3, 0)
    )

    assert obligation.configurations == ()
    certificate = no_configuration_exit_certificate(
        hg,
        group,
        obligation,
    )
    assert certificate is not None
    data = certificate.as_dict()

    assert data["exit_type"] == "external-old-anchor-blocker"
    assert data["mass"] == obligation.weight
    assert data["first_real_edge"] == "{0_0,1_0,3_0}"
    assert data["payload"]["original_first_real_edge"] == (
        "{0_0,2_0,3_0}"
    )
    assert data["payload"]["ledger_charge"] is None


def test_eight_edge_no_configuration_obligations_all_retype() -> None:
    hg = eight_edge_model()
    count = 0
    mass = 0.0

    for order in permutations(range(4)):
        for group in build_root_groups(hg, order):
            for obligation in group.obligations:
                if obligation.configurations:
                    continue
                certificate = no_configuration_exit_certificate(
                    hg,
                    group,
                    obligation,
                )
                assert certificate is not None
                assert certificate.ledger is None
                count += 1
                mass += certificate.mass

    assert count == 96
    assert mass == 96.0


def test_profile_maximum_on_binary_corners() -> None:
    for n in range(2, 9):
        maximum = max(
            old_anchor_profile_score(profile)
            for profile in product((0.0, 1.0), repeat=n)
        )
        assert maximum == pytest.approx(
            old_anchor_profile_maximum(n)
        )


def test_profile_stability_identity() -> None:
    profile = (1.0, 0.75, 0.2, 0.0, 0.6)
    summary = old_anchor_profile_summary(profile)

    assert summary["stability_identity_residual"] < 1e-12
    assert abs(summary["imbalance"]) <= (
        summary["endpoint_bound"] + 1e-12
    )
    assert summary["polarization_defect"] >= 0.0


def test_temporal_certificate_has_sharp_one_step_example() -> None:
    certificate = old_anchor_temporal_certificate(
        profiles=[
            {"A": 1.0, "B": 1.0, "C": 0.0, "D": 0.0},
            {"B": 1.0, "C": 0.0, "D": 0.0},
        ],
        removed_blocks=["A"],
        tau=0.0,
    )

    assert certificate["status"] == "certified"
    assert certificate["weighted_temporal_holds"]
    assert certificate["lifespan_holds"]
    assert certificate["weighted_temporal_slack"] == pytest.approx(0.0)
    assert certificate["steps"][0]["survivor_drift"] == pytest.approx(
        0.0
    )


def test_temporal_certificate_rejects_profile_increase() -> None:
    with pytest.raises(ValueError, match="cannot increase"):
        old_anchor_temporal_certificate(
            profiles=[
                {"A": 1.0, "B": 0.5, "C": 0.0},
                {"B": 0.6, "C": 0.0},
            ],
            removed_blocks=["A"],
            tau=0.0,
        )
