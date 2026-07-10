"""UnifiedService mixin for dbt-ldif utilities."""

from __future__ import annotations

from pathlib import Path
from typing import override

from flext_dbt_ldif import FlextDbtLdifSettings, c, m, p, r, s, t, u


class FlextDbtLdifUnifiedService:
    """Mixin providing UnifiedService for dbt-ldif utilities."""

    class UnifiedService(s):
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
            settings: FlextDbtLdifSettings | None = None,
            name: str = "ldif_generator",
            project_dir: Path | None = None,
        ) -> None:
            """Initialize service with optional injected settings + project context."""
            # NOTE (multi-agent): mro-rn88 — accept injected settings and pass them to the
            # ServiceBase runtime so self.settings resolves the injected instance.
            super().__init__()
            if settings is not None:
                self.runtime_settings = settings
            self.name = name
            self.project_dir = Path(project_dir or Path.cwd())

        @override
        def execute(self) -> p.Result[t.JsonMapping]:
            """Execute service and return metadata payload."""
            payload: t.JsonMapping = {
                "name": self.name,
                "project_dir": str(self.project_dir),
                "status": c.DbtLdif.WORKFLOW_STATUS_READY,
            }
            return r[t.JsonMapping].ok(payload)

        def generate_analytics_models(
            self,
            staging_models: t.SequenceOf[m.DbtLdif.DbtModel],
        ) -> p.Result[list[m.DbtLdif.DbtModel]]:
            """Generate one analytics model derived from staging set."""
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

        def generate_staging_models(
            self,
            entries: t.SequenceOf[t.JsonMapping],
        ) -> p.Result[list[m.DbtLdif.DbtModel]]:
            """Generate simple staging models for provided LDIF entries."""
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
