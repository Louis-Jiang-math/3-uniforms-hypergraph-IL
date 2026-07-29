from __future__ import annotations

import hashlib
import math
import time
from collections import Counter
from itertools import combinations, permutations, product
from typing import Dict, List, Optional, Sequence, Tuple

import networkx as nx
import numpy as np
import scipy.sparse as sp
from scipy.optimize import Bounds, LinearConstraint, linprog, milp

from .execution import (
    Configuration,
    ExecutionRecord,
    Obligation,
    RootGroup,
    SlotKey,
    build_root_groups,
)
from .models import Edge, Hypergraph, Vertex, canonical_edge, edge_name, vertex_name


def configuration_budget_lp(group: RootGroup) -> Dict:
    obligations = group.obligations
    if any(not obligation.configurations for obligation in obligations):
        return {
            "status": "no-configuration",
            "no_configuration_ids": [
                obligation.obligation_id
                for obligation in obligations
                if not obligation.configurations
            ],
        }

    pivots = sorted(
        {
            configuration.pivot
            for obligation in obligations
            for configuration in obligation.configurations
        }
    )
    slots = sorted(
        {
            configuration.slot
            for obligation in obligations
            for configuration in obligation.configurations
        }
    )
    q_variables = [
        (a_index, c_index, configuration)
        for a_index, obligation in enumerate(obligations)
        for c_index, configuration in enumerate(obligation.configurations)
    ]
    q_count = len(q_variables)
    variable_count = q_count + len(pivots)
    objective = np.zeros(variable_count)
    objective[q_count:] = 1.0

    equality_rows = []
    equality_rhs = []
    for a_index, obligation in enumerate(obligations):
        row = np.zeros(variable_count)
        for q_index, (candidate_a, _, _) in enumerate(q_variables):
            if candidate_a == a_index:
                row[q_index] = 1.0
        equality_rows.append(row)
        equality_rhs.append(obligation.weight)

    upper_rows = []
    upper_rhs = []
    for slot in slots:
        row = np.zeros(variable_count)
        for q_index, (_, _, configuration) in enumerate(q_variables):
            if configuration.slot == slot:
                row[q_index] = 1.0
        row[q_count + pivots.index(slot.pivot)] = -1.0
        upper_rows.append(row)
        upper_rhs.append(0.0)

    primal = linprog(
        objective,
        A_ub=np.asarray(upper_rows),
        b_ub=np.asarray(upper_rhs),
        A_eq=np.asarray(equality_rows),
        b_eq=np.asarray(equality_rhs),
        bounds=(0, None),
        method="highs",
    )
    if not primal.success:
        return {"status": "lp-failure", "message": primal.message}

    dual_count = len(obligations) + len(slots)
    dual_objective = np.zeros(dual_count)
    dual_objective[: len(obligations)] = [
        -obligation.weight for obligation in obligations
    ]
    dual_rows = []
    dual_rhs = []
    for a_index, obligation in enumerate(obligations):
        for slot in {configuration.slot for configuration in obligation.configurations}:
            row = np.zeros(dual_count)
            row[a_index] = 1.0
            row[len(obligations) + slots.index(slot)] = -1.0
            dual_rows.append(row)
            dual_rhs.append(0.0)
    for pivot in pivots:
        row = np.zeros(dual_count)
        for slot_index, slot in enumerate(slots):
            if slot.pivot == pivot:
                row[len(obligations) + slot_index] = 1.0
        dual_rows.append(row)
        dual_rhs.append(1.0)

    dual = linprog(
        dual_objective,
        A_ub=np.asarray(dual_rows),
        b_ub=np.asarray(dual_rhs),
        bounds=(0, None),
        method="highs",
    )
    if not dual.success:
        return {"status": "dual-failure", "message": dual.message}

    t_min = float(primal.fun)
    dual_value = float(-dual.fun)
    q_solution = {}
    for q_index, (a_index, c_index, configuration) in enumerate(q_variables):
        value = float(primal.x[q_index])
        if value > 1e-9:
            q_solution[f"{obligations[a_index].obligation_id}:c{c_index}"] = {
                "flow": value,
                "root_projection_id": configuration.root_projection_id,
                "pivot": vertex_name(configuration.pivot),
                "edge": edge_name(configuration.root_edge),
            }
    return {
        "status": "optimal",
        "t_min": t_min,
        "eta": max(0.0, t_min - 1.0),
        "primal_objective": t_min,
        "dual_objective": dual_value,
        "duality_gap": abs(t_min - dual_value),
        "q": q_solution,
        "root_projection_id": group.root_record.root_projection_id,
    }


