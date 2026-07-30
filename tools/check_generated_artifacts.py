#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from hypergraph_il.artifacts import SOURCE_COMMIT, validate_artifact
from hypergraph_il.q0015 import run_regressions

BASELINE = ROOT / "evidence/experiments/q0015/baselines/q0015_audit_results.json"
ROUTE_B_BASELINE = ROOT / "evidence/experiments/route_b/baselines/route_b_lp_atlas_validation.json"


def main() -> int:
    errors: list[str] = []
    if not BASELINE.exists():
        errors.append(f"missing generated artifact: {BASELINE.relative_to(ROOT)}")
    else:
        try:
            value = json.loads(BASELINE.read_text(encoding="utf-8"))
            validate_artifact(value)
            metadata = value["metadata"]
            if metadata.get("source_commit") != SOURCE_COMMIT:
                errors.append("baseline source commit is not locked to the project baseline")
            if metadata.get("generator") != "tools/regenerate_baseline.py":
                errors.append("baseline generator is not tools/regenerate_baseline.py")
            if metadata.get("result_type") != "exhaustive-regression":
                errors.append("baseline is not labelled exhaustive-regression")
            expected_payload = json.loads(json.dumps({"regressions": run_regressions()}, ensure_ascii=False))
            if value.get("payload") != expected_payload:
                errors.append("baseline payload differs from a fresh deterministic regression run")
        except Exception as exc:
            errors.append(f"{BASELINE.relative_to(ROOT)}: {exc}")
    if not ROUTE_B_BASELINE.exists():
        errors.append(f"missing generated artifact: {ROUTE_B_BASELINE.relative_to(ROOT)}")
    else:
        try:
            value = json.loads(ROUTE_B_BASELINE.read_text(encoding="utf-8"))
            validate_artifact(value)
            metadata = value["metadata"]
            payload = value["payload"]
            if metadata.get("generator") != "enumerate/route_b_lp_atlas_validation.py":
                errors.append("Route-B baseline generator mismatch")
            if metadata.get("result_type") != "mixed-exhaustive-and-bounded-random":
                errors.append("Route-B baseline result type mismatch")
            expected_q4 = {
                "block_minimal": 50524,
                "multi_blocker_M": 50256,
                "nonnormal_N": 260,
                "normal_Q4": 8,
                "not_block_minimal": 4,
                "star_forests_total": 50528,
            }
            if payload.get("q4_star_forests") != expected_q4:
                errors.append("Route-B exhaustive Q4 star-forest payload mismatch")
            policy = payload.get("normal_q4_release_policies", {})
            if policy.get("coordinate_perfect_matchings") != 272 or policy.get("normal_matchings") != 8:
                errors.append("Route-B normal-Q4 matching counts mismatch")
            parameters = metadata.get("parameters", {})
            if parameters.get("exact") != 200 or parameters.get("general4") != 200 or parameters.get("general5") != 50:
                errors.append("Route-B committed bounded-search parameters changed")
        except Exception as exc:
            errors.append(f"{ROUTE_B_BASELINE.relative_to(ROOT)}: {exc}")
    if errors:
        print("Generated artifact errors:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("generated artifact checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
