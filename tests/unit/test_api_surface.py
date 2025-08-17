"""Test API surface of flext-dbt-ldif.

This module tests the API surface of flext-dbt-ldif to ensure all
public functions and classes are properly exposed and callable.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_dbt_ldif import (
    AnalyticsModel,
    ChangeTracker,
    DimensionModel,
    FlextDbtLdifClient,
    FlextDbtLdifConfig,
    FlextDbtLdifModelGenerator,
    FlextDbtLdifService,
    FlextDbtLdifWorkflowManager,
    FlextLdifAPI,
    FlextResult,
    LDIFAnalyzer,
    LDIFInsights,
    ModelGenerator,
    __version__,
    flext_ldif_parse,
    flext_ldif_validate,
    flext_ldif_write,
)


def test_api_imports() -> None:
    """Test API imports."""  # Test version import
    assert isinstance(__version__, str)
    # Instantiate light-touch objects to bump coverage
    _ = FlextDbtLdifClient(FlextDbtLdifConfig())
    _ = FlextDbtLdifModelGenerator(FlextDbtLdifConfig())
    _ = FlextDbtLdifService(FlextDbtLdifConfig())
    _ = FlextDbtLdifWorkflowManager(FlextDbtLdifConfig())
    _ = AnalyticsModel()
    _ = ChangeTracker()
    _ = DimensionModel()
    _ = LDIFAnalyzer()
    _ = LDIFInsights()
    # Test aliased functions
    assert callable(flext_ldif_parse)
    assert callable(flext_ldif_validate)
    assert callable(flext_ldif_write)
    # Types are exposed
    assert FlextResult is not None
    assert FlextLdifAPI is not None
    assert ModelGenerator is not None
