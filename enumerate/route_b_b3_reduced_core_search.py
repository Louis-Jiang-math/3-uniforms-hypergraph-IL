from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations, product
import json
import math
import random
import time
from pathlib import Path

import networkx as nx
import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# q=3 four-block exact covers by axis-parallel lines
# ---------------------------------------------------------------------------

Q = 3
M = 4
WORDS4 = tuple(product(range(Q), repeat=M))
WORD_INDEX4 = {word: i for i, word in enumerate(WORDS4)}

LINES4 = []
LINE_WORDS4 = []
POINT_TO_LINES4 = [[] for _ in WORDS4]

for omitted in range(M):
    fixed_blocks = tuple(block for block in range(M) if block != omitted)
    for fixed_values in product(range(Q), repeat=3):
        edge = tuple(zip(fixed_blocks, fixed_values))
        line_words = []
        for omitted_value in range(Q):
            word = [0] * M
            for block, value in edge:
                word[block] = value
            word[omitted] = omitted_value
            line_words.append(WORD_INDEX4[tuple(word)])
        line_index = len(LINES4)
        LINES4.append(edge)
        LINE_WORDS4.append(tuple(line_words))
        for word_index in line_words:
            POINT_TO_LINES4[word_index].append(line_index)

LINES4 = tuple(LINES4)
LINE_WORDS4 = tuple(LINE_WORDS4)
POINT_TO_LINES4 = tuple(tuple(x) for x in POINT_TO_LINES4)


def random_exact_cover_q3_4(rng: random.Random, node_limit: int = 20000):
    """Randomized Algorithm X; returns 27 line indices or None."""
    uncovered = set(range(len(WORDS4)))
    selected = []
    nodes = 0

    def recurse():
        nonlocal nodes
        nodes += 1
        if nodes > node_limit:
            return False
        if not uncovered:
            return True

        best_point = None
        best_candidates = None
        # Minimum remaining values.
        points = list(uncovered)
        rng.shuffle(points)
        for point in points:
            candidates = [
                line_index
                for line_index in POINT_TO_LINES4[point]
                if all(word in uncovered for word in LINE_WORDS4[line_index])
            ]
            if not candidates:
                return False
            if best_candidates is None or len(candidates) < len(best_candidates):
                best_point = point
                best_candidates = candidates
                if len(candidates) == 1:
                    break

        rng.shuffle(best_candidates)
        for line_index in best_candidates:
            covered_words = LINE_WORDS4[line_index]
            for word in covered_words:
                uncovered.remove(word)
            selected.append(line_index)

            if recurse():
                return True

            selected.pop()
            uncovered.update(covered_words)
        return False

    if recurse():
        return tuple(sorted(selected))
    return None


def exact_cover_direction_map(key):
    direction = {}
    for line_index in key:
        omitted = next(block for block in range(4) if block not in {b for b, _ in LINES4[line_index]})
        for word_index in LINE_WORDS4[line_index]:
            direction[WORDS4[word_index]] = omitted
    return direction


def block_minimal_exact_cover_q3_4(key) -> bool:
    edges = [LINES4[index] for index in key]
    for deleted in range(4):
        active = [block for block in range(4) if block != deleted]
        found = False
        for values in product(range(3), repeat=3):
            chosen = dict(zip(active, values))
            blocked = any(
                all(block in chosen and chosen[block] == value for block, value in edge)
                for edge in edges
            )
            if not blocked:
                found = True
                break
        if not found:
            return False
    return True


# Binary Q4 normality test reused on every 2x2x2x2 restriction.
Q4_FACES = []
for free_coordinates in combinations(range(4), 2):
    fixed_coordinates = tuple(i for i in range(4) if i not in free_coordinates)
    for fixed_values in product((0, 1), repeat=2):
        face = []
        for free_values in product((0, 1), repeat=2):
            bits = [0] * 4
            for coordinate, value in zip(fixed_coordinates, fixed_values):
                bits[coordinate] = value
            for coordinate, value in zip(free_coordinates, free_values):
                bits[coordinate] = value
            face.append(tuple(bits))
        Q4_FACES.append(tuple(face))


def binary_restriction_is_normal(direction_map, value_pairs):
    bit_direction = {}
    for bits in product((0, 1), repeat=4):
        word = tuple(value_pairs[i][bits[i]] for i in range(4))
        bit_direction[bits] = direction_map[word]

    # A direction map on a binary cube is a coordinate perfect matching iff
    # flipping the assigned coordinate preserves the assigned direction.
    for bits, direction in bit_direction.items():
        flipped = list(bits)
        flipped[direction] ^= 1
        flipped = tuple(flipped)
        if bit_direction[flipped] != direction:
            return False

    return all(
        len({bit_direction[bits] for bits in face}) == 3
        for face in Q4_FACES
    )


def all_binary_restriction_profile(direction_map):
    normal = 0
    nonnormal = 0
    invalid = 0
    pair_choices = tuple(combinations(range(3), 2))
    for value_pairs in product(pair_choices, repeat=4):
        # Convert to tuples in increasing order.
        value_pairs = tuple(tuple(pair) for pair in value_pairs)
        # Test matching first.
        bit_direction = {}
        valid = True
        for bits in product((0, 1), repeat=4):
            word = tuple(value_pairs[i][bits[i]] for i in range(4))
            bit_direction[bits] = direction_map[word]
        for bits, direction in bit_direction.items():
            flipped = list(bits)
            flipped[direction] ^= 1
            if bit_direction[tuple(flipped)] != direction:
                valid = False
                break
        if not valid:
            invalid += 1
        elif all(
            len({bit_direction[bits] for bits in face}) == 3
            for face in Q4_FACES
        ):
            normal += 1
        else:
            nonnormal += 1
    return normal, nonnormal, invalid


