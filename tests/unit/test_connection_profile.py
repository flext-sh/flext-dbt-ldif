"""Behavior contract for the dbt LDIF connection profile.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/test_connection_profile
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import p

from flext_dbt_ldif import FlextDbtLdifServiceBase, m


def test_connection_profile_returns_typed_ldif_wire_shape() -> None:
    """Test connection profile returns typed ldif wire shape."""
    profile = FlextDbtLdifServiceBase().connection_profile

    assert isinstance(profile, m.DbtLdif.DbtConnectionProfile)
    assert isinstance(profile, p.Meltano.DbtConnectionProfile)
    assert profile.model_dump() == {
        "type": "ldif",
        "path": profile.path,
        "project": "dbt-ldif",
    }
