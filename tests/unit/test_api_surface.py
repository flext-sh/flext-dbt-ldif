"""Test API surface for FLEXT DBT LDIF.

Public functions and classes are properly exposed and callable.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import r

from flext_dbt_ldif import FlextDbtLdif, FlextDbtLdifSettings, __version__, u


def test_api_imports() -> None:
    """Test API imports."""
    assert isinstance(__version__, str)
    _ = u.DbtLdif.Client(FlextDbtLdifSettings.get_global())
    _ = u.DbtLdif.Service(FlextDbtLdifSettings.get_global())
    assert callable(FlextDbtLdif)
    assert r is not None
