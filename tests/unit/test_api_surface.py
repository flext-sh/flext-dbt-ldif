"""Test API surface for FLEXT DBT LDIF.

Public functions and classes are properly exposed and callable.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_dbt_ldif import (
    FlextDbtLdif,
    FlextDbtLdifClient,
    FlextDbtLdifServiceMixin,
    FlextDbtLdifSettings,
    __version__,
)
from tests import r


class TestsFlextDbtLdifApiSurface:
    """Behavior contract for test_api_surface."""

    def test_api_imports(self) -> None:
        """Test API imports."""
        assert isinstance(__version__, str)
        _ = FlextDbtLdifClient.Client(FlextDbtLdifSettings.fetch_global())
        _ = FlextDbtLdifServiceMixin.Service(FlextDbtLdifSettings.fetch_global())
        assert callable(FlextDbtLdif)
        assert r is not None
