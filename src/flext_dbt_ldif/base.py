"""Shared service foundation for flext-dbt-ldif components.

Inherits from FlextMeltanoDbtServiceBase which provides dbt command
execution (run_models, run_tests, compile, docs, manifest, CLI).
This base adds typed settings access for dbt-ldif domain.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

from flext_dbt_ldif import FlextDbtLdifSettings, m, p, settings, t, u
from flext_meltano import FlextMeltanoDbtServiceBase


class FlextDbtLdifServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-ldif services."""

    dbt_project_name: Annotated[
        t.NonEmptyStr,
        u.Field(description="Canonical dbt project name for DBT LDIF services"),
    ] = "dbt-ldif"

    @classmethod
    def _runtime_bootstrap_options(cls) -> p.RuntimeBootstrapOptions:
        """Return runtime bootstrap options for DBT LDIF services."""
        return m.RuntimeBootstrapOptions(settings_type=FlextDbtLdifSettings)

    @property
    @override
    def connection_profile(self) -> p.Meltano.DbtConnectionProfile:
        """Dbt connection profile for LDIF-backed workflows."""
        # NOTE (multi-agent): mro-rn88 ADR-006 thin-driver — read INJECTED settings.
        return m.DbtLdif.DbtConnectionProfile(
            path=settings.DbtLdif.ldif_file_path,
            project=self.dbt_project_name,
        )


s = FlextDbtLdifServiceBase

__all__: list[str] = ["FlextDbtLdifServiceBase", "s"]
