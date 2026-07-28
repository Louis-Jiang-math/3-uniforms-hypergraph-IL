from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, FrozenSet, Iterable, Optional, Sequence, Tuple

Vertex = Tuple[int, int]
Edge = FrozenSet[Vertex]


def canonical_edge(vertices: Iterable[Vertex]) -> Edge:
    edge = frozenset(vertices)
    if len(edge) != 3:
        raise ValueError(f"expected a 3-edge, got {edge}")
    if len({block for block, _ in edge}) != 3:
        raise ValueError(f"edge is not transversal across three blocks: {edge}")
    return edge


def vertex_name(vertex: Vertex) -> str:
    return f"{vertex[0]}_{vertex[1]}"


def edge_name(edge: Edge) -> str:
    return "{" + ",".join(vertex_name(v) for v in sorted(edge)) + "}"


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
        if m <= 0 or b <= 0:
            raise ValueError("m and b must be positive")
        edge_tuple = tuple(canonical_edge(edge) for edge in edges)
        if len(set(edge_tuple)) != len(edge_tuple):
            raise ValueError("duplicate real edges are not allowed")
        order_tuple = (
            tuple(canonical_edge(edge) for edge in edge_order)
            if edge_order is not None
            else edge_tuple
        )
        if len(order_tuple) != len(edge_tuple) or set(order_tuple) != set(edge_tuple):
            raise ValueError("edge_order must contain every real edge exactly once")
        for edge in edge_tuple:
            for block, index in edge:
                if not (0 <= block < m and 0 <= index < b):
                    raise ValueError(f"vertex {(block, index)} outside declared blocks")
        return cls(m=m, b=b, edges=edge_tuple, edge_order=order_tuple)

    @property
    def edge_rank(self) -> Dict[Edge, int]:
        return {edge: index for index, edge in enumerate(self.edge_order)}

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

    def blocking_edges(self, trace: Sequence[Vertex], attempted: Vertex) -> Tuple[Edge, ...]:
        chosen = set(trace)
        chosen.add(attempted)
        return tuple(edge for edge in self.edges if edge <= chosen)

    def first_blocking_edge(self, trace: Sequence[Vertex], attempted: Vertex) -> Optional[Edge]:
        blockers = self.blocking_edges(trace, attempted)
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