def flow_cut_summary(graph: nx.DiGraph, source: str, sink: str) -> Dict:
    value, _ = nx.maximum_flow(graph, source, sink, capacity="capacity")
    cut_value, partition = nx.minimum_cut(graph, source, sink, capacity="capacity")
    source_side, sink_side = partition
    cut_edges = sorted(
        [
            {"from": str(u), "to": str(v), "capacity": float(attrs["capacity"])}
            for u in source_side
            for v, attrs in graph[u].items()
            if v in sink_side and attrs.get("capacity", 0) > 0
        ],
        key=lambda item: (item["from"], item["to"], item["capacity"]),
    )
    return {
        "max_flow": float(value),
        "min_cut": float(cut_value),
        "source_side": sorted(map(str, source_side)),
        "sink_side": sorted(map(str, sink_side)),
        "cut_edges": cut_edges,
    }


def fixed_budget_slot_flow(group: RootGroup, lambdas: Dict[Vertex, float]) -> Dict:
    graph = nx.DiGraph()
    source, sink = "source", "sink"
    demand = sum(obligation.weight for obligation in group.obligations)
    slots = set()
    for obligation in group.obligations:
        obligation_node = f"a:{obligation.obligation_id}"
        graph.add_edge(source, obligation_node, capacity=obligation.weight)
        for configuration in obligation.configurations:
            slot = configuration.slot
            slots.add(slot)
            slot_node = (
                f"slot:{slot.root_projection_id}|{vertex_name(slot.pivot)}|"
                f"{edge_name(slot.root_edge)}"
            )
            graph.add_edge(obligation_node, slot_node, capacity=demand + 1.0)
    for slot in sorted(slots):
        slot_node = (
            f"slot:{slot.root_projection_id}|{vertex_name(slot.pivot)}|"
            f"{edge_name(slot.root_edge)}"
        )
        graph.add_edge(slot_node, sink, capacity=float(lambdas.get(slot.pivot, 0.0)))
    answer = flow_cut_summary(graph, source, sink)
    answer["demand"] = float(demand)
    answer["unmet"] = float(demand - answer["max_flow"])
    answer["ledger"] = "slot"
    return answer


def global_real_edge_flow(group: RootGroup, edge_capacity: float = 1.0) -> Dict:
    graph = nx.DiGraph()
    source, sink = "source", "sink"
    demand = sum(obligation.weight for obligation in group.obligations)
    real_edges = set()
    for obligation in group.obligations:
        obligation_node = f"a:{obligation.obligation_id}"
        graph.add_edge(source, obligation_node, capacity=obligation.weight)
        for configuration in obligation.configurations:
            edge = configuration.root_edge
            real_edges.add(edge)
            graph.add_edge(
                obligation_node, f"edge:{edge_name(edge)}", capacity=demand + 1.0
            )
    for edge in sorted(real_edges):
        graph.add_edge(f"edge:{edge_name(edge)}", sink, capacity=edge_capacity)
    answer = flow_cut_summary(graph, source, sink)
    answer["demand"] = float(demand)
    answer["unmet"] = float(demand - answer["max_flow"])
    answer["ledger"] = "global-real-edge"
    return answer


def classify_group(group: RootGroup) -> Tuple[str, Dict]:
    lp = configuration_budget_lp(group)
    if lp["status"] == "no-configuration":
        return "no-configuration", lp
    if lp["status"] != "optimal":
        return "solver-failure", lp
    if lp["eta"] <= 1e-8:
        return "zero-error-budget-feasible", lp
    return "positive-root-budget-gap", lp


