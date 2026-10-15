"""Behavior contract for the dbt LDIF connection profile.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_ldif import FlextDbtLdifServiceBase
from tests import m, p


class TestsFlextDbtLdifConnectionProfile:
    """The dbt LDIF connection profile wire contract."""

    @staticmethod
    def test_connection_profile_returns_typed_ldif_wire_shape() -> None:
        """The service base exposes a typed LDIF connection profile."""
        profile = FlextDbtLdifServiceBase().connection_profile

        assert isinstance(profile, m.DbtLdif.DbtConnectionProfile)
        assert isinstance(profile, p.Meltano.DbtConnectionProfile)
        assert profile.model_dump() == {
            "type": "ldif",
            "path": profile.path,
            "project": "dbt-ldif",
        }
