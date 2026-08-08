from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csr_matrix, lil_matrix

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from hypergraph_il.artifacts import atomic_write_json, build_artifact

D = 4
VERTICES = tuple(range(1 << D))


def bit(vertex: int, coordinate: int) -> int:
    return (vertex >> coordinate) & 1


def neighbors(vertex: int) -> tuple[int, ...]:
    return tuple(vertex ^ (1 << coordinate) for coordinate in range(D))


@lru_cache(None)
def enumerate_matchings(remaining: tuple[int, ...]):
    if not remaining:
        return ((),)
    pool = set(remaining)
    vertex = min(pool)
    output = []
    for other in neighbors(vertex):
        if other not in pool:
            continue
        rest = tuple(sorted(pool - {vertex, other}))
        for tail in enumerate_matchings(rest):
            output.append(((min(vertex, other), max(vertex, other)),) + tail)
    return tuple(output)


def with_directions(matching):
    return tuple((left, right, (left ^ right).bit_length() - 1) for left, right in matching)


FACES = []
for free in combinations(range(D), 2):
    fixed = tuple(i for i in range(D) if i not in free)
    for fixed_values in product((0, 1), repeat=2):
        face = []
        for free_values in product((0, 1), repeat=2):
            values = [0] * D
            for coordinate, value in zip(fixed, fixed_values):
                values[coordinate] = value
            for coordinate, value in zip(free, free_values):
                values[coordinate] = value
            face.append(sum(values[i] << i for i in range(D)))
        FACES.append(tuple(face))


def direction_and_edge_maps(matching):
    direction = {}
    edge_id = {}
    for index, (left, right, omitted) in enumerate(matching):
        direction[left] = direction[right] = omitted
        edge_id[left] = edge_id[right] = index
    return direction, edge_id


def is_normal(matching) -> bool:
    direction, _ = direction_and_edge_maps(matching)
    return all(len({direction[vertex] for vertex in face}) == 3 for face in FACES)


def state_from_full_remove(vertex: int, missing: int):
    return tuple(None if i == missing else bit(vertex, i) for i in range(D))


def blocker_hyperedge(matching, edge_id: int):
    left, _, omitted = matching[edge_id]
    return frozenset((i, bit(left, i)) for i in range(D) if i != omitted)


def hyperedge_states(matching):
    return {
        state_from_full_remove(left, omitted): edge_id
        for edge_id, (left, _, omitted) in enumerate(matching)
    }


def independent_states(matching):
    forbidden = hyperedge_states(matching)
    output = []
    for missing in range(D):
        for values in product((0, 1), repeat=3):
            iterator = iter(values)
            state = tuple(None if i == missing else next(iterator) for i in range(D))
            if state not in forbidden:
                output.append(state)
    return output


def full_from_state(state, attempted: int):
    values = list(state)
    hole = values.index(None)
    values[hole] = attempted
    vertex = sum(values[i] << i for i in range(D))
    return vertex, hole


def moves_from_state(matching, state):
    direction, edge_id = direction_and_edge_maps(matching)
    output = []
    for attempted in (0, 1):
        vertex, hole = full_from_state(state, attempted)
        omitted = direction[vertex]
        assert omitted != hole
        old = [i for i in range(D) if i not in (hole, omitted)]
        for release in old:
            pivot = next(i for i in old if i != release)
            values = [bit(vertex, i) for i in range(D)]
            values[release] = None
            output.append(
                {
                    "attempted_bit": attempted,
                    "blocker_edge": edge_id[vertex],
                    "release": release,
                    "pivot": (pivot, bit(vertex, pivot)),
                    "target": tuple(values),
                }
            )
    return output


def transition_graph(matching):
    return {state: moves_from_state(matching, state) for state in independent_states(matching)}


def reachable_masks(matching, start, initial_mask: int):
    graph = transition_graph(matching)
    reachable = {state: set() for state in graph}
    queue = deque([(start, initial_mask)])
    seen = {(start, initial_mask)}
    reachable[start].add(initial_mask)
    while queue:
        state, mask = queue.popleft()
        for move in graph[state]:
            edge_mask = 1 << move["blocker_edge"]
            if mask & edge_mask:
                continue
            target = move["target"]
            new_mask = mask | edge_mask
            item = (target, new_mask)
            if item not in seen:
                seen.add(item)
                queue.append(item)
                reachable[target].add(new_mask)
    return reachable


