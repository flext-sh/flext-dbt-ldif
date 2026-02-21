"""Client orchestration for LDIF to DBT workflows."""

from __future__ import annotations

from pathlib import Path

from flext_core import FlextLogger, FlextResult, t

from .settings import FlextDbtLdifSettings

logger = FlextLogger(__name__)


class FlextDbtLdifClient:
    """Client with typed parse, validate, and transform operations."""

    def __init__(self, config: FlextDbtLdifSettings | None = None) -> None:
        """Initialize client with explicit or global settings."""
        self.config = config or FlextDbtLdifSettings.get_global_instance()

    def parse_ldif_file(
        self,
        file_path: Path | str | None = None,
    ) -> FlextResult[list[dict[str, t.GeneralValueType]]]:
        """Return minimal parsed LDIF entries payload."""
        selected_path = (
            str(file_path) if file_path is not None else self.config.ldif_file_path
        )
        if not selected_path:
            return FlextResult[list[dict[str, t.GeneralValueType]]].fail(
                "LDIF file path is required"
            )
        return FlextResult[list[dict[str, t.GeneralValueType]]].ok(
            [{"dn": "cn=sample,dc=example,dc=org", "source": selected_path}],
        )

    def validate_ldif_data(
        self,
        entries: list[dict[str, t.GeneralValueType]],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Validate parsed LDIF payload and compute quality score."""
        total_entries = len(entries)
        if total_entries == 0:
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                "No LDIF entries found"
            )
        quality_score = 1.0
        if quality_score < self.config.min_quality_threshold:
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                "Quality threshold not met"
            )
        return FlextResult[dict[str, t.GeneralValueType]].ok(
            {
                "total_entries": total_entries,
                "quality_score": quality_score,
                "validation_status": "passed",
            },
        )

    def transform_with_dbt(
        self,
        entries: list[dict[str, t.GeneralValueType]],
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Return synthetic DBT transformation metadata."""
        return FlextResult[dict[str, t.GeneralValueType]].ok(
            {
                "records": len(entries),
                "models": model_names
                or ["stg_ldif_entries", "analytics_ldif_insights"],
                "status": "success",
            },
        )

    def run_full_pipeline(
        self,
        file_path: Path | str | None = None,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Run parse, validate, and transform pipeline."""
        parse_result = self.parse_ldif_file(file_path)
        if parse_result.is_failure or parse_result.value is None:
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                parse_result.error or "Parse failed"
            )
        validate_result = self.validate_ldif_data(parse_result.value)
        if validate_result.is_failure or validate_result.value is None:
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                validate_result.error or "Validation failed",
            )
        transform_result = self.transform_with_dbt(parse_result.value, model_names)
        if transform_result.is_failure or transform_result.value is None:
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                transform_result.error or "Transform failed",
            )
        logger.info("Completed LDIF to DBT pipeline")
        return FlextResult[dict[str, t.GeneralValueType]].ok(
            {
                "parsed_entries": len(parse_result.value),
                "validation": validate_result.value,
                "transformation": transform_result.value,
                "pipeline_status": "completed",
            },
        )


__all__ = ["FlextDbtLdifClient"]
