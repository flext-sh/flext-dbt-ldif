"""DBT services for LDIF workflow orchestration.

Provides high-level orchestration services for complete LDIF-to-DBT workflows.
Integrates all components: config, client, models, and exceptions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path

from flext_core import FlextResult, get_logger
from flext_ldif.models import FlextLdifEntry

from .dbt_client import FlextDbtLdifClient
from .dbt_config import FlextDbtLdifConfig
from .dbt_models import FlextDbtLdifModelGenerator, FlextLdifDbtModel

logger = get_logger(__name__)
# Quality assessment thresholds
HIGH_QUALITY_THRESHOLD = 90.0
MEDIUM_QUALITY_THRESHOLD = 70.0
MAX_OBJECT_CLASSES_THRESHOLD = 20


class FlextDbtLdifService:
    """High-level service for LDIF-to-DBT workflow orchestration.

    Provides complete workflow management combining parsing, validation,
    model generation, and transformation execution.
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
        self.config = config or FlextDbtLdifConfig()
        self.project_dir = project_dir or Path.cwd()

        # Initialize components with maximum composition
        self.client = FlextDbtLdifClient(self.config)
        self.model_generator = FlextDbtLdifModelGenerator(self.config, self.project_dir)

        logger.info("Initialized DBT LDIF service: %s", self.project_dir)

    def run_complete_workflow(
        self,
        ldif_file: Path | str,
        *,
        generate_models: bool = True,
        run_transformations: bool = True,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, object]]:
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

        workflow_results: dict[str, object] = {
            "ldif_file": str(ldif_file),
            "workflow_status": "started",
            "steps_completed": [],
        }

        try:
            # Step 1: Parse and validate LDIF
            parse_result = self.parse_and_validate_ldif(ldif_file)
            if not parse_result.success:
                return FlextResult[None].fail(
                    f"LDIF parsing/validation failed: {parse_result.error}",
                )

            parse_data = parse_result.data or {}
            entries = parse_data.get("entries", [])
            workflow_results["parse_validation"] = parse_data
            if isinstance(workflow_results["steps_completed"], list):
                workflow_results["steps_completed"].append("parse_validation")

            # Step 2: Generate models if requested
            if generate_models:
                model_result = self.generate_and_write_models(
                    entries if isinstance(entries, list) else [],
                )
                if not model_result.success:
                    return FlextResult[None].fail(
                        f"Model generation failed: {model_result.error}",
                    )

                workflow_results["model_generation"] = model_result.data or {}
                if isinstance(workflow_results["steps_completed"], list):
                    workflow_results["steps_completed"].append("model_generation")

            # Step 3: Run transformations if requested
            if run_transformations:
                transform_result = self.client.transform_with_dbt(
                    entries if isinstance(entries, list) else [],
                    model_names,
                )
                if not transform_result.success:
                    return FlextResult[None].fail(
                        f"DBT transformation failed: {transform_result.error}",
                    )

                workflow_results["transformations"] = transform_result.data or {}
                if isinstance(workflow_results["steps_completed"], list):
                    workflow_results["steps_completed"].append("transformations")

            workflow_results["workflow_status"] = "completed"
            logger.info("Complete LDIF-to-DBT workflow finished successfully")
            return FlextResult[None].ok(workflow_results)

        except Exception as e:
            logger.exception("Unexpected error in complete workflow")
            workflow_results["workflow_status"] = "failed"
            workflow_results["error"] = str(e)
            return FlextResult[None].fail(
                f"Complete workflow error: {e}",
            )

    def parse_and_validate_ldif(
        self,
        ldif_file: Path | str,
    ) -> FlextResult[dict[str, object]]:
        """Parse and validate LDIF file.

        Args:
            ldif_file: Path to LDIF file

        Returns:
            FlextResult containing parsing and validation results

        """
        logger.info("Parsing and validating LDIF file: %s", ldif_file)

        try:
            # Parse LDIF file
            parse_result = self.client.parse_ldif_file(ldif_file)
            if not parse_result.success:
                return FlextResult[None].fail(f"Parse failed: {parse_result.error}")

            entries = parse_result.data or []

            # Validate entries
            validation_result = self.client.validate_ldif_data(entries)
            if not validation_result.success:
                return validation_result

            return FlextResult[None].ok(
                {
                    "entries": entries,
                    "entry_count": len(entries),
                    "validation_metrics": validation_result.data,
                    "status": "validated",
                },
            )

        except Exception as e:
            logger.exception("Error in parse and validate")
            return FlextResult[None].fail(f"Parse/validation error: {e}")

    def generate_and_write_models(
        self,
        entries: list[FlextLdifEntry],
        *,
        overwrite: bool = False,
    ) -> FlextResult[dict[str, object]]:
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
            staging_result = self.model_generator.generate_staging_models(entries)
            if not staging_result.success:
                return FlextResult[None].fail(
                    f"Staging generation failed: {staging_result.error}",
                )

            staging_models = staging_result.data or []

            # Generate analytics models
            analytics_result = self.model_generator.generate_analytics_models(
                staging_models,
            )
            if not analytics_result.success:
                return FlextResult[None].fail(
                    f"Analytics generation failed: {analytics_result.error}",
                )

            analytics_models = analytics_result.data or []

            # Combine all models
            all_models = staging_models + analytics_models

            # Write models to disk
            write_result = self.model_generator.write_models_to_disk(
                all_models,
                overwrite=overwrite,
            )
            if not write_result.success:
                return write_result

            write_info = write_result.data or {}

            return FlextResult[None].ok(
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
            return FlextResult[None].fail(f"Model generation error: {e}")

    def run_data_quality_assessment(
        self,
        ldif_file: Path | str,
    ) -> FlextResult[dict[str, object]]:
        """Run comprehensive data quality assessment on LDIF file.

        Args:
            ldif_file: Path to LDIF file

        Returns:
            FlextResult containing comprehensive quality assessment

        """
        logger.info("Running data quality assessment: %s", ldif_file)

        try:
            # Parse LDIF
            parse_result = self.client.parse_ldif_file(ldif_file)
            if not parse_result.success:
                return FlextResult[None].fail(f"Parse failed: {parse_result.error}")

            entries = parse_result.data or []

            # Run validation
            validation_result = self.client.validate_ldif_data(entries)
            validation_metrics = (
                validation_result.data if validation_result.success else {}
            )
            if validation_metrics is None:
                validation_metrics = {}

            # Analyze schema using model generator
            schema_result = self.model_generator.analyze_ldif_schema(entries)
            schema_info = schema_result.data if schema_result.success else {}
            if schema_info is None:
                schema_info = {}

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
            return FlextResult[None].ok(dict(quality_assessment))

        except Exception as e:
            logger.exception("Error in data quality assessment")
            return FlextResult[None].fail(f"Quality assessment error: {e}")

    def generate_model_documentation(
        self,
        entries: list[FlextLdifEntry],
    ) -> FlextResult[dict[str, object]]:
        """Generate documentation for DBT models based on LDIF analysis.

        Args:
            entries: List of LDIF entries

        Returns:
            FlextResult containing model documentation

        """
        logger.info("Generating model documentation for %d entries", len(entries))

        try:
            # Analyze schema
            schema_result = self.model_generator.analyze_ldif_schema(entries)
            if not schema_result.success:
                return schema_result

            schema_info = schema_result.data or {}

            # Generate models for analysis
            staging_result = self.model_generator.generate_staging_models(entries)
            if not staging_result.success:
                return FlextResult[None].fail(
                    f"Staging model generation failed: {staging_result.error}",
                )

            staging_models = staging_result.data or []

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
                            "tests": len(model.tests),
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
            return FlextResult[None].ok(documentation)

        except Exception as e:
            logger.exception("Error generating model documentation")
            return FlextResult[None].fail(f"Documentation generation error: {e}")

    def _assess_risk_level(self, quality_score: float) -> str:
        """Assess risk level based on quality score."""
        if quality_score >= HIGH_QUALITY_THRESHOLD:
            return "low"
        if quality_score >= MEDIUM_QUALITY_THRESHOLD:
            return "medium"
        return "high"

    def _generate_quality_recommendations(
        self,
        validation_metrics: dict[str, object],
        schema_info: dict[str, object],
    ) -> list[str]:
        """Generate quality improvement recommendations."""
        recommendations = []

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

        object_classes_obj = schema_info.get("object_classes", [])
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
        models: list[FlextLdifDbtModel],
    ) -> dict[str, object]:
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


