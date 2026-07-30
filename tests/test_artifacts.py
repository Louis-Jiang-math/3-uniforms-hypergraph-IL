from __future__ import annotations

import json
from pathlib import Path

import pytest

from hypergraph_il.artifacts import atomic_write_json, build_artifact, validate_artifact
from hypergraph_il.cli import main


def test_artifact_payload_hash_detects_manual_edit() -> None:
    artifact = build_artifact(
        {"value": 1},
        artifact_type="experiment",
        result_type="exhaustive",
        generator="test",
        command="test",
        parameters={},
        scope="unit test",
        generated_at="2026-07-28T00:00:00Z",
    )
    validate_artifact(artifact)
    artifact["payload"]["value"] = 2
    with pytest.raises(ValueError, match="payload hash mismatch"):
        validate_artifact(artifact)


def test_atomic_write_json_replaces_complete_document(tmp_path: Path) -> None:
    target = tmp_path / "artifact.json"
    atomic_write_json(target, {"a": 1})
    atomic_write_json(target, {"b": 2})
    assert json.loads(target.read_text(encoding="utf-8")) == {"b": 2}
    assert not list(tmp_path.glob("*.tmp"))


def test_cli_writes_auditable_artifact(tmp_path: Path) -> None:
    assert main([
        "--regressions-only",
        "--output-dir", str(tmp_path),
        "--generated-at", "2026-07-28T00:00:00Z",
    ]) == 0
    value = json.loads((tmp_path / "q0015_audit_results.json").read_text(encoding="utf-8"))
    validate_artifact(value)
    assert value["metadata"]["result_type"] == "exhaustive-regression"
    assert value["payload"]["regressions"]["all_24_orders"]["root_groups_with_failures"] == 144


def test_cli_rejects_nonpositive_time_limit() -> None:
    with pytest.raises(SystemExit):
        main(["--time-limit", "0"])


def test_route_b_baseline_is_auditable() -> None:
    path = Path(__file__).resolve().parents[1] / "evidence/experiments/route_b/baselines/route_b_lp_atlas_validation.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    validate_artifact(value)
    assert value["metadata"]["result_type"] == "mixed-exhaustive-and-bounded-random"
    assert value["payload"]["q4_star_forests"]["normal_Q4"] == 8
    assert value["payload"]["b3_four_block_general_cover"]["classification"]["reduced_residual_cycle"] == 0