def splice_witnesses(matching, first, second):
    first_mask = 1 << first["blocker_edge"]
    second_mask = 1 << second["blocker_edge"]
    if first_mask & second_mask:
        return []
    left = reachable_masks(matching, first["target"], first_mask)
    right = reachable_masks(matching, second["target"], second_mask)
    output = []
    for state in left:
        for left_mask in left[state]:
            for right_mask in right[state]:
                if left_mask & right_mask == 0:
                    output.append((state, left_mask, right_mask))
    return output


def paths_avoiding(matching, start, initial_used, maximum=8):
    graph = transition_graph(matching)
    output = defaultdict(list)

    def dfs(state, used, edges):
        output[state].append(tuple(edges))
        if len(used) >= maximum:
            return
        for move in graph[state]:
            edge = move["blocker_edge"]
            if edge in used:
                continue
            dfs(move["target"], used | {edge}, edges + [edge])

    dfs(start, set(initial_used), [])
    return output


def unique_bridge_order(matching, first, second):
    left = paths_avoiding(matching, first["target"], {first["blocker_edge"]})
    right = paths_avoiding(matching, second["target"], {second["blocker_edge"]})
    orders = set()
    cuts = 0
    for state in set(left) & set(right):
        for left_edges in left[state]:
            for right_edges in right[state]:
                first_edges = (first["blocker_edge"],) + left_edges
                second_edges = (second["blocker_edge"],) + right_edges
                if set(first_edges).isdisjoint(second_edges) and len(set(first_edges) | set(second_edges)) == 8:
                    orders.add(first_edges + tuple(reversed(second_edges)))
                    cuts += 1
    return orders, cuts


def endpoint_data(matching, state):
    moves = moves_from_state(matching, state)
    left = [move for move in moves if move["attempted_bit"] == 0]
    right = [move for move in moves if move["attempted_bit"] == 1]
    edge_ids = (left[0]["blocker_edge"], right[0]["blocker_edge"])
    edges = tuple(blocker_hyperedge(matching, edge_id) for edge_id in edge_ids)
    common = edges[0] & edges[1]
    return {
        "edge_ids": edge_ids,
        "edges": edges,
        "q": next(iter(common)) if len(common) == 1 else None,
        "hole": state.index(None),
    }


def complement_state(state):
    return tuple(None if value is None else 1 - value for value in state)


def canonical_splice_pair(matching, state):
    data = endpoint_data(matching, state)
    q = data["q"]
    moves = moves_from_state(matching, state)
    left = [move for move in moves if move["attempted_bit"] == 0]
    right = [move for move in moves if move["attempted_bit"] == 1]
    first = next(move for move in left if move["pivot"] == q)
    second = next(move for move in right if move["pivot"] != q)
    return first, second


def bridge_order(matching, state):
    first, second = canonical_splice_pair(matching, state)
    orders, cuts = unique_bridge_order(matching, first, second)
    assert len(orders) == 1 and cuts == 7
    return next(iter(orders))


def root_defects(matching):
    defects = []
    for state in independent_states(matching):
        moves = moves_from_state(matching, state)
        first = next(move for move in moves if move["attempted_bit"] == 0)
        second = next(move for move in moves if move["attempted_bit"] == 1)
        edge_first = blocker_hyperedge(matching, first["blocker_edge"])
        edge_second = blocker_hyperedge(matching, second["blocker_edge"])
        if len(edge_first & edge_second) == 2:
            defects.append(state)
    return defects


def edge_key(edge):
    return tuple(sorted(edge))


