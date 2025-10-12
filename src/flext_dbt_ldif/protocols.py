"""DBT LDIF protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextCore


class FlextDbtLdifProtocols:
    """DBT LDIF protocols with explicit re-exports from FlextCore.Protocols foundation.

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

    Foundation = FlextCore.Protocols.Foundation
    Domain = FlextCore.Protocols.Domain
    Application = FlextCore.Protocols.Application
    Infrastructure = FlextCore.Protocols.Infrastructure
    Extensions = FlextCore.Protocols.Extensions
    Commands = FlextCore.Protocols.Commands

    # ============================================================================
    # DBT LDIF-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class DbtLdif:
        """DBT LDIF domain protocols for LDIF data transformation and analytics."""

        @runtime_checkable
        class DbtProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT operations with LDIF data."""

            def run_dbt_models(
                self,
                models: FlextCore.Types.StringList | None = None,
                config: FlextCore.Types.Dict | None = None,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Run DBT models with LDIF data sources.

                Args:
                    models: Specific models to run, or None for all models
                    config: DBT configuration parameters

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT run results or error

                """

            def test_dbt_models(
                self,
                models: FlextCore.Types.StringList | None = None,
                config: FlextCore.Types.Dict | None = None,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Test DBT models with LDIF data validation.

                Args:
                    models: Specific models to test, or None for all models
                    config: DBT test configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT test results or error

                """

            def compile_dbt_models(
                self,
                models: FlextCore.Types.StringList | None = None,
                config: FlextCore.Types.Dict | None = None,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Compile DBT models for LDIF data processing.

                Args:
                    models: Specific models to compile, or None for all models
                    config: DBT compilation configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT compilation results or error

                """

            def get_dbt_manifest(self) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Get DBT manifest with LDIF model definitions.

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT manifest or error

                """

            def validate_dbt_project(self, project_path: str) -> FlextCore.Result[bool]:
                """Validate DBT project configuration for LDIF integration.

                Args:
                    project_path: Path to DBT project directory

                Returns:
                    FlextCore.Result[bool]: Validation status or error

                """

        @runtime_checkable
        class LdifIntegrationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDIF data integration operations."""

            def parse_ldif_file(
                self, ldif_file_path: str, parsing_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Parse LDIF file for DBT processing.

                Args:
                    ldif_file_path: Path to LDIF file
                    parsing_config: LDIF parsing configuration

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Parsed LDIF entries or error

                """

            def transform_ldif_to_dbt_format(
                self,
                ldif_data: list[FlextCore.Types.Dict],
                transformation_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Transform LDIF data to DBT-compatible format.

                Args:
                    ldif_data: Raw LDIF data
                    transformation_config: Transformation parameters

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Transformed data or error

                """

            def validate_ldif_data_quality(
                self,
                data: list[FlextCore.Types.Dict],
                quality_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Validate LDIF data quality for DBT processing.

                Args:
                    data: LDIF data to validate
                    quality_rules: Data quality validation rules

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Quality validation results or error

                """

            def export_ldif_to_warehouse(
                self,
                ldif_data: list[FlextCore.Types.Dict],
                warehouse_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Export LDIF data to data warehouse for DBT processing.

                Args:
                    ldif_data: LDIF data to export
                    warehouse_config: Data warehouse configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Export operation results or error

                """

        @runtime_checkable
        class ModelingProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDIF data modeling operations."""

            def create_entry_dimension(
                self,
                ldif_entries: list[FlextCore.Types.Dict],
                dimension_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create entry dimension model from LDIF entry data.

                Args:
                    ldif_entries: LDIF entry data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Entry dimension model or error

                """

            def create_attribute_dimension(
                self,
                ldif_attributes: list[FlextCore.Types.Dict],
                dimension_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create attribute dimension model from LDIF attribute data.

                Args:
                    ldif_attributes: LDIF attribute data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Attribute dimension model or error

                """

            def create_change_tracking_model(
                self,
                ldif_changes: list[FlextCore.Types.Dict],
                tracking_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create change tracking model from LDIF change data.

                Args:
                    ldif_changes: LDIF change data
                    tracking_config: Change tracking configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Change tracking model or error

                """

            def generate_fact_tables(
                self,
                dimensions: list[FlextCore.Types.Dict],
                fact_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Generate fact tables from LDIF dimensions.

                Args:
                    dimensions: LDIF dimension models
                    fact_config: Fact table configuration

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Generated fact tables or error

                """

        @runtime_checkable
        class TransformationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDIF data transformation operations."""

            def normalize_ldif_attributes(
                self,
                ldif_entries: list[FlextCore.Types.Dict],
                normalization_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Normalize LDIF attributes for consistent data processing.

                Args:
                    ldif_entries: Raw LDIF entries
                    normalization_rules: Attribute normalization rules

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Normalized LDIF data or error

                """

            def process_ldif_changesets(
                self,
                ldif_changes: list[FlextCore.Types.Dict],
                processing_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Process LDIF changeset data for analytics.

                Args:
                    ldif_changes: LDIF changeset data
                    processing_config: Changeset processing configuration

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Processed changeset data or error

                """

            def apply_business_rules(
                self,
                data: list[FlextCore.Types.Dict],
                business_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Apply business rules to LDIF data transformations.

                Args:
                    data: LDIF data to transform
                    business_rules: Business transformation rules

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Transformed data or error

                """

            def generate_derived_attributes(
                self,
                ldif_data: list[FlextCore.Types.Dict],
                derivation_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Generate derived attributes from LDIF base attributes.

                Args:
                    ldif_data: Base LDIF data
                    derivation_config: Attribute derivation configuration

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Data with derived attributes or error

                """

        @runtime_checkable
        class MacroProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT macro operations with LDIF data."""

            def generate_ldif_source_macro(
                self, source_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Generate DBT macro for LDIF data sources.

                Args:
                    source_config: LDIF source configuration

                Returns:
                    FlextCore.Result[str]: Generated DBT macro or error

                """

            def create_ldif_test_macro(
                self, test_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Create DBT test macro for LDIF data validation.

                Args:
                    test_config: LDIF test configuration

                Returns:
                    FlextCore.Result[str]: Generated test macro or error

                """

            def generate_ldif_transformation_macro(
                self, transformation_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Generate DBT transformation macro for LDIF data.

                Args:
                    transformation_config: Transformation configuration

                Returns:
                    FlextCore.Result[str]: Generated transformation macro or error

                """

            def create_ldif_snapshot_macro(
                self, snapshot_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Create DBT snapshot macro for LDIF data versioning.

                Args:
                    snapshot_config: Snapshot configuration

                Returns:
                    FlextCore.Result[str]: Generated snapshot macro or error

                """

        @runtime_checkable
        class QualityProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDIF data quality operations."""

            def validate_ldif_format_compliance(
                self,
                ldif_data: list[FlextCore.Types.Dict],
                format_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Validate LDIF data against format compliance rules.

                Args:
                    ldif_data: LDIF data to validate
                    format_rules: Format compliance rules

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Format validation results or error

                """

            def check_data_completeness(
                self,
                data: list[FlextCore.Types.Dict],
                completeness_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Check LDIF data completeness for DBT processing.

                Args:
                    data: LDIF data to check
                    completeness_config: Completeness validation configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Completeness check results or error

                """

            def detect_data_anomalies(
                self,
                data: list[FlextCore.Types.Dict],
                anomaly_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Detect anomalies in LDIF data for quality assurance.

                Args:
                    data: LDIF data to analyze
                    anomaly_config: Anomaly detection configuration

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Detected anomalies or error

                """

            def generate_quality_report(
                self,
                quality_results: list[FlextCore.Types.Dict],
                report_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Generate data quality report for LDIF DBT processing.

                Args:
                    quality_results: Quality validation results
                    report_config: Report generation configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Quality report or error

                """

        @runtime_checkable
        class PerformanceProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT LDIF performance optimization operations."""

            def optimize_dbt_models(
                self,
                model_config: FlextCore.Types.Dict,
                performance_metrics: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Optimize DBT models for LDIF data processing performance.

                Args:
                    model_config: DBT model configuration
                    performance_metrics: Current performance metrics

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Optimization recommendations or error

                """

            def cache_ldif_parsing(
                self,
                parsing_config: FlextCore.Types.Dict,
                cache_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[bool]:
                """Cache LDIF parsing operations for improved performance.

                Args:
                    parsing_config: LDIF parsing configuration
                    cache_config: Caching configuration

                Returns:
                    FlextCore.Result[bool]: Caching setup success status

                """

            def monitor_dbt_performance(
                self, run_results: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Monitor DBT performance with LDIF data processing.

                Args:
                    run_results: DBT run results

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Performance metrics or error

                """

            def optimize_ldif_parsing(
                self, parsing_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Optimize LDIF parsing operations for DBT data processing.

                Args:
                    parsing_config: LDIF parsing configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Parsing optimization results or error

                """

        @runtime_checkable
        class MonitoringProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT LDIF monitoring operations."""

            def track_dbt_run_metrics(
                self, run_id: str, metrics: FlextCore.Types.Dict
            ) -> FlextCore.Result[bool]:
                """Track DBT run metrics for LDIF data processing.

                Args:
                    run_id: DBT run identifier
                    metrics: Run metrics data

                Returns:
                    FlextCore.Result[bool]: Metric tracking success status

                """

            def monitor_ldif_data_freshness(
                self, freshness_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Monitor LDIF data freshness for DBT processing.

                Args:
                    freshness_config: Data freshness monitoring configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Data freshness status or error

                """

            def get_health_status(self) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Get DBT LDIF integration health status.

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Health status or error

                """

            def create_monitoring_dashboard(
                self, dashboard_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create monitoring dashboard for DBT LDIF operations.

                Args:
                    dashboard_config: Dashboard configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Dashboard creation result or error

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
