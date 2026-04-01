"""Shared service foundation for flext-dbt-ldif components.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from abc import ABC
from typing import override

from flext_core import FlextSettings, s

from flext_dbt_ldif import FlextDbtLdifSettings, t


class FlextDbtLdifServiceBase(s[t.ContainerMapping], ABC):
    """Base class for flext-dbt-ldif services with typed configuration access."""

    @property
    @override
    def settings(self) -> FlextDbtLdifSettings:
        """Return the typed dbt-ldif settings namespace."""
        return FlextSettings.get_global().get_namespace(
            "dbt_ldif", FlextDbtLdifSettings
        )


__all__ = ["FlextDbtLdifServiceBase"]