def q4_payload(matchings, normal):
    categories = Counter()
    release_square = Counter()
    root_intersections = Counter()
    defect_distribution = Counter()
    bridge_order_counts = Counter()
    bridge_cut_counts = Counter()
    endpoint_migration = Counter()
    endpoint_incidence = Counter()
    cyclic_signatures = Counter()
    source_tuple_support_multiplicity = defaultdict(set)

    for matching in matchings:
        defect_distribution[(is_normal(matching), len(root_defects(matching)))] += 1

    supports = []
    for matching_index, matching in enumerate(normal):
        support = frozenset(edge_key(blocker_hyperedge(matching, edge_id)) for edge_id in range(8))
        supports.append(support)
        for state in independent_states(matching):
            data = endpoint_data(matching, state)
            first_edge, second_edge = data["edges"]
            root_intersections[len(first_edge & second_edge)] += 1
            source_tuple_support_multiplicity[
                (edge_key(first_edge), edge_key(second_edge), data["q"])
            ].add(support)

            moves = moves_from_state(matching, state)
            left = [move for move in moves if move["attempted_bit"] == 0]
            right = [move for move in moves if move["attempted_bit"] == 1]
            for first in left:
                for second in right:
                    edge_first = blocker_hyperedge(matching, first["blocker_edge"])
                    edge_second = blocker_hyperedge(matching, second["blocker_edge"])
                    q = next(iter(edge_first & edge_second))
                    keep_first = q == first["pivot"]
                    keep_second = q == second["pivot"]
                    witnesses = splice_witnesses(matching, first, second)
                    category = (
                        "C"
                        if first["pivot"] == second["pivot"]
                        else ("S" if witnesses else "R")
                    )
                    categories[category] += 1
                    release_square[(int(keep_first), int(keep_second), category)] += 1
                    if category != "S":
                        continue
                    orders, cuts = unique_bridge_order(matching, first, second)
                    bridge_order_counts[len(orders)] += 1
                    bridge_cut_counts[cuts] += 1
                    assert len(orders) == 1
                    order = next(iter(orders))
                    hyperedges = [blocker_hyperedge(matching, edge_id) for edge_id in order]
                    e1, e2 = hyperedges[0], hyperedges[-1]
                    f1, f2 = hyperedges[1], hyperedges[-2]
                    q_endpoint = next(iter(e1 & e2))
                    r = next(iter(f1 & f2))
                    endpoint_incidence[
                        (
                            len(e1 & e2),
                            len(f1 & f2),
                            int(q_endpoint in f1),
                            int(q_endpoint in f2),
                            len(e1 & f1),
                            len(e1 & f2),
                            len(e2 & f1),
                            len(e2 & f2),
                            "e1" if r in e1 else "e2" if r in e2 else "none",
                        )
                    ] += 1
                    vertices = [next(iter(hyperedges[i] & hyperedges[(i + 1) % 8])) for i in range(8)]
                    vertex_index = {vertex: index for index, vertex in enumerate(vertices)}
                    offsets = []
                    valid = len(vertex_index) == 8
                    if valid:
                        for index, edge in enumerate(hyperedges):
                            positions = {vertex_index[vertex] for vertex in edge}
                            third = positions - {(index - 1) % 8, index}
                            if len(third) != 1:
                                valid = False
                                break
                            offsets.append((next(iter(third)) - index) % 8)
                    degrees = Counter(vertex for edge in hyperedges for vertex in edge)
                    cyclic_signatures[(valid, tuple(offsets), tuple(sorted(degrees.values())))] += 1

            antipode = complement_state(state)
            new_data = endpoint_data(matching, antipode)
            old_order = bridge_order(matching, state)
            new_order = bridge_order(matching, antipode)
            positions = {edge_id: index for index, edge_id in enumerate(old_order)}
            endpoint_migration[
                (
                    int(set(old_order) == set(new_order)),
                    len(set(data["edge_ids"]) & set(new_data["edge_ids"])),
                    int(data["q"] == new_data["q"]),
                    tuple(positions[edge_id] for edge_id in data["edge_ids"]),
                    tuple(positions[edge_id] for edge_id in new_data["edge_ids"]),
                )
            ] += 1

    support_pair_overlap = Counter()
    support_graph = {index: set() for index in range(len(supports))}
    blocker_multiplicity = Counter()
    for support in supports:
        blocker_multiplicity.update(support)
    for first_index, first_support in enumerate(supports):
        for second_index in range(first_index + 1, len(supports)):
            overlap = len(first_support & supports[second_index])
            support_pair_overlap[overlap] += 1
            if overlap == 2:
                support_graph[first_index].add(second_index)
                support_graph[second_index].add(first_index)
    bipartition = {}
    for start in range(len(supports)):
        if start in bipartition:
            continue
        bipartition[start] = 0
        queue = [start]
        while queue:
            vertex = queue.pop()
            for neighbor in support_graph[vertex]:
                if neighbor not in bipartition:
                    bipartition[neighbor] = 1 - bipartition[vertex]
                    queue.append(neighbor)
    part_sizes = Counter(bipartition.values())

    return {
        "coordinate_perfect_matchings": len(matchings),
        "normal_matchings": len(normal),
        "normal_rooted_states": sum(len(independent_states(matching)) for matching in normal),
        "root_blocker_intersection_sizes": dict(sorted(root_intersections.items())),
        "release_categories": dict(categories),
        "release_square": {str(key): value for key, value in sorted(release_square.items())},
        "nonnormal_root_two_intersection_defect_distribution": {
            str(defects): count
            for (normal_flag, defects), count in sorted(defect_distribution.items())
            if not normal_flag
        },
        "minimum_nonnormal_root_defects": min(
            defects for (normal_flag, defects), count in defect_distribution.items() if not normal_flag and count
        ),
        "splice_unique_bridge_order_count_distribution": dict(bridge_order_counts),
        "splice_edge_disjoint_cut_count_distribution": dict(bridge_cut_counts),
        "endpoint_incidence_signatures": {str(key): value for key, value in endpoint_incidence.items()},
        "cyclic_8_3_signatures": {str(key): value for key, value in cyclic_signatures.items()},
        "endpoint_antipode_migration": {str(key): value for key, value in endpoint_migration.items()},
        "source_tuple_support_multiplicity": dict(Counter(len(value) for value in source_tuple_support_multiplicity.values())),
        "normal_support_distinct_blocker_triples": len(blocker_multiplicity),
        "normal_support_blocker_multiplicity_distribution": dict(Counter(blocker_multiplicity.values())),
        "normal_support_pair_overlap_distribution": dict(support_pair_overlap),
        "normal_support_overlap_graph_part_sizes": dict(part_sizes),
        "normal_support_overlap_graph_is_K4_4": (
            len(supports) == 8
            and sorted(part_sizes.values()) == [4, 4]
            and all(len(neighbors_) == 4 for neighbors_ in support_graph.values())
        ),
    }