def one_hole_transition_graph_exact_cover_q3_4(key):
    direction_map = exact_cover_direction_map(key)
    edge_by_word = {}
    for line_index in key:
        for word_index in LINE_WORDS4[line_index]:
            edge_by_word[WORDS4[word_index]] = line_index

    states = []
    for missing in range(4):
        for values in product(range(3), repeat=3):
            it = iter(values)
            state = tuple(None if block == missing else next(it) for block in range(4))
            # Independent iff the selected triple is not itself a real edge.
            selected = {(block, value) for block, value in enumerate(state) if value is not None}
            if any(set(LINES4[line_index]) <= selected for line_index in key):
                continue
            states.append(state)

    state_set = set(states)
    graph = nx.DiGraph()
    graph.add_nodes_from(states)

    for state in states:
        missing = state.index(None)
        for attempted in range(3):
            word = tuple(attempted if block == missing else state[block] for block in range(4))
            line_index = edge_by_word[word]
            edge = LINES4[line_index]
            for released_block, released_value in edge:
                if released_block == missing:
                    continue
                target = list(state)
                target[missing] = attempted
                target[released_block] = None
                target = tuple(target)
                if target not in state_set:
                    raise AssertionError("Unique blocker release should be independent.")
                graph.add_edge(state, target)
    return graph, direction_map


def terminal_sccs(graph):
    result = []
    for component in nx.strongly_connected_components(graph):
        component = set(component)
        if any(
            target not in component
            for source in component
            for target in graph.successors(source)
        ):
            continue
        if len(component) > 1 or any(graph.has_edge(v, v) for v in component):
            result.append(component)
    return result


def state_binary_box_profile(state, component, direction_map):
    """
    Conservative N/Q classifier:
    - Q if at least one faithful normal binary box exists.
    - N if at least one faithful nonnormal box exists and no normal box exists.
    - S otherwise (all candidate boxes fail recurrent-support compatibility).
    """
    missing = state.index(None)
    old_blocks = [block for block in range(4) if block != missing]

    normal_boxes = 0
    nonnormal_boxes = 0
    support_failures = 0

    for missing_pair in combinations(range(3), 2):
        for alternatives in product(
            *[
                tuple(value for value in range(3) if value != state[block])
                for block in old_blocks
            ]
        ):
            value_pairs = [None] * 4
            value_pairs[missing] = tuple(missing_pair)
            for block, alternative in zip(old_blocks, alternatives):
                value_pairs[block] = tuple(sorted((int(state[block]), alternative)))
            value_pairs = tuple(value_pairs)

            # Faithful support check: required one-hole states after releasing
            # a blocker endpoint must remain in this recurrent component.
            faithful = True
            bit_direction = {}
            for bits in product((0, 1), repeat=4):
                word = tuple(value_pairs[i][bits[i]] for i in range(4))
                direction = direction_map[word]
                bit_direction[bits] = direction

                blocker_blocks = set(range(4)) - {direction}
                for hole in blocker_blocks:
                    candidate = tuple(
                        None if block == hole else word[block]
                        for block in range(4)
                    )
                    if candidate not in component:
                        faithful = False
                        break
                if not faithful:
                    break

            if not faithful:
                support_failures += 1
                continue

            valid_matching = True
            for bits, direction in bit_direction.items():
                flipped = list(bits)
                flipped[direction] ^= 1
                if bit_direction[tuple(flipped)] != direction:
                    valid_matching = False
                    break

            if not valid_matching:
                nonnormal_boxes += 1
                continue

            is_normal = all(
                len({bit_direction[bits] for bits in face}) == 3
                for face in Q4_FACES
            )
            if is_normal:
                normal_boxes += 1
            else:
                nonnormal_boxes += 1

    if normal_boxes:
        return "Q", normal_boxes, nonnormal_boxes, support_failures
    if nonnormal_boxes:
        return "N", normal_boxes, nonnormal_boxes, support_failures
    return "S", normal_boxes, nonnormal_boxes, support_failures


def residual_cycle_after_N(graph, component, labels):
    # Remove actual cyclic SCCs contained in N-labeled states.
    n_states = [state for state in component if labels[state] == "N"]
    n_subgraph = graph.subgraph(n_states).copy()
    removable = set()
    for kernel in nx.strongly_connected_components(n_subgraph):
        kernel = set(kernel)
        if len(kernel) > 1 or (
            len(kernel) == 1 and n_subgraph.has_edge(next(iter(kernel)), next(iter(kernel)))
        ):
            removable.update(kernel)
    residual = graph.subgraph(set(component) - removable).copy()
    return not nx.is_directed_acyclic_graph(residual), removable, residual


def audit_exact_cover_key(key):
    graph, direction_map = one_hole_transition_graph_exact_cover_q3_4(key)
    components = terminal_sccs(graph)
    profile = all_binary_restriction_profile(direction_map)
    component_results = []

    for component in components:
        labels = {}
        local_counts = {}
        for state in component:
            label, n_normal, n_nonnormal, n_support = state_binary_box_profile(
                state, component, direction_map
            )
            labels[state] = label
            local_counts[state] = (n_normal, n_nonnormal, n_support)

        residual_cyclic, removed, residual = residual_cycle_after_N(
            graph, component, labels
        )
        component_results.append(
            {
                "size": len(component),
                "label_profile": dict(Counter(labels.values())),
                "residual_cyclic_after_N": residual_cyclic,
                "removed_N_states": len(removed),
                "residual_states": len(residual),
            }
        )

    return {
        "block_minimal": block_minimal_exact_cover_q3_4(key),
        "global_binary_profile": {
            "normal": profile[0],
            "nonnormal": profile[1],
            "invalid": profile[2],
        },
        "state_count": len(graph),
        "terminal_components": component_results,
    }




