"""Test constants for flext-dbt-ldif tests.

Provides TestsFlextDbtLdifConstants, extending FlextTestsConstants with
flext-dbt-ldif-specific constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants

from flext_dbt_ldif import c


class TestsFlextDbtLdifConstants(FlextTestsConstants, c):
    """Constants for flext-dbt-ldif tests.

    Inherits from FlextTestsConstants and c for
    full production constant access.
    """

    class DbtLdif(c.DbtLdif):
        """DbtLdif test constants namespace."""

        class Tests(FlextTestsConstants.Tests):
            """Project-specific test constants."""


c = TestsFlextDbtLdifConstants
__all__: list[str] = ["TestsFlextDbtLdifConstants", "c"]
