"""Test protocol definitions for flext-dbt-ldif.

Provides TestsFlextDbtLdifProtocols, combining TestsFlextProtocols with
p for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_dbt_ldif import FlextDbtLdifProtocols


class TestsFlextDbtLdifProtocols(FlextTestsProtocols, FlextDbtLdifProtocols):
    """Test protocols combining TestsFlextProtocols and p."""

    class DbtLdif(FlextDbtLdifProtocols.DbtLdif):
        """DbtLdif test protocols namespace."""

        class Tests:
            """Project-specific test protocols."""


p = TestsFlextDbtLdifProtocols
__all__: list[str] = ["TestsFlextDbtLdifProtocols", "p"]
