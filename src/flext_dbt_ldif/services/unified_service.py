"""UnifiedService mixin for dbt-ldif utilities.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldif/services/unified_service
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
from typing import Annotated, override

from flext_meltano import FlextMeltanoDbtServiceBase

from flext_dbt_ldif import c, m, p, r, s, t


class FlextDbtLdifUnifiedService:
    """Mixin providing UnifiedService for dbt-ldif utilities."""

    class UnifiedService(s):
        """Service that generates lightweight DBT model artifacts from LDIF entries."""

        name: Annotated[
            str,
            m.Field(
                description="Service name used in generated metadata payloads.",
                validate_default=True,
            ),
        ] = c.DbtLdif.GENERATOR_SERVICE_NAME
        project_dir: Annotated[
            Path,
            m.Field(description="Project directory used to emit generated artifacts."),
        ] = m.Field(default_factory=Path.cwd)

        def __init__(
            self,
            settings: p.Settings | None = None,
            name: str = c.DbtLdif.GENERATOR_SERVICE_NAME,
            project_dir: Path | None = None,
        ) -> None:
            """Initialize service with optional injected settings + project context.

            Args:
                settings: Settings contract forwarded to the service base
                    runtime; the global singleton is used when omitted.
                name: Service name recorded in generated metadata payloads.
                project_dir: Directory for generated artifacts; defaults
                    to the current working directory when omitted.

            """
            # NOTE (multi-agent): mro-rn88 — forward the canonical settings contract
            # to the ServiceBase runtime so the injected snapshot is honored.
            FlextMeltanoDbtServiceBase.__init__(self, settings=settings)
            self.name = name
            self.project_dir = Path(project_dir or Path.cwd())

        @override
        def execute(self) -> p.Result[t.JsonMapping]:
            """Execute service and return metadata payload.

            Returns:
                Result wrapping the readiness metadata for this service.

            """
            payload: t.JsonMapping = {
                "name": self.name,
                "project_dir": str(self.project_dir),
                "status": c.DbtLdif.WORKFLOW_STATUS_READY,
            }
            return r[t.JsonMapping].ok(payload)

        @staticmethod
        def generate_analytics_models(
            staging_models: Sequence[m.DbtLdif.DbtModel],
        ) -> p.Result[list[m.DbtLdif.DbtModel]]:
            """Generate one analytics model derived from staging set.

            Args:
                staging_models: Staging models the analytics model
                    depends on.

            Returns:
                Result wrapping the analytics model, or an empty list
                when no staging models are provided.

            """
            if not staging_models:
                return r[list[m.DbtLdif.DbtModel]].ok([])
            analytics = m.DbtLdif.DbtModel(
                name=c.DbtLdif.ANALYTICS_MODEL_NAME,
                dbt_model_type=c.DbtLdif.DBT_MODEL_TYPE_ANALYTICS,
                ldif_source=c.DbtLdif.LDIF_SOURCE_NAME,
                materialization=c.DbtLdif.DBT_MATERIALIZATION_TABLE,
                sql_content="select * from {{ ref('stg_ldif_entries') }}",
                description=c.DbtLdif.ANALYTICS_MODEL_DESCRIPTION,
                columns=[],
                dependencies=[c.DbtLdif.STAGING_MODEL_NAME],
            )
            return r[list[m.DbtLdif.DbtModel]].ok([analytics])

        @staticmethod
        def generate_staging_models(
            entries: Sequence[t.JsonMapping],
        ) -> p.Result[list[m.DbtLdif.DbtModel]]:
            """Generate simple staging models for provided LDIF entries.

            Args:
                entries: Parsed LDIF entries to derive the staging model
                    from.

            Returns:
                Result wrapping the staging model, or an empty list when
                no entries are provided.

            """
            if not entries:
                return r[list[m.DbtLdif.DbtModel]].ok([])
            model = m.DbtLdif.DbtModel(
                name=c.DbtLdif.STAGING_MODEL_NAME,
                dbt_model_type=c.DbtLdif.DBT_MODEL_TYPE_STAGING,
                ldif_source=c.DbtLdif.LDIF_SOURCE_NAME,
                materialization=c.DbtLdif.DBT_MATERIALIZATION_VIEW,
                sql_content="select * from {{ source('ldif', 'raw_ldif_entries') }}",
                description=c.DbtLdif.STAGING_MODEL_DESCRIPTION,
                columns=[],
                dependencies=[],
            )
            return r[list[m.DbtLdif.DbtModel]].ok([model])


__all__: list[str] = ["FlextDbtLdifUnifiedService"]
