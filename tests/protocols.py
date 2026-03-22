"""Test protocol definitions for flext-dbt-ldif.

Provides FlextDbtLdifTestProtocols, combining FlextTestsProtocols with
FlextDbtLdifProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_dbt_ldif import FlextDbtLdifProtocols


class FlextDbtLdifTestProtocols(FlextTestsProtocols, FlextDbtLdifProtocols):
    """Test protocols combining FlextTestsProtocols and FlextDbtLdifProtocols."""

    class DbtLdif(FlextDbtLdifProtocols.DbtLdif):
        """DbtLdif test protocols namespace."""

        class Tests:
            """Project-specific test protocols."""


p = FlextDbtLdifTestProtocols
__all__ = ["FlextDbtLdifTestProtocols", "p"]
