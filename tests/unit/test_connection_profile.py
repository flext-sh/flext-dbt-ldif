"""Behavior contract for the dbt LDIF connection profile.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_ldif import FlextDbtLdifServiceBase
from tests import m, p, tm


class TestsFlextDbtLdifConnectionProfile:
    """The dbt LDIF connection profile wire contract."""

    @staticmethod
    def test_connection_profile_returns_typed_ldif_wire_shape() -> None:
        """The service base exposes a typed LDIF connection profile."""
        service = FlextDbtLdifServiceBase()
        profile = service.connection_profile

        tm.that(profile, is_=m.DbtLdif.DbtConnectionProfile)
        tm.that(profile, is_=p.Meltano.DbtConnectionProfile)
        tm.that(
            profile.model_dump(),
            eq={
                "type": "ldif",
                "path": service.settings.DbtLdif.ldif_file_path,
                "project": service.dbt_project_name,
            },
        )
