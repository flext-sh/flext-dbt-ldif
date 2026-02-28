"""Model generation helpers for DBT LDIF pipelines."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import override

from flext_core import FlextResult, FlextService, t

from .constants import FlextDbtLdifConstants as c
from .models import FlextDbtLdifModels
from .settings import FlextDbtLdifSettings


class FlextDbtLdifUnifiedService(FlextService[Mapping[str, t.JsonValue]]):
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
        super().__init__()
        self.name = name
        self.project_dir = Path(project_dir or Path.cwd())
        self._settings = config or FlextDbtLdifSettings.get_global_instance()

    @override
    def execute(self) -> FlextResult[Mapping[str, t.JsonValue]]:
        """Execute service and return metadata payload."""
        return FlextResult[Mapping[str, t.JsonValue]].ok(
            {
                "name": self.name,
                "project_dir": str(self.project_dir),
                "status": c.WORKFLOW_STATUS_READY,
            },
        )

    def generate_staging_models(
        self,
        entries: Sequence[Mapping[str, t.JsonValue]],
    ) -> FlextResult[list[FlextDbtLdifModels.DbtModel]]:
        """Generate simple staging models for provided LDIF entries."""
        if not entries:
            return FlextResult[list[FlextDbtLdifModels.DbtModel]].ok([])

        model = FlextDbtLdifModels.DbtModel(
            name=c.STAGING_MODEL_NAME,
            dbt_model_type=c.DBT_MODEL_TYPE_STAGING,
            ldif_source=c.LDIF_SOURCE_NAME,
            materialization=c.DBT_MATERIALIZATION_VIEW,
            sql_content=f"select * from {{{{ source('ldif', '{c.LDIF_RAW_SOURCE}') }}}}",
            description=c.STAGING_MODEL_DESCRIPTION,
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
            name=c.ANALYTICS_MODEL_NAME,
            dbt_model_type=c.DBT_MODEL_TYPE_ANALYTICS,
            ldif_source=c.LDIF_SOURCE_NAME,
            materialization=c.DBT_MATERIALIZATION_TABLE,
            sql_content=f"select * from {{{{ ref('{c.STAGING_MODEL_NAME}') }}}}",
            description=c.ANALYTICS_MODEL_DESCRIPTION,
            dependencies=[c.STAGING_MODEL_NAME],
        )
        return FlextResult[list[FlextDbtLdifModels.DbtModel]].ok([analytics])


__all__ = ["FlextDbtLdifUnifiedService"]