from scipy.optimize import linprog

def exact_cover_moves_q3_4(key):
    direction_map = exact_cover_direction_map(key)
    edge_by_word = {}
    for line_index in key:
        for word_index in LINE_WORDS4[line_index]:
            edge_by_word[WORDS4[word_index]] = line_index

    states = []
    for missing in range(4):
        for values in product(range(3), repeat=3):
            it = iter(values)
            state = tuple(None if block == missing else next(it) for block in range(4))
            selected = {(block, value) for block, value in enumerate(state) if value is not None}
            if any(set(LINES4[line_index]) <= selected for line_index in key):
                continue
            states.append(state)

    state_set = set(states)
    graph = nx.MultiDiGraph()
    graph.add_nodes_from(states)
    moves = []

    for state in states:
        missing = state.index(None)
        for attempted in range(3):
            word = tuple(attempted if block == missing else state[block] for block in range(4))
            line_index = edge_by_word[word]
            edge = LINES4[line_index]
            omitted = direction_map[word]
            for released_block, released_value in edge:
                if released_block == missing:
                    continue
                target = list(state)
                target[missing] = attempted
                target[released_block] = None
                target = tuple(target)
                move_id = len(moves)
                move = {
                    "source": state,
                    "target": target,
                    "attempted": attempted,
                    "word": word,
                    "blocker": line_index,
                    "omitted": omitted,
                    "released_block": released_block,
                }
                moves.append(move)
                graph.add_edge(state, target, key=move_id, move_id=move_id)
    return graph, moves, direction_map


def classify_box(direction_map, value_pairs, component):
    bit_direction = {}
    for bits in product((0, 1), repeat=4):
        word = tuple(value_pairs[i][bits[i]] for i in range(4))
        direction = direction_map[word]
        bit_direction[bits] = direction

        blocker_blocks = set(range(4)) - {direction}
        for hole in blocker_blocks:
            candidate = tuple(
                None if block == hole else word[block]
                for block in range(4)
            )
            if candidate not in component:
                return "S"

    for bits, direction in bit_direction.items():
        flipped = list(bits)
        flipped[direction] ^= 1
        if bit_direction[tuple(flipped)] != direction:
            return "N"

    if all(
        len({bit_direction[bits] for bits in face}) == 3
        for face in Q4_FACES
    ):
        return "Q"
    return "N"


def transition_box_certificates(move, component, direction_map):
    source = move["source"]
    missing = source.index(None)
    old_blocks = [block for block in range(4) if block != missing]
    attempted = move["attempted"]

    certificates = Counter()
    missing_partners = [value for value in range(3) if value != attempted]

    for missing_partner in missing_partners:
        for alternatives in product(
            *[
                tuple(value for value in range(3) if value != source[block])
                for block in old_blocks
            ]
        ):
            value_pairs = [None] * 4
            value_pairs[missing] = tuple(sorted((attempted, missing_partner)))
            for block, alternative in zip(old_blocks, alternatives):
                value_pairs[block] = tuple(sorted((int(source[block]), alternative)))
            label = classify_box(direction_map, tuple(value_pairs), component)
            certificates[label] += 1

    return certificates


def minimum_cycle_mean_binary_feature(graph, moves, component, feature_values):
    edge_ids = [
        move_id
        for move_id, move in enumerate(moves)
        if move["source"] in component and move["target"] in component
    ]
    nodes = list(component)
    node_index = {node: i for i, node in enumerate(nodes)}

    A_eq = np.zeros((len(nodes) + 1, len(edge_ids)))
    b_eq = np.zeros(len(nodes) + 1)
    b_eq[-1] = 1.0

    for column, move_id in enumerate(edge_ids):
        move = moves[move_id]
        A_eq[node_index[move["source"]], column] += 1.0
        A_eq[node_index[move["target"]], column] -= 1.0
    A_eq[-1, :] = 1.0

    costs = np.array([feature_values[move_id] for move_id in edge_ids], dtype=float)
    result = linprog(
        costs,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=(0.0, None),
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)

    support = [
        edge_ids[i] for i, mass in enumerate(result.x) if mass > 1e-8
    ]
    return float(result.fun), support


def transition_level_audit(key):
    graph, moves, direction_map = exact_cover_moves_q3_4(key)
    component_results = []

    for component in terminal_sccs(nx.DiGraph(graph)):
        certs = {
            move_id: transition_box_certificates(move, component, direction_map)
            for move_id, move in enumerate(moves)
            if move["source"] in component and move["target"] in component
        }

        existential_N = {
            move_id: int(certs[move_id]["N"] > 0)
            for move_id in certs
        }
        forced_N = {
            move_id: int(
                certs[move_id]["N"] > 0
                and certs[move_id]["Q"] == 0
                and certs[move_id]["S"] == 0
            )
            for move_id in certs
        }
        existential_Q = {
            move_id: int(certs[move_id]["Q"] > 0)
            for move_id in certs
        }

        min_existential_N, support_existential = minimum_cycle_mean_binary_feature(
            graph, moves, component, existential_N
        )
        min_forced_N, support_forced = minimum_cycle_mean_binary_feature(
            graph, moves, component, forced_N
        )
        min_Q, support_Q = minimum_cycle_mean_binary_feature(
            graph, moves, component, existential_Q
        )

        profile = Counter()
        for c in certs.values():
            key_profile = "+".join(
                label for label in ("Q", "N", "S") if c[label] > 0
            )
            profile[key_profile] += 1

        component_results.append(
            {
                "size": len(component),
                "move_count": len(certs),
                "certificate_profile": dict(profile),
                "min_existential_N_cycle_density": min_existential_N,
                "min_forced_N_cycle_density": min_forced_N,
                "min_existential_Q_cycle_density": min_Q,
                "existential_N_zero_cycle_length": len(support_existential)
                if min_existential_N <= 1e-9 else 0,
                "forced_N_zero_cycle_length": len(support_forced)
                if min_forced_N <= 1e-9 else 0,
            }
        )

    return component_results




