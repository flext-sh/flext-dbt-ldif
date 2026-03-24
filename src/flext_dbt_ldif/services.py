"""Service layer for LDIF to DBT workflows."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path

from flext_core import FlextLogger, FlextTypes, r
from pydantic import RootModel

from flext_dbt_ldif import (
    FlextDbtLdifClient,
    FlextDbtLdifSettings,
    FlextDbtLdifUnifiedService,
    c,
    m,
    t,
)


class EntryContainerListAdapter(
    RootModel[Sequence[Mapping[str, FlextTypes.ContainerValue]]]
):
    """Adapter for list of container entries."""

    root: Sequence[Mapping[str, FlextTypes.ContainerValue]]


logger = FlextLogger(__name__)


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
        entries: Sequence[Mapping[str, t.ContainerValue]],
        *,
        overwrite: bool = False,
    ) -> r[m.DbtLdif.ModelGenerationResult]:
        """Generate staging and analytics models for entries."""
        _ = overwrite
        staging_payload: Sequence[Mapping[str, t.ContainerValue]] = [
            {"dn": str(entry.get("dn", ""))} for entry in entries
        ]
        staging = self.model_generator.generate_staging_models(staging_payload)
        if staging.is_failure:
            return r[m.DbtLdif.ModelGenerationResult].fail(
                staging.error or "Staging model generation failed"
            )
        analytics = self.model_generator.generate_analytics_models(staging.value)
        if analytics.is_failure:
            return r[m.DbtLdif.ModelGenerationResult].fail(
                analytics.error or "Analytics model generation failed"
            )
        all_models = [*staging.value, *analytics.value]
        return r[m.DbtLdif.ModelGenerationResult].ok(
            m.DbtLdif.ModelGenerationResult(
                models_generated=len(all_models),
                model_names=[model.name for model in all_models],
            )
        )

    def parse_and_validate_ldif(
        self, ldif_file: Path | str
    ) -> r[m.DbtLdif.ParseValidationResult]:
        """Parse and validate LDIF file in one operation."""
        parse_result = self.client.parse_ldif_file(ldif_file)
        if parse_result.is_failure:
            return r[m.DbtLdif.ParseValidationResult].fail(
                parse_result.error or "Parse failed"
            )
        entries = EntryContainerListAdapter.model_validate(parse_result.value).root
        validation = self.client.validate_ldif_data(entries)
        if validation.is_failure:
            return r[m.DbtLdif.ParseValidationResult].fail(
                validation.error or "Validation failed"
            )
        return r[m.DbtLdif.ParseValidationResult].ok(
            m.DbtLdif.ParseValidationResult(
                entry_count=len(entries),
                quality_score=validation.value.quality_score,
                validation_status=validation.value.validation_status,
            )
        )

    def run_complete_workflow(
        self,
        ldif_file: Path | str,
        *,
        generate_models: bool = True,
        run_transformations: bool = True,
        model_names: t.StrSequence | None = None,
    ) -> r[m.DbtLdif.WorkflowResult]:
        """Execute complete LDIF to DBT workflow."""
        parse_result = self.client.parse_ldif_file(ldif_file)
        if parse_result.is_failure:
            return r[m.DbtLdif.WorkflowResult].fail(
                parse_result.error or "Parse failed"
            )
        entries = EntryContainerListAdapter.model_validate(parse_result.value).root
        validation = self.client.validate_ldif_data(entries)
        if validation.is_failure:
            return r[m.DbtLdif.WorkflowResult].fail(
                validation.error or "Validation failed"
            )
        workflow_result = m.DbtLdif.WorkflowResult(
            ldif_file=str(ldif_file),
            entry_count=len(entries),
            validation_status=validation.value.validation_status,
            workflow_status=c.DbtLdif.WORKFLOW_STATUS_COMPLETED,
        )
        if generate_models:
            model_result = self.generate_and_write_models(entries)
            if model_result.is_failure:
                return r[m.DbtLdif.WorkflowResult].fail(
                    model_result.error or "Model generation workflow failed"
                )
            workflow_result.models_generated = model_result.value.models_generated
        if run_transformations:
            transform_payload: Sequence[Mapping[str, t.ContainerValue]] = [
                {"dn": str(entry.get("dn", ""))} for entry in entries
            ]
            transform = self.client.transform_with_dbt(transform_payload, model_names)
            if transform.is_failure:
                return r[m.DbtLdif.WorkflowResult].fail(
                    transform.error or "Transformation workflow failed"
                )
            workflow_result.transformation_status = transform.value.status
        logger.info("Completed DBT LDIF workflow")
        return r[m.DbtLdif.WorkflowResult].ok(workflow_result)

    def run_data_quality_assessment(
        self, ldif_file: Path | str
    ) -> r[m.DbtLdif.ParseValidationResult]:
        """Run quality assessment focused workflow."""
        return self.parse_and_validate_ldif(ldif_file)


s = FlextDbtLdifService

__all__ = ["FlextDbtLdifService", "s"]
