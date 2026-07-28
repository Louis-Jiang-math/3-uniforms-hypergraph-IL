from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import List, Sequence, Tuple

from .models import Edge, Hypergraph, Vertex, canonical_edge


@dataclass(frozen=True, order=True)
class SlotKey:
    """A slot is local to a real root projection; it is not merely (pivot, edge)."""

    root_projection_id: str
    pivot: Vertex
    root_edge: Edge


@dataclass(frozen=True)
class ExecutionRecord:
    record_id: str
    root_projection_id: str
    block_word: Tuple[int, ...]
    trace: Tuple[Vertex, ...]
    genealogy: Tuple[str, ...]


@dataclass(frozen=True)
class Configuration:
    root_record_id: str
    root_projection_id: str
    released_vertex: Vertex
    pivot: Vertex
    root_edge: Edge
    released_trace: Tuple[Vertex, ...]

    @property
    def slot(self) -> SlotKey:
        return SlotKey(self.root_projection_id, self.pivot, self.root_edge)


@dataclass(frozen=True)
class Obligation:
    obligation_id: str
    parent_record_id: str
    root_projection_id: str
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


def make_obligation_id(
    root_record_id: str, inserted: Vertex, attempted: Vertex, first_edge: Edge
) -> str:
    raw = repr((root_record_id, inserted, attempted, tuple(sorted(first_edge)))).encode()
    return hashlib.sha256(raw).hexdigest()[:16]


def build_root_groups(hg: Hypergraph, block_order: Sequence[int]) -> List[RootGroup]:
    order = tuple(block_order)
    current = [
        ExecutionRecord(
            record_id=make_record_id(order, ()),
            root_projection_id=make_record_id(order, ()),
            block_word=(),
            trace=(),
            genealogy=(),
        )
    ]
    groups: List[RootGroup] = []

    for step, block in enumerate(order):
        if step >= 1 and step + 1 < len(order):
            failure_block = order[step + 1]
            for root in current:
                obligations: List[Obligation] = []
                for inserted_index in range(hg.b):
                    inserted = (block, inserted_index)
                    inserted_trace = root.trace + (inserted,)
                    if not hg.is_independent(inserted_trace):
                        continue
                    parent_id = make_record_id(order, inserted_trace)
                    for attempted_index in range(hg.b):
                        attempted = (failure_block, attempted_index)
                        first_edge = hg.first_blocking_edge(inserted_trace, attempted)
                        if first_edge is None:
                            continue
                        released_trace = root.trace + (attempted,)
                        configurations: List[Configuration] = []
                        # Removing the inserted endpoint must be followed by a full
                        # independence check; first-blocker uniqueness is insufficient.
                        if hg.is_independent(released_trace):
                            for pivot in root.trace:
                                if first_edge == canonical_edge((pivot, inserted, attempted)):
                                    configurations.append(
                                        Configuration(
                                            root_record_id=root.record_id,
                                            root_projection_id=root.root_projection_id,
                                            released_vertex=inserted,
                                            pivot=pivot,
                                            root_edge=first_edge,
                                            released_trace=released_trace,
                                        )
                                    )
                        obligations.append(
                            Obligation(
                                obligation_id=make_obligation_id(
                                    root.record_id, inserted, attempted, first_edge
                                ),
                                parent_record_id=parent_id,
                                root_projection_id=root.root_projection_id,
                                inserted_vertex=inserted,
                                attempted_vertex=attempted,
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
                candidate = (block, index)
                trace = record.trace + (candidate,)
                if not hg.is_independent(trace):
                    continue
                record_id = make_record_id(order, trace)
                new_records.append(
                    ExecutionRecord(
                        record_id=record_id,
                        root_projection_id=record_id,
                        block_word=record.block_word + (block,),
                        trace=trace,
                        genealogy=record.genealogy
                        + (f"choose:{block}_{index}",),
                    )
                )
        current = new_records
    return groups
