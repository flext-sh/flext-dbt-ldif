"""Test models for flext-dbt-ldif.

Provides FlextDbtLdifTestModels, combining FlextTestsModels with
FlextDbtLdifModels for test-specific model definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_dbt_ldif import FlextDbtLdifModels


class FlextDbtLdifTestModels(FlextTestsModels, FlextDbtLdifModels):
    """Test models combining FlextTestsModels with flext-dbt-ldif models."""

    class DbtLdif(FlextDbtLdifModels.DbtLdif):
        """DbtLdif test models namespace."""

        class Tests:
            """Project-specific test models."""


m = FlextDbtLdifTestModels

__all__ = [
    "FlextDbtLdifTestModels",
    "m",
]
