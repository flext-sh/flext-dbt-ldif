"""Test type definitions for flext-dbt-ldif.

Provides TestsFlextDbtLdifTypes, combining TestsFlextTypes with
t for test-specific type definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_dbt_ldif import t


class TestsFlextDbtLdifTypes(FlextTestsTypes, t):
    """Test types combining FlextTestsTypes with flext-dbt-ldif types."""

    class DbtLdif(t.DbtLdif):
        """DbtLdif test types namespace."""

        class Tests:
            """Test-specific type aliases."""


t = TestsFlextDbtLdifTypes

__all__: list[str] = [
    "TestsFlextDbtLdifTypes",
    "t",
]