from itertools import combinations, product
from collections import Counter
import random
import time
import json
import networkx as nx

PAIR_CHOICES_Q3 = tuple(combinations(range(3), 2))
BOXES_Q3_4 = tuple(product(PAIR_CHOICES_Q3, repeat=4))


def precompute_box_labels(direction_map, component):
    labels = {}
    for value_pairs in BOXES_Q3_4:
        labels[value_pairs] = classify_box(direction_map, value_pairs, component)
    return labels


def word_box_profile(word, box_labels):
    counts = Counter()
    for value_pairs in BOXES_Q3_4:
        if all(word[i] in value_pairs[i] for i in range(4)):
            counts[box_labels[value_pairs]] += 1
    if sum(counts.values()) != 16:
        raise AssertionError("Each ternary word must lie in exactly 16 binary boxes.")
    return counts


def fast_transition_core_audit(key, retain_example=False):
    graph, moves, direction_map = exact_cover_moves_q3_4(key)
    digraph = nx.DiGraph(graph)
    output = []

    for component in terminal_sccs(digraph):
        box_labels = precompute_box_labels(direction_map, component)
        word_profiles = {
            word: word_box_profile(word, box_labels)
            for word in WORDS4
        }

        q_only_move_ids = []
        n_certified_move_ids = []
        for move_id, move in enumerate(moves):
            if move["source"] not in component or move["target"] not in component:
                continue
            profile = word_profiles[move["word"]]
            if profile["N"] > 0:
                n_certified_move_ids.append(move_id)
            if profile["Q"] > 0 and profile["N"] == 0 and profile["S"] == 0:
                q_only_move_ids.append(move_id)

        q_graph = nx.MultiDiGraph()
        q_graph.add_nodes_from(component)
        for move_id in q_only_move_ids:
            move = moves[move_id]
            q_graph.add_edge(
                move["source"],
                move["target"],
                key=move_id,
                move_id=move_id,
            )

        kernels = []
        for kernel_states in nx.strongly_connected_components(nx.DiGraph(q_graph)):
            kernel_states = set(kernel_states)
            if len(kernel_states) == 1:
                node = next(iter(kernel_states))
                if not q_graph.has_edge(node, node):
                    continue
            kernel_moves = [
                move_id
                for move_id in q_only_move_ids
                if moves[move_id]["source"] in kernel_states
                and moves[move_id]["target"] in kernel_states
            ]
            record = {
                "state_count": len(kernel_states),
                "move_count": len(kernel_moves),
            }
            if retain_example:
                record["states"] = [
                    list(state) for state in sorted(kernel_states, key=str)
                ]
                record["moves"] = [
                    {
                        "source": list(moves[move_id]["source"]),
                        "target": list(moves[move_id]["target"]),
                        "word": list(moves[move_id]["word"]),
                        "attempted": moves[move_id]["attempted"],
                        "released_block": moves[move_id]["released_block"],
                        "omitted": moves[move_id]["omitted"],
                        "blocker_edge": [
                            list(vertex)
                            for vertex in LINES4[moves[move_id]["blocker"]]
                        ],
                        "box_profile": dict(word_profiles[moves[move_id]["word"]]),
                    }
                    for move_id in kernel_moves
                ]
            kernels.append(record)

        output.append(
            {
                "component_size": len(component),
                "move_count": sum(
                    1
                    for move in moves
                    if move["source"] in component and move["target"] in component
                ),
                "box_label_profile": dict(Counter(box_labels.values())),
                "q_only_move_count": len(q_only_move_ids),
                "n_certified_move_count": len(n_certified_move_ids),
                "q_only_kernels": kernels,
                "residual_q_core": bool(kernels),
            }
        )

    return output




def has_reduced_cycle(move_ids, moves):
    """
    Detect a cyclic move sequence whose consecutive blocker identities differ,
    including the last-to-first junction.
    """
    adjacency = nx.DiGraph()
    adjacency.add_nodes_from(move_ids)

    by_source = defaultdict(list)
    for move_id in move_ids:
        by_source[moves[move_id]["source"]].append(move_id)

    for first in move_ids:
        target = moves[first]["target"]
        first_blocker = moves[first]["blocker"]
        for second in by_source.get(target, []):
            if moves[second]["blocker"] != first_blocker:
                adjacency.add_edge(first, second)

    return not nx.is_directed_acyclic_graph(adjacency)


def fast_reduced_core_audit(key):
    graph, moves, direction_map = exact_cover_moves_q3_4(key)
    digraph = nx.DiGraph(graph)
    output = []

    for component in terminal_sccs(digraph):
        box_labels = precompute_box_labels(direction_map, component)
        word_profiles = {
            word: word_box_profile(word, box_labels)
            for word in WORDS4
        }

        q_only_moves = [
            move_id
            for move_id, move in enumerate(moves)
            if move["source"] in component
            and move["target"] in component
            and word_profiles[move["word"]]["Q"] > 0
            and word_profiles[move["word"]]["N"] == 0
            and word_profiles[move["word"]]["S"] == 0
        ]

        output.append(
            {
                "component_size": len(component),
                "q_only_move_count": len(q_only_moves),
                "has_q_cycle": bool(q_only_moves)
                and not nx.is_directed_acyclic_graph(
                    nx.DiGraph(
                        [
                            (moves[move_id]["source"], moves[move_id]["target"])
                            for move_id in q_only_moves
                        ]
                    )
                ),
                "has_reduced_q_cycle": has_reduced_cycle(q_only_moves, moves)
                if q_only_moves else False,
            }
        )
    return output




