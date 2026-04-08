"""Test models for flext-dbt-ldif.

Provides TestsFlextDbtLdifModels, combining TestsFlextModels with
FlextDbtLdifModels for test-specific model definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_dbt_ldif import FlextDbtLdifModels


class TestsFlextDbtLdifModels(FlextTestsModels, FlextDbtLdifModels):
    """Test models combining TestsFlextModels with flext-dbt-ldif models."""

    class DbtLdif(FlextDbtLdifModels.DbtLdif):
        """DbtLdif test models namespace."""

        class Tests:
            """Project-specific test models."""


m = TestsFlextDbtLdifModels

__all__ = [
    "TestsFlextDbtLdifModels",
    "m",
]
