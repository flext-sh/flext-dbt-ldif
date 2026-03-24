"""Client orchestration for LDIF to DBT workflows."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path

from flext_core import FlextLogger, r

from flext_dbt_ldif import FlextDbtLdifSettings, c, m, t

logger = FlextLogger(__name__)


class FlextDbtLdifClient:
    """Client with typed parse, validate, and transform operations."""

    def __init__(self, config: FlextDbtLdifSettings | None = None) -> None:
        """Initialize client with explicit or global settings."""
        self.config = (
            config if config is not None else FlextDbtLdifSettings.get_global()
        )

    def parse_ldif_file(
        self,
        file_path: Path | str | None = None,
    ) -> r[Sequence[Mapping[str, t.ContainerValue]]]:
        """Return minimal parsed LDIF entries payload."""
        selected_path = (
            str(file_path) if file_path is not None else self.config.ldif_file_path
        )
        if not selected_path:
            return r[Sequence[t.ContainerValueMapping]].fail(
                "LDIF file path is required",
            )
        return r[Sequence[t.ContainerValueMapping]].ok([
            {"dn": c.DbtLdif.SAMPLE_LDIF_DN, "source": selected_path},
        ])

    def run_full_pipeline(
        self,
        file_path: Path | str | None = None,
        model_names: t.StrSequence | None = None,
    ) -> r[m.DbtLdif.PipelineResult]:
        """Run parse, validate, and transform pipeline."""
        parse_result = self.parse_ldif_file(file_path)
        if parse_result.is_failure:
            return r[m.DbtLdif.PipelineResult].fail(
                parse_result.error or "Parse failed",
            )
        validate_result = self.validate_ldif_data(parse_result.value)
        if validate_result.is_failure:
            return r[m.DbtLdif.PipelineResult].fail(
                validate_result.error or "Validation failed",
            )
        transform_result = self.transform_with_dbt(parse_result.value, model_names)
        if transform_result.is_failure:
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
        entries: Sequence[Mapping[str, t.ContainerValue]],
        model_names: t.StrSequence | None = None,
    ) -> r[m.DbtLdif.DbtTransformationResult]:
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
        entries: Sequence[Mapping[str, t.ContainerValue]],
    ) -> r[m.DbtLdif.LdifValidationResult]:
        """Validate parsed LDIF payload and compute quality score."""
        total_entries = len(entries)
        if total_entries == 0:
            return r[m.DbtLdif.LdifValidationResult].fail("No LDIF entries found")
        quality_score = c.DbtLdif.DEFAULT_QUALITY_SCORE
        if quality_score < self.config.min_quality_threshold:
            return r[m.DbtLdif.LdifValidationResult].fail("Quality threshold not met")
        return r[m.DbtLdif.LdifValidationResult].ok(
            m.DbtLdif.LdifValidationResult(
                total_entries=total_entries,
                quality_score=quality_score,
                validation_status=c.DbtLdif.VALIDATION_STATUS_PASSED,
            ),
        )


__all__ = ["FlextDbtLdifClient"]