# ---------------------------------------------------------------------------
# General four-block q=3 edge-minimal covers
# ---------------------------------------------------------------------------

LINE_MASKS4 = []
for words in LINE_WORDS4:
    mask = 0
    for word_index in words:
        mask |= 1 << word_index
    LINE_MASKS4.append(mask)
LINE_MASKS4 = tuple(LINE_MASKS4)
FULL_WORD_MASK4 = (1 << len(WORDS4)) - 1


def random_edge_minimal_cover_q3_4(rng: random.Random):
    uncovered = FULL_WORD_MASK4
    selected = []

    while uncovered:
        gains = []
        max_gain = 0
        for line_index, mask in enumerate(LINE_MASKS4):
            gain = (mask & uncovered).bit_count()
            if gain:
                if gain > max_gain:
                    max_gain = gain
                    gains = [line_index]
                elif gain == max_gain:
                    gains.append(line_index)
        # Mostly choose a best line, sometimes a near-best line to diversify.
        if rng.random() < 0.8:
            chosen = rng.choice(gains)
        else:
            candidates = [
                line_index
                for line_index, mask in enumerate(LINE_MASKS4)
                if (mask & uncovered).bit_count() >= max(1, max_gain - 1)
            ]
            chosen = rng.choice(candidates)
        selected.append(chosen)
        uncovered &= ~LINE_MASKS4[chosen]

    # Inclusion-minimize in random order.
    changed = True
    while changed:
        changed = False
        rng.shuffle(selected)
        for line_index in selected[:]:
            covered = 0
            for other in selected:
                if other != line_index:
                    covered |= LINE_MASKS4[other]
            if covered == FULL_WORD_MASK4:
                selected.remove(line_index)
                changed = True

    return tuple(sorted(selected))


def block_minimal_cover_q3_4(key):
    edges = [LINES4[index] for index in key]
    for deleted in range(4):
        active = [block for block in range(4) if block != deleted]
        if not any(
            not any(
                all(
                    block in dict(zip(active, values))
                    and dict(zip(active, values))[block] == value
                    for block, value in edge
                )
                for edge in edges
            )
            for values in product(range(3), repeat=3)
        ):
            return False
    return True


def blockers_by_word_general_q3_4(key):
    blockers = [[] for _ in WORDS4]
    for line_index in key:
        for word_index in LINE_WORDS4[line_index]:
            blockers[word_index].append(line_index)
    return tuple(tuple(items) for items in blockers)


def moves_general_q3_4(key):
    blockers_by_word = blockers_by_word_general_q3_4(key)
    states = []
    edge_sets = {line_index: set(LINES4[line_index]) for line_index in key}

    for missing in range(4):
        for values in product(range(3), repeat=3):
            iterator = iter(values)
            state = tuple(
                None if block == missing else next(iterator)
                for block in range(4)
            )
            selected = {
                (block, value)
                for block, value in enumerate(state)
                if value is not None
            }
            if any(edge_sets[line_index] <= selected for line_index in key):
                continue
            states.append(state)

    state_set = set(states)
    graph = nx.MultiDiGraph()
    graph.add_nodes_from(states)
    moves = []

    for state in states:
        missing = state.index(None)
        for attempted in range(3):
            word = tuple(
                attempted if block == missing else state[block]
                for block in range(4)
            )
            word_index = WORD_INDEX4[word]
            for line_index in blockers_by_word[word_index]:
                edge = LINES4[line_index]
                for released_block, released_value in edge:
                    if released_block == missing:
                        continue
                    target = list(state)
                    target[missing] = attempted
                    target[released_block] = None
                    target = tuple(target)
                    if target not in state_set:
                        continue
                    move_id = len(moves)
                    moves.append(
                        {
                            "source": state,
                            "target": target,
                            "attempted": attempted,
                            "word": word,
                            "blocker": line_index,
                            "released_block": released_block,
                            "blocker_count": len(blockers_by_word[word_index]),
                        }
                    )
                    graph.add_edge(
                        state, target, key=move_id, move_id=move_id
                    )
    return graph, moves, blockers_by_word


def classify_general_box(value_pairs, component, blockers_by_word):
    directions = {}
    for bits in product((0, 1), repeat=4):
        word = tuple(value_pairs[i][bits[i]] for i in range(4))
        blockers = blockers_by_word[WORD_INDEX4[word]]
        if len(blockers) != 1:
            return "M"
        line_index = blockers[0]
        omitted = next(
            block
            for block in range(4)
            if block not in {b for b, _ in LINES4[line_index]}
        )
        directions[bits] = omitted

        blocker_blocks = set(range(4)) - {omitted}
        for hole in blocker_blocks:
            candidate = tuple(
                None if block == hole else word[block]
                for block in range(4)
            )
            if candidate not in component:
                return "S"

    for bits, direction in directions.items():
        flipped = list(bits)
        flipped[direction] ^= 1
        if directions[tuple(flipped)] != direction:
            return "N"

    if all(
        len({directions[bits] for bits in face}) == 3
        for face in Q4_FACES
    ):
        return "Q"
    return "N"


