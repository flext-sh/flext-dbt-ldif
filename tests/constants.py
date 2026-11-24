"""Test constants for flext-dbt-ldif tests.

Provides TestsFlextDbtLdifConstants, extending FlextTestsConstants with
flext-dbt-ldif-specific constants.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants

from tests import FlextDbtLdifConstants


class TestsFlextDbtLdifConstants(FlextTestsConstants, FlextDbtLdifConstants):
    """Constants for flext-dbt-ldif tests.

    Inherits from FlextTestsConstants and c for
    full production constant access.
    """

    class Tests(FlextTestsConstants.Tests):
        """Project-specific test constants."""


c = TestsFlextDbtLdifConstants
__all__: list[str] = ["TestsFlextDbtLdifConstants", "c"]
