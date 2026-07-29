#!/usr/bin/env python3
"""Generate the bounded-exhaustive Q-0015 reset-compensation artifact."""
from __future__ import annotations

import argparse
import shlex
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SRC = REPO / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from hypergraph_il.artifacts import atomic_write_json, build_artifact
from hypergraph_il.q0015_reset import run_reset_compensation_experiment


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/runs/q0015/reset_compensation_results.json"),
    )
    parser.add_argument(
        "--generated-at",
        help="override timestamp for a reproducible committed artifact",
    )
    args = parser.parse_args(argv)

    payload = run_reset_compensation_experiment()
    command = shlex.join(
        [
            "python",
            "enumerate/q0015_reset_compensation.py",
            "--output",
            str(args.output),
            *(
                ["--generated-at", args.generated_at]
                if args.generated_at is not None
                else []
            ),
        ]
    )
    artifact = build_artifact(
        payload,
        artifact_type="counterexample",
        result_type="exhaustive-bounded",
        generator="enumerate/q0015_reset_compensation.py",
        command=command,
        parameters={
            "block_count": 3,
            "block_size": 2,
            "maximum_path_depth": 8,
        },
        scope="all 256 transversal-edge subsets on three blocks of size two",
        generated_at=args.generated_at,
    )
    atomic_write_json(args.output, artifact)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
