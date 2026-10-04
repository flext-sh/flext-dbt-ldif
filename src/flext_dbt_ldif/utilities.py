"""Utility functions for flext-dbt-ldif transformations.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldif/utilities
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifUtilities
from flext_meltano import FlextMeltanoUtilities


class FlextDbtLdifUtilities(FlextMeltanoUtilities, FlextLdifUtilities):
    """Utilities for dbt-ldif operations inheriting LDIF processing capabilities."""

    class DbtLdif:
        """DBT LDIF namespace over the canonical LDIF utility branch."""


u = FlextDbtLdifUtilities

__all__: list[str] = ["FlextDbtLdifUtilities", "u"]
