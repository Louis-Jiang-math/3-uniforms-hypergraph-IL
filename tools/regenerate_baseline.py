#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from hypergraph_il.artifacts import atomic_write_json, build_artifact
from hypergraph_il.q0015 import run_regressions


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "evidence/experiments/q0015/baselines/q0015_audit_results.json",
    )
    parser.add_argument("--generated-at", default="2026-07-28T00:00:00Z")
    args = parser.parse_args()

    payload = {"regressions": run_regressions()}
    artifact = build_artifact(
        payload,
        artifact_type="experiment-baseline",
        result_type="exhaustive-regression",
        generator="tools/regenerate_baseline.py",
        command=(
            "python tools/regenerate_baseline.py --generated-at "
            f"{args.generated_at} --output {args.output.relative_to(ROOT) if args.output.is_relative_to(ROOT) else args.output}"
        ),
        parameters={"generated_at": args.generated_at},
        scope="F-0029 public regression family over all 24 block orders",
        generated_at=args.generated_at,
    )
    atomic_write_json(args.output, artifact)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
