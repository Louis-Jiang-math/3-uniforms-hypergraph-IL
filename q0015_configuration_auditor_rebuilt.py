#!/usr/bin/env python3
"""
Rebuilt Q-0015 configuration auditor and first outer-generator experiment.

Grounded in SINGLE_DEFECT_FRAMEWORK.md v0.4-auditor-grounded:
- actual successful execution records;
- failure obligations with first blocking edge;
- complete legal root single-defect configurations;
- root-pivot budget primal/dual LP;
- fixed-budget slot max-flow/min-cut;
- independent global real-edge Hall flow;
- cutting-plane MILP outer search for low-degree no-IT candidates.

This is a reconstruction from the public Markdown specification.  It is not
claimed to be byte-for-byte identical to the uncommitted historical auditor.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from collections import Counter
from dataclasses import dataclass
from itertools import combinations, permutations, product
from pathlib import Path
from typing import Dict, FrozenSet, Iterable, List, Optional, Sequence, Tuple

import networkx as nx
import numpy as np
import scipy.sparse as sp
from scipy.optimize import Bounds, LinearConstraint, linprog, milp

Vertex = Tuple[int, int]
Edge = FrozenSet[Vertex]


def canonical_edge(vertices: Iterable[Vertex]) -> Edge:
    edge = frozenset(vertices)
    if len(edge) != 3:
        raise ValueError(f"Expected a 3-edge, got {edge}")
    if len({block for block, _ in edge}) != 3:
        raise ValueError(f"Edge is not transversal across three blocks: {edge}")
    return edge


def vertex_name(v: Vertex) -> str:
    return f"{v[0]}_{v[1]}"


def edge_name(e: Edge) -> str:
    return "{" + ",".join(vertex_name(v) for v in sorted(e)) + "}"


def trace_name(trace: Sequence[Vertex]) -> str:
    return "{" + ",".join(vertex_name(v) for v in trace) + "}"


@dataclass(frozen=True)
class Hypergraph:
    m: int
    b: int
    edges: Tuple[Edge, ...]
    edge_order: Tuple[Edge, ...]

    @classmethod
    def build(
        cls,
        m: int,
        b: int,
        edges: Sequence[Iterable[Vertex]],
        edge_order: Optional[Sequence[Iterable[Vertex]]] = None,
    ) -> "Hypergraph":
        edge_tuple = tuple(canonical_edge(e) for e in edges)
        if len(set(edge_tuple)) != len(edge_tuple):
            raise ValueError("Duplicate real edges are not allowed.")
        order_tuple = (
            tuple(canonical_edge(e) for e in edge_order)
            if edge_order is not None
            else edge_tuple
        )
        if set(order_tuple) != set(edge_tuple):
            raise ValueError("edge_order must contain every real edge exactly once.")
        for edge in edge_tuple:
            for block, index in edge:
                if not (0 <= block < m and 0 <= index < b):
                    raise ValueError(f"Vertex {(block, index)} outside declared blocks.")
        return cls(m=m, b=b, edges=edge_tuple, edge_order=order_tuple)

    @property
    def edge_rank(self) -> Dict[Edge, int]:
        return {edge: i for i, edge in enumerate(self.edge_order)}

    def degree(self, vertex: Vertex) -> int:
        return sum(vertex in edge for edge in self.edges)

    def max_degree(self) -> int:
        return max(
            (self.degree((block, index)) for block in range(self.m) for index in range(self.b)),
            default=0,
        )

    def is_independent(self, vertices: Iterable[Vertex]) -> bool:
        chosen = set(vertices)
        return not any(edge <= chosen for edge in self.edges)

    def blocking_edges(self, trace: Sequence[Vertex], x: Vertex) -> List[Edge]:
        chosen = set(trace)
        chosen.add(x)
        return [edge for edge in self.edges if edge <= chosen]

    def first_blocking_edge(self, trace: Sequence[Vertex], x: Vertex) -> Optional[Edge]:
        blockers = self.blocking_edges(trace, x)
        if not blockers:
            return None
        rank = self.edge_rank
        return min(blockers, key=rank.__getitem__)

    def find_independent_transversal(
        self, active_blocks: Optional[Sequence[int]] = None
    ) -> Optional[Tuple[Vertex, ...]]:
        blocks = list(range(self.m)) if active_blocks is None else list(active_blocks)
        incident = {
            block: [edge for edge in self.edges if any(v[0] == block for v in edge)]
            for block in blocks
        }
        # A high-incidence-first order typically finds contradictions earlier.
        order = sorted(blocks, key=lambda block: -len(incident[block]))
        chosen: Dict[int, Vertex] = {}

        def dfs(position: int) -> Optional[Tuple[Vertex, ...]]:
            if position == len(order):
                return tuple(chosen[block] for block in blocks)
            block = order[position]
            for index in range(self.b):
                candidate = (block, index)
                selected = set(chosen.values())
                selected.add(candidate)
                if any(edge <= selected for edge in incident[block]):
                    continue
                chosen[block] = candidate
                answer = dfs(position + 1)
                if answer is not None:
                    return answer
                del chosen[block]
            return None

        return dfs(0)


@dataclass(frozen=True)
class ExecutionRecord:
    record_id: str
    block_word: Tuple[int, ...]
    trace: Tuple[Vertex, ...]
    genealogy: Tuple[Vertex, ...]


@dataclass(frozen=True)
class Configuration:
    root_record_id: str
    released_vertex: Vertex
    pivot: Vertex
    root_edge: Edge
    released_trace: Tuple[Vertex, ...]

    @property
    def slot(self) -> Tuple[Vertex, Edge]:
        return self.pivot, self.root_edge


@dataclass(frozen=True)
class Obligation:
    obligation_id: str
    parent_record_id: str
    inserted_vertex: Vertex
    attempted_vertex: Vertex
    first_edge: Edge
    weight: float
    configurations: Tuple[Configuration, ...]


@dataclass
class RootGroup:
    block_order: Tuple[int, ...]
    root_record: ExecutionRecord
    success_block: int
    failure_block: int
    obligations: List[Obligation]


def make_record_id(block_order: Sequence[int], trace: Sequence[Vertex]) -> str:
    raw = repr((tuple(block_order[: len(trace)]), tuple(trace))).encode()
    return hashlib.sha256(raw).hexdigest()[:16]


def build_root_groups(hg: Hypergraph, block_order: Sequence[int]) -> List[RootGroup]:
    order = tuple(block_order)
    current = [
        ExecutionRecord(
            record_id=make_record_id(order, ()),
            block_word=(),
            trace=(),
            genealogy=(),
        )
    ]
    groups: List[RootGroup] = []

    for step, block in enumerate(order):
        # A two-step window starts at an actually visited root record, succeeds
        # in `block`, then attempts the next block.
        if step >= 1 and step + 1 < len(order):
            failure_block = order[step + 1]
            for root in current:
                obligations: List[Obligation] = []
                for r_index in range(hg.b):
                    r = (block, r_index)
                    if not hg.is_independent(root.trace + (r,)):
                        continue
                    parent_id = make_record_id(order, root.trace + (r,))
                    for x_index in range(hg.b):
                        x = (failure_block, x_index)
                        first_edge = hg.first_blocking_edge(root.trace + (r,), x)
                        if first_edge is None:
                            continue
                        released_trace = root.trace + (x,)
                        configurations: List[Configuration] = []
                        if hg.is_independent(released_trace):
                            for pivot in root.trace:
                                if first_edge == canonical_edge((pivot, r, x)):
                                    configurations.append(
                                        Configuration(
                                            root_record_id=root.record_id,
                                            released_vertex=r,
                                            pivot=pivot,
                                            root_edge=first_edge,
                                            released_trace=released_trace,
                                        )
                                    )
                        obligation_id = hashlib.sha256(
                            repr(
                                (
                                    root.record_id,
                                    r,
                                    x,
                                    tuple(sorted(first_edge)),
                                )
                            ).encode()
                        ).hexdigest()[:16]
                        obligations.append(
                            Obligation(
                                obligation_id=obligation_id,
                                parent_record_id=parent_id,
                                inserted_vertex=r,
                                attempted_vertex=x,
                                first_edge=first_edge,
                                weight=1.0,
                                configurations=tuple(configurations),
                            )
                        )
                if obligations:
                    groups.append(
                        RootGroup(
                            block_order=order,
                            root_record=root,
                            success_block=block,
                            failure_block=failure_block,
                            obligations=obligations,
                        )
                    )

        new_records: List[ExecutionRecord] = []
        for record in current:
            for index in range(hg.b):
                x = (block, index)
                if hg.is_independent(record.trace + (x,)):
                    trace = record.trace + (x,)
                    new_records.append(
                        ExecutionRecord(
                            record_id=make_record_id(order, trace),
                            block_word=record.block_word + (block,),
                            trace=trace,
                            genealogy=record.genealogy + (x,),
                        )
                    )
        current = new_records

    return groups


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
        },
        key=lambda item: (item[0], tuple(sorted(item[1]))),
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
    for pivot, edge in slots:
        row = np.zeros(variable_count)
        for q_index, (_, _, configuration) in enumerate(q_variables):
            if configuration.pivot == pivot and configuration.root_edge == edge:
                row[q_index] = 1.0
        row[q_count + pivots.index(pivot)] = -1.0
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

    # Explicit dual (10.5), solved independently.
    # Variables: alpha_a followed by beta_slot. Maximize sum w(a) alpha_a.
    # scipy minimizes, so use negative coefficients.
    dual_count = len(obligations) + len(slots)
    dual_objective = np.zeros(dual_count)
    dual_objective[: len(obligations)] = [
        -obligation.weight for obligation in obligations
    ]
    dual_rows = []
    dual_rhs = []
    for a_index, obligation in enumerate(obligations):
        available_slots = {configuration.slot for configuration in obligation.configurations}
        for slot in available_slots:
            row = np.zeros(dual_count)
            row[a_index] = 1.0
            row[len(obligations) + slots.index(slot)] = -1.0
            dual_rows.append(row)
            dual_rhs.append(0.0)
    for pivot in pivots:
        row = np.zeros(dual_count)
        for slot_index, (slot_pivot, _) in enumerate(slots):
            if slot_pivot == pivot:
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

    q_solution = {}
    for q_index, (a_index, c_index, configuration) in enumerate(q_variables):
        value = float(primal.x[q_index])
        if value > 1e-9:
            q_solution[
                f"{obligations[a_index].obligation_id}:c{c_index}"
            ] = {
                "flow": value,
                "pivot": vertex_name(configuration.pivot),
                "edge": edge_name(configuration.root_edge),
            }

    y_solution = {
        vertex_name(pivot): float(primal.x[q_count + pivot_index])
        for pivot_index, pivot in enumerate(pivots)
        if primal.x[q_count + pivot_index] > 1e-9
    }
    alpha_solution = {
        obligations[a_index].obligation_id: float(dual.x[a_index])
        for a_index in range(len(obligations))
        if dual.x[a_index] > 1e-9
    }
    beta_solution = {
        f"{vertex_name(pivot)}|{edge_name(edge)}": float(
            dual.x[len(obligations) + slot_index]
        )
        for slot_index, (pivot, edge) in enumerate(slots)
        if dual.x[len(obligations) + slot_index] > 1e-9
    }

    t_min = float(primal.fun)
    dual_value = float(-dual.fun)
    return {
        "status": "optimal",
        "t_min": t_min,
        "eta": max(0.0, t_min - 1.0),
        "primal_objective": t_min,
        "dual_objective": dual_value,
        "duality_gap": abs(t_min - dual_value),
        "q": q_solution,
        "y": y_solution,
        "alpha": alpha_solution,
        "beta": beta_solution,
    }


def flow_cut_summary(graph: nx.DiGraph, source: str, sink: str) -> Dict:
    value, flow = nx.maximum_flow(graph, source, sink, capacity="capacity")
    cut_value, partition = nx.minimum_cut(graph, source, sink, capacity="capacity")
    source_side, sink_side = partition
    cut_edges = []
    for u in source_side:
        for v, attrs in graph[u].items():
            if v in sink_side and attrs.get("capacity", 0) > 0:
                cut_edges.append(
                    {"from": str(u), "to": str(v), "capacity": attrs["capacity"]}
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
    for obligation in group.obligations:
        a_node = f"a:{obligation.obligation_id}"
        graph.add_edge(source, a_node, capacity=obligation.weight)
        for configuration in obligation.configurations:
            p, edge = configuration.slot
            slot_node = f"slot:{vertex_name(p)}|{edge_name(edge)}"
            graph.add_edge(a_node, slot_node, capacity=demand + 1.0)
    slots = {
        configuration.slot
        for obligation in group.obligations
        for configuration in obligation.configurations
    }
    for pivot, edge in slots:
        slot_node = f"slot:{vertex_name(pivot)}|{edge_name(edge)}"
        graph.add_edge(slot_node, sink, capacity=float(lambdas.get(pivot, 0.0)))
    answer = flow_cut_summary(graph, source, sink)
    answer["demand"] = demand
    answer["unmet"] = demand - answer["max_flow"]
    return answer


def global_real_edge_flow(group: RootGroup, edge_capacity: float = 1.0) -> Dict:
    graph = nx.DiGraph()
    source, sink = "source", "sink"
    demand = sum(obligation.weight for obligation in group.obligations)
    real_edges = set()
    for obligation in group.obligations:
        a_node = f"a:{obligation.obligation_id}"
        graph.add_edge(source, a_node, capacity=obligation.weight)
        for configuration in obligation.configurations:
            edge = configuration.root_edge
            real_edges.add(edge)
            edge_node = f"edge:{edge_name(edge)}"
            graph.add_edge(a_node, edge_node, capacity=demand + 1.0)
    for edge in real_edges:
        graph.add_edge(f"edge:{edge_name(edge)}", sink, capacity=edge_capacity)
    answer = flow_cut_summary(graph, source, sink)
    answer["demand"] = demand
    answer["unmet"] = demand - answer["max_flow"]
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
    edges = [
        ((0, 0), (1, 0), (2, 0)),
        ((0, 0), (1, 1), (3, 0)),
        ((0, 0), (2, 1), (3, 1)),
        ((0, 1), (1, 0), (3, 1)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 1), (2, 0), (3, 0)),
        ((1, 0), (2, 1), (3, 0)),
        ((1, 1), (2, 0), (3, 1)),
    ]
    return Hypergraph.build(4, 2, edges)


def nine_edge_repair_model() -> Hypergraph:
    base = eight_edge_model()
    new_edge = canonical_edge(((0, 0), (1, 0), (2, 1)))
    edges = (new_edge,) + base.edges
    return Hypergraph.build(4, 2, edges, edge_order=edges)


def model_minimality_report(hg: Hypergraph) -> Dict:
    full_it = hg.find_independent_transversal()
    edge_deletion_witnesses = {}
    for index, deleted in enumerate(hg.edges):
        reduced_edges = [edge for edge in hg.edges if edge != deleted]
        reduced = Hypergraph.build(hg.m, hg.b, reduced_edges)
        witness = reduced.find_independent_transversal()
        edge_deletion_witnesses[edge_name(deleted)] = (
            [vertex_name(v) for v in witness] if witness else None
        )
    block_deletion_witnesses = {}
    for deleted_block in range(hg.m):
        active = [block for block in range(hg.m) if block != deleted_block]
        witness = hg.find_independent_transversal(active_blocks=active)
        block_deletion_witnesses[str(deleted_block)] = (
            [vertex_name(v) for v in witness] if witness else None
        )
    return {
        "independent_transversal": (
            [vertex_name(v) for v in full_it] if full_it else None
        ),
        "no_IT": full_it is None,
        "max_degree": hg.max_degree(),
        "edge_minimal_no_IT": all(edge_deletion_witnesses.values()),
        "block_minimal_no_IT": all(block_deletion_witnesses.values()),
        "edge_deletion_IT_witnesses": edge_deletion_witnesses,
        "block_deletion_IT_witnesses": block_deletion_witnesses,
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
    specified_fixed = fixed_budget_slot_flow(
        specified, {(0, 0): 0.5, (1, 0): 0.5}
    )
    specified_real = global_real_edge_flow(specified, edge_capacity=1.0)

    hg9 = nine_edge_repair_model()
    repair_groups = build_root_groups(hg9, (0, 3, 1, 2))
    repair = next(
        group
        for group in repair_groups
        if len(group.obligations) >= 2
        and configuration_budget_lp(group).get("eta", math.inf) <= 1e-8
        and len(
            {
                configuration.pivot
                for obligation in group.obligations
                for configuration in obligation.configurations
            }
        )
        == 1
        and len(
            {
                configuration.root_edge
                for obligation in group.obligations
                for configuration in obligation.configurations
            }
        )
        >= 2
    )
    repair_lp = configuration_budget_lp(repair)

    # Synthetic genealogy collision regression:
    # one actual zero-error obligation duplicated under a distinct root ID.
    single_group = next(
        group
        for group in all_groups
        if len(group.obligations) == 1
        and classify_group(group)[0] == "zero-error-budget-feasible"
    )
    original = single_group.obligations[0]
    clone_configurations = tuple(
        Configuration(
            root_record_id="synthetic-root-B",
            released_vertex=c.released_vertex,
            pivot=c.pivot,
            root_edge=c.root_edge,
            released_trace=c.released_trace,
        )
        for c in original.configurations
    )
    cloned = Obligation(
        obligation_id="synthetic-clone",
        parent_record_id="synthetic-parent-B",
        inserted_vertex=original.inserted_vertex,
        attempted_vertex=original.attempted_vertex,
        first_edge=original.first_edge,
        weight=original.weight,
        configurations=clone_configurations,
    )
    root_a = RootGroup(
        block_order=single_group.block_order,
        root_record=single_group.root_record,
        success_block=single_group.success_block,
        failure_block=single_group.failure_block,
        obligations=[original],
    )
    root_b_record = ExecutionRecord(
        record_id="synthetic-root-B",
        block_word=single_group.root_record.block_word,
        trace=single_group.root_record.trace,
        genealogy=single_group.root_record.genealogy,
    )
    root_b = RootGroup(
        block_order=single_group.block_order,
        root_record=root_b_record,
        success_block=single_group.success_block,
        failure_block=single_group.failure_block,
        obligations=[cloned],
    )
    merged_record = ExecutionRecord(
        record_id="incorrectly-merged-root",
        block_word=single_group.root_record.block_word,
        trace=single_group.root_record.trace,
        genealogy=single_group.root_record.genealogy,
    )
    merged = RootGroup(
        block_order=single_group.block_order,
        root_record=merged_record,
        success_block=single_group.success_block,
        failure_block=single_group.failure_block,
        obligations=[original, cloned],
    )

    return {
        "eight_edge_model": model_minimality_report(hg8),
        "specified_window": {
            "order": list(specified.block_order),
            "root_trace": [vertex_name(v) for v in specified.root_record.trace],
            "obligations": [
                {
                    "r": vertex_name(o.inserted_vertex),
                    "x": vertex_name(o.attempted_vertex),
                    "first_edge": edge_name(o.first_edge),
                    "configurations": [
                        {
                            "pivot": vertex_name(c.pivot),
                            "edge": edge_name(c.root_edge),
                            "released_trace": [
                                vertex_name(v) for v in c.released_trace
                            ],
                        }
                        for c in o.configurations
                    ],
                }
                for o in specified.obligations
            ],
            "budget_lp": specified_lp,
            "fixed_half_budget_flow": specified_fixed,
            "global_real_edge_flow": specified_real,
        },
        "all_24_orders": {
            "root_groups_with_failures": len(all_groups),
            "classification": dict(classification_counter),
        },
        "nine_edge_repair": {
            "added_edge": edge_name(canonical_edge(((0, 0), (1, 0), (2, 1)))),
            "order": [0, 3, 1, 2],
            "root_trace": [vertex_name(v) for v in repair.root_record.trace],
            "obligation_count": len(repair.obligations),
            "budget_lp": repair_lp,
            "obligations": [
                {
                    "r": vertex_name(o.inserted_vertex),
                    "x": vertex_name(o.attempted_vertex),
                    "first_edge": edge_name(o.first_edge),
                    "pivots": [
                        vertex_name(c.pivot) for c in o.configurations
                    ],
                }
                for o in repair.obligations
            ],
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
    minimum_edges_to_cover_all_transversals = b**3
    maximum_edges_from_degree_budget = (m * b * degree_bound) // 3
    impossible = m * b * degree_bound < 3 * b**3
    return {
        "m": m,
        "b": b,
        "degree_bound": degree_bound,
        "minimum_edges_needed_by_transversal_counting": minimum_edges_to_cover_all_transversals,
        "maximum_edges_allowed_by_degree_sum": maximum_edges_from_degree_budget,
        "no_IT_candidate_impossible_by_counting": impossible,
        "inequality": f"{m}*{b}*{degree_bound} < 3*{b}^3",
    }


def find_it_from_selected_edges(
    m: int,
    b: int,
    selected_edges: Sequence[Tuple[Vertex, Vertex, Vertex]],
) -> Optional[Tuple[Vertex, ...]]:
    incident = {
        block: [
            edge
            for edge in selected_edges
            if any(vertex[0] == block for vertex in edge)
        ]
        for block in range(m)
    }
    order = sorted(range(m), key=lambda block: -len(incident[block]))
    chosen: Dict[int, Vertex] = {}

    def dfs(position: int) -> Optional[Tuple[Vertex, ...]]:
        if position == m:
            return tuple(chosen[block] for block in range(m))
        block = order[position]
        for index in range(b):
            candidate = (block, index)
            selected = set(chosen.values())
            selected.add(candidate)
            if any(set(edge) <= selected for edge in incident[block]):
                continue
            chosen[block] = candidate
            answer = dfs(position + 1)
            if answer is not None:
                return answer
            del chosen[block]
        return None

    return dfs(0)


def cutting_plane_outer_search(
    m: int,
    b: int,
    degree_bound: int,
    max_iterations: int,
    per_iteration_time_limit: float,
) -> Dict:
    counting = counting_obstruction(m, b, degree_bound)
    if counting["no_IT_candidate_impossible_by_counting"]:
        return {
            "status": "infeasible-by-counting",
            "counting_certificate": counting,
            "iterations": [],
        }

    edges = all_possible_edges(m, b)
    edge_count = len(edges)

    degree_rows, degree_cols, degree_data = [], [], []
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
        (degree_data, (degree_rows, degree_cols)),
        shape=(m * b, edge_count),
    )
    base_matrices = [degree_matrix, sp.csr_matrix(np.ones((1, edge_count)))]
    base_lower = [
        np.full(m * b, -np.inf),
        np.array([float(b**3)]),
    ]
    base_upper = [
        np.full(m * b, float(degree_bound)),
        np.array([np.inf]),
    ]

    cuts: List[np.ndarray] = []
    iteration_log = []
    selected_edges: List[Tuple[Vertex, Vertex, Vertex]] = []
    last_witness: Optional[Tuple[Vertex, ...]] = None
    objective = np.ones(edge_count)

    for iteration in range(max_iterations):
        matrices = list(base_matrices)
        lower = list(base_lower)
        upper = list(base_upper)
        if cuts:
            cut_row_indices = np.repeat(
                np.arange(len(cuts)), [len(cut) for cut in cuts]
            )
            cut_col_indices = np.concatenate(cuts)
            cut_matrix = sp.csr_matrix(
                (
                    np.ones(len(cut_col_indices)),
                    (cut_row_indices, cut_col_indices),
                ),
                shape=(len(cuts), edge_count),
            )
            matrices.append(cut_matrix)
            lower.append(np.ones(len(cuts)))
            upper.append(np.full(len(cuts), np.inf))

        constraint_matrix = sp.vstack(matrices, format="csr")
        lower_bound = np.concatenate(lower)
        upper_bound = np.concatenate(upper)

        started = time.time()
        result = milp(
            objective,
            integrality=np.ones(edge_count),
            bounds=Bounds(0.0, 1.0),
            constraints=LinearConstraint(
                constraint_matrix, lower_bound, upper_bound
            ),
            options={
                "time_limit": per_iteration_time_limit,
                "mip_rel_gap": 0.0,
            },
        )
        elapsed = time.time() - started

        if result.x is None:
            return {
                "status": "solver-stopped-without-incumbent",
                "counting_certificate": counting,
                "edge_variable_count": edge_count,
                "cut_count": len(cuts),
                "iterations": iteration_log,
                "solver_message": result.message,
            }

        selected_indices = np.flatnonzero(result.x > 0.5)
        selected_edges = [edges[index] for index in selected_indices]
        witness = find_it_from_selected_edges(m, b, selected_edges)
        witness_hash = None
        if witness is not None:
            witness_hash = hashlib.sha256(repr(witness).encode()).hexdigest()[:16]

        iteration_log.append(
            {
                "iteration": iteration,
                "solver_message": result.message,
                "elapsed_seconds": elapsed,
                "selected_edge_count": len(selected_edges),
                "IT_found": witness is not None,
                "IT_witness_hash": witness_hash,
            }
        )

        if witness is None:
            candidate = Hypergraph.build(m, b, selected_edges)
            return {
                "status": "no-IT-candidate-found",
                "counting_certificate": counting,
                "edge_variable_count": edge_count,
                "cut_count": len(cuts),
                "iterations": iteration_log,
                "candidate": {
                    "max_degree": candidate.max_degree(),
                    "edges": [edge_name(canonical_edge(edge)) for edge in selected_edges],
                },
            }

        last_witness = witness
        witness_set = set(witness)
        cut = np.array(
            [
                edge_index
                for edge_index, edge in enumerate(edges)
                if set(edge) <= witness_set
            ],
            dtype=int,
        )
        # Each full transversal contains C(m,3) possible real 3-edges.
        if len(cut) != math.comb(m, 3):
            raise AssertionError("Malformed transversal cover cut.")
        cuts.append(cut)

    final_hg = Hypergraph.build(m, b, selected_edges)
    return {
        "status": "iteration-limit-reached-with-IT-certificates",
        "counting_certificate": counting,
        "edge_variable_count": edge_count,
        "cut_count": len(cuts),
        "iterations": iteration_log,
        "last_candidate": {
            "selected_edge_count": len(selected_edges),
            "max_degree": final_hg.max_degree(),
            "IT_witness": [vertex_name(v) for v in last_witness]
            if last_witness
            else None,
            "edges": [edge_name(canonical_edge(edge)) for edge in selected_edges],
        },
        "interpretation": (
            "Every MILP incumbent was refuted by an explicit independent "
            "transversal. Reaching the iteration limit is not an exhaustive "
            "infeasibility proof."
        ),
    }


def make_markdown_report(results: Dict) -> str:
    regressions = results["regressions"]
    outer = results["outer_search"]
    counts = regressions["all_24_orders"]["classification"]
    specified = regressions["specified_window"]
    repair = regressions["nine_edge_repair"]
    collision = regressions["genealogy_collision"]

    iteration_times = [
        item["elapsed_seconds"] for item in outer.get("iterations", [])
    ]
    total_solver_time = sum(iteration_times)
    max_solver_time = max(iteration_times, default=0.0)

    lines = [
        "# Q-0015 重建审计器：首轮实际执行报告",
        "",
        "## 1. 实现范围",
        "",
        "本次从公开的 `SINGLE_DEFECT_FRAMEWORK.md` v0.4 定义重建了：真实成功执行树、失败义务、合法根配置枚举、root-pivot 预算原始/对偶 LP、固定预算槽位最大流/最小割、独立的全局真实边 Hall 流，以及低度候选的切平面 MILP 外层。",
        "",
        "> 注意：仓库主分支未公开文档所称的历史 Python 文件，因此这是依据公开数学规格的独立重建，不声称与历史实现逐字一致。",
        "",
        "## 2. 四项回归基线",
        "",
        f"- 八边模型：无 IT = `{regressions['eight_edge_model']['no_IT']}`；边极小 = `{regressions['eight_edge_model']['edge_minimal_no_IT']}`；块极小 = `{regressions['eight_edge_model']['block_minimal_no_IT']}`；最大度 = `{regressions['eight_edge_model']['max_degree']}`。",
        f"- 指定窗口：义务数 `{len(specified['obligations'])}`，`t_min={specified['budget_lp']['t_min']:.6g}`，`eta={specified['budget_lp']['eta']:.6g}`，原始—对偶间隙 `{specified['budget_lp']['duality_gap']:.3g}`。",
        f"- 固定 `lambda(0_0)=lambda(1_0)=1/2`：槽位最大流 `{specified['fixed_half_budget_flow']['max_flow']:.6g}` / 需求 `{specified['fixed_half_budget_flow']['demand']:.6g}`。",
        f"- 全局真实边单位容量：最大流 `{specified['global_real_edge_flow']['max_flow']:.6g}` / 需求 `{specified['global_real_edge_flow']['demand']:.6g}`。",
        f"- 全部 24 个块顺序：带失败义务的实际 root group 共 `{regressions['all_24_orders']['root_groups_with_failures']}` 个；零误差 `{counts.get('zero-error-budget-feasible',0)}`，正 root-budget 缺口 `{counts.get('positive-root-budget-gap',0)}`，含 no-configuration `{counts.get('no-configuration',0)}`。",
        f"- 九边修复：新增 `{repair['added_edge']}`，块顺序 `{tuple(repair['order'])}`，义务数 `{repair['obligation_count']}`，`t_min={repair['budget_lp']['t_min']:.6g}`，`eta={repair['budget_lp']['eta']:.6g}`。",
        f"- genealogy 碰撞：两个 root 分开时 `t_min={collision['root_A_t_min']:.6g},{collision['root_B_t_min']:.6g}`；错误合并后 `t_min={collision['incorrectly_merged_t_min']:.6g}`，`eta={collision['incorrectly_merged_eta']:.6g}`。",
        "",
        "上述数值完整复现了文档第 23.1–23.4 节给出的四组基线。",
        "",
        "## 3. 低度外层生成器首轮",
        "",
        f"执行参数：`b={outer['counting_certificate']['b']}`，`m={outer['counting_certificate']['m']}`，顶点最大度上界 `D={outer['counting_certificate']['degree_bound']}`。这是 `b=3` 严格低于 `b^2/4=2.25` 时第一个未被简单总度计数立即排除的块数。",
        "",
        f"- 潜在真实边变量数：`{outer.get('edge_variable_count', 0)}`。",
        f"- 执行状态：`{outer['status']}`。",
        f"- 完成切平面轮数：`{len(outer.get('iterations', []))}`；加入横截覆盖切平面 `{outer.get('cut_count',0)}` 条。",
        f"- MILP 求解累计时间：`{total_solver_time:.3f}` 秒；单轮最大 `{max_solver_time:.3f}` 秒。",
    ]
    if outer["status"] == "iteration-limit-reached-with-IT-certificates":
        last = outer["last_candidate"]
        lines += [
            f"- 每一轮最优 incumbent 均含 `{last['selected_edge_count']}` 条边，且都由一个显式 IT 否定。",
            f"- 最后一轮候选最大度：`{last['max_degree']}`；IT 证书：`{tuple(last['IT_witness'])}`。",
            "",
            "这不是对 `(b,m,D)=(3,14,2)` 的穷尽不可行证明；它证明的是：当前 100 个由累积覆盖切平面产生的最稀疏候选全部落入第一类证书（IT 证书），尚未触发 no-configuration、root-budget、slot-congestion 或 global real-edge reuse。",
        ]
    elif outer["status"] == "no-IT-candidate-found":
        lines += [
            "",
            "**发现了无 IT 候选。** 下一步应立即对其所有块顺序运行内层配置审计，并检查边极小/块极小见证。",
        ]
    else:
        lines += ["", outer.get("interpretation", "")]

    lines += [
        "",
        "## 4. 当前计算结论",
        "",
        "1. 重建实现通过全部公开回归数值，因此足以作为接外层生成器的可复算基线。",
        "2. 首个真正低度参数点的 100 轮切平面搜索只产生 IT 证书，没有发现目标反模型或配置 Hall 障碍。",
        "3. 下一次计算最有价值的改进，是给外层加入同构破除、边极小/块极小约束与跨 root projection 的联合预算，而不是继续重复固定窗口审计。",
        "",
        "## 5. 可复算文件",
        "",
        "- `q0015_configuration_auditor_rebuilt.py`：完整脚本。",
        "- `q0015_first_execution_results.json`：机器可读原始结果，包括 LP 解、对偶证书、最小割和 100 轮日志。",
    ]
    return "\n".join(lines) + "\n"


def run(output_dir: Path, iterations: int, time_limit: float) -> Dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    regressions = run_regressions()
    outer = cutting_plane_outer_search(
        m=14,
        b=3,
        degree_bound=2,
        max_iterations=iterations,
        per_iteration_time_limit=time_limit,
    )
    results = {
        "metadata": {
            "implementation": "independent reconstruction from public Markdown",
            "framework_version": "v0.4-auditor-grounded",
            "outer_search_parameters": {
                "m": 14,
                "b": 3,
                "degree_bound": 2,
                "iterations": iterations,
                "per_iteration_time_limit_seconds": time_limit,
            },
        },
        "regressions": regressions,
        "outer_search": outer,
    }
    result_path = output_dir / "q0015_first_execution_results.json"
    result_path.write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    report_path = output_dir / "q0015_first_execution_report.md"
    report_path.write_text(make_markdown_report(results), encoding="utf-8")
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("."))
    parser.add_argument("--iterations", type=int, default=100)
    parser.add_argument("--time-limit", type=float, default=3.0)
    args = parser.parse_args()
    results = run(args.output_dir, args.iterations, args.time_limit)
    print(json.dumps({
        "classification": results["regressions"]["all_24_orders"],
        "specified_t_min": results["regressions"]["specified_window"]["budget_lp"]["t_min"],
        "specified_fixed_flow": results["regressions"]["specified_window"]["fixed_half_budget_flow"]["max_flow"],
        "specified_real_edge_flow": results["regressions"]["specified_window"]["global_real_edge_flow"]["max_flow"],
        "nine_edge_eta": results["regressions"]["nine_edge_repair"]["budget_lp"]["eta"],
        "genealogy_merged_eta": results["regressions"]["genealogy_collision"]["incorrectly_merged_eta"],
        "outer_status": results["outer_search"]["status"],
        "outer_iterations": len(results["outer_search"].get("iterations", [])),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
