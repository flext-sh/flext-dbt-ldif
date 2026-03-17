"""Module skeleton for TestsFlextDbtLdifUtilities.

Test utilities for flextdbtldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsUtilities

from flext_dbt_ldif import FlextDbtLdifUtilities


class TestsFlextDbtLdifUtilities(FlextTestsUtilities, FlextDbtLdifUtilities):
    """Test utilities for flextdbtldif."""

    class DbtLdif(FlextDbtLdifUtilities.DbtLdif):
        """DbtLdif test utilities namespace."""

        class Tests:
            """Project-specific test utilities."""


u = TestsFlextDbtLdifUtilities

__all__ = ["TestsFlextDbtLdifUtilities", "u"]