def abstract_normal_supports(normal):
    return [
        frozenset(edge_key(blocker_hyperedge(matching, edge_id)) for edge_id in range(8))
        for matching in normal
    ]


def embed_support(support, window):
    return frozenset(
        edge_key((coordinate, window[coordinate][value]) for coordinate, value in edge)
        for edge in support
    )


def transform_embedded_support(support, block_permutation, value_permutations):
    transformed = []
    for edge in support:
        transformed.append(
            edge_key(
                (block_permutation[coordinate], value_permutations[coordinate][value])
                for coordinate, value in edge
            )
        )
    return frozenset(transformed)


def ternary_payload(normal):
    abstract = abstract_normal_supports(normal)
    pairs = list(combinations(range(3), 2))
    embedded = []
    for window in product(pairs, repeat=4):
        oriented = tuple(tuple(pair) for pair in window)
        for support in abstract:
            embedded.append(embed_support(support, oriented))
    embedded = list(dict.fromkeys(embedded))
    all_edges = sorted(set().union(*embedded))

    overlap_distribution = Counter()
    for first_index, first_support in enumerate(embedded):
        for second_support in embedded[first_index + 1 :]:
            overlap_distribution[len(first_support & second_support)] += 1

    # Verify transitivity of the full S_4 x S_3^4 action on the 648 embedded supports.
    fixed = embedded[0]
    orbit = set()
    value_permutations = list(permutations(range(3)))
    for block_permutation in permutations(range(4)):
        for value_maps in product(value_permutations, repeat=4):
            orbit.add(transform_embedded_support(fixed, block_permutation, value_maps))
    transitive = set(embedded) == orbit

    edge_index = {edge: index for index, edge in enumerate(all_edges)}
    candidates = [index for index, support in enumerate(embedded) if index != 0 and support.isdisjoint(fixed)]
    matrix = lil_matrix((len(all_edges), len(candidates)), dtype=float)
    for column, support_index in enumerate(candidates):
        for edge in embedded[support_index]:
            matrix[edge_index[edge], column] = 1.0
    matrix = csr_matrix(matrix)
    edge_constraint = LinearConstraint(matrix, lb=np.zeros(len(all_edges)), ub=np.ones(len(all_edges)))
    bounds = Bounds(np.zeros(len(candidates)), np.ones(len(candidates)))
    integrality = np.ones(len(candidates))

    # 12-packing: fixed support plus 11 disjoint additional supports.
    twelve_constraint = LinearConstraint(
        np.ones((1, len(candidates))), lb=np.array([11.0]), ub=np.array([11.0])
    )
    twelve = milp(
        c=np.zeros(len(candidates)),
        integrality=integrality,
        bounds=bounds,
        constraints=[edge_constraint, twelve_constraint],
    )

    # 13-packing: by transitivity we may fix one support, then ask for 12 more.
    thirteen_constraint = LinearConstraint(
        np.ones((1, len(candidates))), lb=np.array([12.0]), ub=np.array([12.0])
    )
    thirteen = milp(
        c=np.zeros(len(candidates)),
        integrality=integrality,
        bounds=bounds,
        constraints=[edge_constraint, thirteen_constraint],
    )

    selected = [0]
    if twelve.x is not None:
        selected.extend(candidates[index] for index, value in enumerate(twelve.x) if value > 0.5)
    covered = set().union(*(embedded[index] for index in selected))
    uncovered = set(all_edges) - covered
    uncovered_by_direction = Counter(
        next(iter(set(range(4)) - {coordinate for coordinate, _ in edge})) for edge in uncovered
    )

    return {
        "binary_windows": len(pairs) ** 4,
        "candidate_supports": len(embedded),
        "possible_actual_blocker_triples": len(all_edges),
        "pair_overlap_distribution": dict(sorted(overlap_distribution.items())),
        "full_automorphism_orbit_size_of_fixed_support": len(orbit),
        "support_action_transitive": transitive,
        "fixed_support_disjoint_candidates": len(candidates),
        "twelve_packing_solver_status": int(twelve.status),
        "twelve_packing_feasible": bool(twelve.x is not None and len(selected) == 12),
        "thirteen_packing_solver_status": int(thirteen.status),
        "thirteen_packing_infeasible": int(thirteen.status) == 2,
        "maximum_edge_disjoint_supports": 12 if transitive and twelve.x is not None and int(thirteen.status) == 2 else None,
        "one_twelve_packing_covered_edges": len(covered),
        "one_twelve_packing_uncovered_edges": len(uncovered),
        "one_twelve_packing_uncovered_by_omitted_direction": dict(uncovered_by_direction),
    }


