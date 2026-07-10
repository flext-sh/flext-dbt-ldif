"""Shared service foundation for flext-dbt-ldif components.

Inherits from FlextMeltanoDbtServiceBase which provides dbt command
execution (run_models, run_tests, compile, docs, manifest, CLI).
This base adds typed settings access for dbt-ldif domain.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

from flext_dbt_ldif import FlextDbtLdifSettings, m, t
from flext_meltano import FlextMeltanoDbtServiceBase, u


class FlextDbtLdifServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-ldif services."""

    dbt_project_name: Annotated[
        t.NonEmptyStr,
        u.Field(description="Canonical dbt project name for DBT LDIF services"),
    ] = "dbt-ldif"

    @classmethod
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        """Return runtime bootstrap options for DBT LDIF services."""
        return m.RuntimeBootstrapOptions(settings_type=FlextDbtLdifSettings)

    @property
    @override
    def settings(self) -> FlextDbtLdifSettings:
        """The typed dbt-ldif settings namespace."""
        return settings

    @property
    @override
    def connection_profile(self) -> t.JsonMapping:
        """Dbt connection profile for LDIF-backed workflows."""
        return {
            "type": "ldif",
            "path": settings.DbtLdif.ldif_file_path,
            "project": self.dbt_project_name,
        }


s = FlextDbtLdifServiceBase

__all__: list[str] = ["FlextDbtLdifServiceBase", "s"]
