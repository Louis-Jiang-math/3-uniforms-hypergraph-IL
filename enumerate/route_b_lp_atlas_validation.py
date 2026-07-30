from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from hypergraph_il.artifacts import atomic_write_json, build_artifact
from enumerate.q4_splice_pay_cylinder_validation import classify_normal_models
from enumerate.route_b_b3_reduced_core_search import (
    audit_q3_5_cover,
    block_minimal_q3_5,
    random_edge_minimal_cover_q3_5,
    run_exact_search_2000,
    run_general4_search_2000,
)

D = 4
VERTICES = tuple(range(1 << D))


def neighbors(vertex: int) -> tuple[int, ...]:
    return tuple(vertex ^ (1 << coordinate) for coordinate in range(D))


def enumerate_star_forests():
    remaining_all = set(VERTICES)

    def recurse(unassigned: set[int], components):
        if not unassigned:
            yield tuple(
                sorted(
                    tuple(sorted((center, leaf)))
                    for center, leaves in components
                    for leaf in leaves
                )
            )
            return

        vertex = min(unassigned)
        available_neighbors = sorted(set(neighbors(vertex)) & unassigned)

        for size in range(1, len(available_neighbors) + 1):
            for leaves in combinations(available_neighbors, size):
                used = {vertex, *leaves}
                yield from recurse(unassigned - used, components + [(vertex, leaves)])

        for center in available_neighbors:
            other_neighbors = sorted((set(neighbors(center)) & unassigned) - {vertex})
            for extra_size in range(1, len(other_neighbors) + 1):
                for extra in combinations(other_neighbors, extra_size):
                    leaves = (vertex,) + extra
                    used = {center, *leaves}
                    yield from recurse(unassigned - used, components + [(center, leaves)])

    yield from recurse(remaining_all, [])


FACES = []
for free_coordinates in combinations(range(D), 2):
    fixed_coordinates = tuple(i for i in range(D) if i not in free_coordinates)
    for fixed_values in product((0, 1), repeat=2):
        face = []
        for free_values in product((0, 1), repeat=2):
            bits = [0] * D
            for coordinate, value in zip(fixed_coordinates, fixed_values):
                bits[coordinate] = value
            for coordinate, value in zip(free_coordinates, free_values):
                bits[coordinate] = value
            face.append(sum(bits[i] << i for i in range(D)))
        FACES.append(tuple(face))


def matching_is_normal(edges: tuple[tuple[int, int], ...]) -> bool:
    if len(edges) != 8:
        return False
    degree = Counter()
    direction = {}
    for left, right in edges:
        degree[left] += 1
        degree[right] += 1
        coordinate = (left ^ right).bit_length() - 1
        direction[left] = direction[right] = coordinate
    if any(degree[vertex] != 1 for vertex in VERTICES):
        return False
    return all(len({direction[vertex] for vertex in face}) == 3 for face in FACES)


def q4_edge_patterns(forest: tuple[tuple[int, int], ...]):
    patterns = []
    for left, right in forest:
        omitted = (left ^ right).bit_length() - 1
        patterns.append(tuple(
            (coordinate, (left >> coordinate) & 1)
            for coordinate in range(D)
            if coordinate != omitted
        ))
    return tuple(patterns)


def independent_transversal_exists(patterns, active_blocks):
    for values in product((0, 1), repeat=len(active_blocks)):
        assignment = dict(zip(active_blocks, values))
        if not any(
            all(block in assignment and assignment[block] == value for block, value in edge)
            for edge in patterns
        ):
            return True
    return False


def block_minimal(patterns) -> bool:
    if independent_transversal_exists(patterns, tuple(range(4))):
        return False
    return all(
        independent_transversal_exists(patterns, tuple(i for i in range(4) if i != deleted))
        for deleted in range(4)
    )