def eight_edge_model() -> Hypergraph:
    return Hypergraph.build(
        4,
        2,
        [
            ((0, 0), (1, 0), (2, 0)),
            ((0, 0), (1, 1), (3, 0)),
            ((0, 0), (2, 1), (3, 1)),
            ((0, 1), (1, 0), (3, 1)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 1), (2, 0), (3, 0)),
            ((1, 0), (2, 1), (3, 0)),
            ((1, 1), (2, 0), (3, 1)),
        ],
    )


def nine_edge_repair_model() -> Hypergraph:
    base = eight_edge_model()
    new_edge = canonical_edge(((0, 0), (1, 0), (2, 1)))
    edges = (new_edge,) + base.edges
    return Hypergraph.build(4, 2, edges, edge_order=edges)


def model_minimality_report(hg: Hypergraph) -> Dict:
    full_it = hg.find_independent_transversal()
    edge_witnesses = {}
    for deleted in hg.edges:
        reduced = Hypergraph.build(hg.m, hg.b, [edge for edge in hg.edges if edge != deleted])
        witness = reduced.find_independent_transversal()
        edge_witnesses[edge_name(deleted)] = [vertex_name(v) for v in witness] if witness else None
    block_witnesses = {}
    for deleted_block in range(hg.m):
        active = [block for block in range(hg.m) if block != deleted_block]
        witness = hg.find_independent_transversal(active)
        block_witnesses[str(deleted_block)] = [vertex_name(v) for v in witness] if witness else None
    return {
        "independent_transversal": [vertex_name(v) for v in full_it] if full_it else None,
        "no_IT": full_it is None,
        "max_degree": hg.max_degree(),
        "edge_minimal_no_IT": all(edge_witnesses.values()),
        "block_minimal_no_IT": all(block_witnesses.values()),
    }


