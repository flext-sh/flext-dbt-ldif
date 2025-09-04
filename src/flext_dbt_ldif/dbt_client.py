"""DBT client for LDIF operations.

Provides high-level interface for DBT LDIF transformations.
Integrates flext-ldif and flext-meltano for complete data pipeline operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path

from flext_core import FlextLogger, FlextResult
from flext_ldif import FlextLDIFAPI
from flext_ldif.models import FlextLDIFEntry
from flext_meltano import create_dbt_hub
from flext_meltano.dbt_hub import FlextDbtHub

from .dbt_config import FlextDbtLdifConfig
from .dbt_exceptions import (
    FlextDbtLdifConfigurationError,
    FlextDbtLdifModelError,
    FlextDbtLdifProcessingError,
    FlextDbtLdifTransformationError,
    FlextDbtLdifValidationError,
)

logger = FlextLogger(__name__)


class FlextDbtLdifClient:
    """DBT client for LDIF data transformations.

    Provides unified interface for LDIF data processing, validation,
    and DBT transformation operations using maximum composition
    with flext-ldif and flext-meltano.
    """

    def __init__(
        self,
        config: FlextDbtLdifConfig | None = None,
    ) -> None:
        """Initialize DBT LDIF client.

        Args:
            config: Configuration for LDIF and DBT operations

        """
        self.config = config or FlextDbtLdifConfig()
        
        # Validate configuration using flext-core patterns
        validation_result = self.config.validate_config()
        if not validation_result.success:
            raise FlextDbtLdifConfigurationError(
                f"Configuration validation failed: {validation_result.error}"
            )
        
        self._ldif_api = FlextLDIFAPI()
        self._dbt_hub: FlextDbtHub | None = None
        logger.info("Initialized DBT LDIF client with validated config")

    @property
    def dbt_hub(self) -> FlextDbtHub:
        """Get or create DBT hub instance using flext-meltano patterns."""
        if self._dbt_hub is None:
            try:
                meltano_config = self.config.get_meltano_config()
                self._dbt_hub = create_dbt_hub(config=meltano_config)
                logger.info("Created DBT hub with flext-meltano configuration")
            except Exception as e:
                logger.exception("Failed to create DBT hub")
                raise FlextDbtLdifConfigurationError(
                    f"DBT hub initialization failed: {e}"
                ) from e
        return self._dbt_hub

    def parse_ldif_file(
        self,
        file_path: Path | str | None = None,
    ) -> FlextResult[list[FlextLDIFEntry]]:
        """Parse LDIF file for DBT processing.

        Args:
            file_path: Path to LDIF file (defaults to config path)

        Returns:
            FlextResult containing list of LDIF entries

        """
        try:
            ldif_path = (
                Path(file_path) if file_path else Path(self.config.ldif_file_path)
            )
            
            if not ldif_path.exists():
                raise FlextDbtLdifProcessingError(
                    f"LDIF file not found: {ldif_path}",
                    error_code="FILE_NOT_FOUND",
                )
            
            logger.info("Parsing LDIF file: %s", ldif_path)
            
            # Use flext-ldif API for parsing
            result = self._ldif_api.parse_file(ldif_path)
            if result.success:
                entries = result.value or []
                logger.info("Successfully parsed %d LDIF entries", len(entries))
                return result
            else:
                logger.error("LDIF parsing failed: %s", result.error)
                raise FlextDbtLdifProcessingError(
                    f"LDIF parsing failed: {result.error}",
                    error_code="PARSE_FAILED",
                )
                
        except FlextDbtLdifProcessingError:
            # Re-raise our custom exceptions
            raise
        except Exception as e:
            logger.exception("Unexpected error during LDIF parsing")
            raise FlextDbtLdifProcessingError(
                f"LDIF parsing error: {e}",
                error_code="UNEXPECTED_ERROR",
            ) from e

    def validate_ldif_data(
        self,
        entries: list[FlextLDIFEntry],
    ) -> FlextResult[dict[str, object]]:
        """Validate LDIF data quality for DBT processing.

        Args:
            entries: List of LDIF entries to validate
        Returns:
            FlextResult containing validation metrics

        """
        try:
            logger.info("Validating %d LDIF entries for data quality", len(entries))
            
            # Use flext-ldif API for validation
            validation_result = self._ldif_api.validate(entries)
            if not validation_result.success:
                logger.error("LDIF validation failed: %s", validation_result.error)
                raise FlextDbtLdifValidationError(
                    f"LDIF validation failed: {validation_result.error}",
                    error_code="VALIDATION_FAILED",
                )
                
            # Get statistics using flext-ldif API
            stats_result = self._ldif_api.get_entry_statistics(entries)
            if not stats_result.success:
                raise FlextDbtLdifValidationError(
                    f"Statistics generation failed: {stats_result.error}",
                    error_code="STATS_FAILED",
                )
                
            stats = stats_result.value or {}
            quality_score = stats.get("quality_score", 0.0)
            
            logger.info(
                "LDIF data validation completed: quality_score=%.2f",
                quality_score,
            )
            
            if quality_score < self.config.min_quality_threshold:
                raise FlextDbtLdifValidationError(
                    f"Data quality below threshold: {quality_score} < {self.config.min_quality_threshold}",
                    error_code="QUALITY_THRESHOLD_NOT_MET",
                )
                
            return FlextResult[dict[str, object]].ok(
                {
                    **stats,
                    "quality_score": quality_score,
                    "validation_status": "passed",
                    "threshold": self.config.min_quality_threshold,
                },
            )
            
        except FlextDbtLdifValidationError:
            # Re-raise validation errors
            raise
        except Exception as e:
            logger.exception("Unexpected error during LDIF validation")
            raise FlextDbtLdifValidationError(
                f"LDIF validation error: {e}",
                error_code="UNEXPECTED_ERROR",
            ) from e

    def transform_with_dbt(
        self,
        entries: list[FlextLDIFEntry],
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Transform LDIF data using DBT models via flext-meltano.

        Args:
            entries: LDIF entries to transform
            model_names: Specific DBT models to run (None = all)

        Returns:
            FlextResult containing transformation results

        """
        try:
            logger.info(
                "Running DBT transformations on %d LDIF entries, models=%s",
                len(entries),
                model_names,
            )
            
            # Prepare LDIF data for DBT using flext-ldif API
            prepared_result = self._prepare_ldif_data_for_dbt(entries)
            if not prepared_result.success:
                raise FlextDbtLdifProcessingError(
                    f"Data preparation failed: {prepared_result.error}"
                )
            
            prepared_data = prepared_result.value or {}
            
            # Use flext-meltano DBT hub for execution
            dbt_hub = self.dbt_hub
            
            try:
                if model_names:
                    # Run specific models using flext-meltano
                    logger.info("Running specific DBT models: %s", model_names)
                    run_result = dbt_hub.run_models(
                        models=model_names,
                        target=self.config.dbt_target,
                        profiles_dir=self.config.dbt_profiles_dir,
                    )
                else:
                    # Run all models using flext-meltano
                    logger.info("Running all DBT models")
                    run_result = dbt_hub.run_all(
                        target=self.config.dbt_target,
                        profiles_dir=self.config.dbt_profiles_dir,
                    )
                    
                if not run_result.success:
                    raise FlextDbtLdifTransformationError(
                        f"DBT execution failed: {run_result.error}",
                        transformation_type="dbt_run",
                    )
                    
                # Get transformation metrics
                transformation_results = {
                    "prepared_data_schemas": list(prepared_data.keys()),
                    "prepared_entries_count": sum(
                        len(v) if isinstance(v, list) else 1 
                        for v in prepared_data.values()
                    ),
                    "models_executed": model_names or ["all"],
                    "dbt_result": run_result.value,
                    "transformation_status": "completed",
                }
                
                logger.info("DBT transformation completed successfully")
                return FlextResult[dict[str, object]].ok(transformation_results)
                
            except Exception as dbt_error:
                logger.exception("DBT execution failed")
                raise FlextDbtLdifTransformationError(
                    f"DBT execution error: {dbt_error}",
                    transformation_type="dbt_execution",
                ) from dbt_error
                
        except FlextDbtLdifTransformationError:
            # Re-raise transformation errors
            raise
        except Exception as e:
            logger.exception("Unexpected error during DBT transformation")
            raise FlextDbtLdifTransformationError(
                f"DBT transformation error: {e}",
                transformation_type="general",
            ) from e

    def run_full_pipeline(
        self,
        file_path: Path | str | None = None,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Run complete LDIF to DBT transformation pipeline.

        Args:
            file_path: LDIF file path
            model_names: DBT models to run
        Returns:
            FlextResult containing complete pipeline results

        """
        logger.info("Starting full LDIF-to-DBT pipeline")
        
        try:
            # Step 1: Parse LDIF data
            entries = self.parse_ldif_file(file_path)
            
            # Step 2: Validate data quality
            validation_metrics = self.validate_ldif_data(entries)
            
            # Step 3: Transform with DBT
            transformation_results = self.transform_with_dbt(entries, model_names)
            
            # Combine results
            pipeline_results = {
                "parsed_entries": len(entries),
                "validation_metrics": validation_metrics,
                "transformation_results": transformation_results,
                "pipeline_status": "completed",
            }
            
            logger.info("Full LDIF-to-DBT pipeline completed successfully")
            return FlextResult[dict[str, object]].ok(pipeline_results)
            
        except (
            FlextDbtLdifProcessingError,
            FlextDbtLdifValidationError,
            FlextDbtLdifTransformationError,
        ) as e:
            logger.error("Pipeline failed: %s", e)
            return FlextResult[dict[str, object]].fail(str(e))
        except Exception as e:
            logger.exception("Unexpected error in pipeline")
            return FlextResult[dict[str, object]].fail(f"Pipeline error: {e}")

    def _prepare_ldif_data_for_dbt(
        self,
        entries: list[FlextLDIFEntry],
    ) -> FlextResult[dict[str, object]]:
        """Prepare LDIF entries for DBT processing using flext-ldif API.

        Converts LDIF entries to format suitable for DBT models using
        maximum composition with flext-ldif functionality.

        Args:
            entries: List of LDIF entries
        Returns:
            FlextResult containing prepared data for DBT

        """
        try:
            prepared_data: dict[str, list[dict[str, object]]] = {}
            # Get object class distribution using flext-ldif classification
            stats_result = self._ldif_api.get_objectclass_distribution(entries)
            if not stats_result.success:
                return FlextResult[dict[str, object]].fail(
                    f"Entry statistics failed: {stats_result.error}",
                )
            # Apply schema mapping from config - simple transformation approach
            for entry in entries:
                if hasattr(entry, "object_classes") and entry.object_classes:
                    # Find the primary object class
                    primary_class = (
                        entry.object_classes[0] if entry.object_classes else "unknown"
                    )
                    entry_type = (
                        self.config.get_entry_type_for_object_class(primary_class)
                        or "unknown"
                    )
                    schema_name = self.config.get_schema_for_entry_type(entry_type)
                    if schema_name:
                        if schema_name not in prepared_data:
                            prepared_data[schema_name] = []
                        # Convert entry to dict format
                        if hasattr(entry, "dn") and hasattr(entry, "attributes"):
                            # Convert LDIF entry to a plain dict for DBT mapping
                            entry_dict: dict[str, object] = {"dn": entry.dn}
                            # flext-ldif exposes attributes mapping via entry.attributes.attributes
                            attrs = getattr(entry.attributes, "attributes", {})
                            if isinstance(attrs, dict):
                                for k, v in attrs.items():
                                    entry_dict[str(k)] = v  # preserve original values
                            mapped_entry = self._map_entry_attributes(entry_dict)
                            prepared_data[schema_name].append(mapped_entry)
            logger.debug(
                "Prepared LDIF data for DBT: %s",
                {
                    k: len(v) if isinstance(v, list) else 1
                    for k, v in prepared_data.items()
                },
            )
            return FlextResult[dict[str, object]].ok(dict(prepared_data))
        except Exception as e:
            logger.exception("Error preparing LDIF data for DBT")
            return FlextResult[dict[str, object]].fail(f"Data preparation error: {e}")

    def _map_entry_attributes(self, entry_data: dict[str, object]) -> dict[str, object]:
        """Map LDIF entry attributes using configuration mapping."""
        mapped_attrs = {"dn": entry_data.get("dn")}
        for ldif_attr, dbt_attr in self.config.ldif_attribute_mapping.items():
            if ldif_attr in entry_data:
                mapped_attrs[dbt_attr] = entry_data[ldif_attr]
        # Add unmapped attributes with original names
        mapped_attrs.update(
            {
                attr: value
                for attr, value in entry_data.items()
                if attr not in self.config.ldif_attribute_mapping
            },
        )
        return mapped_attrs


__all__: list[str] = [
    "FlextDbtLdifClient",
]
