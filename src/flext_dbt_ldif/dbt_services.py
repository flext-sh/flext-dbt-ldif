"""Service layer for LDIF to DBT workflows."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path

from flext_core import FlextLogger, r, t
from pydantic import TypeAdapter

from .constants import c
from .dbt_client import FlextDbtLdifClient
from .dbt_models import FlextDbtLdifUnifiedService
from .settings import FlextDbtLdifSettings

logger = FlextLogger(__name__)
_ENTRY_CONTAINER_LIST_ADAPTER = TypeAdapter(list[dict[str, t.ContainerValue]])


class FlextDbtLdifService:
    """Orchestrates parsing, validation, model generation, and transformations."""

    def __init__(
        self,
        config: FlextDbtLdifSettings | None = None,
        project_dir: Path | None = None,
    ) -> None:
        """Initialize service dependencies."""
        self.config = (
            config if config is not None else FlextDbtLdifSettings.get_global()
        )
        self.project_dir = project_dir or Path(str(self.config.ldif_file_path or "."))
        self.client = FlextDbtLdifClient(self.config)
        self.model_generator = FlextDbtLdifUnifiedService(
            config=self.config, project_dir=self.project_dir
        )

    def generate_and_write_models(
        self,
        entries: Sequence[dict[str, t.ContainerValue]],
        *,
        overwrite: bool = False,
    ) -> r[t.Dict]:
        """Generate staging and analytics models for entries."""
        _ = overwrite
        staging_payload: list[Mapping[str, t.ContainerValue]] = [
            {"dn": str(entry.get("dn", ""))} for entry in entries
        ]
        staging = self.model_generator.generate_staging_models(staging_payload)
        if staging.is_failure:
            return r[t.Dict].fail(staging.error or "Staging model generation failed")
        analytics = self.model_generator.generate_analytics_models(staging.value)
        if analytics.is_failure:
            return r[t.Dict].fail(
                analytics.error or "Analytics model generation failed"
            )
        all_models = [*staging.value, *analytics.value]
        return r[t.Dict].ok({
            "models_generated": len(all_models),
            "model_names": ",".join(model.name for model in all_models),
        })

    def parse_and_validate_ldif(self, ldif_file: Path | str) -> r[t.Dict]:
        """Parse and validate LDIF file in one operation."""
        parse_result = self.client.parse_ldif_file(ldif_file)
        if parse_result.is_failure:
            return r[t.Dict].fail(parse_result.error or "Parse failed")
        entries = _ENTRY_CONTAINER_LIST_ADAPTER.validate_python(parse_result.value)
        validation = self.client.validate_ldif_data(entries)
        if validation.is_failure:
            return r[t.Dict].fail(validation.error or "Validation failed")
        quality_score_value = validation.value.get("quality_score", 0.0)
        quality_score = (
            float(quality_score_value)
            if isinstance(quality_score_value, t.Primitives)
            else 0.0
        )
        return r[t.Dict].ok({
            "entry_count": len(entries),
            "quality_score": quality_score,
            "validation_status": str(validation.value.get("validation_status", "")),
        })

    def run_complete_workflow(
        self,
        ldif_file: Path | str,
        *,
        generate_models: bool = True,
        run_transformations: bool = True,
        model_names: list[str] | None = None,
    ) -> r[t.Dict]:
        """Execute complete LDIF to DBT workflow."""
        parse_result = self.client.parse_ldif_file(ldif_file)
        if parse_result.is_failure:
            return r[t.Dict].fail(parse_result.error or "Parse failed")
        entries = _ENTRY_CONTAINER_LIST_ADAPTER.validate_python(parse_result.value)
        validation = self.client.validate_ldif_data(entries)
        if validation.is_failure:
            return r[t.Dict].fail(validation.error or "Validation failed")
        workflow_result: dict[str, t.Scalar] = {
            "ldif_file": str(ldif_file),
            "entry_count": len(entries),
            "validation_status": str(validation.value.get("validation_status", "")),
        }
        if generate_models:
            model_result = self.generate_and_write_models(entries)
            if model_result.is_failure:
                return r[t.Dict].fail(
                    model_result.error or "Model generation workflow failed"
                )
            models_generated_value = model_result.value.get("models_generated", 0)
            models_generated = (
                int(models_generated_value)
                if isinstance(models_generated_value, t.Primitives)
                else 0
            )
            workflow_result["models_generated"] = int(models_generated)
        if run_transformations:
            transform_payload: list[dict[str, t.ContainerValue]] = [
                {"dn": str(entry.get("dn", ""))} for entry in entries
            ]
            transform = self.client.transform_with_dbt(transform_payload, model_names)
            if transform.is_failure:
                return r[t.Dict].fail(
                    transform.error or "Transformation workflow failed"
                )
            workflow_result["transformation_status"] = str(
                transform.value.get("status", "")
            )
        workflow_result["workflow_status"] = c.DbtLdif.WORKFLOW_STATUS_COMPLETED
        logger.info("Completed DBT LDIF workflow")
        return r[t.Dict].ok(workflow_result)

    def run_data_quality_assessment(self, ldif_file: Path | str) -> r[t.Dict]:
        """Run quality assessment focused workflow."""
        return self.parse_and_validate_ldif(ldif_file)


__all__ = ["FlextDbtLdifService"]
