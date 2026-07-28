from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from .execution import SlotKey
from .models import Edge

_TOL = 1e-9


class CapacityError(ValueError):
    pass


@dataclass
class RootBudgetLedger:
    capacity_by_projection_and_pivot: Dict[tuple[str, tuple[int, int]], float]
    used: Dict[tuple[str, tuple[int, int]], float] = field(default_factory=dict)

    def charge(self, projection_id: str, pivot: tuple[int, int], amount: float) -> None:
        key = (projection_id, pivot)
        _charge(self.capacity_by_projection_and_pivot, self.used, key, amount, "root budget")


@dataclass
class SlotLedger:
    capacity_by_slot: Dict[SlotKey, float]
    used: Dict[SlotKey, float] = field(default_factory=dict)

    def charge(self, slot: SlotKey, amount: float) -> None:
        _charge(self.capacity_by_slot, self.used, slot, amount, "slot")


@dataclass
class RealEdgeLedger:
    capacity_by_edge: Dict[Edge, float]
    used: Dict[Edge, float] = field(default_factory=dict)

    def charge(self, edge: Edge, amount: float) -> None:
        _charge(self.capacity_by_edge, self.used, edge, amount, "real edge")

    def remaining(self, edge: Edge) -> float:
        return self.capacity_by_edge.get(edge, 0.0) - self.used.get(edge, 0.0)


def _charge(capacity: Dict, used: Dict, key, amount: float, label: str) -> None:
    if amount < -_TOL:
        raise CapacityError(f"negative {label} charge")
    cap = float(capacity.get(key, 0.0))
    new_value = float(used.get(key, 0.0)) + float(amount)
    if new_value > cap + _TOL:
        raise CapacityError(f"{label} capacity exceeded for {key}: {new_value} > {cap}")
    used[key] = new_value
