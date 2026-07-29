from __future__ import annotations

from collections import Counter, deque
import json
from functools import lru_cache
from itertools import combinations, product

D = 4
V = tuple(range(1 << D))

def neighbors(v: int):
    return tuple(v ^ (1 << i) for i in range(D))

@lru_cache(None)
def enumerate_matchings(rem: tuple[int, ...]):
    if not rem:
        return ((),)
    remaining = set(rem)
    v = min(remaining)
    out = []
    for w in neighbors(v):
        if w not in remaining:
            continue
        nxt = tuple(sorted(remaining - {v, w}))
        for rest in enumerate_matchings(nxt):
            out.append(((min(v, w), max(v, w)),) + rest)
    return tuple(out)

def with_directions(matching):
    return tuple((x, y, (x ^ y).bit_length() - 1) for x, y in matching)

def direction_and_edge_maps(matching):
    direction, edge_id = {}, {}
    for i, (x, y, d) in enumerate(matching):
        direction[x] = direction[y] = d
        edge_id[x] = edge_id[y] = i
    return direction, edge_id

FACES = []
for free in combinations(range(D), 2):
    fixed = tuple(i for i in range(D) if i not in free)
    for fixed_values in product((0, 1), repeat=2):
        vertices = []
        for free_values in product((0, 1), repeat=2):
            bits = [0] * D
            for i, value in zip(fixed, fixed_values):
                bits[i] = value
            for i, value in zip(free, free_values):
                bits[i] = value
            vertices.append(sum(bits[i] << i for i in range(D)))
        FACES.append(tuple(vertices))

def is_normal(matching):
    direction, _ = direction_and_edge_maps(matching)
    return all(len({direction[v] for v in face}) == 3 for face in FACES)

def bit(v: int, i: int) -> int:
    return (v >> i) & 1

def state_from_full_remove(v: int, missing: int):
    return tuple(None if i == missing else bit(v, i) for i in range(D))

def hyperedge_states(matching):
    return {
        state_from_full_remove(x, d): edge_id
        for edge_id, (x, _, d) in enumerate(matching)
    }

def independent_states(matching):
    forbidden = hyperedge_states(matching)
    states = []
    for missing in range(D):
        for values in product((0, 1), repeat=D - 1):
            it = iter(values)
            state = tuple(None if i == missing else next(it) for i in range(D))
            if state not in forbidden:
                states.append(state)
    return states

def full_from_state(state, attempted_bit):
    values = list(state)
    missing = values.index(None)
    values[missing] = attempted_bit
    vertex = sum(values[i] << i for i in range(D))
    return vertex, missing

def moves_from_state(matching, state):
    direction, edge_id = direction_and_edge_maps(matching)
    out = []
    for attempted_bit in (0, 1):
        vertex, attempted_coord = full_from_state(state, attempted_bit)
        omitted = direction[vertex]
        assert omitted != attempted_coord
        old_blocker_coords = [
            i for i in range(D) if i not in (attempted_coord, omitted)
        ]
        for release in old_blocker_coords:
            pivot = next(i for i in old_blocker_coords if i != release)
            values = [bit(vertex, i) for i in range(D)]
            values[release] = None
            target = tuple(values)
            out.append({
                "attempted_bit": attempted_bit,
                "blocker_edge": edge_id[vertex],
                "release": release,
                "pivot": (pivot, bit(vertex, pivot)),
                "target": target,
            })
    return out

def transition_graph(matching):
    return {
        state: moves_from_state(matching, state)
        for state in independent_states(matching)
    }

def reachable_masks(matching, start, initial_mask):
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
            new_mask = mask | edge_mask
            new_state = move["target"]
            item = (new_state, new_mask)
            if item not in seen:
                seen.add(item)
                reachable[new_state].add(new_mask)
                queue.append(item)
    return reachable

def splice_witnesses(matching, first, second):
    first_mask = 1 << first["blocker_edge"]
    second_mask = 1 << second["blocker_edge"]
    if first_mask & second_mask:
        return []

    left = reachable_masks(matching, first["target"], first_mask)
    right = reachable_masks(matching, second["target"], second_mask)
    witnesses = []

    for state in left:
        for lm in left[state]:
            for rm in right[state]:
                if lm & rm == 0:
                    witnesses.append((state, lm, rm))
    return witnesses

def classify_normal_models():
    matchings = [with_directions(m) for m in enumerate_matchings(V)]
    normal = [m for m in matchings if is_normal(m)]

    categories = Counter()
    per_state_patterns = Counter()
    splice_edge_counts = Counter()

    for matching in normal:
        for state in independent_states(matching):
            moves = moves_from_state(matching, state)
            left = [m for m in moves if m["attempted_bit"] == 0]
            right = [m for m in moves if m["attempted_bit"] == 1]
            state_categories = []

            for first in left:
                for second in right:
                    same_pivot = first["pivot"] == second["pivot"]
                    witnesses = splice_witnesses(matching, first, second)
                    spliceable = bool(witnesses)

                    if same_pivot:
                        category = "same-pivot cylinder"
                    elif spliceable:
                        category = "edge-disjoint splice"
                        minimum = min(
                            (lm | rm).bit_count()
                            for _, lm, rm in witnesses
                        )
                        splice_edge_counts[minimum] += 1
                    else:
                        category = "unavoidable real-edge reuse"

                    categories[category] += 1
                    state_categories.append(category)

            per_state_patterns[tuple(sorted(state_categories))] += 1

    return {
        "coordinate_perfect_matchings": len(matchings),
        "normal_matchings": len(normal),
        "normal_independent_states": sum(
            len(independent_states(m)) for m in normal
        ),
        "future_complete_release_policies": sum(categories.values()),
        "categories": dict(categories),
        "per_state_patterns": {
            " | ".join(key): value for key, value in per_state_patterns.items()
        },
        "minimum_distinct_real_edges_per_splice": dict(splice_edge_counts),
    }

if __name__ == "__main__":
    result = classify_normal_models()
    print(json.dumps(result, indent=2, ensure_ascii=False))

    assert result["coordinate_perfect_matchings"] == 272
    assert result["normal_matchings"] == 8
    assert result["normal_independent_states"] == 192
    assert result["future_complete_release_policies"] == 768
    assert result["categories"] == {
        "edge-disjoint splice": 384,
        "unavoidable real-edge reuse": 192,
        "same-pivot cylinder": 192,
    }
    assert result["minimum_distinct_real_edges_per_splice"] == {8: 384}
