import pytest

from hypergraph_il.certificates import ExitCertificate, ExitType


def test_capacity_cut_names_ledger() -> None:
    cert = ExitCertificate(
        certificate_id="c1",
        exit_type=ExitType.SLOT_CUT,
        mass=1.0,
        root_record_id="r",
        root_projection_id="rho",
        genealogy=[],
    )
    with pytest.raises(ValueError):
        cert.validate()


def test_real_edge_exit_names_real_edge() -> None:
    cert = ExitCertificate(
        certificate_id="c2",
        exit_type=ExitType.REAL_EDGE_HALL_CUT,
        mass=1.0,
        root_record_id="r",
        root_projection_id="rho",
        genealogy=["step"],
        ledger="global-real-edge",
    )
    with pytest.raises(ValueError):
        cert.validate()


def test_valid_certificate_is_machine_serializable() -> None:
    cert = ExitCertificate(
        certificate_id="c3",
        exit_type=ExitType.NO_CONFIGURATION,
        mass=0.25,
        root_record_id="r",
        root_projection_id="rho",
        genealogy=["choose:0_0"],
        status="certified",
    )
    data = cert.as_dict()
    assert data["schema_version"] == "q0015-e-exit-v1"
    assert data["exit_type"] == "no-configuration"
    assert data["root_projection_id"] == "rho"