def codimension_one_payload(normal):
    profile = Counter()
    completion_profile = Counter()
    for matching in normal:
        for state in independent_states(matching):
            first, second = canonical_splice_pair(matching, state)
            orders, _ = unique_bridge_order(matching, first, second)
            order = next(iter(orders))
            edges = [blocker_hyperedge(matching, edge_id) for edge_id in order]
            endpoints = edges[0] | edges[-1]
            first_inward = endpoints | edges[1] | edges[-2]
            central = endpoints | edges[3] | edges[4]
            profile[(len(endpoints), len(first_inward), len(central))] += 1
            all_vertices = set().union(*edges)
            completion_profile[
                (len(all_vertices - endpoints), len(all_vertices - first_inward), len(all_vertices - central))
            ] += 1
    return {
        "vertex_union_size_profile_endpoint_first_inward_central": {str(key): value for key, value in profile.items()},
        "missing_vertex_profile_endpoint_first_inward_central": {str(key): value for key, value in completion_profile.items()},
        "general_complete_universe_completion_counts": {
            "endpoint_pair_only": "(b-1)^3",
            "endpoint_pair_plus_first_inward_pair": "b-1",
            "endpoint_pair_plus_central_completion": "1",
        },
        "nonclaim": "the remaining b-ary value is not automatically a source-owned 1/b charge",
    }


def build_payload():
    matchings = [with_directions(matching) for matching in enumerate_matchings(VERTICES)]
    normal = [matching for matching in matchings if is_normal(matching)]
    return {
        "schema_version": "q0019-rank-two-zipper-validation-v1",
        "q4": q4_payload(matchings, normal),
        "ternary_supports": ternary_payload(normal),
        "codimension_one": codimension_one_payload(normal),
        "interpretation": {
            "bounded_scope": "binary normal Q4 and embedded ternary [3]^4 normal-support geometry",
            "nonclaims": [
                "finite computation does not close Q-0019",
                "state confluence is not by itself a P^2 -> P obligation merge",
                "endpoint tuple persistence is false; only the normal support is invariant under the antipodal zipper inside a fixed window",
                "the codimension-one missing value is not automatically an independent entropy charge",
            ],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--generated-at",
        default="2026-08-08T02:45:00Z",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "evidence/experiments/q0019_rank_two/baselines/q0019_rank_two_zipper_validation.json",
    )
    args = parser.parse_args()
    payload = build_payload()
    command = (
        "python enumerate/q0019_rank_two_zipper_validation.py "
        f"--generated-at {args.generated_at} --output {args.output.as_posix()}"
    )
    artifact = build_artifact(
        payload,
        artifact_type="experiment-baseline",
        result_type="bounded-exhaustive-plus-exact-milp",
        generator="enumerate/q0019_rank_two_zipper_validation.py",
        command=command,
        parameters={"q4_dimension": 4, "ternary_alphabet": 3},
        scope="complete normal-Q4 state/release spaces and all 648 embedded normal supports in [3]^4",
        generated_at=args.generated_at,
    )
    atomic_write_json(args.output, artifact)
    print(json.dumps(artifact, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
