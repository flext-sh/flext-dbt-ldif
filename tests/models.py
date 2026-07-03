"""Test models for flext-dbt-ldif.

Provides TestsFlextDbtLdifModels, combining TestsFlextModels with
m for test-specific model definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_dbt_ldif import m


class TestsFlextDbtLdifModels(FlextTestsModels, m):
    """Test models combining TestsFlextModels with flext-dbt-ldif models."""

    class DbtLdif(m.DbtLdif):
        """DbtLdif test models namespace."""

        class Tests:
            """Project-specific test models."""


m = TestsFlextDbtLdifModels

__all__: list[str] = [
    "TestsFlextDbtLdifModels",
    "m",
]