def run_regressions() -> Dict:
    hg8 = eight_edge_model()
    all_groups: List[RootGroup] = []
    classification_counter = Counter()
    for order in permutations(range(4)):
        groups = build_root_groups(hg8, order)
        all_groups.extend(groups)
        for group in groups:
            classification, _ = classify_group(group)
            classification_counter[classification] += 1

    specified = next(
        group
        for group in all_groups
        if group.block_order == (0, 1, 2, 3)
        and group.root_record.trace == ((0, 0), (1, 0))
        and group.success_block == 2
        and group.failure_block == 3
    )
    specified_lp = configuration_budget_lp(specified)
    specified_fixed = fixed_budget_slot_flow(specified, {(0, 0): 0.5, (1, 0): 0.5})
    specified_real = global_real_edge_flow(specified, 1.0)

    repair_groups = build_root_groups(nine_edge_repair_model(), (0, 3, 1, 2))
    repair = next(
        group
        for group in repair_groups
        if len(group.obligations) >= 2
        and configuration_budget_lp(group).get("eta", math.inf) <= 1e-8
        and len({c.pivot for o in group.obligations for c in o.configurations}) == 1
        and len({c.root_edge for o in group.obligations for c in o.configurations}) >= 2
    )

    single_group = next(
        group
        for group in all_groups
        if len(group.obligations) == 1 and classify_group(group)[0] == "zero-error-budget-feasible"
    )
    original = single_group.obligations[0]
    projection_b = "synthetic-projection-B"
    cloned = Obligation(
        obligation_id="synthetic-clone",
        parent_record_id="synthetic-parent-B",
        root_projection_id=projection_b,
        inserted_vertex=original.inserted_vertex,
        attempted_vertex=original.attempted_vertex,
        first_edge=original.first_edge,
        weight=original.weight,
        configurations=tuple(
            Configuration(
                root_record_id="synthetic-root-B",
                root_projection_id=projection_b,
                released_vertex=c.released_vertex,
                pivot=c.pivot,
                root_edge=c.root_edge,
                released_trace=c.released_trace,
            )
            for c in original.configurations
        ),
    )
    root_a = RootGroup(
        single_group.block_order,
        single_group.root_record,
        single_group.success_block,
        single_group.failure_block,
        [original],
    )
    root_b_record = ExecutionRecord(
        "synthetic-root-B",
        projection_b,
        single_group.root_record.block_word,
        single_group.root_record.trace,
        single_group.root_record.genealogy + ("synthetic:B",),
    )
    root_b = RootGroup(
        single_group.block_order,
        root_b_record,
        single_group.success_block,
        single_group.failure_block,
        [cloned],
    )
    # This deliberately strips projection identity to reproduce the forbidden merge.
    merged_projection = "incorrectly-merged-projection"
    merged_configs = []
    for obligation in (original, cloned):
        merged_configs.append(
            Obligation(
                obligation_id=obligation.obligation_id,
                parent_record_id=obligation.parent_record_id,
                root_projection_id=merged_projection,
                inserted_vertex=obligation.inserted_vertex,
                attempted_vertex=obligation.attempted_vertex,
                first_edge=obligation.first_edge,
                weight=obligation.weight,
                configurations=tuple(
                    Configuration(
                        root_record_id="incorrectly-merged-root",
                        root_projection_id=merged_projection,
                        released_vertex=c.released_vertex,
                        pivot=c.pivot,
                        root_edge=c.root_edge,
                        released_trace=c.released_trace,
                    )
                    for c in obligation.configurations
                ),
            )
        )
    merged = RootGroup(
        single_group.block_order,
        ExecutionRecord(
            "incorrectly-merged-root",
            merged_projection,
            single_group.root_record.block_word,
            single_group.root_record.trace,
            ("forbidden:merge",),
        ),
        single_group.success_block,
        single_group.failure_block,
        merged_configs,
    )

    return {
        "schema_version": "q0015-regressions-v2",
        "eight_edge_model": model_minimality_report(hg8),
        "specified_window": {
            "obligation_count": len(specified.obligations),
            "budget_lp": specified_lp,
            "fixed_half_budget_flow": specified_fixed,
            "global_real_edge_flow": specified_real,
        },
        "all_24_orders": {
            "root_groups_with_failures": len(all_groups),
            "classification": dict(classification_counter),
        },
        "nine_edge_repair": {
            "obligation_count": len(repair.obligations),
            "budget_lp": configuration_budget_lp(repair),
        },
        "genealogy_collision": {
            "root_A_t_min": configuration_budget_lp(root_a)["t_min"],
            "root_B_t_min": configuration_budget_lp(root_b)["t_min"],
            "incorrectly_merged_t_min": configuration_budget_lp(merged)["t_min"],
            "incorrectly_merged_eta": configuration_budget_lp(merged)["eta"],
        },
    }


def all_possible_edges(m: int, b: int) -> List[Tuple[Vertex, Vertex, Vertex]]:
    return [
        tuple(zip(blocks, values))
        for blocks in combinations(range(m), 3)
        for values in product(range(b), repeat=3)
    ]


def counting_obstruction(m: int, b: int, degree_bound: int) -> Dict:
    impossible = m * b * degree_bound < 3 * b**3
    return {
        "m": m,
        "b": b,
        "degree_bound": degree_bound,
        "minimum_edges_needed_by_transversal_counting": b**3,
        "maximum_edges_allowed_by_degree_sum": (m * b * degree_bound) // 3,
        "no_IT_candidate_impossible_by_counting": impossible,
    }


def find_it_from_selected_edges(
    m: int, b: int, selected_edges: Sequence[Tuple[Vertex, Vertex, Vertex]]
) -> Optional[Tuple[Vertex, ...]]:
    hg = Hypergraph.build(m, b, selected_edges)
    return hg.find_independent_transversal()