def audit_general_cover_q3_4(key):
    graph, moves, blockers_by_word = moves_general_q3_4(key)
    digraph = nx.DiGraph(graph)
    components = []

    for component in terminal_sccs(digraph):
        box_labels = {
            value_pairs: classify_general_box(
                value_pairs, component, blockers_by_word
            )
            for value_pairs in BOXES_Q3_4
        }
        word_profiles = {
            word: word_box_profile(word, box_labels)
            for word in WORDS4
        }

        residual_moves = []
        q_only_moves = []
        s_or_q_moves = []

        for move_id, move in enumerate(moves):
            if move["source"] not in component or move["target"] not in component:
                continue
            profile = word_profiles[move["word"]]
            # M and N are certified modules. S and Q remain uncharged.
            if profile["M"] == 0 and profile["N"] == 0:
                residual_moves.append(move_id)
                if profile["Q"] > 0 and profile["S"] == 0:
                    q_only_moves.append(move_id)
                if profile["Q"] > 0 or profile["S"] > 0:
                    s_or_q_moves.append(move_id)

        components.append(
            {
                "size": len(component),
                "move_count": sum(
                    1 for move in moves
                    if move["source"] in component and move["target"] in component
                ),
                "box_profile": dict(Counter(box_labels.values())),
                "residual_move_count": len(residual_moves),
                "q_only_move_count": len(q_only_moves),
                "has_raw_residual_cycle": bool(residual_moves)
                and not nx.is_directed_acyclic_graph(
                    nx.DiGraph(
                        [
                            (moves[mid]["source"], moves[mid]["target"])
                            for mid in residual_moves
                        ]
                    )
                ),
                "has_reduced_residual_cycle": has_reduced_cycle(
                    residual_moves, moves
                ) if residual_moves else False,
                "has_reduced_q_only_cycle": has_reduced_cycle(
                    q_only_moves, moves
                ) if q_only_moves else False,
            }
        )
    return components




# ---------------------------------------------------------------------------
# Five-block q=3 random edge-minimal covers with staged localization audit
# ---------------------------------------------------------------------------

M5 = 5
WORDS5 = tuple(product(range(3), repeat=M5))
WORD_INDEX5 = {word: i for i, word in enumerate(WORDS5)}

EDGES5 = []
EDGE_WORDS5 = []
EDGE_MASKS5 = []

for blocks in combinations(range(M5), 3):
    for values in product(range(3), repeat=3):
        edge = tuple(zip(blocks, values))
        word_indices = []
        for word in WORDS5:
            if all(word[block] == value for block, value in edge):
                word_indices.append(WORD_INDEX5[word])
        mask = 0
        for index in word_indices:
            mask |= 1 << index
        EDGES5.append(edge)
        EDGE_WORDS5.append(tuple(word_indices))
        EDGE_MASKS5.append(mask)

EDGES5 = tuple(EDGES5)
EDGE_WORDS5 = tuple(EDGE_WORDS5)
EDGE_MASKS5 = tuple(EDGE_MASKS5)
FULL_WORD_MASK5 = (1 << len(WORDS5)) - 1


def random_edge_minimal_cover_q3_5(rng):
    uncovered = FULL_WORD_MASK5
    selected = []

    while uncovered:
        gains = []
        max_gain = 0
        for edge_index, mask in enumerate(EDGE_MASKS5):
            gain = (mask & uncovered).bit_count()
            if gain > max_gain:
                max_gain = gain
                gains = [edge_index]
            elif gain == max_gain and gain:
                gains.append(edge_index)
        if rng.random() < 0.85:
            chosen = rng.choice(gains)
        else:
            candidates = [
                edge_index
                for edge_index, mask in enumerate(EDGE_MASKS5)
                if (mask & uncovered).bit_count() >= max(1, max_gain - 2)
            ]
            chosen = rng.choice(candidates)
        selected.append(chosen)
        uncovered &= ~EDGE_MASKS5[chosen]

    changed = True
    while changed:
        changed = False
        rng.shuffle(selected)
        for edge_index in selected[:]:
            covered = 0
            for other in selected:
                if other != edge_index:
                    covered |= EDGE_MASKS5[other]
            if covered == FULL_WORD_MASK5:
                selected.remove(edge_index)
                changed = True

    return tuple(sorted(selected))


def block_minimal_q3_5(key):
    edges = [EDGES5[index] for index in key]
    for deleted in range(5):
        active = [block for block in range(5) if block != deleted]
        found = False
        for values in product(range(3), repeat=4):
            chosen = dict(zip(active, values))
            if not any(
                all(
                    block in chosen and chosen[block] == value
                    for block, value in edge
                )
                for edge in edges
            ):
                found = True
                break
        if not found:
            return False
    return True


def blockers_by_word_q3_5(key):
    result = [[] for _ in WORDS5]
    for edge_index in key:
        for word_index in EDGE_WORDS5[edge_index]:
            result[word_index].append(edge_index)
    return tuple(tuple(items) for items in result)


