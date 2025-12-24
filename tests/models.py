"""Test models for flext-dbt-ldif tests.

Provides TestsFlextDbtLdifModels, extending FlextTestsModels with flext-dbt-ldif-specific
models using COMPOSITION INHERITANCE.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests.models import FlextTestsModels

from flext_dbt_ldif.models import FlextDbtLdifModels


class TestsFlextDbtLdifModels(FlextTestsModels, FlextDbtLdifModels):
    """Models for flext-dbt-ldif tests using COMPOSITION INHERITANCE.

    MANDATORY: Inherits from BOTH:
    1. FlextTestsModels - for test infrastructure (.Tests.*)
    2. FlextDbtLdifModels - for domain models

    Access patterns:
    - tm.Tests.* (generic test models from FlextTestsModels)
    - tm.DbtLdif.* (DBT LDIF domain models)
    - m.* (production models via alternative alias)
    """

    class Tests:
        """Project-specific test fixtures namespace."""

        class DbtLdif:
            """DBT LDIF-specific test fixtures."""


# Short aliases per FLEXT convention
tm = TestsFlextDbtLdifModels
m = TestsFlextDbtLdifModels

__all__ = [
    "TestsFlextDbtLdifModels",
    "m",
    "tm",
]
