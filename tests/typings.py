"""Test type definitions for flext-dbt-ldif.

Provides TestsFlextDbtLdifTypes, combining TestsFlextTypes with
t for test-specific type definitions.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from tests import FlextDbtLdifTypes


class TestsFlextDbtLdifTypes(FlextTestsTypes, FlextDbtLdifTypes):
    """Test types combining FlextTestsTypes with flext-dbt-ldif types."""

    class Tests(FlextTestsTypes.Tests):
        """Test-specific type aliases."""


t = TestsFlextDbtLdifTypes

__all__: list[str] = ["TestsFlextDbtLdifTypes", "t"]