def classify_q4_star_forests() -> dict[str, int]:
    counts = Counter()
    total = 0
    for forest in enumerate_star_forests():
        total += 1
        patterns = q4_edge_patterns(forest)
        if not block_minimal(patterns):
            counts["not_block_minimal"] += 1
            continue
        counts["block_minimal"] += 1
        degree = Counter(vertex for edge in forest for vertex in edge)
        is_matching = len(forest) == 8 and all(degree[vertex] == 1 for vertex in VERTICES)
        if not is_matching:
            counts["multi_blocker_M"] += 1
        elif matching_is_normal(forest):
            counts["normal_Q4"] += 1
        else:
            counts["nonnormal_N"] += 1
    counts["star_forests_total"] = total
    return dict(counts)


def run_five_block_search(target: int, seed: int) -> dict:
    import random
    import time

    rng = random.Random(seed)
    keys = set()
    records = []
    attempts = 0
    started = time.time()
    while len(records) < target and attempts < target * 30:
        attempts += 1
        key = random_edge_minimal_cover_q3_5(rng)
        if key in keys:
            continue
        keys.add(key)
        if not block_minimal_q3_5(key):
            continue
        records.append((key, audit_q3_5_cover(key)))

    classifications = Counter()
    edge_counts = Counter()
    for key, components in records:
        edge_counts[len(key)] += 1
        residual = any(component["has_reduced_residual_cycle"] for component in components)
        q_core = any(component["has_reduced_q_cycle"] for component in components)
        classifications["reduced_residual_core"] += int(residual)
        classifications["reduced_q_core"] += int(q_core)
        classifications["covered_after_WMAN_and_R"] += int(not residual)
    return {
        "target": target,
        "attempts": attempts,
        "unique_models": len(records),
        "seed": seed,
        "elapsed_seconds": time.time() - started,
        "edge_count_distribution": dict(sorted(edge_counts.items())),
        "classification": dict(classifications),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exact", type=int, default=2000)
    parser.add_argument("--general4", type=int, default=2000)
    parser.add_argument("--general5", type=int, default=200)
    parser.add_argument("--generated-at", default="2026-07-30T16:34:00Z")
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "artifacts/runs/route_b/route_b_lp_atlas_validation.json",
    )
    args = parser.parse_args()

    exact_result = run_exact_search_2000(args.exact, 20260737)
    general4_result = run_general4_search_2000(args.general4, 20260738)
    general5_result = run_five_block_search(args.general5, 20260734)
    for result in (exact_result, general4_result, general5_result):
        result.pop("elapsed_seconds", None)

    payload = {
        "schema_version": "route-b-lp-atlas-validation-v1",
        "q4_star_forests": classify_q4_star_forests(),
        "normal_q4_release_policies": classify_normal_models(),
        "b3_four_block_exact_cover": exact_result,
        "b3_four_block_general_cover": general4_result,
        "b3_five_block_general_cover": general5_result,
        "interpretation": {
            "certified_modules": ["W", "M", "A", "N"],
            "same_edge_R_reduction": "consecutive moves using the same actual blocker edge do not form a residual history cycle",
            "nonclaim": "bounded computation does not prove a general atlas or core classification theorem",
        },
    }
    parameters = {
        "exact": args.exact,
        "general4": args.general4,
        "general5": args.general5,
        "seeds": {"exact": 20260737, "general4": 20260738, "general5": 20260734},
    }
    command = (
        "python enumerate/route_b_lp_atlas_validation.py "
        f"--exact {args.exact} --general4 {args.general4} --general5 {args.general5} "
        f"--generated-at {args.generated_at} --output {args.output.as_posix()}"
    )
    artifact = build_artifact(
        payload,
        artifact_type="experiment-baseline",
        result_type="mixed-exhaustive-and-bounded-random",
        generator="enumerate/route_b_lp_atlas_validation.py",
        command=command,
        parameters=parameters,
        scope=(
            "complete b=2 Q4 star-forest and normal-policy spaces; fixed-seed "
            "bounded b=3 exact/general cover searches"
        ),
        generated_at=args.generated_at,
    )
    atomic_write_json(args.output, artifact)
    print(json.dumps(artifact, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
