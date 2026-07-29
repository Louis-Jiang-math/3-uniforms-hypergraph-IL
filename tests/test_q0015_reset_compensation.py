import pytest

from hypergraph_il.models import canonical_edge
from hypergraph_il.q0015_reset import (
    BlockingObligationState,
    OneHoleState,
    build_one_hole_obligation_graph,
    exhaustive_reset_compensation_summary,
    find_immediate_reset_counterexample,
    minimal_reset_counterexample,
    run_reset_compensation_experiment,
)


def test_minimal_reset_counterexample_uses_three_orientations() -> None:
    witness = minimal_reset_counterexample()

    assert witness["path_length"] == 3
    assert witness["edges"] == [[[0, 0], [1, 0], [2, 0]]]
    path = witness["path"]
    assert [state["hole_block"] for state in path] == [0, 1, 2]
    assert len(
        {
            tuple(map(tuple, state["blocker_edge"]))
            for state in path
        }
    ) == 1
    assert len(
        {
            tuple(map(tuple, state["carrier_pair"]))
            for state in path
        }
    ) == 3


def test_all_nonempty_three_block_models_refute_immediate_reset() -> None:
    assert exhaustive_reset_compensation_summary() == {
        "tested_hypergraphs": 256,
        "counterexamples": 255,
        "non_counterexamples": 1,
    }


def test_reset_experiment_payload_is_deterministic() -> None:
    assert run_reset_compensation_experiment() == (
        run_reset_compensation_experiment()
    )


def test_reset_search_rejects_invalid_depth_and_adjacency() -> None:
    edge = canonical_edge(((0, 0), (1, 0), (2, 0)))
    obligation = BlockingObligationState(
        state=OneHoleState(
            hole_block=0,
            selected=frozenset(((1, 0), (2, 0))),
        ),
        test_vertex=(0, 0),
        blocker_edge=edge,
    )

    with pytest.raises(ValueError, match="at least two"):
        find_immediate_reset_counterexample(
            (obligation,),
            ((),),
            max_depth=1,
        )
    with pytest.raises(ValueError, match="one row"):
        find_immediate_reset_counterexample(
            (obligation,),
            (),
        )
