"""DBT LDIF protocols for FLEXT ecosystem.

This module provides protocol definitions for DBT operations with LDIF data.
Protocols use types from typings.py and t - NO imports of Models/Config.
Uses Python 3.13+ PEP 695 syntax and Mapping types instead of dict[str, object].

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from flext_core import FlextResult, p, t

from flext_dbt_ldif.typings import FlextDbtLdifTypes


class FlextDbtLdifProtocols:
    """DBT LDIF protocols with explicit re-exports from p foundation.

    This class provides protocol definitions for DBT operations with LDIF data integration,
    data transformation, modeling, and enterprise LDIF analytics patterns.

    Domain Extension Pattern:
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in DbtLdif namespace
    - Uses types from typings.py - NO imports of Models/Config
    - 100% backward compatibility through aliases
    """

    # ============================================================================
    # DBT LDIF-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class DbtLdif:
        """DBT LDIF domain protocols for LDIF data transformation and analytics."""

        @runtime_checkable
        class DbtProtocol(p.Service, Protocol):
            """Protocol for DBT operations with LDIF data.

            Uses types from FlextDbtLdifTypes and t.
            NO imports of Models/Config per protocol rules.
            """

            def run_dbt_models(
                self,
                models: Sequence[str] | None = None,
                config: FlextDbtLdifTypes.DbtLdifTransformation.TransformationConfig
                | None = None,
            ) -> FlextResult[t.JsonDict]:
                """Run DBT models with LDIF data sources.

                Args:
                    models: Specific models to run, or None for all models
                    config: DBT configuration parameters

                Returns:
                    FlextResult[t.JsonDict]: DBT run results or error

                """

            def test_dbt_models(
                self,
                models: Sequence[str] | None = None,
                config: FlextDbtLdifTypes.DbtLdifTransformation.TransformationConfig
                | None = None,
            ) -> FlextResult[t.JsonDict]:
                """Test DBT models with LDIF data validation.

                Args:
                    models: Specific models to test, or None for all models
                    config: DBT test configuration

                Returns:
                    FlextResult[t.JsonDict]: DBT test results or error

                """

            def compile_dbt_models(
                self,
                models: Sequence[str] | None = None,
                config: FlextDbtLdifTypes.DbtLdifTransformation.TransformationConfig
                | None = None,
            ) -> FlextResult[t.JsonDict]:
                """Compile DBT models for LDIF data processing.

                Args:
                    models: Specific models to compile, or None for all models
                    config: DBT compilation configuration

                Returns:
                    FlextResult[t.JsonDict]: DBT compilation results or error

                """

            def get_dbt_manifest(self) -> FlextResult[t.JsonDict]:
                """Get DBT manifest with LDIF model definitions.

                Returns:
                    FlextResult[t.JsonDict]: DBT manifest or error

                """

            def validate_dbt_project(self, project_path: str) -> FlextResult[bool]:
                """Validate DBT project configuration for LDIF integration.

                Args:
                    project_path: Path to DBT project directory

                Returns:
                    FlextResult[bool]: Validation status or error

                """

        @runtime_checkable
        class LdifIntegrationProtocol(p.Service, Protocol):
            """Protocol for LDIF data integration operations.

            Uses types from FlextDbtLdifTypes.LdifData.
            NO imports of Models/Config per protocol rules.
            """

            def parse_ldif_file(
                self,
                ldif_file_path: str,
                parsing_config: FlextDbtLdifTypes.LdifParsing.ParserConfiguration,
            ) -> FlextResult[Sequence[FlextDbtLdifTypes.LdifData.LdifEntry]]:
                """Parse LDIF file for DBT processing.

                Args:
                    ldif_file_path: Path to LDIF file
                    parsing_config: LDIF parsing configuration

                Returns:
                    FlextResult[Sequence[LdifEntry]]: Parsed LDIF entries or error

                """

            def transform_ldif_to_dbt_format(
                self,
                ldif_data: Sequence[FlextDbtLdifTypes.LdifData.LdifEntry],
                transformation_config: FlextDbtLdifTypes.DbtLdifTransformation.TransformationConfig,
            ) -> FlextResult[Sequence[FlextDbtLdifTypes.LdifData.LdifEntry]]:
                """Transform LDIF data to DBT-compatible format.

                Args:
                    ldif_data: Raw LDIF data
                    transformation_config: Transformation parameters

                Returns:
                    FlextResult[Sequence[LdifEntry]]: Transformed data or error

                """

            def validate_ldif_data_quality(
                self,
                data: Sequence[FlextDbtLdifTypes.LdifData.LdifEntry],
                quality_rules: FlextDbtLdifTypes.LdifParsing.ValidationRules,
            ) -> FlextResult[FlextDbtLdifTypes.LdifProcessing.QualityValidation]:
                """Validate LDIF data quality for DBT processing.

                Args:
                    data: LDIF data to validate
                    quality_rules: Data quality validation rules

                Returns:
                    FlextResult[QualityValidation]: Quality validation results or error

                """

            def export_ldif_to_warehouse(
                self,
                ldif_data: Sequence[FlextDbtLdifTypes.LdifData.LdifEntry],
                warehouse_config: FlextDbtLdifTypes.LdifExport.ExportConfiguration,
            ) -> FlextResult[t.JsonDict]:
                """Export LDIF data to data warehouse for DBT processing.

                Args:
                    ldif_data: LDIF data to export
                    warehouse_config: Data warehouse configuration

                Returns:
                    FlextResult[t.JsonDict]: Export operation results or error

                """

        @runtime_checkable
        class ModelingProtocol(p.Service, Protocol):
            """Protocol for LDIF data modeling operations.

            Uses types from FlextDbtLdifTypes.DbtLdifModel.
            NO imports of Models/Config per protocol rules.
            """

            def create_entry_dimension(
                self,
                ldif_entries: Sequence[FlextDbtLdifTypes.LdifData.LdifEntry],
                dimension_config: FlextDbtLdifTypes.DbtLdifModel.LdifModelConfig,
            ) -> FlextResult[FlextDbtLdifTypes.DbtLdifModel.DimensionalModel]:
                """Create entry dimension model from LDIF entry data.

                Args:
                    ldif_entries: LDIF entry data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextResult[DimensionalModel]: Entry dimension model or error

                """

            def create_attribute_dimension(
                self,
                ldif_attributes: Sequence[FlextDbtLdifTypes.LdifData.LdifAttributes],
                dimension_config: FlextDbtLdifTypes.DbtLdifModel.LdifModelConfig,
            ) -> FlextResult[FlextDbtLdifTypes.DbtLdifModel.DimensionalModel]:
                """Create attribute dimension model from LDIF attribute data.

                Args:
                    ldif_attributes: LDIF attribute data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextResult[DimensionalModel]: Attribute dimension model or error

                """

            def create_change_tracking_model(
                self,
                ldif_changes: Sequence[FlextDbtLdifTypes.LdifData.LdifChangeRecord],
                tracking_config: FlextDbtLdifTypes.DbtLdifModel.LdifModelConfig,
            ) -> FlextResult[FlextDbtLdifTypes.DbtLdifModel.FactModel]:
                """Create change tracking model from LDIF change data.

                Args:
                    ldif_changes: LDIF change data
                    tracking_config: Change tracking configuration

                Returns:
                    FlextResult[FactModel]: Change tracking model or error

                """

            def generate_fact_tables(
                self,
                dimensions: Sequence[FlextDbtLdifTypes.DbtLdifModel.DimensionalModel],
                fact_config: FlextDbtLdifTypes.DbtLdifModel.LdifModelConfig,
            ) -> FlextResult[Sequence[FlextDbtLdifTypes.DbtLdifModel.FactModel]]:
                """Generate fact tables from LDIF dimensions.

                Args:
                    dimensions: LDIF dimension models
                    fact_config: Fact table configuration

                Returns:
                    FlextResult[Sequence[FactModel]]: Generated fact tables or error

                """

        @runtime_checkable
        class TransformationProtocol(p.Service, Protocol):
            """Protocol for LDIF data transformation operations.

            Uses types from FlextDbtLdifTypes.DbtLdifTransformation.
            NO imports of Models/Config per protocol rules.
            """

            def normalize_ldif_attributes(
                self,
                ldif_entries: Sequence[FlextDbtLdifTypes.LdifData.LdifEntry],
                normalization_rules: FlextDbtLdifTypes.DbtLdifTransformation.DataNormalization,
            ) -> FlextResult[Sequence[FlextDbtLdifTypes.LdifData.LdifEntry]]:
                """Normalize LDIF attributes for consistent data processing.

                Args:
                    ldif_entries: Raw LDIF entries
                    normalization_rules: Attribute normalization rules

                Returns:
                    FlextResult[Sequence[LdifEntry]]: Normalized LDIF data or error

                """

            def process_ldif_changesets(
                self,
                ldif_changes: Sequence[FlextDbtLdifTypes.LdifData.LdifChangeRecord],
                processing_config: FlextDbtLdifTypes.LdifProcessing.BatchProcessing,
            ) -> FlextResult[Sequence[FlextDbtLdifTypes.LdifData.LdifChangeRecord]]:
                """Process LDIF changeset data for analytics.

                Args:
                    ldif_changes: LDIF changeset data
                    processing_config: Changeset processing configuration

                Returns:
                    FlextResult[Sequence[LdifChangeRecord]]: Processed changeset data or error

                """

            def apply_business_rules(
                self,
                data: Sequence[FlextDbtLdifTypes.LdifData.LdifEntry],
                business_rules: FlextDbtLdifTypes.DbtLdifTransformation.TransformationConfig,
            ) -> FlextResult[Sequence[FlextDbtLdifTypes.LdifData.LdifEntry]]:
                """Apply business rules to LDIF data transformations.

                Args:
                    data: LDIF data to transform
                    business_rules: Business transformation rules

                Returns:
                    FlextResult[Sequence[LdifEntry]]: Transformed data or error

                """

            def generate_derived_attributes(
                self,
                ldif_data: Sequence[FlextDbtLdifTypes.LdifData.LdifEntry],
                derivation_config: FlextDbtLdifTypes.DbtLdifTransformation.AttributeMapping,
            ) -> FlextResult[Sequence[FlextDbtLdifTypes.LdifData.LdifEntry]]:
                """Generate derived attributes from LDIF base attributes.

                Args:
                    ldif_data: Base LDIF data
                    derivation_config: Attribute derivation configuration

                Returns:
                    FlextResult[Sequence[LdifEntry]]: Data with derived attributes or error

                """

        @runtime_checkable
        class MacroProtocol(p.Service, Protocol):
            """Protocol for DBT macro operations with LDIF data.

            Uses types from FlextDbtLdifTypes.
            NO imports of Models/Config per protocol rules.
            """

            def generate_ldif_source_macro(
                self,
                source_config: FlextDbtLdifTypes.DbtLdifModel.ModelDefinition,
            ) -> FlextResult[str]:
                """Generate DBT macro for LDIF data sources.

                Args:
                    source_config: LDIF source configuration

                Returns:
                    FlextResult[str]: Generated DBT macro or error

                """

            def create_ldif_test_macro(
                self,
                test_config: FlextDbtLdifTypes.LdifParsing.ValidationRules,
            ) -> FlextResult[str]:
                """Create DBT test macro for LDIF data validation.

                Args:
                    test_config: LDIF test configuration

                Returns:
                    FlextResult[str]: Generated test macro or error

                """

            def generate_ldif_transformation_macro(
                self,
                transformation_config: FlextDbtLdifTypes.DbtLdifTransformation.TransformationConfig,
            ) -> FlextResult[str]:
                """Generate DBT transformation macro for LDIF data.

                Args:
                    transformation_config: Transformation configuration

                Returns:
                    FlextResult[str]: Generated transformation macro or error

                """

            def create_ldif_snapshot_macro(
                self,
                snapshot_config: FlextDbtLdifTypes.DbtLdifModel.LdifModelConfig,
            ) -> FlextResult[str]:
                """Create DBT snapshot macro for LDIF data versioning.

                Args:
                    snapshot_config: Snapshot configuration

                Returns:
                    FlextResult[str]: Generated snapshot macro or error

                """

        @runtime_checkable
        class QualityProtocol(p.Service, Protocol):
            """Protocol for LDIF data quality operations.

            Uses types from FlextDbtLdifTypes.LdifProcessing.
            NO imports of Models/Config per protocol rules.
            """

            def validate_ldif_format_compliance(
                self,
                ldif_data: Sequence[FlextDbtLdifTypes.LdifData.LdifEntry],
                format_rules: FlextDbtLdifTypes.LdifParsing.ValidationRules,
            ) -> FlextResult[FlextDbtLdifTypes.LdifProcessing.QualityValidation]:
                """Validate LDIF data against format compliance rules.

                Args:
                    ldif_data: LDIF data to validate
                    format_rules: Format compliance rules

                Returns:
                    FlextResult[QualityValidation]: Format validation results or error

                """

            def check_data_completeness(
                self,
                data: Sequence[FlextDbtLdifTypes.LdifData.LdifEntry],
                completeness_config: FlextDbtLdifTypes.LdifParsing.ValidationRules,
            ) -> FlextResult[FlextDbtLdifTypes.LdifProcessing.QualityValidation]:
                """Check LDIF data completeness for DBT processing.

                Args:
                    data: LDIF data to check
                    completeness_config: Completeness validation configuration

                Returns:
                    FlextResult[QualityValidation]: Completeness check results or error

                """

            def detect_data_anomalies(
                self,
                data: Sequence[FlextDbtLdifTypes.LdifData.LdifEntry],
                anomaly_config: FlextDbtLdifTypes.LdifParsing.ValidationRules,
            ) -> FlextResult[Sequence[FlextDbtLdifTypes.LdifData.LdifEntry]]:
                """Detect anomalies in LDIF data for quality assurance.

                Args:
                    data: LDIF data to analyze
                    anomaly_config: Anomaly detection configuration

                Returns:
                    FlextResult[Sequence[LdifEntry]]: Detected anomalies or error

                """

            def generate_quality_report(
                self,
                quality_results: Sequence[
                    FlextDbtLdifTypes.LdifProcessing.QualityValidation
                ],
                report_config: FlextDbtLdifTypes.LdifExport.ExportConfiguration,
            ) -> FlextResult[t.JsonDict]:
                """Generate data quality report for LDIF DBT processing.

                Args:
                    quality_results: Quality validation results
                    report_config: Report generation configuration

                Returns:
                    FlextResult[t.JsonDict]: Quality report or error

                """

        @runtime_checkable
        class PerformanceProtocol(p.Service, Protocol):
            """Protocol for DBT LDIF performance optimization operations.

            Uses types from FlextDbtLdifTypes.LdifProcessing.
            NO imports of Models/Config per protocol rules.
            """

            def optimize_dbt_models(
                self,
                model_config: FlextDbtLdifTypes.DbtLdifModel.LdifModelConfig,
                performance_metrics: FlextDbtLdifTypes.LdifProcessing.ProcessingMetrics,
            ) -> FlextResult[t.JsonDict]:
                """Optimize DBT models for LDIF data processing performance.

                Args:
                    model_config: DBT model configuration
                    performance_metrics: Current performance metrics

                Returns:
                    FlextResult[t.JsonDict]: Optimization recommendations or error

                """

            def cache_ldif_parsing(
                self,
                parsing_config: FlextDbtLdifTypes.LdifParsing.ParserConfiguration,
                cache_config: FlextDbtLdifTypes.LdifProcessing.BatchProcessing,
            ) -> FlextResult[bool]:
                """Cache LDIF parsing operations for improved performance.

                Args:
                    parsing_config: LDIF parsing configuration
                    cache_config: Caching configuration

                Returns:
                    FlextResult[bool]: Caching setup success status

                """

            def monitor_dbt_performance(
                self,
                run_results: t.JsonDict,
            ) -> FlextResult[FlextDbtLdifTypes.LdifProcessing.ProcessingMetrics]:
                """Monitor DBT performance with LDIF data processing.

                Args:
                    run_results: DBT run results

                Returns:
                    FlextResult[ProcessingMetrics]: Performance metrics or error

                """

            def optimize_ldif_parsing(
                self,
                parsing_config: FlextDbtLdifTypes.LdifParsing.ParserConfiguration,
            ) -> FlextResult[FlextDbtLdifTypes.LdifProcessing.ProcessingMetrics]:
                """Optimize LDIF parsing operations for DBT data processing.

                Args:
                    parsing_config: LDIF parsing configuration

                Returns:
                    FlextResult[ProcessingMetrics]: Parsing optimization results or error

                """

        @runtime_checkable
        class MonitoringProtocol(p.Service, Protocol):
            """Protocol for DBT LDIF monitoring operations.

            Uses types from FlextDbtLdifTypes.LdifProcessing.
            NO imports of Models/Config per protocol rules.
            """

            def track_dbt_run_metrics(
                self,
                run_id: str,
                metrics: FlextDbtLdifTypes.LdifProcessing.ProcessingMetrics,
            ) -> FlextResult[bool]:
                """Track DBT run metrics for LDIF data processing.

                Args:
                    run_id: DBT run identifier
                    metrics: Run metrics data

                Returns:
                    FlextResult[bool]: Metric tracking success status

                """

            def monitor_ldif_data_freshness(
                self,
                freshness_config: FlextDbtLdifTypes.LdifProcessing.BatchProcessing,
            ) -> FlextResult[FlextDbtLdifTypes.LdifProcessing.ProcessingMetrics]:
                """Monitor LDIF data freshness for DBT processing.

                Args:
                    freshness_config: Data freshness monitoring configuration

                Returns:
                    FlextResult[ProcessingMetrics]: Data freshness status or error

                """

            def get_health_status(self) -> FlextResult[t.JsonDict]:
                """Get DBT LDIF integration health status.

                Returns:
                    FlextResult[t.JsonDict]: Health status or error

                """

            def create_monitoring_dashboard(
                self,
                dashboard_config: FlextDbtLdifTypes.LdifExport.ExportConfiguration,
            ) -> FlextResult[t.JsonDict]:
                """Create monitoring dashboard for DBT LDIF operations.

                Args:
                    dashboard_config: Dashboard configuration

                Returns:
                    FlextResult[t.JsonDict]: Dashboard creation result or error

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


__all__: list[str] = [
    "FlextDbtLdifProtocols",
]
