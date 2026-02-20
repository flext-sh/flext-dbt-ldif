"""Service layer for LDIF to DBT workflows."""

from __future__ import annotations

from pathlib import Path

from flext_core import FlextLogger, FlextResult, FlextTypes as t

from .dbt_client import FlextDbtLdifClient
from .dbt_models import FlextDbtLdifUnifiedService
from .settings import FlextDbtLdifSettings

logger = FlextLogger(__name__)


class FlextDbtLdifService:
    """Orchestrates parsing, validation, model generation, and transformations."""

    def __init__(
        self,
        config: FlextDbtLdifSettings | None = None,
        project_dir: Path | None = None,
    ) -> None:
        """Initialize service dependencies."""
        self.config = config or FlextDbtLdifSettings.get_global_instance()
        self.project_dir = project_dir or Path(self.config.dbt_project_dir)
        self.client = FlextDbtLdifClient(self.config)
        self.model_generator = FlextDbtLdifUnifiedService(
            config=self.config,
            project_dir=self.project_dir,
        )

    def parse_and_validate_ldif(
        self,
        ldif_file: Path | str,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Parse and validate LDIF file in one operation."""
        parse_result = self.client.parse_ldif_file(ldif_file)
        if parse_result.is_failure or parse_result.value is None:
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                parse_result.error or "Parse failed",
            )
        validation = self.client.validate_ldif_data(parse_result.value)
        if validation.is_failure or validation.value is None:
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                validation.error or "Validation failed",
            )
        return FlextResult[dict[str, t.GeneralValueType]].ok(
            {
                "entries": parse_result.value,
                "entry_count": len(parse_result.value),
                "validation_metrics": validation.value,
            },
        )

    def generate_and_write_models(
        self,
        entries: list[dict[str, t.GeneralValueType]],
        *,
        overwrite: bool = False,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Generate staging and analytics models for entries."""
        _ = overwrite
        staging_payload: list[dict[str, t.JsonValue]] = [
            {"dn": str(entry.get("dn", ""))} for entry in entries
        ]
        staging = self.model_generator.generate_staging_models(staging_payload)
        if staging.is_failure or staging.value is None:
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                staging.error or "Staging model generation failed",
            )
        analytics = self.model_generator.generate_analytics_models(staging.value)
        if analytics.is_failure or analytics.value is None:
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                analytics.error or "Analytics model generation failed",
            )
        all_models = [*staging.value, *analytics.value]
        return FlextResult[dict[str, t.GeneralValueType]].ok(
            {
                "models_generated": len(all_models),
                "model_names": [model.name for model in all_models],
            },
        )

    def run_complete_workflow(
        self,
        ldif_file: Path | str,
        *,
        generate_models: bool = True,
        run_transformations: bool = True,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Execute complete LDIF to DBT workflow."""
        parse_validation = self.parse_and_validate_ldif(ldif_file)
        if parse_validation.is_failure or parse_validation.value is None:
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                parse_validation.error or "Parse/validate workflow failed",
            )

        workflow_result: dict[str, t.GeneralValueType] = {
            "ldif_file": str(ldif_file),
            "parse_validation": parse_validation.value,
        }

        entries_raw = parse_validation.value.get("entries", [])
        entries_payload = entries_raw if isinstance(entries_raw, list) else []
        entries = [entry for entry in entries_payload if isinstance(entry, dict)]

        if generate_models:
            model_result = self.generate_and_write_models(entries)
            if model_result.is_failure or model_result.value is None:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    model_result.error or "Model generation workflow failed",
                )
            workflow_result["model_generation"] = model_result.value

        if run_transformations:
            transform_payload: list[dict[str, t.GeneralValueType]] = [
                {"dn": str(entry.get("dn", ""))} for entry in entries
            ]
            transform = self.client.transform_with_dbt(transform_payload, model_names)
            if transform.is_failure or transform.value is None:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    transform.error or "Transformation workflow failed",
                )
            workflow_result["transformations"] = transform.value

        workflow_result["workflow_status"] = "completed"
        logger.info("Completed DBT LDIF workflow")
        return FlextResult[dict[str, t.GeneralValueType]].ok(workflow_result)

    def run_data_quality_assessment(
        self,
        ldif_file: Path | str,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Run quality assessment focused workflow."""
        return self.parse_and_validate_ldif(ldif_file)


__all__ = ["FlextDbtLdifService"]
