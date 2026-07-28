from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List


class ExitType(str, Enum):
    NO_CONFIGURATION = "no-configuration"
    EXECUTION_BOUNDARY = "execution-boundary"
    ROOT_PROJECTION_FAILURE = "root-projection-failure"
    ROOT_BUDGET_CUT = "root-budget-cut"
    SLOT_CUT = "slot-cut"
    REAL_EDGE_HALL_CUT = "real-edge-hall-cut"
    SWITCH_NO_REROOT = "switch-no-reroot-lift"
    MULTI_DEFECT = "multi-defect"
    EXTERNAL_OLD_ANCHOR = "external-old-anchor-blocker"
    EXACT_FUTURE_QUOTIENT = "exact-future-quotient"
    AUGMENTATION = "augmentation"
    SURVIVOR = "survivor"
    UNCLASSIFIED = "unclassified"


@dataclass(frozen=True)
class ExitCertificate:
    certificate_id: str
    exit_type: ExitType
    mass: float
    root_record_id: str
    root_projection_id: str
    genealogy: List[str]
    attempted_vertex: str | None = None
    first_real_edge: str | None = None
    ledger: str | None = None
    payload: Dict[str, Any] = field(default_factory=dict)
    status: str = "observed"

    def validate(self) -> None:
        if not self.certificate_id:
            raise ValueError("certificate_id is required")
        if self.mass < 0:
            raise ValueError("mass must be nonnegative")
        if not self.root_record_id or not self.root_projection_id:
            raise ValueError("real root record and projection are required")
        if not isinstance(self.genealogy, list):
            raise ValueError("genealogy must be a list")
        if self.exit_type in {
            ExitType.ROOT_BUDGET_CUT,
            ExitType.SLOT_CUT,
            ExitType.REAL_EDGE_HALL_CUT,
        } and self.ledger is None:
            raise ValueError("capacity-cut certificates must name their ledger")
        if self.exit_type in {
            ExitType.REAL_EDGE_HALL_CUT,
            ExitType.MULTI_DEFECT,
            ExitType.EXTERNAL_OLD_ANCHOR,
        } and self.first_real_edge is None:
            raise ValueError("this exit requires a real-edge label")

    def as_dict(self) -> Dict[str, Any]:
        self.validate()
        return {
            "schema_version": "q0015-e-exit-v1",
            "certificate_id": self.certificate_id,
            "exit_type": self.exit_type.value,
            "mass": self.mass,
            "root_record_id": self.root_record_id,
            "root_projection_id": self.root_projection_id,
            "genealogy": self.genealogy,
            "attempted_vertex": self.attempted_vertex,
            "first_real_edge": self.first_real_edge,
            "ledger": self.ledger,
            "payload": self.payload,
            "status": self.status,
        }
