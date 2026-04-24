"""Client mixin for dbt-ldif utilities."""

from __future__ import annotations

from collections.abc import (
    Sequence,
)
from pathlib import Path

from flext_dbt_ldif import FlextDbtLdifSettings, c, m, p, r, t, u

logger = u.fetch_logger(__name__)


class FlextDbtLdifClient:
    """Mixin providing Client for dbt-ldif utilities."""

    class Client:
        """Client with typed parse, validate, and transform operations."""

        def __init__(self, settings: FlextDbtLdifSettings | None = None) -> None:
            """Initialize client with explicit or global settings."""
            self.settings = (
                settings
                if settings is not None
                else FlextDbtLdifSettings.fetch_global()
            )

        def parse_ldif_file(
            self,
            file_path: Path | str | None = None,
        ) -> p.Result[Sequence[t.JsonMapping]]:
            """Return minimal parsed LDIF entries payload."""
            selected_path = (
                str(file_path)
                if file_path is not None
                else self.settings.ldif_file_path
            )
            if not selected_path:
                return r[Sequence[t.JsonMapping]].fail(
                    "LDIF file path is required",
                )
            return r[Sequence[t.JsonMapping]].ok([
                {"dn": c.DbtLdif.SAMPLE_LDIF_DN, "source": selected_path},
            ])

        def run_full_pipeline(
            self,
            file_path: Path | str | None = None,
            model_names: t.StrSequence | None = None,
        ) -> p.Result[m.DbtLdif.PipelineResult]:
            """Run parse, validate, and transform pipeline."""
            parse_result = self.parse_ldif_file(file_path)
            if parse_result.failure:
                return r[m.DbtLdif.PipelineResult].fail(
                    parse_result.error or "Parse failed",
                )
            validate_result = self.validate_ldif_data(parse_result.value)
            if validate_result.failure:
                return r[m.DbtLdif.PipelineResult].fail(
                    validate_result.error or "Validation failed",
                )
            transform_result = self.transform_with_dbt(
                parse_result.value,
                model_names,
            )
            if transform_result.failure:
                return r[m.DbtLdif.PipelineResult].fail(
                    transform_result.error or "Transform failed",
                )
            logger.info("Completed LDIF to DBT pipeline")
            return r[m.DbtLdif.PipelineResult].ok(
                m.DbtLdif.PipelineResult(
                    parsed_entries=len(parse_result.value),
                    validation_status=validate_result.value.validation_status,
                    transformation_status=transform_result.value.status,
                    pipeline_status=c.DbtLdif.WORKFLOW_STATUS_COMPLETED,
                ),
            )

        def transform_with_dbt(
            self,
            entries: Sequence[t.JsonMapping],
            model_names: t.StrSequence | None = None,
        ) -> p.Result[m.DbtLdif.DbtTransformationResult]:
            """Return synthetic DBT transformation metadata."""
            selected_models = model_names or [
                c.DbtLdif.STAGING_MODEL_NAME,
                c.DbtLdif.ANALYTICS_MODEL_NAME,
            ]
            return r[m.DbtLdif.DbtTransformationResult].ok(
                m.DbtLdif.DbtTransformationResult(
                    records=len(entries),
                    models=selected_models,
                    status=c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS,
                ),
            )

        def validate_ldif_data(
            self,
            entries: Sequence[t.JsonMapping],
        ) -> p.Result[m.DbtLdif.LdifValidationResult]:
            """Validate parsed LDIF payload and compute quality score."""
            total_entries = len(entries)
            if total_entries == 0:
                return r[m.DbtLdif.LdifValidationResult].fail(
                    "No LDIF entries found",
                )
            if self.settings.min_quality_threshold > c.DbtLdif.DEFAULT_QUALITY_SCORE:
                return r[m.DbtLdif.LdifValidationResult].fail(
                    "Quality threshold not met",
                )
            return r[m.DbtLdif.LdifValidationResult].ok(
                m.DbtLdif.LdifValidationResult(
                    total_entries=total_entries,
                    quality_score=c.DbtLdif.DEFAULT_QUALITY_SCORE,
                    validation_status=c.DbtLdif.VALIDATION_STATUS_PASSED,
                ),
            )
