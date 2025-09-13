"""Test exceptions for FLEXT DBT LDIF.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_ldif import (
    FlextDbtLdifConfigurationError,
    FlextDbtLdifError,
    FlextDbtLdifModelError,
    FlextDbtLdifParseError,
    FlextDbtLdifProcessingError,
    FlextDbtLdifTestError,
    FlextDbtLdifTransformationError,
    FlextDbtLdifValidationError,
)


def test_exception_hierarchy() -> None:
    """Test exception hierarchy."""
    assert issubclass(FlextDbtLdifValidationError, FlextDbtLdifError)
    assert issubclass(FlextDbtLdifProcessingError, FlextDbtLdifError)
    assert issubclass(FlextDbtLdifConfigurationError, FlextDbtLdifError)


def test_exception_instances() -> None:
    """Test exception instances."""
    e1 = FlextDbtLdifParseError("msg", line_number=10, entry_dn="cn=x")
    assert isinstance(e1, FlextDbtLdifProcessingError)

    e2 = FlextDbtLdifModelError("m", model_name="x", model_type="staging")
    assert isinstance(e2, FlextDbtLdifProcessingError)

    e3 = FlextDbtLdifTransformationError("t", transformation_type="analytics")
    assert isinstance(e3, FlextDbtLdifProcessingError)

    e4 = FlextDbtLdifTestError("t", test_name="n", model_name="m")
    assert isinstance(e4, FlextDbtLdifValidationError)