class FlextDbtLdifWorkflowManager:
    """Advanced workflow manager for batch LDIF processing.

    Handles multiple LDIF files and complex workflow orchestration.
    """

    def __init__(
        self,
        config: FlextDbtLdifConfig | None = None,
        project_dir: Path | None = None,
    ) -> None:
        """Initialize workflow manager.

        Args:
            config: Configuration for operations
            project_dir: DBT project directory

        """
        self.config = config or FlextDbtLdifConfig()
        self.project_dir = project_dir or Path.cwd()
        self.service = FlextDbtLdifService(self.config, self.project_dir)

        logger.info("Initialized DBT LDIF workflow manager")

    def process_multiple_ldif_files(
        self,
        ldif_files: list[Path | str],
        *,
        batch_size: int = 10,
    ) -> FlextResult[dict[str, object]]:
        """Process multiple LDIF files in batches.

        Args:
            ldif_files: List of LDIF file paths
            batch_size: Number of files to process per batch

        Returns:
            FlextResult containing batch processing results

        """
        logger.info(
            "Processing %d LDIF files in batches of %d",
            len(ldif_files),
            batch_size,
        )

        try:
            batch_results = []

            for i in range(0, len(ldif_files), batch_size):
                batch = ldif_files[i : i + batch_size]
                logger.info(
                    "Processing batch %d: %d files",
                    i // batch_size + 1,
                    len(batch),
                )

                batch_result = self._process_file_batch(batch)
                batch_results.append(
                    batch_result.data
                    if batch_result.success
                    else {"error": batch_result.error},
                )

            return FlextResult[None].ok(
                {
                    "total_files": len(ldif_files),
                    "batch_size": batch_size,
                    "batch_count": len(batch_results),
                    "batch_results": batch_results,
                    "status": "completed",
                },
            )

        except Exception as e:
            logger.exception("Error in batch processing")
            return FlextResult[None].fail(f"Batch processing error: {e}")

    def _process_file_batch(
        self,
        file_batch: list[Path | str],
    ) -> FlextResult[dict[str, object]]:
        """Process a batch of LDIF files."""
        batch_results: dict[str, object] = {
            "files": [str(f) for f in file_batch],
            "results": [],
            "summary": {"success": 0, "failed": 0},
        }

        summary = batch_results["summary"]
        results = batch_results["results"]

        for file_path in file_batch:
            try:
                result = self.service.run_complete_workflow(file_path)
                if result.success:
                    if isinstance(summary, dict) and "success" in summary:
                        summary["success"] = int(summary["success"]) + 1
                elif isinstance(summary, dict) and "failed" in summary:
                    summary["failed"] = int(summary["failed"]) + 1

                if isinstance(results, list):
                    results.append(
                        {
                            "file": str(file_path),
                            "status": "success" if result.success else "failed",
                            "data": result.data if result.success else None,
                            "error": str(result.error) if not result.success else None,
                        },
                    )

            except Exception as e:
                logger.exception("Error processing file: %s", file_path)
                if isinstance(summary, dict) and "failed" in summary:
                    summary["failed"] = int(summary["failed"]) + 1
                if isinstance(results, list):
                    results.append(
                        {
                            "file": str(file_path),
                            "status": "failed",
                            "error": str(e),
                        },
                    )

        return FlextResult[None].ok(batch_results)


__all__: list[str] = [
    "FlextDbtLdifService",
    "FlextDbtLdifWorkflowManager",
]
