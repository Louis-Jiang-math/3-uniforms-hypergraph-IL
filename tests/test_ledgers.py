import pytest

from hypergraph_il.execution import SlotKey
from hypergraph_il.ledgers import (
    CapacityError,
    RealEdgeLedger,
    RootBudgetLedger,
    SlotLedger,
)
from hypergraph_il.models import canonical_edge


def test_root_budget_is_projection_sensitive() -> None:
    pivot = (0, 0)
    ledger = RootBudgetLedger({("root-A", pivot): 1.0, ("root-B", pivot): 1.0})
    ledger.charge("root-A", pivot, 1.0)
    ledger.charge("root-B", pivot, 1.0)
    with pytest.raises(CapacityError):
        ledger.charge("root-A", pivot, 0.1)


def test_slots_are_projection_sensitive() -> None:
    edge = canonical_edge(((0, 0), (1, 0), (2, 0)))
    a = SlotKey("root-A", (0, 0), edge)
    b = SlotKey("root-B", (0, 0), edge)
    assert a != b
    ledger = SlotLedger({a: 1.0, b: 1.0})
    ledger.charge(a, 1.0)
    ledger.charge(b, 1.0)


def test_real_edge_capacity_is_global_across_histories() -> None:
    edge = canonical_edge(((0, 0), (1, 0), (2, 0)))
    ledger = RealEdgeLedger({edge: 1.0})
    ledger.charge(edge, 0.6)
    with pytest.raises(CapacityError):
        ledger.charge(edge, 0.5)


def test_negative_charge_is_rejected() -> None:
    edge = canonical_edge(((0, 0), (1, 0), (2, 0)))
    ledger = RealEdgeLedger({edge: 1.0})
    with pytest.raises(CapacityError):
        ledger.charge(edge, -0.1)
