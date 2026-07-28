from __future__ import annotations

import argparse
import json
import shlex
import sys
from pathlib import Path

from .artifacts import atomic_write_json, build_artifact
from .q0015 import cutting_plane_outer_search, run_regressions


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Auditable Q-0015 configuration and ledger regressions")
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/runs/q0015"))
    parser.add_argument("--regressions-only", action="store_true")
    parser.add_argument("--iterations", type=int, default=3)
    parser.add_argument("--time-limit", type=float, default=1.0)
    parser.add_argument("--generated-at", help="override artifact timestamp for reproducible committed baselines")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.iterations < 0:
        parser.error("--iterations must be nonnegative")
    if args.time_limit <= 0:
        parser.error("--time-limit must be positive")

    payload: dict[str, object] = {"regressions": run_regressions()}
    result_type = "exhaustive-regression"
    if not args.regressions_only:
        payload["outer_search"] = cutting_plane_outer_search(
            m=14,
            b=3,
            degree_bound=2,
            max_iterations=args.iterations,
            per_iteration_time_limit=args.time_limit,
        )
        result_type = str(payload["outer_search"].get("status", "unresolved"))  # type: ignore[union-attr]

    command_parts = [
        "python", "enumerate/q0015_configuration_auditor.py",
        "--output-dir", str(args.output_dir),
        "--iterations", str(args.iterations),
        "--time-limit", str(args.time_limit),
    ]
    if args.regressions_only:
        command_parts.append("--regressions-only")
    artifact = build_artifact(
        payload,
        artifact_type="experiment",
        result_type=result_type,
        generator="enumerate/q0015_configuration_auditor.py",
        command=shlex.join(command_parts),
        parameters={
            "regressions_only": args.regressions_only,
            "iterations": args.iterations,
            "time_limit": args.time_limit,
        },
        scope="Q-0015 public regression family and optional bounded outer search",
        generated_at=args.generated_at,
    )
    output = args.output_dir / "q0015_audit_results.json"
    atomic_write_json(output, artifact)

    regressions = payload["regressions"]  # type: ignore[assignment]
    summary = {
        "output": str(output),
        "payload_sha256": artifact["metadata"]["payload_sha256"],
        "classification": regressions["all_24_orders"],  # type: ignore[index]
        "specified_t_min": regressions["specified_window"]["budget_lp"]["t_min"],  # type: ignore[index]
        "genealogy_merged_eta": regressions["genealogy_collision"]["incorrectly_merged_eta"],  # type: ignore[index]
        "outer_status": payload.get("outer_search", {}).get("status", "not-run"),  # type: ignore[union-attr]
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
