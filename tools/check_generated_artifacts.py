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
    if errors:
        print("Generated artifact errors:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("generated artifact checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
