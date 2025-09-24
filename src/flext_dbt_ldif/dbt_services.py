"""DBT services functionality for flext-dbt-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path

from flext_core import FlextLogger, FlextResult, FlextTypes
from flext_dbt_ldif.dbt_client import FlextDbtLdifClient
from flext_dbt_ldif.dbt_config import FlextDbtLdifConfig
from flext_dbt_ldif.dbt_models import FlextDbtLdifUnifiedService
from flext_ldif import FlextLdifModels

logger = FlextLogger(__name__)
# Quality assessment thresholds
HIGH_QUALITY_THRESHOLD = 90.0
MEDIUM_QUALITY_THRESHOLD = 70.0
MAX_OBJECT_CLASSES_THRESHOLD = 20


class FlextDbtLdifService:
    """Unified LDIF-to-DBT service with complete workflow orchestration.

    Provides complete workflow management combining parsing, validation,
    model generation, transformation execution, and batch processing.
    Follows single class per module pattern with nested helpers.
    """

    def __init__(
        self,
        config: FlextDbtLdifConfig | None = None,
        project_dir: Path | None = None,
    ) -> None:
        """Initialize DBT LDIF service.

        Args:
            config: Configuration for LDIF and DBT operations
            project_dir: DBT project directory

        """
        self.config: dict[str, object] = config or FlextDbtLdifConfig()
        self.project_dir = project_dir or Path.cwd()

        # Initialize components with maximum composition
        self.client = FlextDbtLdifClient(self.config)
        self.model_generator = FlextDbtLdifUnifiedService(
            name="default_generator",
            config=self.config,
            project_dir=self.project_dir,
        )

        logger.info("Initialized DBT LDIF service: %s", self.project_dir)

    def run_complete_workflow(
        self,
        ldif_file: Path | str,
        *,
        generate_models: bool = True,
        run_transformations: bool = True,
        model_names: FlextTypes.Core.StringList | None = None,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Run complete LDIF-to-DBT workflow.

        Args:
            ldif_file: Path to LDIF file
            generate_models: Whether to generate DBT models
            run_transformations: Whether to run DBT transformations
            model_names: Specific models to run (None = all)

        Returns:
            FlextResult containing complete workflow results

        """
        logger.info(
            "Starting complete LDIF-to-DBT workflow: file=%s, generate=%s, transform=%s",
            ldif_file,
            generate_models,
            run_transformations,
        )

        workflow_results: FlextTypes.Core.Dict = {
            "ldif_file": str(ldif_file),
            "workflow_status": "started",
            "steps_completed": [],
        }

        try:
            # Step 1: Parse and validate LDIF
            parse_result: FlextResult[object] = self.parse_and_validate_ldif(ldif_file)
            if not parse_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    f"LDIF parsing/validation failed: {parse_result.error}",
                )

            parse_data = parse_result.value or {}
            entries: list[object] = parse_data.get("entries", [])
            workflow_results["parse_validation"] = parse_data
            if isinstance(workflow_results["steps_completed"], list):
                workflow_results["steps_completed"].append("parse_validation")

            # Step 2: Generate models if requested
            if generate_models:
                model_result = self.generate_and_write_models(
                    entries if isinstance(entries, list) else [],
                )
                if not model_result.success:
                    return FlextResult[FlextTypes.Core.Dict].fail(
                        f"Model generation failed: {model_result.error}",
                    )

                workflow_results["model_generation"] = model_result.value or {}
                if isinstance(workflow_results["steps_completed"], list):
                    workflow_results["steps_completed"].append("model_generation")

            # Step 3: Run transformations if requested
            if run_transformations:
                transform_result = self.client.transform_with_dbt(
                    entries if isinstance(entries, list) else [],
                    model_names,
                )
                if not transform_result.success:
                    return FlextResult[FlextTypes.Core.Dict].fail(
                        f"DBT transformation failed: {transform_result.error}",
                    )

                workflow_results["transformations"] = transform_result.value or {}
                if isinstance(workflow_results["steps_completed"], list):
                    workflow_results["steps_completed"].append("transformations")

            workflow_results["workflow_status"] = "completed"
            logger.info("Complete LDIF-to-DBT workflow finished successfully")
            return FlextResult[FlextTypes.Core.Dict].ok(workflow_results)

        except Exception as e:
            logger.exception("Unexpected error in complete workflow")
            workflow_results["workflow_status"] = "failed"
            workflow_results["error"] = str(e)
            return FlextResult[FlextTypes.Core.Dict].fail(
                f"Complete workflow error: {e}",
            )

    def parse_and_validate_ldif(
        self,
        ldif_file: Path | str,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Parse and validate LDIF file.

        Args:
            ldif_file: Path to LDIF file

        Returns:
            FlextResult containing parsing and validation results

        """
        logger.info("Parsing and validating LDIF file: %s", ldif_file)

        try:
            # Parse LDIF file
            parse_result: FlextResult[object] = self.client.parse_ldif_file(ldif_file)
            if not parse_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    f"Parse failed: {parse_result.error}",
                )

            entries = parse_result.value or []

            # Validate entries
            validation_result: FlextResult[object] = self.client.validate_ldif_data(
                entries
            )
            if not validation_result.success:
                return validation_result

            return FlextResult[FlextTypes.Core.Dict].ok(
                {
                    "entries": entries,
                    "entry_count": len(entries),
                    "validation_metrics": validation_result.value,
                    "status": "validated",
                },
            )

        except Exception as e:
            logger.exception("Error in parse and validate")
            return FlextResult[FlextTypes.Core.Dict].fail(
                f"Parse/validation error: {e}",
            )

    def generate_and_write_models(
        self,
        entries: list[FlextLdifModels.Entry],
        *,
        overwrite: bool = False,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Generate and write DBT models for LDIF entries.

        Args:
            entries: List of LDIF entries
            overwrite: Whether to overwrite existing models

        Returns:
            FlextResult containing model generation results

        """
        logger.info("Generating and writing DBT models for %d entries", len(entries))

        try:
            # Generate staging models
            staging_result: FlextResult[object] = (
                self.model_generator.generate_staging_models(entries)
            )
            if not staging_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    f"Staging generation failed: {staging_result.error}",
                )

            staging_models = staging_result.value or []

            # Generate analytics models
            analytics_result = self.model_generator.generate_analytics_models(
                staging_models,
            )
            if not analytics_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    f"Analytics generation failed: {analytics_result.error}",
                )

            analytics_models = analytics_result.value or []

            # Combine all models
            all_models = staging_models + analytics_models

            # Write models to disk
            write_result = self.model_generator.write_models_to_disk(
                all_models,
                overwrite=overwrite,
            )
            if not write_result.success:
                return write_result

            write_info = write_result.value or {}

            return FlextResult[FlextTypes.Core.Dict].ok(
                {
                    "staging_models": len(staging_models),
                    "analytics_models": len(analytics_models),
                    "total_models": len(all_models),
                    "files_written": write_info.get("written_files", []),
                    "output_dir": write_info.get("output_dir"),
                    "status": "generated",
                },
            )

        except Exception as e:
            logger.exception("Error in generate and write models")
            return FlextResult[FlextTypes.Core.Dict].fail(
                f"Model generation error: {e}",
            )

    def run_data_quality_assessment(
        self,
        ldif_file: Path | str,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Run comprehensive data quality assessment on LDIF file.

        Args:
            ldif_file: Path to LDIF file

        Returns:
            FlextResult containing comprehensive quality assessment

        """
        logger.info("Running data quality assessment: %s", ldif_file)

        try:
            # Parse LDIF
            parse_result: FlextResult[object] = self.client.parse_ldif_file(ldif_file)
            if not parse_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    f"Parse failed: {parse_result.error}",
                )

            entries = parse_result.value or []

            # Run validation
            validation_result: FlextResult[object] = self.client.validate_ldif_data(
                entries
            )
            validation_metrics = (
                validation_result.value if validation_result.success else {}
            ) or {}

            # Analyze schema using model generator
            schema_result: FlextResult[object] = (
                self.model_generator.analyze_ldif_schema(entries)
            )
            schema_info = (schema_result.value if schema_result.success else {}) or {}

            # Compile comprehensive assessment
            quality_assessment = {
                "file_info": {
                    "path": str(ldif_file),
                    "total_entries": len(entries),
                },
                "validation_metrics": validation_metrics,
                "schema_analysis": schema_info,
                "quality_summary": {
                    "overall_score": validation_metrics.get("quality_score", 0.0)
                    if validation_metrics
                    else 0.0,
                    "threshold_met": self._safe_float_conversion(
                        validation_metrics.get("quality_score", 0.0)
                        if validation_metrics
                        else 0.0,
                    )
                    >= self.config.min_quality_threshold,
                    "risk_level": self._assess_risk_level(
                        self._safe_float_conversion(
                            validation_metrics.get("quality_score", 0.0)
                            if validation_metrics
                            else 0.0,
                        ),
                    ),
                },
                "recommendations": self._generate_quality_recommendations(
                    validation_metrics or {},
                    schema_info or {},
                ),
                "status": "completed",
            }

            logger.info("Data quality assessment completed")
            return FlextResult[FlextTypes.Core.Dict].ok(dict(quality_assessment))

        except Exception as e:
            logger.exception("Error in data quality assessment")
            return FlextResult[FlextTypes.Core.Dict].fail(
                f"Quality assessment error: {e}",
            )

    def generate_model_documentation(
        self,
        entries: list[FlextLdifModels.Entry],
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Generate documentation for DBT models based on LDIF analysis.

        Args:
            entries: List of LDIF entries

        Returns:
            FlextResult containing model documentation

        """
        logger.info("Generating model documentation for %d entries", len(entries))

        try:
            # Analyze schema
            schema_result: FlextResult[object] = (
                self.model_generator.analyze_ldif_schema(entries)
            )
            if not schema_result.success:
                return schema_result

            schema_info = schema_result.value or {}

            # Generate models for analysis
            staging_result: FlextResult[object] = (
                self.model_generator.generate_staging_models(entries)
            )
            if not staging_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    f"Staging model generation failed: {staging_result.error}",
                )

            staging_models = staging_result.value or []

            # Create documentation structure
            documentation = {
                "project_info": {
                    "name": "LDIF Data Transformation",
                    "description": "DBT models for LDIF data analytics and transformations",
                    "version": "1.0.0",
                },
                "schema_analysis": schema_info,
                "model_catalog": {
                    "staging_models": [
                        {
                            "name": model.name,
                            "description": model.description,
                            "columns": len(model.columns),
                            "tests": 0,  # Tests are embedded in columns
                        }
                        for model in staging_models
                    ],
                },
                "data_lineage": self._generate_lineage_info(staging_models),
                "quality_metrics": {
                    "threshold": self.config.min_quality_threshold,
                    "required_attributes": self.config.required_attributes,
                },
                "generated_at": "{{ current_timestamp }}",
            }

            logger.info("Model documentation generated")
            return FlextResult[FlextTypes.Core.Dict].ok(documentation)

        except Exception as e:
            logger.exception("Error generating model documentation")
            return FlextResult[FlextTypes.Core.Dict].fail(
                f"Documentation generation error: {e}",
            )

    def _assess_risk_level(self, quality_score: float) -> str:
        """Assess risk level based on quality score."""
        if quality_score >= HIGH_QUALITY_THRESHOLD:
            return "low"
        if quality_score >= MEDIUM_QUALITY_THRESHOLD:
            return "medium"
        return "high"

    def _generate_quality_recommendations(
        self,
        validation_metrics: FlextTypes.Core.Dict,
        schema_info: FlextTypes.Core.Dict,
    ) -> FlextTypes.Core.StringList:
        """Generate quality improvement recommendations."""
        recommendations: list[str] = []

        quality_score_obj = validation_metrics.get("quality_score", 0.0) or 0.0
        quality_score = (
            float(quality_score_obj)
            if isinstance(quality_score_obj, (int, float, str))
            else 0.0
        )

        if quality_score < self.config.min_quality_threshold:
            recommendations.append(
                "Quality score below threshold - review data validation rules",
            )

        invalid_dns_obj = validation_metrics.get("invalid_dns", 0) or 0
        invalid_dns_count = (
            int(invalid_dns_obj)
            if isinstance(invalid_dns_obj, (int, float, str))
            else 0
        )
        if invalid_dns_count > 0:
            recommendations.append(
                "Invalid DN entries found - check DN format and syntax",
            )

        object_classes_obj: list[object] = schema_info.get("object_classes", [])
        object_classes = (
            object_classes_obj if isinstance(object_classes_obj, list) else []
        )
        if len(object_classes) > MAX_OBJECT_CLASSES_THRESHOLD:
            recommendations.append(
                "High number of object classes - consider data normalization",
            )

        return recommendations

    def _safe_float_conversion(self, value: object) -> float:
        """Safely convert object to float."""
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                return 0.0
        return 0.0

    def _generate_lineage_info(
        self,
        models: list[FlextDbtLdifUnifiedService],
    ) -> FlextTypes.Core.Dict:
        """Generate data lineage information for models."""
        return {
            "source": "ldif_files",
            "staging_layer": [
                model.name for model in models if model.name.startswith("stg_")
            ],
            "analytics_layer": [
                model.name for model in models if model.name.startswith("analytics_")
            ],
            "dependencies": {model.name: ["ldif_source"] for model in models},
        }

    class _WorkflowManager:
        """Nested workflow manager for batch LDIF processing.

        Handles multiple LDIF files and complex workflow orchestration
        as part of the unified service class.
        """

        def __init__(self, parent_service: FlextDbtLdifService) -> None:
            """Initialize workflow manager with parent service reference."""
            self.parent_service = parent_service
            self.config: dict[str, object] = parent_service.config
            self.project_dir = parent_service.project_dir

        def process_multiple_files(
            self,
            file_paths: list[Path],
            *,
            parallel: bool = False,
        ) -> FlextResult[FlextTypes.Core.Dict]:
            """Process multiple LDIF files in sequence or parallel."""
            logger.info(
                "Processing %d files with parallel=%s",
                len(file_paths),
                parallel,
            )

            batch_results: FlextTypes.Core.Dict = {
                "total": len(file_paths),
                "successful": 0,
                "failed": 0,
                "results": [],
            }

            for file_path in file_paths:
                try:
                    # Use parent service for individual file processing
                    result = self.parent_service.run_complete_workflow(
                        ldif_file=file_path,
                    )

                    if result.success:
                        current_success = batch_results.get("successful", 0)
                        if isinstance(current_success, int):
                            batch_results["successful"] = current_success + 1
                        else:
                            batch_results["successful"] = 1
                    else:
                        current_failed = batch_results.get("failed", 0)
                        if isinstance(current_failed, int):
                            batch_results["failed"] = current_failed + 1
                        else:
                            batch_results["failed"] = 1

                    if isinstance(batch_results["results"], list):
                        batch_results["results"].append(
                            {
                                "file": str(file_path),
                                "status": "success" if result.success else "failed",
                                "data": result.value if result.success else None,
                                "error": str(result.error)
                                if not result.success
                                else None,
                            },
                        )

                except Exception as e:
                    logger.exception("Error processing file: %s", file_path)
                    current_failed = batch_results.get("failed", 0)
                    if isinstance(current_failed, int):
                        batch_results["failed"] = current_failed + 1
                    else:
                        batch_results["failed"] = 1
                    if isinstance(batch_results["results"], list):
                        batch_results["results"].append(
                            {
                                "file": str(file_path),
                                "status": "failed",
                                "error": str(e),
                            },
                        )

            return FlextResult[FlextTypes.Core.Dict].ok(batch_results)

    def get_workflow_manager(self: object) -> _WorkflowManager:
        """Get workflow manager for batch processing operations."""
        return self._WorkflowManager(self)


__all__: FlextTypes.Core.StringList = [
    "FlextDbtLdifService",
]
