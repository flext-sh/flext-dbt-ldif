"""Test protocol definitions for flext-dbt-ldif.

Provides TestsFlextDbtLdifProtocols, combining FlextTestsProtocols with
FlextDbtLdifProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_ldif.protocols import FlextDbtLdifProtocols
from flext_tests.protocols import FlextTestsProtocols


class TestsFlextDbtLdifProtocols(FlextTestsProtocols, FlextDbtLdifProtocols):
    """Test protocols combining FlextTestsProtocols and FlextDbtLdifProtocols.

    Provides access to:
    - tp.Tests.Docker.* (from FlextTestsProtocols)
    - tp.Tests.Factory.* (from FlextTestsProtocols)
    - tp.DbtLdif.* (from FlextDbtLdifProtocols)
    """

    class Tests:
        """Project-specific test protocols.

        Extends FlextTestsProtocols.Tests with DbtLdif-specific protocols.
        """

        class DbtLdif:
            """DbtLdif-specific test protocols."""


# Runtime aliases
p = TestsFlextDbtLdifProtocols
tp = TestsFlextDbtLdifProtocols

__all__ = ["TestsFlextDbtLdifProtocols", "p", "tp"]
