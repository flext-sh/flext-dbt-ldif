"""DBT LDIF protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextProtocols, FlextResult, FlextTypes


class FlextDbtLdifProtocols:
    """DBT LDIF protocols with explicit re-exports from FlextProtocols foundation.

    This class provides protocol definitions for DBT operations with LDIF data integration,
    data transformation, modeling, and enterprise LDIF analytics patterns.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in DbtLdif namespace
    - 100% backward compatibility through aliases
    """

    # ============================================================================
    # RE-EXPORT FOUNDATION PROTOCOLS (EXPLICIT PATTERN)
    # ============================================================================

    # ============================================================================
    # DBT LDIF-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class DbtLdif:
        """DBT LDIF domain protocols for LDIF data transformation and analytics."""

        @runtime_checkable
        class DbtProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT operations with LDIF data."""

            def run_dbt_models(
                self,
                models: FlextTypes.StringList | None = None,
                config: FlextTypes.Dict | None = None,
            ) -> FlextResult[FlextTypes.Dict]:
                """Run DBT models with LDIF data sources.

                Args:
                    models: Specific models to run, or None for all models
                    config: DBT configuration parameters

                Returns:
                    FlextResult[FlextTypes.Dict]: DBT run results or error

                """

            def test_dbt_models(
                self,
                models: FlextTypes.StringList | None = None,
                config: FlextTypes.Dict | None = None,
            ) -> FlextResult[FlextTypes.Dict]:
                """Test DBT models with LDIF data validation.

                Args:
                    models: Specific models to test, or None for all models
                    config: DBT test configuration

                Returns:
                    FlextResult[FlextTypes.Dict]: DBT test results or error

                """

            def compile_dbt_models(
                self,
                models: FlextTypes.StringList | None = None,
                config: FlextTypes.Dict | None = None,
            ) -> FlextResult[FlextTypes.Dict]:
                """Compile DBT models for LDIF data processing.

                Args:
                    models: Specific models to compile, or None for all models
                    config: DBT compilation configuration

                Returns:
                    FlextResult[FlextTypes.Dict]: DBT compilation results or error

                """

            def get_dbt_manifest(self) -> FlextResult[FlextTypes.Dict]:
                """Get DBT manifest with LDIF model definitions.

                Returns:
                    FlextResult[FlextTypes.Dict]: DBT manifest or error

                """

            def validate_dbt_project(self, project_path: str) -> FlextResult[bool]:
                """Validate DBT project configuration for LDIF integration.

                Args:
                    project_path: Path to DBT project directory

                Returns:
                    FlextResult[bool]: Validation status or error

                """

        @runtime_checkable
        class LdifIntegrationProtocol(FlextProtocols.Service, Protocol):
            """Protocol for LDIF data integration operations."""

            def parse_ldif_file(
                self, ldif_file_path: str, parsing_config: FlextTypes.Dict
            ) -> FlextResult[list[FlextTypes.Dict]]:
                """Parse LDIF file for DBT processing.

                Args:
                    ldif_file_path: Path to LDIF file
                    parsing_config: LDIF parsing configuration

                Returns:
                    FlextResult[list[FlextTypes.Dict]]: Parsed LDIF entries or error

                """

            def transform_ldif_to_dbt_format(
                self,
                ldif_data: list[FlextTypes.Dict],
                transformation_config: FlextTypes.Dict,
            ) -> FlextResult[list[FlextTypes.Dict]]:
                """Transform LDIF data to DBT-compatible format.

                Args:
                    ldif_data: Raw LDIF data
                    transformation_config: Transformation parameters

                Returns:
                    FlextResult[list[FlextTypes.Dict]]: Transformed data or error

                """

            def validate_ldif_data_quality(
                self,
                data: list[FlextTypes.Dict],
                quality_rules: FlextTypes.Dict,
            ) -> FlextResult[FlextTypes.Dict]:
                """Validate LDIF data quality for DBT processing.

                Args:
                    data: LDIF data to validate
                    quality_rules: Data quality validation rules

                Returns:
                    FlextResult[FlextTypes.Dict]: Quality validation results or error

                """

            def export_ldif_to_warehouse(
                self,
                ldif_data: list[FlextTypes.Dict],
                warehouse_config: FlextTypes.Dict,
            ) -> FlextResult[FlextTypes.Dict]:
                """Export LDIF data to data warehouse for DBT processing.

                Args:
                    ldif_data: LDIF data to export
                    warehouse_config: Data warehouse configuration

                Returns:
                    FlextResult[FlextTypes.Dict]: Export operation results or error

                """

        @runtime_checkable
        class ModelingProtocol(FlextProtocols.Service, Protocol):
            """Protocol for LDIF data modeling operations."""

            def create_entry_dimension(
                self,
                ldif_entries: list[FlextTypes.Dict],
                dimension_config: FlextTypes.Dict,
            ) -> FlextResult[FlextTypes.Dict]:
                """Create entry dimension model from LDIF entry data.

                Args:
                    ldif_entries: LDIF entry data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextResult[FlextTypes.Dict]: Entry dimension model or error

                """

            def create_attribute_dimension(
                self,
                ldif_attributes: list[FlextTypes.Dict],
                dimension_config: FlextTypes.Dict,
            ) -> FlextResult[FlextTypes.Dict]:
                """Create attribute dimension model from LDIF attribute data.

                Args:
                    ldif_attributes: LDIF attribute data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextResult[FlextTypes.Dict]: Attribute dimension model or error

                """

            def create_change_tracking_model(
                self,
                ldif_changes: list[FlextTypes.Dict],
                tracking_config: FlextTypes.Dict,
            ) -> FlextResult[FlextTypes.Dict]:
                """Create change tracking model from LDIF change data.

                Args:
                    ldif_changes: LDIF change data
                    tracking_config: Change tracking configuration

                Returns:
                    FlextResult[FlextTypes.Dict]: Change tracking model or error

                """

            def generate_fact_tables(
                self,
                dimensions: list[FlextTypes.Dict],
                fact_config: FlextTypes.Dict,
            ) -> FlextResult[list[FlextTypes.Dict]]:
                """Generate fact tables from LDIF dimensions.

                Args:
                    dimensions: LDIF dimension models
                    fact_config: Fact table configuration

                Returns:
                    FlextResult[list[FlextTypes.Dict]]: Generated fact tables or error

                """

        @runtime_checkable
        class TransformationProtocol(FlextProtocols.Service, Protocol):
            """Protocol for LDIF data transformation operations."""

            def normalize_ldif_attributes(
                self,
                ldif_entries: list[FlextTypes.Dict],
                normalization_rules: FlextTypes.Dict,
            ) -> FlextResult[list[FlextTypes.Dict]]:
                """Normalize LDIF attributes for consistent data processing.

                Args:
                    ldif_entries: Raw LDIF entries
                    normalization_rules: Attribute normalization rules

                Returns:
                    FlextResult[list[FlextTypes.Dict]]: Normalized LDIF data or error

                """

            def process_ldif_changesets(
                self,
                ldif_changes: list[FlextTypes.Dict],
                processing_config: FlextTypes.Dict,
            ) -> FlextResult[list[FlextTypes.Dict]]:
                """Process LDIF changeset data for analytics.

                Args:
                    ldif_changes: LDIF changeset data
                    processing_config: Changeset processing configuration

                Returns:
                    FlextResult[list[FlextTypes.Dict]]: Processed changeset data or error

                """

            def apply_business_rules(
                self,
                data: list[FlextTypes.Dict],
                business_rules: FlextTypes.Dict,
            ) -> FlextResult[list[FlextTypes.Dict]]:
                """Apply business rules to LDIF data transformations.

                Args:
                    data: LDIF data to transform
                    business_rules: Business transformation rules

                Returns:
                    FlextResult[list[FlextTypes.Dict]]: Transformed data or error

                """

            def generate_derived_attributes(
                self,
                ldif_data: list[FlextTypes.Dict],
                derivation_config: FlextTypes.Dict,
            ) -> FlextResult[list[FlextTypes.Dict]]:
                """Generate derived attributes from LDIF base attributes.

                Args:
                    ldif_data: Base LDIF data
                    derivation_config: Attribute derivation configuration

                Returns:
                    FlextResult[list[FlextTypes.Dict]]: Data with derived attributes or error

                """

        @runtime_checkable
        class MacroProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT macro operations with LDIF data."""

            def generate_ldif_source_macro(
                self, source_config: FlextTypes.Dict
            ) -> FlextResult[str]:
                """Generate DBT macro for LDIF data sources.

                Args:
                    source_config: LDIF source configuration

                Returns:
                    FlextResult[str]: Generated DBT macro or error

                """

            def create_ldif_test_macro(
                self, test_config: FlextTypes.Dict
            ) -> FlextResult[str]:
                """Create DBT test macro for LDIF data validation.

                Args:
                    test_config: LDIF test configuration

                Returns:
                    FlextResult[str]: Generated test macro or error

                """

            def generate_ldif_transformation_macro(
                self, transformation_config: FlextTypes.Dict
            ) -> FlextResult[str]:
                """Generate DBT transformation macro for LDIF data.

                Args:
                    transformation_config: Transformation configuration

                Returns:
                    FlextResult[str]: Generated transformation macro or error

                """

            def create_ldif_snapshot_macro(
                self, snapshot_config: FlextTypes.Dict
            ) -> FlextResult[str]:
                """Create DBT snapshot macro for LDIF data versioning.

                Args:
                    snapshot_config: Snapshot configuration

                Returns:
                    FlextResult[str]: Generated snapshot macro or error

                """

        @runtime_checkable
        class QualityProtocol(FlextProtocols.Service, Protocol):
            """Protocol for LDIF data quality operations."""

            def validate_ldif_format_compliance(
                self,
                ldif_data: list[FlextTypes.Dict],
                format_rules: FlextTypes.Dict,
            ) -> FlextResult[FlextTypes.Dict]:
                """Validate LDIF data against format compliance rules.

                Args:
                    ldif_data: LDIF data to validate
                    format_rules: Format compliance rules

                Returns:
                    FlextResult[FlextTypes.Dict]: Format validation results or error

                """

            def check_data_completeness(
                self,
                data: list[FlextTypes.Dict],
                completeness_config: FlextTypes.Dict,
            ) -> FlextResult[FlextTypes.Dict]:
                """Check LDIF data completeness for DBT processing.

                Args:
                    data: LDIF data to check
                    completeness_config: Completeness validation configuration

                Returns:
                    FlextResult[FlextTypes.Dict]: Completeness check results or error

                """

            def detect_data_anomalies(
                self,
                data: list[FlextTypes.Dict],
                anomaly_config: FlextTypes.Dict,
            ) -> FlextResult[list[FlextTypes.Dict]]:
                """Detect anomalies in LDIF data for quality assurance.

                Args:
                    data: LDIF data to analyze
                    anomaly_config: Anomaly detection configuration

                Returns:
                    FlextResult[list[FlextTypes.Dict]]: Detected anomalies or error

                """

            def generate_quality_report(
                self,
                quality_results: list[FlextTypes.Dict],
                report_config: FlextTypes.Dict,
            ) -> FlextResult[FlextTypes.Dict]:
                """Generate data quality report for LDIF DBT processing.

                Args:
                    quality_results: Quality validation results
                    report_config: Report generation configuration

                Returns:
                    FlextResult[FlextTypes.Dict]: Quality report or error

                """

        @runtime_checkable
        class PerformanceProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT LDIF performance optimization operations."""

            def optimize_dbt_models(
                self,
                model_config: FlextTypes.Dict,
                performance_metrics: FlextTypes.Dict,
            ) -> FlextResult[FlextTypes.Dict]:
                """Optimize DBT models for LDIF data processing performance.

                Args:
                    model_config: DBT model configuration
                    performance_metrics: Current performance metrics

                Returns:
                    FlextResult[FlextTypes.Dict]: Optimization recommendations or error

                """

            def cache_ldif_parsing(
                self,
                parsing_config: FlextTypes.Dict,
                cache_config: FlextTypes.Dict,
            ) -> FlextResult[bool]:
                """Cache LDIF parsing operations for improved performance.

                Args:
                    parsing_config: LDIF parsing configuration
                    cache_config: Caching configuration

                Returns:
                    FlextResult[bool]: Caching setup success status

                """

            def monitor_dbt_performance(
                self, run_results: FlextTypes.Dict
            ) -> FlextResult[FlextTypes.Dict]:
                """Monitor DBT performance with LDIF data processing.

                Args:
                    run_results: DBT run results

                Returns:
                    FlextResult[FlextTypes.Dict]: Performance metrics or error

                """

            def optimize_ldif_parsing(
                self, parsing_config: FlextTypes.Dict
            ) -> FlextResult[FlextTypes.Dict]:
                """Optimize LDIF parsing operations for DBT data processing.

                Args:
                    parsing_config: LDIF parsing configuration

                Returns:
                    FlextResult[FlextTypes.Dict]: Parsing optimization results or error

                """

        @runtime_checkable
        class MonitoringProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT LDIF monitoring operations."""

            def track_dbt_run_metrics(
                self, run_id: str, metrics: FlextTypes.Dict
            ) -> FlextResult[bool]:
                """Track DBT run metrics for LDIF data processing.

                Args:
                    run_id: DBT run identifier
                    metrics: Run metrics data

                Returns:
                    FlextResult[bool]: Metric tracking success status

                """

            def monitor_ldif_data_freshness(
                self, freshness_config: FlextTypes.Dict
            ) -> FlextResult[FlextTypes.Dict]:
                """Monitor LDIF data freshness for DBT processing.

                Args:
                    freshness_config: Data freshness monitoring configuration

                Returns:
                    FlextResult[FlextTypes.Dict]: Data freshness status or error

                """

            def get_health_status(self) -> FlextResult[FlextTypes.Dict]:
                """Get DBT LDIF integration health status.

                Returns:
                    FlextResult[FlextTypes.Dict]: Health status or error

                """

            def create_monitoring_dashboard(
                self, dashboard_config: FlextTypes.Dict
            ) -> FlextResult[FlextTypes.Dict]:
                """Create monitoring dashboard for DBT LDIF operations.

                Args:
                    dashboard_config: Dashboard configuration

                Returns:
                    FlextResult[FlextTypes.Dict]: Dashboard creation result or error

                """

    # ============================================================================
    # BACKWARD COMPATIBILITY ALIASES (100% COMPATIBILITY)
    # ============================================================================

    # DBT operations
    DbtProtocol = DbtLdif.DbtProtocol

    # LDIF integration
    LdifIntegrationProtocol = DbtLdif.LdifIntegrationProtocol

    # Data modeling
    ModelingProtocol = DbtLdif.ModelingProtocol

    # Transformations
    TransformationProtocol = DbtLdif.TransformationProtocol

    # DBT macros
    MacroProtocol = DbtLdif.MacroProtocol

    # Data quality
    QualityProtocol = DbtLdif.QualityProtocol

    # Performance optimization
    PerformanceProtocol = DbtLdif.PerformanceProtocol

    # Monitoring
    MonitoringProtocol = DbtLdif.MonitoringProtocol

    # Convenience aliases for downstream usage
    DbtLdifProtocol = DbtLdif.DbtProtocol
    DbtLdifIntegrationProtocol = DbtLdif.LdifIntegrationProtocol
    DbtLdifModelingProtocol = DbtLdif.ModelingProtocol
    DbtLdifTransformationProtocol = DbtLdif.TransformationProtocol
    DbtLdifMacroProtocol = DbtLdif.MacroProtocol
    DbtLdifQualityProtocol = DbtLdif.QualityProtocol
    DbtLdifPerformanceProtocol = DbtLdif.PerformanceProtocol
    DbtLdifMonitoringProtocol = DbtLdif.MonitoringProtocol


__all__ = [
    "FlextDbtLdifProtocols",
]