def cutting_plane_outer_search(
    m: int,
    b: int,
    degree_bound: int,
    max_iterations: int,
    per_iteration_time_limit: float,
) -> Dict:
    counting = counting_obstruction(m, b, degree_bound)
    if counting["no_IT_candidate_impossible_by_counting"]:
        return {"status": "infeasible-by-counting", "counting_certificate": counting, "iterations": []}

    edges = all_possible_edges(m, b)
    edge_count = len(edges)
    degree_rows: List[int] = []
    degree_cols: List[int] = []
    degree_data: List[float] = []
    row = 0
    for block in range(m):
        for index in range(b):
            vertex = (block, index)
            for edge_index, edge in enumerate(edges):
                if vertex in edge:
                    degree_rows.append(row)
                    degree_cols.append(edge_index)
                    degree_data.append(1.0)
            row += 1
    degree_matrix = sp.csr_matrix(
        (degree_data, (degree_rows, degree_cols)), shape=(m * b, edge_count)
    )
    base_matrices = [degree_matrix, sp.csr_matrix(np.ones((1, edge_count)))]
    base_lower = [np.full(m * b, -np.inf), np.array([float(b**3)])]
    base_upper = [np.full(m * b, float(degree_bound)), np.array([np.inf])]
    cuts: List[np.ndarray] = []
    iteration_log = []
    selected_edges: List[Tuple[Vertex, Vertex, Vertex]] = []
    last_witness = None

    for iteration in range(max_iterations):
        matrices = list(base_matrices)
        lower = list(base_lower)
        upper = list(base_upper)
        if cuts:
            rows = np.repeat(np.arange(len(cuts)), [len(cut) for cut in cuts])
            cols = np.concatenate(cuts)
            matrices.append(
                sp.csr_matrix((np.ones(len(cols)), (rows, cols)), shape=(len(cuts), edge_count))
            )
            lower.append(np.ones(len(cuts)))
            upper.append(np.full(len(cuts), np.inf))
        matrix = sp.vstack(matrices, format="csr")
        started = time.time()
        result = milp(
            np.ones(edge_count),
            integrality=np.ones(edge_count),
            bounds=Bounds(0.0, 1.0),
            constraints=LinearConstraint(matrix, np.concatenate(lower), np.concatenate(upper)),
            options={"time_limit": per_iteration_time_limit, "mip_rel_gap": 0.0},
        )
        elapsed = time.time() - started
        if result.x is None:
            return {
                "status": "solver-stopped-without-incumbent",
                "counting_certificate": counting,
                "iterations": iteration_log,
                "solver_message": result.message,
            }
        selected_indices = np.flatnonzero(result.x > 0.5)
        selected_edges = [edges[index] for index in selected_indices]
        witness = find_it_from_selected_edges(m, b, selected_edges)
        iteration_log.append(
            {
                "iteration": iteration,
                "elapsed_seconds": elapsed,
                "selected_edge_count": len(selected_edges),
                "IT_found": witness is not None,
                "IT_witness_hash": hashlib.sha256(repr(witness).encode()).hexdigest()[:16]
                if witness
                else None,
            }
        )
        if witness is None:
            candidate = Hypergraph.build(m, b, selected_edges)
            return {
                "status": "no-IT-candidate-found",
                "counting_certificate": counting,
                "iterations": iteration_log,
                "candidate": {
                    "max_degree": candidate.max_degree(),
                    "edges": [edge_name(canonical_edge(edge)) for edge in selected_edges],
                },
            }
        last_witness = witness
        witness_set = set(witness)
        cut = np.array(
            [index for index, edge in enumerate(edges) if set(edge) <= witness_set], dtype=int
        )
        if len(cut) != math.comb(m, 3):
            raise AssertionError("malformed transversal cover cut")
        cuts.append(cut)

    return {
        "status": "iteration-limit-reached-with-IT-certificates",
        "counting_certificate": counting,
        "edge_variable_count": edge_count,
        "cut_count": len(cuts),
        "iterations": iteration_log,
        "last_IT_witness": [vertex_name(v) for v in last_witness] if last_witness else None,
        "interpretation": "Non-exhaustive: every incumbent was refuted by an explicit IT.",
    }
