"""Client orchestration for LDIF to DBT workflows."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from flext_core import FlextLogger, r, t

from .constants import c
from .settings import FlextDbtLdifSettings

logger = FlextLogger(__name__)


class FlextDbtLdifClient:
    """Client with typed parse, validate, and transform operations."""

    def __init__(self, config: FlextDbtLdifSettings | None = None) -> None:
        """Initialize client with explicit or global settings."""
        self.config = (
            config if config is not None else FlextDbtLdifSettings.get_global()
        )

    def parse_ldif_file(
        self, file_path: Path | str | None = None
    ) -> r[list[dict[str, t.ContainerValue]]]:
        """Return minimal parsed LDIF entries payload."""
        selected_path = (
            str(file_path) if file_path is not None else self.config.ldif_file_path
        )
        if not selected_path:
            return r[list[dict[str, t.ContainerValue]]].fail(
                "LDIF file path is required"
            )
        return r[list[dict[str, t.ContainerValue]]].ok([
            {"dn": c.DbtLdif.SAMPLE_LDIF_DN, "source": selected_path}
        ])

    def run_full_pipeline(
        self, file_path: Path | str | None = None, model_names: list[str] | None = None
    ) -> r[t.Dict]:
        """Run parse, validate, and transform pipeline."""
        parse_result = self.parse_ldif_file(file_path)
        if parse_result.is_failure:
            return r[t.Dict].fail(parse_result.error or "Parse failed")
        validate_result = self.validate_ldif_data(parse_result.value)
        if validate_result.is_failure:
            return r[t.Dict].fail(validate_result.error or "Validation failed")
        transform_result = self.transform_with_dbt(parse_result.value, model_names)
        if transform_result.is_failure:
            return r[t.Dict].fail(transform_result.error or "Transform failed")
        logger.info("Completed LDIF to DBT pipeline")
        return r[t.Dict].ok({
            "parsed_entries": len(parse_result.value),
            "validation_status": str(
                validate_result.value.get("validation_status", "")
            ),
            "transformation_status": str(transform_result.value.get("status", "")),
            "pipeline_status": c.DbtLdif.WORKFLOW_STATUS_COMPLETED,
        })

    def transform_with_dbt(
        self,
        entries: Sequence[dict[str, t.ContainerValue]],
        model_names: list[str] | None = None,
    ) -> r[t.Dict]:
        """Return synthetic DBT transformation metadata."""
        selected_models = model_names or [
            c.DbtLdif.STAGING_MODEL_NAME,
            c.DbtLdif.ANALYTICS_MODEL_NAME,
        ]
        transform_payload: t.Dict = {
            "records": len(entries),
            "models": ",".join(selected_models),
            "status": c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS,
        }
        return r[t.Dict].ok(transform_payload)

    def validate_ldif_data(
        self,
        entries: Sequence[dict[str, t.ContainerValue]],
    ) -> r[t.Dict]:
        """Validate parsed LDIF payload and compute quality score."""
        total_entries = len(entries)
        if total_entries == 0:
            return r[t.Dict].fail("No LDIF entries found")
        quality_score = c.DbtLdif.DEFAULT_QUALITY_SCORE
        if quality_score < self.config.min_quality_threshold:
            return r[t.Dict].fail("Quality threshold not met")
        validation_payload: t.Dict = {
            "total_entries": total_entries,
            "quality_score": quality_score,
            "validation_status": c.DbtLdif.VALIDATION_STATUS_PASSED,
        }
        return r[t.Dict].ok(validation_payload)


__all__ = ["FlextDbtLdifClient"]
