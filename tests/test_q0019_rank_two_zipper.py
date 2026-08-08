from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "enumerate/q0019_rank_two_zipper_validation.py"

spec = importlib.util.spec_from_file_location("q0019_rank_two_zipper_validation", SCRIPT)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def normal_models():
    matchings = [module.with_directions(matching) for matching in module.enumerate_matchings(module.VERTICES)]
    return matchings, [matching for matching in matchings if module.is_normal(matching)]


def test_normal_q4_rank_two_geometry() -> None:
    matchings, normal = normal_models()
    payload = module.q4_payload(matchings, normal)
    assert payload["coordinate_perfect_matchings"] == 272
    assert payload["normal_matchings"] == 8
    assert payload["normal_rooted_states"] == 192
    assert payload["release_categories"] == {"C": 192, "S": 384, "R": 192}
    assert payload["minimum_nonnormal_root_defects"] == 6
    assert payload["splice_unique_bridge_order_count_distribution"] == {1: 384}
    assert payload["splice_edge_disjoint_cut_count_distribution"] == {7: 384}
    assert payload["source_tuple_support_multiplicity"] == {1: 192}
    assert payload["normal_support_overlap_graph_is_K4_4"] is True


def test_endpoint_and_codimension_profiles() -> None:
    _, normal = normal_models()
    q4 = module.q4_payload([module.with_directions(m) for m in module.enumerate_matchings(module.VERTICES)], normal)
    assert q4["endpoint_antipode_migration"] == {
        "(1, 0, 0, (0, 7), (3, 4))": 192
    }
    codimension = module.codimension_one_payload(normal)
    assert codimension["vertex_union_size_profile_endpoint_first_inward_central"] == {
        "(5, 7, 8)": 192
    }
    assert codimension["missing_vertex_profile_endpoint_first_inward_central"] == {
        "(3, 1, 0)": 192
    }


def test_committed_ternary_packing_certificate() -> None:
    artifact = json.loads(
        (ROOT / "evidence/experiments/q0019_rank_two/baselines/q0019_rank_two_zipper_validation.json")
        .read_text(encoding="utf-8")
    )
    payload = artifact["payload"]["ternary_supports"]
    assert payload["candidate_supports"] == 648
    assert payload["possible_actual_blocker_triples"] == 108
    assert payload["support_action_transitive"] is True
    assert payload["full_automorphism_orbit_size_of_fixed_support"] == 648
    assert payload["twelve_packing_feasible"] is True
    assert payload["thirteen_packing_infeasible"] is True
    assert payload["maximum_edge_disjoint_supports"] == 12
