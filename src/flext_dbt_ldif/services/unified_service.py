"""UnifiedService mixin for dbt-ldif utilities."""

from __future__ import annotations

from collections.abc import (
    Sequence,
)
from pathlib import Path
from typing import override

from flext_dbt_ldif import FlextDbtLdifSettings, c, m, p, r, s, t, u


class FlextDbtLdifUnifiedService:
    """Mixin providing UnifiedService for dbt-ldif utilities."""

    class UnifiedService(s[m.DbtLdif.UnifiedServicePayload]):
        """Service that generates lightweight DBT model artifacts from LDIF entries."""

        name: str = u.Field(
            "ldif_generator",
            description="Service name used in generated metadata payloads.",
            validate_default=True,
        )
        project_dir: Path = u.Field(
            default_factory=Path.cwd,
            description="Project directory used to emit generated artifacts.",
        )

        def __init__(
            self,
            name: str = "ldif_generator",
            settings: FlextDbtLdifSettings | None = None,
            project_dir: Path | None = None,
        ) -> None:
            """Initialize service with project and settings context."""
            super().__init__()
            self.name = name
            self.project_dir = Path(project_dir or Path.cwd())
            self._settings = (
                settings
                if settings is not None
                else FlextDbtLdifSettings.fetch_global()
            )

        @override
        def execute(self) -> p.Result[m.DbtLdif.UnifiedServicePayload]:
            """Execute service and return metadata payload."""
            return r[m.DbtLdif.UnifiedServicePayload].ok(
                m.DbtLdif.UnifiedServicePayload(
                    payload={
                        "name": self.name,
                        "project_dir": str(self.project_dir),
                        "status": c.DbtLdif.WORKFLOW_STATUS_READY,
                    }
                )
            )

        def generate_analytics_models(
            self,
            staging_models: Sequence[m.DbtLdif.DbtModel],
        ) -> p.Result[Sequence[m.DbtLdif.DbtModel]]:
            """Generate one analytics model derived from staging set."""
            if not staging_models:
                return r[Sequence[m.DbtLdif.DbtModel]].ok([])
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
            return r[Sequence[m.DbtLdif.DbtModel]].ok([analytics])

        def generate_staging_models(
            self,
            entries: Sequence[t.JsonMapping],
        ) -> p.Result[Sequence[m.DbtLdif.DbtModel]]:
            """Generate simple staging models for provided LDIF entries."""
            if not entries:
                return r[Sequence[m.DbtLdif.DbtModel]].ok([])
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
            return r[Sequence[m.DbtLdif.DbtModel]].ok([model])
