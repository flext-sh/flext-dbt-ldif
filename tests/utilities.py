"""Test utilities for flext-dbt-ldif.

Provides TestsFlextDbtLdifUtilities, combining TestsFlextUtilities with
FlextDbtLdifUtilities for test-specific utility definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsUtilities

from flext_dbt_ldif import FlextDbtLdifUtilities


class TestsFlextDbtLdifUtilities(FlextTestsUtilities, FlextDbtLdifUtilities):
    """Test utilities combining TestsFlextUtilities with flext-dbt-ldif utilities."""

    class DbtLdif(FlextDbtLdifUtilities.DbtLdif):
        """DbtLdif test utilities namespace."""

        class Tests:
            """Project-specific test utilities."""


u = TestsFlextDbtLdifUtilities

__all__ = ["TestsFlextDbtLdifUtilities", "u"]
