"""Service mixin for dbt-ldif utilities."""

from __future__ import annotations

from pathlib import Path

from flext_dbt_ldif import (
    FlextDbtLdifSettings,
    c,
    m,
    p,
    r,
    t,
    u,
)
from flext_dbt_ldif.services.client import FlextDbtLdifClient
from flext_dbt_ldif.services.unified_service import FlextDbtLdifUnifiedService


class FlextDbtLdifServiceMixin:
    """Mixin providing Service for dbt-ldif utilities."""

    logger = u.fetch_logger(__name__)

    class Service:
        """Orchestrates parsing, validation, model generation, and transformations."""

        def __init__(
            self,
            settings: FlextDbtLdifSettings | None = None,
            project_dir: Path | None = None,
        ) -> None:
            """Initialize service dependencies with optional injected settings."""
            # NOTE (multi-agent): mro-rn88 — resolve effective settings (injected override
            # or global) and inject the SAME instance into client + generator.
            effective_settings = settings or FlextDbtLdifSettings.fetch_global()
            self.project_dir = project_dir or Path(
                effective_settings.DbtLdif.ldif_file_path or ".",
            )
            self.client = FlextDbtLdifClient.Client(effective_settings)
            self.model_generator = FlextDbtLdifUnifiedService.UnifiedService(
                settings=effective_settings,
                project_dir=self.project_dir,
            )

        def generate_and_write_models(
            self,
            entries: t.SequenceOf[t.JsonMapping],
            *,
            overwrite: bool = False,
        ) -> p.Result[p.DbtLdif.ModelGenerationResult]:
            """Generate staging and analytics models for entries."""
            _ = overwrite
            staging_payload: t.SequenceOf[t.JsonMapping] = [
                {"dn": str(entry.get("dn", ""))} for entry in entries
            ]
            staging = self.model_generator.generate_staging_models(staging_payload)
            if staging.failure:
                return r[p.DbtLdif.ModelGenerationResult].fail(
                    staging.error or "Staging model generation failed",
                )
            analytics = self.model_generator.generate_analytics_models(
                staging.value,
            )
            if analytics.failure:
                return r[p.DbtLdif.ModelGenerationResult].fail(
                    analytics.error or "Analytics model generation failed",
                )
            all_models = [*staging.value, *analytics.value]
            return r[p.DbtLdif.ModelGenerationResult].ok(
                m.DbtLdif.ModelGenerationResult(
                    models_generated=len(all_models),
                    model_names=[model.name for model in all_models],
                ),
            )

        def parse_and_validate_ldif(
            self,
            ldif_file: Path | str,
        ) -> p.Result[p.DbtLdif.ParseValidationResult]:
            """Parse and validate LDIF file in one operation."""
            parse_result = self.client.parse_ldif_file(ldif_file)
            if parse_result.failure:
                return r[p.DbtLdif.ParseValidationResult].fail(
                    parse_result.error or "Parse failed",
                )
            entries = t.json_mapping_sequence_adapter().validate_python(
                parse_result.value,
            )
            validation = self.client.validate_ldif_data(entries)
            if validation.failure:
                return r[p.DbtLdif.ParseValidationResult].fail(
                    validation.error or "Validation failed",
                )
            return r[p.DbtLdif.ParseValidationResult].ok(
                m.DbtLdif.ParseValidationResult(
                    entry_count=len(entries),
                    quality_score=validation.value.quality_score,
                    validation_status=validation.value.validation_status,
                ),
            )

        def run_complete_workflow(
            self,
            ldif_file: Path | str,
            *,
            generate_models: bool = True,
            run_transformations: bool = True,
            model_names: t.StrSequence | None = None,
        ) -> p.Result[p.DbtLdif.WorkflowResult]:
            """Execute complete LDIF to DBT workflow."""
            parse_result = self.client.parse_ldif_file(ldif_file)
            if parse_result.failure:
                return r[p.DbtLdif.WorkflowResult].fail(
                    parse_result.error or "Parse failed",
                )
            entries = t.json_mapping_sequence_adapter().validate_python(
                parse_result.value,
            )
            validation = self.client.validate_ldif_data(entries)
            if validation.failure:
                return r[p.DbtLdif.WorkflowResult].fail(
                    validation.error or "Validation failed",
                )
            workflow_result = m.DbtLdif.WorkflowResult(
                ldif_file=str(ldif_file),
                entry_count=len(entries),
                validation_status=validation.value.validation_status,
                workflow_status=c.DbtLdif.WORKFLOW_STATUS_COMPLETED,
            )
            if generate_models:
                model_result = self.generate_and_write_models(entries)
                if model_result.failure:
                    return r[p.DbtLdif.WorkflowResult].fail(
                        model_result.error or "Model generation workflow failed",
                    )
                workflow_result.models_generated = model_result.value.models_generated
            if run_transformations:
                transform_payload: t.SequenceOf[t.JsonMapping] = [
                    {"dn": str(entry.get("dn", ""))} for entry in entries
                ]
                transform = self.client.transform_with_dbt(
                    transform_payload,
                    model_names,
                )
                if transform.failure:
                    return r[p.DbtLdif.WorkflowResult].fail(
                        transform.error or "Transformation workflow failed",
                    )
                workflow_result.transformation_status = transform.value.status
            FlextDbtLdifServiceMixin.logger.info("Completed DBT LDIF workflow")
            return r[p.DbtLdif.WorkflowResult].ok(workflow_result)

        def run_data_quality_assessment(
            self,
            ldif_file: Path | str,
        ) -> p.Result[p.DbtLdif.ParseValidationResult]:
            """Run quality assessment focused workflow."""
            return self.parse_and_validate_ldif(ldif_file)
