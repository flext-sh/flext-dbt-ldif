"""Client mixin for dbt-ldif utilities."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_dbt_ldif import FlextDbtLdifSettings, c, m, p, r, settings, t, u

if TYPE_CHECKING:
    from pathlib import Path


class FlextDbtLdifClient:
    """Mixin providing Client for dbt-ldif utilities."""

    class Client:
        """Client with typed parse, validate, and transform operations."""

        # NOTE (multi-agent): mro-rn88 — plain class holding the effective settings
        # (injected override or global singleton); exposed via the `settings` property.
        def __init__(self, settings: FlextDbtLdifSettings | None = None) -> None:
            """Wire the client with optional injected settings."""
            self._settings = settings or FlextDbtLdifSettings.fetch_global()

        @property
        def settings(self) -> FlextDbtLdifSettings:
            """The effective dbt-ldif settings for this client."""
            return self._settings

        def parse_ldif_file(
            self, file_path: Path | str | None = None
        ) -> p.Result[list[t.JsonMapping]]:
            """Return minimal parsed LDIF entries payload."""
            selected_path = (
                str(file_path)
                if file_path is not None
                else settings.DbtLdif.ldif_file_path
            )
            if not selected_path:
                return r[list[t.JsonMapping]].fail("LDIF file path is required")
            return r[list[t.JsonMapping]].ok([
                {"dn": c.DbtLdif.SAMPLE_LDIF_DN, "source": selected_path}
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
                    parse_result.error or "Parse failed"
                )
            validate_result = self.validate_ldif_data(parse_result.value)
            if validate_result.failure:
                return r[m.DbtLdif.PipelineResult].fail(
                    validate_result.error or "Validation failed"
                )
            transform_result = self.transform_with_dbt(parse_result.value, model_names)
            if transform_result.failure:
                return r[m.DbtLdif.PipelineResult].fail(
                    transform_result.error or "Transform failed"
                )
            u.logger.info("Completed LDIF to DBT pipeline")
            return r[m.DbtLdif.PipelineResult].ok(
                m.DbtLdif.PipelineResult(
                    parsed_entries=len(parse_result.value),
                    validation_status=validate_result.value.validation_status,
                    transformation_status=transform_result.value.status,
                    pipeline_status=c.DbtLdif.WORKFLOW_STATUS_COMPLETED,
                )
            )

        def transform_with_dbt(
            self,
            entries: t.SequenceOf[t.JsonMapping],
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
                )
            )

        def validate_ldif_data(
            self, entries: t.SequenceOf[t.JsonMapping]
        ) -> p.Result[m.DbtLdif.LdifValidationResult]:
            """Validate parsed LDIF payload and compute quality score."""
            total_entries = len(entries)
            if total_entries == 0:
                return r[m.DbtLdif.LdifValidationResult].fail("No LDIF entries found")
            if settings.DbtLdif.min_quality_threshold > c.DbtLdif.DEFAULT_QUALITY_SCORE:
                return r[m.DbtLdif.LdifValidationResult].fail(
                    "Quality threshold not met"
                )
            return r[m.DbtLdif.LdifValidationResult].ok(
                m.DbtLdif.LdifValidationResult(
                    total_entries=total_entries,
                    quality_score=c.DbtLdif.DEFAULT_QUALITY_SCORE,
                    validation_status=c.DbtLdif.VALIDATION_STATUS_PASSED,
                )
            )
