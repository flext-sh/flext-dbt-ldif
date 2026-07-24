"""Behavior contract for the dbt LDIF connection profile."""

from __future__ import annotations

from flext_dbt_ldif import FlextDbtLdifServiceBase, m
from flext_meltano import p


def test_connection_profile_returns_typed_ldif_wire_shape() -> None:
    profile = FlextDbtLdifServiceBase().connection_profile

    assert isinstance(profile, m.DbtLdif.DbtConnectionProfile)
    assert isinstance(profile, p.Meltano.DbtConnectionProfile)
    assert profile.model_dump() == {
        "type": "ldif",
        "path": profile.path,
        "project": "dbt-ldif",
    }
