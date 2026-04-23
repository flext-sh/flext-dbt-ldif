"""Shared service foundation for flext-dbt-ldif components.

Inherits from FlextMeltanoDbtServiceBase which provides dbt command
execution (run_models, run_tests, compile, docs, manifest, CLI).
This base adds typed settings access for dbt-ldif domain.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_core import FlextSettings
from flext_meltano import FlextMeltanoDbtServiceBase, FlextMeltanoSettings

from flext_dbt_ldif import t


class FlextDbtLdifServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-ldif services.

    Inherits dbt execution infrastructure from FlextMeltanoDbtServiceBase.
    Adds typed settings for the dbt-ldif domain.
    """

    dbt_project_name: t.NonEmptyStr = "dbt-ldif"

    @property
    @override
    def settings(self) -> FlextMeltanoSettings:
        """Return the typed dbt-ldif settings namespace."""
        return FlextSettings.fetch_global().fetch_namespace(
            "dbt_ldif", FlextMeltanoSettings
        )

    @override
    @property
    @override
    def connection_profile(self) -> t.JsonMapping:
        """Dbt connection profile for LDIF (file-based, no DB)."""
        return {"type": "file", "project": self.dbt_project_name}


__all__: list[str] = ["FlextDbtLdifServiceBase"]
