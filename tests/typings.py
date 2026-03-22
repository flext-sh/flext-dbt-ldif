"""Test type definitions for flext-dbt-ldif.

Provides FlextDbtLdifTestTypes, combining FlextTestsTypes with
FlextDbtLdifTypes for test-specific type definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_dbt_ldif import FlextDbtLdifTypes


class FlextDbtLdifTestTypes(FlextTestsTypes, FlextDbtLdifTypes):
    """Test types combining FlextTestsTypes with flext-dbt-ldif types."""


t = FlextDbtLdifTestTypes

__all__ = [
    "FlextDbtLdifTestTypes",
    "t",
]
