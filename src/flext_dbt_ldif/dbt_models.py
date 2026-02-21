"""Model generation helpers for DBT LDIF pipelines."""

from __future__ import annotations

from pathlib import Path

from flext_core import FlextResult, FlextService, t

from .models import FlextDbtLdifModels
from .settings import FlextDbtLdifSettings


class FlextDbtLdifUnifiedService(FlextService[dict[str, t.JsonValue]]):
    """Service that generates lightweight DBT model artifacts from LDIF entries."""

    name: str = "ldif_generator"
    project_dir: Path = Path.cwd()

    def __init__(
        self,
        name: str = "ldif_generator",
        config: FlextDbtLdifSettings | None = None,
        project_dir: Path | None = None,
    ) -> None:
        """Initialize service with project and settings context."""
        super().__init__(name=name, project_dir=project_dir or Path.cwd())
        self._settings = config or FlextDbtLdifSettings.get_global_instance()

    def execute(self) -> FlextResult[dict[str, t.JsonValue]]:
        """Execute service and return metadata payload."""
        return FlextResult[dict[str, t.JsonValue]].ok(
            {
                "name": self.name,
                "project_dir": str(self.project_dir),
                "status": "ready",
            },
        )

    def generate_staging_models(
        self,
        entries: list[dict[str, t.JsonValue]],
    ) -> FlextResult[list[FlextDbtLdifModels.DbtModel]]:
        """Generate simple staging models for provided LDIF entries."""
        if not entries:
            return FlextResult[list[FlextDbtLdifModels.DbtModel]].ok([])

        model = FlextDbtLdifModels.DbtModel(
            name="stg_ldif_entries",
            dbt_model_type="staging",
            ldif_source="ldif_entries",
            materialization="view",
            sql_content="select * from {{ source('ldif', 'raw_ldif_entries') }}",
            description="Staging model for LDIF entries",
        )
        return FlextResult[list[FlextDbtLdifModels.DbtModel]].ok([model])

    def generate_analytics_models(
        self,
        staging_models: list[FlextDbtLdifModels.DbtModel],
    ) -> FlextResult[list[FlextDbtLdifModels.DbtModel]]:
        """Generate one analytics model derived from staging set."""
        if not staging_models:
            return FlextResult[list[FlextDbtLdifModels.DbtModel]].ok([])
        analytics = FlextDbtLdifModels.DbtModel(
            name="analytics_ldif_insights",
            dbt_model_type="analytics",
            ldif_source="ldif_entries",
            materialization="table",
            sql_content="select * from {{ ref('stg_ldif_entries') }}",
            description="Analytics model for LDIF insights",
            dependencies=["stg_ldif_entries"],
        )
        return FlextResult[list[FlextDbtLdifModels.DbtModel]].ok([analytics])


__all__ = ["FlextDbtLdifUnifiedService"]
