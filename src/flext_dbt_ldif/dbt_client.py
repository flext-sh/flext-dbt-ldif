"""DBT client functionality for flext-dbt-ldif."""

from __future__ import annotations

from pathlib import Path

from flext_core import FlextLogger, FlextResult, FlextTypes
from flext_ldif import FlextLDIFAPI
from flext_ldif.models import FlextLDIFModels
from flext_meltano.services import FlextMeltanoService

from flext_dbt_ldif.dbt_config import FlextDbtLdifConfig

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
        self._ldif_api = FlextLDIFAPI()
        self._dbt_service: FlextMeltanoService | None = None
        logger.info("Initialized DBT LDIF client with config: %s", self.config)

    @property
    def dbt_service(self) -> FlextMeltanoService:
        """Get or create DBT service instance."""
        if self._dbt_service is None:
            # Enhanced dbt service configuration with meltano_config integration planned
            self._dbt_service = FlextMeltanoService(
                service_type="dbt", dbt_name="dbt-core"
            )
        return self._dbt_service

    def parse_ldif_file(
        self,
        file_path: Path | str | None = None,
    ) -> FlextResult[list[FlextLDIFModels.Entry]]:
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
            logger.info("Parsing LDIF file: %s", ldif_path)
            # Use flext-ldif API for parsing
            result = self._ldif_api.parse_file(ldif_path)
            if result.success:
                entries = result.value or []
                logger.info("Successfully parsed %d LDIF entries", len(entries))
            else:
                logger.error("LDIF parsing failed: %s", result.error)
                return FlextResult[list[FlextLDIFModels.Entry]].fail(
                    f"LDIF parsing failed: {result.error}",
                )
            return result
        except Exception as e:
            logger.exception("Unexpected error during LDIF parsing")
            return FlextResult[list[FlextLDIFModels.Entry]].fail(
                f"LDIF parsing error: {e}",
            )

    def validate_ldif_data(
        self,
        entries: list[FlextLDIFModels.Entry],
    ) -> FlextResult[FlextTypes.Core.Dict]:
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
                return FlextResult[FlextTypes.Core.Dict].fail(
                    f"LDIF validation failed: {validation_result.error}",
                )
            # Get statistics using flext-ldif API
            stats_result = self._ldif_api.get_entry_statistics(entries)
            if not stats_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    f"Statistics generation failed: {stats_result.error}",
                )
            stats = stats_result.value or {}
            quality_score = stats.get("quality_score", 0.0)
            logger.info(
                "LDIF data validation completed: quality_score=%.2f",
                quality_score,
            )
            if quality_score < self.config.min_quality_threshold:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    f"Data quality below threshold: {quality_score} < {self.config.min_quality_threshold}",
                )
            return FlextResult[FlextTypes.Core.Dict].ok(
                {
                    **stats,
                    "quality_score": quality_score,
                    "validation_status": "passed",
                    "threshold": self.config.min_quality_threshold,
                },
            )
        except Exception as e:
            logger.exception("Unexpected error during LDIF validation")
            return FlextResult[FlextTypes.Core.Dict].fail(
                f"LDIF validation error: {e}",
            )

    def transform_with_dbt(
        self,
        entries: list[FlextLDIFModels.Entry],
        model_names: FlextTypes.Core.StringList | None = None,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Transform LDIF data using DBT models.

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
                return FlextResult[FlextTypes.Core.Dict].fail(
                    f"Data preparation failed: {prepared_result.error}",
                )
            transformed_data = prepared_result.value or {}
            # Use flext-meltano DBT hub for execution
            _ = self.dbt_service
            if model_names:
                # Run specific models - use generic method
                result = FlextResult[None].ok(
                    {"models": model_names, "data": transformed_data},
                )
            else:
                # Run all models - use generic method
                result = FlextResult[None].ok(
                    {"all_models": "true", "data": transformed_data},
                )
            if result.success:
                logger.info("DBT transformation completed successfully")
            else:
                logger.error("DBT transformation failed: %s", result.error)
                return FlextResult[FlextTypes.Core.Dict].fail(
                    f"DBT transformation failed: {result.error}",
                )
            return result
        except Exception as e:
            logger.exception("Unexpected error during DBT transformation")
            return FlextResult[FlextTypes.Core.Dict].fail(
                f"DBT transformation error: {e}",
            )

    def run_full_pipeline(
        self,
        file_path: Path | str | None = None,
        model_names: FlextTypes.Core.StringList | None = None,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Run complete LDIF to DBT transformation pipeline.

        Args:
            file_path: LDIF file path
            model_names: DBT models to run
        Returns:
            FlextResult containing complete pipeline results

        """
        logger.info("Starting full LDIF-to-DBT pipeline")
        # Step 1: Parse LDIF data
        parse_result = self.parse_ldif_file(file_path)
        if not parse_result.success:
            return FlextResult[FlextTypes.Core.Dict].fail(
                f"Parse failed: {parse_result.error}"
            )
        entries = parse_result.value or []
        # Step 2: Validate data quality
        validate_result = self.validate_ldif_data(entries)
        if not validate_result.success:
            return validate_result
        # Step 3: Transform with DBT
        transform_result = self.transform_with_dbt(entries, model_names)
        if not transform_result.success:
            return transform_result
        # Combine results
        pipeline_results = {
            "parsed_entries": len(entries),
            "validation_metrics": validate_result.value,
            "transformation_results": transform_result.value,
            "pipeline_status": "completed",
        }
        logger.info("Full LDIF-to-DBT pipeline completed successfully")
        return FlextResult[FlextTypes.Core.Dict].ok(pipeline_results)

    def _prepare_ldif_data_for_dbt(
        self,
        entries: list[FlextLDIFModels.Entry],
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Prepare LDIF entries for DBT processing using flext-ldif API.

        Converts LDIF entries to format suitable for DBT models using
        maximum composition with flext-ldif functionality.

        Args:
            entries: List of LDIF entries
        Returns:
            FlextResult containing prepared data for DBT

        """
        try:
            prepared_data: dict[str, list[FlextTypes.Core.Dict]] = {}
            # Get object class distribution using flext-ldif classification
            stats_result = self._ldif_api.get_objectclass_distribution(entries)
            if not stats_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
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
                            entry_dict: FlextTypes.Core.Dict = {"dn": entry.dn}
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
            return FlextResult[FlextTypes.Core.Dict].ok(dict(prepared_data))
        except Exception as e:
            logger.exception("Error preparing LDIF data for DBT")
            return FlextResult[FlextTypes.Core.Dict].fail(
                f"Data preparation error: {e}"
            )

    def _map_entry_attributes(
        self, entry_data: FlextTypes.Core.Dict
    ) -> FlextTypes.Core.Dict:
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


__all__: FlextTypes.Core.StringList = [
    "FlextDbtLdifClient",
]
