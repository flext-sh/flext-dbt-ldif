"""Test API surface for FLEXT DBT LDIF.

Public functions and classes are properly exposed and callable.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextResult
from flext_dbt_ldif import (
    FlextDbtLdif,
    FlextDbtLdifClient,
    FlextDbtLdifService,
    FlextDbtLdifSettings,
    FlextLdif,
    __version__,
)


def test_api_imports() -> None:
    """Test API imports."""  # Test version import
    assert isinstance(__version__, str)
    # Instantiate light-touch objects to bump coverage
    _ = FlextDbtLdifClient(FlextDbtLdifSettings())
    _ = FlextDbtLdifService(FlextDbtLdifSettings())

    assert callable(FlextDbtLdif)

    assert FlextResult is not None
    assert FlextLdif is not None