def one_hole_graph_q3_5(key):
    blockers_by_word = blockers_by_word_q3_5(key)
    selected_edge_sets = {
        edge_index: set(EDGES5[edge_index]) for edge_index in key
    }

    states = []
    for missing in range(5):
        for values in product(range(3), repeat=4):
            iterator = iter(values)
            state = tuple(
                None if block == missing else next(iterator)
                for block in range(5)
            )
            chosen = {
                (block, value)
                for block, value in enumerate(state)
                if value is not None
            }
            if any(
                selected_edge_sets[edge_index] <= chosen
                for edge_index in key
            ):
                continue
            states.append(state)

    state_set = set(states)
    graph = nx.MultiDiGraph()
    graph.add_nodes_from(states)
    moves = []
    state_initial_profile = {}

    for state in states:
        missing = state.index(None)
        attempt_blockers = {}
        required_blocks = {missing}

        for attempted in range(3):
            word = tuple(
                attempted if block == missing else state[block]
                for block in range(5)
            )
            blockers = blockers_by_word[WORD_INDEX5[word]]
            attempt_blockers[attempted] = blockers
            for edge_index in blockers:
                required_blocks.update(
                    block for block, value in EDGES5[edge_index]
                )

        if any(len(items) >= 2 for items in attempt_blockers.values()):
            initial_label = "M"
        elif len(required_blocks) > 4:
            initial_label = "W"
        else:
            initial_label = "U"

        state_initial_profile[state] = {
            "label": initial_label,
            "required_blocks": frozenset(required_blocks),
            "attempt_blockers": attempt_blockers,
        }

        for attempted, blockers in attempt_blockers.items():
            word = tuple(
                attempted if block == missing else state[block]
                for block in range(5)
            )
            for edge_index in blockers:
                edge = EDGES5[edge_index]
                for released_block, released_value in edge:
                    if released_block == missing:
                        continue
                    target = list(state)
                    target[missing] = attempted
                    target[released_block] = None
                    target = tuple(target)
                    if target not in state_set:
                        continue
                    move_id = len(moves)
                    moves.append(
                        {
                            "source": state,
                            "target": target,
                            "attempted": attempted,
                            "word": word,
                            "blocker": edge_index,
                            "released_block": released_block,
                            "blocker_count": len(blockers),
                        }
                    )
                    graph.add_edge(
                        state, target, key=move_id, move_id=move_id
                    )

    return graph, moves, blockers_by_word, state_initial_profile


def terminal_components_multigraph(graph):
    digraph = nx.DiGraph(graph)
    return terminal_sccs(digraph)


def has_reduced_cycle_ids(move_ids, moves):
    if not move_ids:
        return False
    return has_reduced_cycle(move_ids, moves)


def classify_five_block_binary_box(
    four_blocks,
    outside_values,
    value_pairs,
    component,
    blockers_by_word,
):
    directions = {}
    sorted_four = sorted(four_blocks)

    for bits in product((0, 1), repeat=4):
        assignment = {
            block: value_pairs[index][bits[index]]
            for index, block in enumerate(sorted_four)
        }
        word = tuple(
            assignment[block]
            if block in four_blocks
            else outside_values[block]
            for block in range(5)
        )
        blockers = blockers_by_word[WORD_INDEX5[word]]

        if len(blockers) != 1:
            return "M"

        edge_index = blockers[0]
        blocker_blocks = {
            block for block, value in EDGES5[edge_index]
        }
        if not blocker_blocks <= four_blocks:
            return "A"

        omitted = next(
            block for block in four_blocks if block not in blocker_blocks
        )
        local_direction = sorted_four.index(omitted)
        directions[bits] = local_direction

        for hole in blocker_blocks:
            candidate = tuple(
                None if block == hole else word[block]
                for block in range(5)
            )
            if candidate not in component:
                return "S"

    for bits, direction in directions.items():
        flipped = list(bits)
        flipped[direction] ^= 1
        if directions[tuple(flipped)] != direction:
            return "N"

    if all(
        len({directions[bits] for bits in face}) == 3
        for face in Q4_FACES
    ):
        return "Q"
    return "N"


def detailed_candidate_audit_q3_5(
    component,
    moves,
    blockers_by_word,
    state_profiles,
):
    # Precompute box labels only for unclassified states that survive W/M.
    move_certificates = {}
    component_set = set(component)

    for move_id, move in enumerate(moves):
        source = move["source"]
        if source not in component_set or move["target"] not in component_set:
            continue

        initial = state_profiles[source]
        if initial["label"] in {"W", "M"}:
            move_certificates[move_id] = Counter({initial["label"]: 1})
            continue

        required = set(initial["required_blocks"])
        candidate_four_sets = [
            set(required) | set(extra)
            for extra in combinations(
                [block for block in range(5) if block not in required],
                4 - len(required),
            )
        ]

        word = move["word"]
        certificates = Counter()

        for four_blocks in candidate_four_sets:
            outside_values = {
                block: word[block]
                for block in range(5)
                if block not in four_blocks
            }
            sorted_four = sorted(four_blocks)
            pair_options = [
                [
                    pair
                    for pair in combinations(range(3), 2)
                    if word[block] in pair
                ]
                for block in sorted_four
            ]
            for value_pairs in product(*pair_options):
                label = classify_five_block_binary_box(
                    four_blocks,
                    outside_values,
                    value_pairs,
                    component_set,
                    blockers_by_word,
                )
                certificates[label] += 1

        if not certificates:
            certificates["S"] = 1
        move_certificates[move_id] = certificates

    residual_move_ids = []
    q_only_move_ids = []
    s_involving_move_ids = []

    for move_id, certs in move_certificates.items():
        # Charge W/M/A/N. Leave S and Q as potential core behavior.
        if not any(certs[label] > 0 for label in ("W", "M", "A", "N")):
            residual_move_ids.append(move_id)
            if certs["Q"] > 0 and certs["S"] == 0:
                q_only_move_ids.append(move_id)
            if certs["S"] > 0:
                s_involving_move_ids.append(move_id)

    return {
        "residual_move_count": len(residual_move_ids),
        "q_only_move_count": len(q_only_move_ids),
        "s_move_count": len(s_involving_move_ids),
        "has_reduced_residual_cycle": has_reduced_cycle_ids(
            residual_move_ids, moves
        ),
        "has_reduced_q_cycle": has_reduced_cycle_ids(
            q_only_move_ids, moves
        ),
        "certificate_profile": dict(
            Counter(
                "+".join(
                    label
                    for label in ("W", "M", "A", "N", "S", "Q")
                    if certs[label] > 0
                )
                for certs in move_certificates.values()
            )
        ),
    }


