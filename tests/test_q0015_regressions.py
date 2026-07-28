from hypergraph_il.q0015 import run_regressions


def test_public_regression_baseline() -> None:
    result = run_regressions()
    assert result["eight_edge_model"] == {
        "independent_transversal": None,
        "no_IT": True,
        "max_degree": 3,
        "edge_minimal_no_IT": True,
        "block_minimal_no_IT": True,
    }
    assert result["all_24_orders"]["root_groups_with_failures"] == 144
    assert result["all_24_orders"]["classification"] == {
        "zero-error-budget-feasible": 48,
        "positive-root-budget-gap": 48,
        "no-configuration": 48,
    }
    specified = result["specified_window"]
    assert specified["obligation_count"] == 2
    assert abs(specified["budget_lp"]["t_min"] - 2.0) < 1e-8
    assert abs(specified["fixed_half_budget_flow"]["max_flow"] - 1.0) < 1e-8
    assert abs(specified["global_real_edge_flow"]["max_flow"] - 2.0) < 1e-8
    assert abs(result["nine_edge_repair"]["budget_lp"]["eta"]) < 1e-8


def test_genealogy_merge_is_detected() -> None:
    collision = run_regressions()["genealogy_collision"]
    assert collision["root_A_t_min"] == 1.0
    assert collision["root_B_t_min"] == 1.0
    assert collision["incorrectly_merged_t_min"] == 2.0
    assert collision["incorrectly_merged_eta"] == 1.0


def test_regression_output_is_deterministic() -> None:
    assert run_regressions() == run_regressions()
