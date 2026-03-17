"""Test models for flext-dbt-ldif tests.

Provides TestsFlextDbtLdifModels, extending FlextTestsModels with flext-dbt-ldif-specific
models using COMPOSITION INHERITANCE.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_dbt_ldif import FlextDbtLdifModels


class TestsFlextDbtLdifModels(FlextTestsModels, FlextDbtLdifModels):
    """Models for flext-dbt-ldif tests using COMPOSITION INHERITANCE.

    MANDATORY: Inherits from BOTH:
    1. FlextTestsModels - for test infrastructure (.Tests.*)
    2. FlextDbtLdifModels - for domain models

    Access patterns:
    - m.Tests.* (generic test models from FlextTestsModels)
    - m.DbtLdif.* (DBT LDIF domain models)
    - m.DbtLdif.Tests.* (project test-only models)
    """

    class DbtLdif(FlextDbtLdifModels.DbtLdif):
        """DbtLdif test models namespace."""

        class Tests:
            """Project-specific test models."""


m = TestsFlextDbtLdifModels

__all__ = [
    "TestsFlextDbtLdifModels",
    "m",
]