def audit_q3_5_cover(key):
    graph, moves, blockers_by_word, state_profiles = one_hole_graph_q3_5(key)
    results = []

    for component in terminal_components_multigraph(graph):
        component_move_ids = [
            move_id
            for move_id, move in enumerate(moves)
            if move["source"] in component and move["target"] in component
        ]
        cheap_residual = [
            move_id
            for move_id in component_move_ids
            if state_profiles[moves[move_id]["source"]]["label"] == "U"
        ]
        cheap_has_reduced_cycle = has_reduced_cycle_ids(
            cheap_residual, moves
        )

        if cheap_has_reduced_cycle:
            detailed = detailed_candidate_audit_q3_5(
                component,
                moves,
                blockers_by_word,
                state_profiles,
            )
        else:
            detailed = {
                "residual_move_count": 0,
                "q_only_move_count": 0,
                "s_move_count": 0,
                "has_reduced_residual_cycle": False,
                "has_reduced_q_cycle": False,
                "certificate_profile": {},
            }

        results.append(
            {
                "component_size": len(component),
                "move_count": len(component_move_ids),
                "cheap_candidate_cycle": cheap_has_reduced_cycle,
                **detailed,
            }
        )
    return results




def run_exact_search_2000(target=2000, seed=20260737):
    rng = random.Random(seed)
    seen = set()
    counts = Counter()
    raw_kernel_sizes = Counter()
    attempts = 0
    started = time.time()

    while len(seen) < target and attempts < target * 20:
        attempts += 1
        key = random_exact_cover_q3_4(rng)
        if key is None or key in seen:
            continue
        if not block_minimal_exact_cover_q3_4(key):
            continue
        seen.add(key)

        raw_audit = fast_transition_core_audit(key)
        reduced_audit = fast_reduced_core_audit(key)

        raw = any(c["residual_q_core"] for c in raw_audit)
        reduced = any(c["has_reduced_q_cycle"] for c in reduced_audit)
        counts["raw_q_cycle"] += int(raw)
        counts["reduced_q_cycle"] += int(reduced)
        counts["N_covered_or_same_edge_R_only"] += int(not reduced)

        for component in raw_audit:
            for kernel in component["q_only_kernels"]:
                raw_kernel_sizes[
                    (kernel["state_count"], kernel["move_count"])
                ] += 1

    return {
        "target": target,
        "attempts": attempts,
        "unique_block_minimal_exact_covers": len(seen),
        "elapsed_seconds": time.time() - started,
        "classification": dict(counts),
        "raw_kernel_sizes": {
            f"{states} states/{moves} moves": count
            for (states, moves), count in sorted(raw_kernel_sizes.items())
        },
    }



def run_general4_search_2000(target=2000, seed=20260738):
    rng = random.Random(seed)
    seen = set()
    counts = Counter()
    edge_counts = Counter()
    attempts = 0
    started = time.time()

    while len(seen) < target and attempts < target * 20:
        attempts += 1
        key = random_edge_minimal_cover_q3_4(rng)
        if key in seen:
            continue
        if not block_minimal_cover_q3_4(key):
            continue
        seen.add(key)

        audit = audit_general_cover_q3_4(key)
        reduced = any(c["has_reduced_residual_cycle"] for c in audit)
        q_only = any(c["has_reduced_q_only_cycle"] for c in audit)
        counts["reduced_residual_cycle"] += int(reduced)
        counts["reduced_q_only_cycle"] += int(q_only)
        counts["covered_after_MN_and_same_edge_reduction"] += int(not reduced)
        edge_counts[len(key)] += 1

    return {
        "target": target,
        "attempts": attempts,
        "unique_block_minimal_covers": len(seen),
        "elapsed_seconds": time.time() - started,
        "classification": dict(counts),
        "edge_count_distribution": dict(sorted(edge_counts.items())),
    }




if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Route-B b=3 reduced core search."
    )
    parser.add_argument("--exact", type=int, default=2000)
    parser.add_argument("--general4", type=int, default=2000)
    parser.add_argument("--general5", type=int, default=200)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/runs/route_b/route_b_b3_search.json"),
    )
    args = parser.parse_args()

    exact_result = run_exact_search_2000(
        target=args.exact,
        seed=20260737,
    )
    general4_result = run_general4_search_2000(
        target=args.general4,
        seed=20260738,
    )

    rng5 = random.Random(20260734)
    keys5 = set()
    records5 = []
    attempts5 = 0
    started5 = time.time()

    while len(records5) < args.general5 and attempts5 < args.general5 * 30:
        attempts5 += 1
        key = random_edge_minimal_cover_q3_5(rng5)
        if key in keys5:
            continue
        keys5.add(key)
        if not block_minimal_q3_5(key):
            continue
        records5.append((key, audit_q3_5_cover(key)))

    counter5 = Counter()
    edge_counts5 = Counter()
    for key, components in records5:
        edge_counts5[len(key)] += 1
        cheap = any(c["cheap_candidate_cycle"] for c in components)
        residual = any(c["has_reduced_residual_cycle"] for c in components)
        qcore = any(c["has_reduced_q_cycle"] for c in components)
        counter5["cheap_candidate_models"] += int(cheap)
        counter5["reduced_residual_core"] += int(residual)
        counter5["reduced_q_core"] += int(qcore)
        counter5["covered_after_WMAN_and_reduction"] += int(not residual)

    five_result = {
        "attempts": attempts5,
        "block_minimal_covers_audited": len(records5),
        "elapsed_seconds": time.time() - started5,
        "edge_count_distribution": dict(sorted(edge_counts5.items())),
        "classification": dict(counter5),
    }

    output = {
        "four_block_exact_cover": exact_result,
        "four_block_general_cover": general4_result,
        "five_block_general_cover": five_result,
    }
    args.output.write_text(
        json.dumps(output, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(json.dumps(output, indent=2, ensure_ascii=False))
