"""Model generation helpers for DBT LDIF pipelines."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import override

from flext_core import FlextService, r, t

from .constants import FlextDbtLdifConstants as c
from .models import FlextDbtLdifModels
from .settings import FlextDbtLdifSettings


class FlextDbtLdifUnifiedService(FlextService[Mapping[str, t.Scalar]]):
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
        self._settings = (
            config if config is not None else FlextDbtLdifSettings.get_global()
        )

    @override
    def execute(self) -> r[Mapping[str, t.Scalar]]:
        """Execute service and return metadata payload."""
        return r[Mapping[str, t.Scalar]].ok({
            "name": self.name,
            "project_dir": str(self.project_dir),
            "status": c.DbtLdif.WORKFLOW_STATUS_READY,
        })

    def generate_analytics_models(
        self, staging_models: list[FlextDbtLdifModels.DbtModel]
    ) -> r[list[FlextDbtLdifModels.DbtModel]]:
        """Generate one analytics model derived from staging set."""
        if not staging_models:
            return r[list[FlextDbtLdifModels.DbtModel]].ok([])
        analytics = FlextDbtLdifModels.DbtModel(
            name=c.DbtLdif.ANALYTICS_MODEL_NAME,
            dbt_model_type=c.DbtLdif.DBT_MODEL_TYPE_ANALYTICS,
            ldif_source=c.DbtLdif.LDIF_SOURCE_NAME,
            materialization=c.DbtLdif.DBT_MATERIALIZATION_TABLE,
            sql_content=f"select * from {{{{ ref('{c.DbtLdif.STAGING_MODEL_NAME}') }}}}",
            description=c.DbtLdif.ANALYTICS_MODEL_DESCRIPTION,
            dependencies=[c.DbtLdif.STAGING_MODEL_NAME],
        )
        return r[list[FlextDbtLdifModels.DbtModel]].ok([analytics])

    def generate_staging_models(
        self, entries: Sequence[Mapping[str, t.Scalar]]
    ) -> r[list[FlextDbtLdifModels.DbtModel]]:
        """Generate simple staging models for provided LDIF entries."""
        if not entries:
            return r[list[FlextDbtLdifModels.DbtModel]].ok([])
        model = FlextDbtLdifModels.DbtModel(
            name=c.DbtLdif.STAGING_MODEL_NAME,
            dbt_model_type=c.DbtLdif.DBT_MODEL_TYPE_STAGING,
            ldif_source=c.DbtLdif.LDIF_SOURCE_NAME,
            materialization=c.DbtLdif.DBT_MATERIALIZATION_VIEW,
            sql_content=f"select * from {{{{ source('ldif', '{c.DbtLdif.LDIF_RAW_SOURCE}') }}}}",
            description=c.DbtLdif.STAGING_MODEL_DESCRIPTION,
        )
        return r[list[FlextDbtLdifModels.DbtModel]].ok([model])


__all__ = ["FlextDbtLdifUnifiedService"]
