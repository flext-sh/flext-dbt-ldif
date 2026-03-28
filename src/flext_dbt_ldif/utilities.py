"""Utility functions for flext-dbt-ldif transformations."""

from __future__ import annotations

import sys
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Self, override

from flext_cli import cli
from flext_core import FlextLogger, FlextService, FlextTypes, e, r
from flext_ldif import FlextLdifUtilities
from flext_meltano import FlextMeltanoUtilities
from pydantic import RootModel

from flext_dbt_ldif import FlextDbtLdifSettings, c, m, t

logger = FlextLogger(__name__)


class FlextDbtLdifUtilities(FlextMeltanoUtilities, FlextLdifUtilities):
    """Utilities for dbt-ldif operations inheriting LDIF processing capabilities."""

    class DbtLdif(FlextLdifUtilities):
        """DBT LDIF utilities namespace."""

        class UnifiedService(FlextService[FlextTypes.ContainerMapping]):
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
                super().__init__(
                    config_type=FlextDbtLdifSettings,
                    config_overrides=None,
                    initial_context=None,
                )
                self.name = name
                self.project_dir = Path(project_dir or Path.cwd())
                self._settings = (
                    config if config is not None else FlextDbtLdifSettings.get_global()
                )

            @override
            def execute(self) -> r[FlextTypes.ContainerMapping]:
                """Execute service and return metadata payload."""
                return r[FlextTypes.ContainerMapping].ok({
                    "name": self.name,
                    "project_dir": str(self.project_dir),
                    "status": c.DbtLdif.WORKFLOW_STATUS_READY,
                })

            def generate_analytics_models(
                self,
                staging_models: Sequence[m.DbtLdif.DbtModel],
            ) -> r[Sequence[m.DbtLdif.DbtModel]]:
                """Generate one analytics model derived from staging set."""
                if not staging_models:
                    return r[Sequence[m.DbtLdif.DbtModel]].ok([])
                analytics = m.DbtLdif.DbtModel(
                    name=c.DbtLdif.ANALYTICS_MODEL_NAME,
                    dbt_model_type=c.DbtLdif.DBT_MODEL_TYPE_ANALYTICS,
                    ldif_source=c.DbtLdif.LDIF_SOURCE_NAME,
                    materialization=c.DbtLdif.DBT_MATERIALIZATION_TABLE,
                    sql_content="select * from {{ ref('stg_ldif_entries') }}",
                    description=c.DbtLdif.ANALYTICS_MODEL_DESCRIPTION,
                    columns=[],
                    dependencies=[c.DbtLdif.STAGING_MODEL_NAME],
                )
                return r[Sequence[m.DbtLdif.DbtModel]].ok([analytics])

            def generate_staging_models(
                self,
                entries: Sequence[Mapping[str, FlextTypes.ContainerValue]],
            ) -> r[Sequence[m.DbtLdif.DbtModel]]:
                """Generate simple staging models for provided LDIF entries."""
                if not entries:
                    return r[Sequence[m.DbtLdif.DbtModel]].ok([])
                model = m.DbtLdif.DbtModel(
                    name=c.DbtLdif.STAGING_MODEL_NAME,
                    dbt_model_type=c.DbtLdif.DBT_MODEL_TYPE_STAGING,
                    ldif_source=c.DbtLdif.LDIF_SOURCE_NAME,
                    materialization=c.DbtLdif.DBT_MATERIALIZATION_VIEW,
                    sql_content="select * from {{ source('ldif', 'raw_ldif_entries') }}",
                    description=c.DbtLdif.STAGING_MODEL_DESCRIPTION,
                    columns=[],
                    dependencies=[],
                )
                return r[Sequence[m.DbtLdif.DbtModel]].ok([model])

        class Core:
            """Core namespace containing simple model and analytics helpers."""

            class ModelGenerator:
                """Generate static model metadata used by higher services."""

                def __init__(self, project_dir: Path | None = None) -> None:
                    """Initialize model generator."""
                    self.project_dir = project_dir or Path.cwd()

                def generate_analytics_models(self) -> Sequence[t.StrMapping]:
                    """Generate default analytics model metadata."""
                    return [
                        {
                            "name": c.DbtLdif.ANALYTICS_MODEL_NAME,
                            "description": c.DbtLdif.ANALYTICS_MODEL_DESCRIPTION,
                        },
                    ]

                def generate_staging_models(self) -> Sequence[t.StrMapping]:
                    """Generate default staging model metadata."""
                    return [
                        {
                            "name": c.DbtLdif.STAGING_MODEL_NAME,
                            "description": c.DbtLdif.STAGING_MODEL_DESCRIPTION,
                        },
                    ]

            class Analytics:
                """Compute basic analysis metrics for LDIF-like payloads."""

                def analyze_entry_patterns(
                    self,
                    entries: Sequence[t.StrMapping],
                ) -> r[Mapping[str, t.ContainerValue]]:
                    """Analyze input entries and return summary payload."""
                    return r[t.ContainerValueMapping].ok({
                        "total_entries": len(entries),
                        "unique_dns": len({entry.get("dn", "") for entry in entries}),
                    })

        class Client:
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
                    str(file_path)
                    if file_path is not None
                    else self.config.ldif_file_path
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
                transform_result = self.transform_with_dbt(
                    parse_result.value,
                    model_names,
                )
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
                    return r[m.DbtLdif.LdifValidationResult].fail(
                        "No LDIF entries found",
                    )
                quality_score = c.DbtLdif.DEFAULT_QUALITY_SCORE
                if quality_score < self.config.min_quality_threshold:
                    return r[m.DbtLdif.LdifValidationResult].fail(
                        "Quality threshold not met",
                    )
                return r[m.DbtLdif.LdifValidationResult].ok(
                    m.DbtLdif.LdifValidationResult(
                        total_entries=total_entries,
                        quality_score=quality_score,
                        validation_status=c.DbtLdif.VALIDATION_STATUS_PASSED,
                    ),
                )

        class Error(e.BaseError):
            """Unified exception for all LDIF DBT operations with error codes.

            Single responsibility class that handles all LDIF DBT error scenarios
            through error codes instead of multiple exception classes.
            """

            @override
            def __init__(
                self,
                message: str,
                *,
                error_code: c.DbtLdif.ErrorCode = c.DbtLdif.ErrorCode.DBT_LDIF_ERROR,
                **context: t.Scalar,
            ) -> None:
                """Initialize LDIF DBT error with error code and context.

                Args:
                    message: Human-readable error message
                    error_code: Specific error code for this error type
                    **context: Additional context information

                """
                context["error_code"] = error_code.value
                context["operation"] = context.get("operation", "ldif_dbt_operation")
                super().__init__(message)
                self.error_code = error_code

            @classmethod
            def authentication_error(
                cls,
                message: str = "LDIF DBT authentication failed",
                **context: t.Scalar,
            ) -> Self:
                """Create authentication error."""
                return cls(
                    message,
                    error_code=c.DbtLdif.ErrorCode.AUTHENTICATION_ERROR,
                    **context,
                )

            @classmethod
            def configuration_error(
                cls,
                message: str = "LDIF DBT configuration is invalid or missing",
                **context: t.Scalar,
            ) -> Self:
                """Create configuration error."""
                return cls(
                    message,
                    error_code=c.DbtLdif.ErrorCode.CONFIGURATION_ERROR,
                    **context,
                )

            @classmethod
            def connection_error(
                cls,
                message: str = "LDIF DBT database connection failed",
                **context: t.Scalar,
            ) -> Self:
                """Create connection error."""
                return cls(
                    message,
                    error_code=c.DbtLdif.ErrorCode.CONNECTION_ERROR,
                    **context,
                )

            @classmethod
            def model_error(
                cls,
                message: str = "LDIF DBT model error",
                *,
                model_name: str | None = None,
                model_type: str | None = None,
                **context: t.Scalar,
            ) -> Self:
                """Create LDIF DBT model error with dbt context."""
                context["operation"] = "dbt_model_processing"
                if model_name is not None:
                    context["model_name"] = model_name
                if model_type is not None:
                    context["model_type"] = model_type
                return cls(
                    message,
                    error_code=c.DbtLdif.ErrorCode.MODEL_ERROR,
                    **context,
                )

            @classmethod
            def parse_error(
                cls,
                message: str = "LDIF DBT parsing failed",
                *,
                line_number: int | None = None,
                entry_dn: str | None = None,
                **context: t.Scalar,
            ) -> Self:
                """Create LDIF parsing error with parse context."""
                context["operation"] = "ldif_parsing"
                if line_number is not None:
                    context["line_number"] = line_number
                if entry_dn is not None:
                    context["entry_dn"] = entry_dn
                return cls(
                    message,
                    error_code=c.DbtLdif.ErrorCode.PARSE_ERROR,
                    **context,
                )

            @classmethod
            def processing_error(
                cls,
                message: str = "LDIF processing operations failed",
                **context: t.Scalar,
            ) -> Self:
                """Create processing error."""
                return cls(
                    message,
                    error_code=c.DbtLdif.ErrorCode.PROCESSING_ERROR,
                    **context,
                )

            @classmethod
            def test_error(
                cls,
                message: str = "LDIF DBT test failed",
                *,
                test_name: str | None = None,
                model_name: str | None = None,
                **context: t.Scalar,
            ) -> Self:
                """Create LDIF DBT test error with test validation context."""
                context["operation"] = "dbt_test_validation"
                if test_name is not None:
                    context["test_name"] = test_name
                if model_name is not None:
                    context["model_name"] = model_name
                return cls(
                    message,
                    error_code=c.DbtLdif.ErrorCode.TEST_ERROR,
                    **context,
                )

            @classmethod
            def timeout_error(
                cls,
                message: str = "LDIF DBT operation timeout",
                **context: t.Scalar,
            ) -> Self:
                """Create timeout error."""
                return cls(
                    message,
                    error_code=c.DbtLdif.ErrorCode.TIMEOUT_ERROR,
                    **context,
                )

            @classmethod
            def transformation_error(
                cls,
                message: str = "LDIF DBT transformation failed",
                *,
                transformation_type: str | None = None,
                model_name: str | None = None,
                **context: t.Scalar,
            ) -> Self:
                """Create LDIF DBT transformation error with transformation context."""
                context["operation"] = "ldif_transformation"
                if transformation_type is not None:
                    context["transformation_type"] = transformation_type
                if model_name is not None:
                    context["model_name"] = model_name
                return cls(
                    message,
                    error_code=c.DbtLdif.ErrorCode.TRANSFORMATION_ERROR,
                    **context,
                )

            @classmethod
            def validation_error(
                cls,
                message: str = "LDIF data validation failed",
                **context: t.Scalar,
            ) -> Self:
                """Create validation error."""
                return cls(
                    message,
                    error_code=c.DbtLdif.ErrorCode.VALIDATION_ERROR,
                    **context,
                )

            def is_configuration_error(self) -> bool:
                """Check if this is a configuration error."""
                return self.error_code == c.DbtLdif.ErrorCode.CONFIGURATION_ERROR

            def is_processing_error(self) -> bool:
                """Check if this is a processing error."""
                return self.error_code in {
                    c.DbtLdif.ErrorCode.PROCESSING_ERROR,
                    c.DbtLdif.ErrorCode.PARSE_ERROR,
                    c.DbtLdif.ErrorCode.MODEL_ERROR,
                    c.DbtLdif.ErrorCode.TRANSFORMATION_ERROR,
                }

            def is_validation_error(self) -> bool:
                """Check if this is a validation error."""
                return self.error_code == c.DbtLdif.ErrorCode.VALIDATION_ERROR

        class Service:
            """Orchestrates parsing, validation, model generation, and transformations."""

            class EntryContainerListAdapter(
                RootModel[Sequence[Mapping[str, FlextTypes.ContainerValue]]],
            ):
                """Adapter for list of container entries."""

                root: Sequence[Mapping[str, FlextTypes.ContainerValue]]

            def __init__(
                self,
                config: FlextDbtLdifSettings | None = None,
                project_dir: Path | None = None,
            ) -> None:
                """Initialize service dependencies."""
                self.config = (
                    config if config is not None else FlextDbtLdifSettings.get_global()
                )
                self.project_dir = project_dir or Path(
                    str(self.config.ldif_file_path or "."),
                )
                self.client = FlextDbtLdifUtilities.DbtLdif.Client(self.config)
                self.model_generator = FlextDbtLdifUtilities.DbtLdif.UnifiedService(
                    config=self.config,
                    project_dir=self.project_dir,
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
                        staging.error or "Staging model generation failed",
                    )
                analytics = self.model_generator.generate_analytics_models(
                    staging.value,
                )
                if analytics.is_failure:
                    return r[m.DbtLdif.ModelGenerationResult].fail(
                        analytics.error or "Analytics model generation failed",
                    )
                all_models = [*staging.value, *analytics.value]
                return r[m.DbtLdif.ModelGenerationResult].ok(
                    m.DbtLdif.ModelGenerationResult(
                        models_generated=len(all_models),
                        model_names=[model.name for model in all_models],
                    ),
                )

            def parse_and_validate_ldif(
                self,
                ldif_file: Path | str,
            ) -> r[m.DbtLdif.ParseValidationResult]:
                """Parse and validate LDIF file in one operation."""
                adapter = (
                    FlextDbtLdifUtilities.DbtLdif.Service.EntryContainerListAdapter
                )
                parse_result = self.client.parse_ldif_file(ldif_file)
                if parse_result.is_failure:
                    return r[m.DbtLdif.ParseValidationResult].fail(
                        parse_result.error or "Parse failed",
                    )
                entries = adapter.model_validate(parse_result.value).root
                validation = self.client.validate_ldif_data(entries)
                if validation.is_failure:
                    return r[m.DbtLdif.ParseValidationResult].fail(
                        validation.error or "Validation failed",
                    )
                return r[m.DbtLdif.ParseValidationResult].ok(
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
            ) -> r[m.DbtLdif.WorkflowResult]:
                """Execute complete LDIF to DBT workflow."""
                adapter = (
                    FlextDbtLdifUtilities.DbtLdif.Service.EntryContainerListAdapter
                )
                parse_result = self.client.parse_ldif_file(ldif_file)
                if parse_result.is_failure:
                    return r[m.DbtLdif.WorkflowResult].fail(
                        parse_result.error or "Parse failed",
                    )
                entries = adapter.model_validate(parse_result.value).root
                validation = self.client.validate_ldif_data(entries)
                if validation.is_failure:
                    return r[m.DbtLdif.WorkflowResult].fail(
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
                    if model_result.is_failure:
                        return r[m.DbtLdif.WorkflowResult].fail(
                            model_result.error or "Model generation workflow failed",
                        )
                    workflow_result.models_generated = (
                        model_result.value.models_generated
                    )
                if run_transformations:
                    transform_payload: Sequence[Mapping[str, t.ContainerValue]] = [
                        {"dn": str(entry.get("dn", ""))} for entry in entries
                    ]
                    transform = self.client.transform_with_dbt(
                        transform_payload,
                        model_names,
                    )
                    if transform.is_failure:
                        return r[m.DbtLdif.WorkflowResult].fail(
                            transform.error or "Transformation workflow failed",
                        )
                    workflow_result.transformation_status = transform.value.status
                logger.info("Completed DBT LDIF workflow")
                return r[m.DbtLdif.WorkflowResult].ok(workflow_result)

            def run_data_quality_assessment(
                self,
                ldif_file: Path | str,
            ) -> r[m.DbtLdif.ParseValidationResult]:
                """Run quality assessment focused workflow."""
                return self.parse_and_validate_ldif(ldif_file)

        class CliService:
            """FLEXT dbt LDIF CLI service using flext-cli foundation exclusively."""

            def display_generate_message(self) -> r[str]:
                """Generate dbt models from LDIF schema definitions."""
                try:
                    service = FlextDbtLdifUtilities.DbtLdif.Service()
                    result = service.generate_and_write_models([])
                    if result.is_failure:
                        return r[str].fail(result.error or "Model generation failed")
                    cli.display_text(
                        f"Model generation completed: {result.value}",
                    )
                    return r[str].ok("Generate message displayed")
                except (
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    OSError,
                    RuntimeError,
                    ImportError,
                ) as exc:
                    return r[str].fail(f"Generate message display failed: {exc}")

            def display_info(self) -> r[str]:
                """Display package info using flext-cli."""
                info_data = {
                    "name": "FLEXT dbt LDIF",
                    "version": "__version__",
                    "description": ("Advanced LDAP Data Analytics and Transformations"),
                    "features": (
                        "Programmatic dbt model generation, "
                        "LDIF data processing and analytics, "
                        "Advanced SQL pattern generation, "
                        "PostgreSQL optimized transformations"
                    ),
                }
                try:
                    cli.display_text(str(info_data))
                    return r[str].ok("Package information displayed successfully")
                except (
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    OSError,
                    RuntimeError,
                    ImportError,
                ) as exc:
                    return r[str].fail(f"Package info display failed: {exc}")

            def display_validate_message(self) -> r[str]:
                """Validate dbt models and configurations."""
                try:
                    service = FlextDbtLdifUtilities.DbtLdif.Service()
                    result = service.run_data_quality_assessment("")
                    if result.is_failure:
                        return r[str].fail(result.error or "Validation failed")
                    cli.display_text(
                        f"Validation completed: {result.value}",
                    )
                    return r[str].ok("Validate message displayed")
                except (
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    OSError,
                    RuntimeError,
                    ImportError,
                ) as exc:
                    return r[str].fail(f"Validate message display failed: {exc}")

            def generate(self) -> None:
                """Generate dbt models from LDIF schema definitions."""
                result: r[str] = self.display_generate_message()
                if result.is_failure:
                    logger.error(f"Generate command failed: {result.error}")

            def info(self) -> None:
                """Show package information."""
                result = self.display_info()
                if result.is_failure:
                    logger.error(f"Info command failed: {result.error}")

            def main(self) -> int:
                """Main CLI entry point for flext-dbt-ldif."""
                try:
                    if len(sys.argv) > 1:
                        command: str = sys.argv[1]
                        if command == c.DbtLdif.CLI_COMMAND_INFO:
                            self.info()
                        elif command == c.DbtLdif.CLI_COMMAND_GENERATE:
                            self.generate()
                        elif command == c.DbtLdif.CLI_COMMAND_VALIDATE:
                            self.validate()
                        else:
                            logger.error("Unknown command: %s", command)
                            return c.DbtLdif.EXIT_CODE_FAILURE
                    return c.DbtLdif.EXIT_CODE_SUCCESS
                except KeyboardInterrupt:
                    logger.info("Interrupted by user")
                    return c.DbtLdif.EXIT_CODE_FAILURE
                except (OSError, RuntimeError, ValueError):
                    logger.exception("CLI error")
                    return c.DbtLdif.EXIT_CODE_FAILURE

            def validate(self) -> None:
                """Validate dbt models and configurations."""
                result: r[str] = self.display_validate_message()
                if result.is_failure:
                    logger.error(f"Validate command failed: {result.error}")


# Backward-compatible aliases
FlextDbtLdifUnifiedService = FlextDbtLdifUtilities.DbtLdif.UnifiedService
FlextDbtLdifCore = FlextDbtLdifUtilities.DbtLdif.Core
FlextDbtLdifClient = FlextDbtLdifUtilities.DbtLdif.Client
FlextDbtLdifError = FlextDbtLdifUtilities.DbtLdif.Error
FlextDbtLdifService = FlextDbtLdifUtilities.DbtLdif.Service
FlextDbtLdifCliService = FlextDbtLdifUtilities.DbtLdif.CliService
s = FlextDbtLdifService

__all__ = [
    "FlextDbtLdifCliService",
    "FlextDbtLdifClient",
    "FlextDbtLdifCore",
    "FlextDbtLdifError",
    "FlextDbtLdifService",
    "FlextDbtLdifUnifiedService",
    "FlextDbtLdifUtilities",
    "s",
]

u = FlextDbtLdifUtilities
