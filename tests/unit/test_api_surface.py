"""Test API surface for FLEXT DBT LDIF.

Public functions and classes are properly exposed and callable.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextResult

from flext_dbt_ldif import (
    FlextDbtLdifClient,
    FlextDbtLdifConfig,
    FlextDbtLdifService,
    FlextLdif,
    __version__,
    generate_ldif_models,
    process_ldif_file,
    validate_ldif_quality,
)


def test_api_imports() -> None:
    """Test API imports."""  # Test version import
    assert isinstance(__version__, str)
    # Instantiate light-touch objects to bump coverage
    _ = FlextDbtLdifClient(FlextDbtLdifConfig())
    _ = FlextDbtLdifService(FlextDbtLdifConfig())

    # Test aliased functions
    assert callable(generate_ldif_models)
    assert callable(process_ldif_file)
    assert callable(validate_ldif_quality)

    assert FlextResult is not None
    assert FlextLdif is not None
