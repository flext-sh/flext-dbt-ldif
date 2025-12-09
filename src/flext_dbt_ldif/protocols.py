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

from flext_ldif.protocols import FlextLdifProtocols as p_ldif
from flext_meltano.protocols import FlextMeltanoProtocols as p_meltano

from flext_dbt_ldif.typings import t


class FlextDbtLdifProtocols(p_meltano, p_ldif):
    """DBT LDIF protocols extending LDIF and Meltano protocols.

    Extends both FlextLdifProtocols and FlextMeltanoProtocols via multiple inheritance
    to inherit all LDIF protocols, Meltano protocols, and foundation protocols.

    Architecture:
    - EXTENDS: FlextLdifProtocols (inherits .Ldif.* protocols)
    - EXTENDS: FlextMeltanoProtocols (inherits .Meltano.* protocols)
    - ADDS: DBT LDIF-specific protocols in Dbt.Ldif namespace
    - PROVIDES: Root-level alias `p` for convenient access
    - Uses types from typings.py - NO imports of Models/Config

    Usage:
    from flext_dbt_ldif.protocols import p

    # Foundation protocols (inherited)
    result: p.Result[str]
    service: p.Service[str]

    # LDIF protocols (inherited)
    entry: p.Models.EntryProtocol

    # Meltano protocols (inherited)
    dbt: p.Meltano.DbtProtocol

    # DBT LDIF-specific protocols
    dbt_protocol: p.Dbt.DbtProtocol
    """

    # ============================================================================
    # DBT LDIF-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class Dbt:
        """DBT domain protocols."""

        class Ldif:
            """DBT LDIF domain protocols for LDIF data transformation and analytics."""

            @runtime_checkable
            class DbtProtocol(p_ldif.Service[object], Protocol):
                """Protocol for DBT operations with LDIF data.

                Uses types from t.
                NO imports of Models/Config per protocol rules.
                """

                def run_dbt_models(
                    self,
                    models: Sequence[str] | None = None,
                    config: t.DbtLdifTransformation.TransformationConfig | None = None,
                ) -> p_meltano.Result[t.JsonDict]:
                    """Run DBT models with LDIF data sources.

                    Args:
                        models: Specific models to run, or None for all models
                        config: DBT configuration parameters

                    Returns:
                        r[t.JsonDict]: DBT run results or error

                    """
                    ...

                def test_dbt_models(
                    self,
                    models: Sequence[str] | None = None,
                    config: t.DbtLdifTransformation.TransformationConfig | None = None,
                ) -> p_meltano.Result[t.JsonDict]:
                    """Test DBT models with LDIF data validation.

                    Args:
                        models: Specific models to test, or None for all models
                        config: DBT test configuration

                    Returns:
                        r[t.JsonDict]: DBT test results or error

                    """
                    ...

                def compile_dbt_models(
                    self,
                    models: Sequence[str] | None = None,
                    config: t.DbtLdifTransformation.TransformationConfig | None = None,
                ) -> p_meltano.Result[t.JsonDict]:
                    """Compile DBT models for LDIF data processing.

                    Args:
                        models: Specific models to compile, or None for all models
                        config: DBT compilation configuration

                    Returns:
                        r[t.JsonDict]: DBT compilation results or error

                    """
                    ...

                def get_dbt_manifest(self) -> p_meltano.Result[t.JsonDict]:
                    """Get DBT manifest with LDIF model definitions.

                    Returns:
                        r[t.JsonDict]: DBT manifest or error

                    """
                    ...

                def validate_dbt_project(
                    self, project_path: str
                ) -> p_meltano.Result[bool]:
                    """Validate DBT project configuration for LDIF integration.

                    Args:
                        project_path: Path to DBT project directory

                    Returns:
                        r[bool]: Validation status or error

                    """
                    ...

            @runtime_checkable
            class LdifIntegrationProtocol(p_ldif.Service[object], Protocol):
                """Protocol for LDIF data integration operations.

                Uses types from t.LdifData.
                NO imports of Models/Config per protocol rules.
                """

                def parse_ldif_file(
                    self,
                    ldif_file_path: str,
                    parsing_config: t.LdifParsing.ParserConfiguration,
                ) -> p_meltano.Result[Sequence[t.LdifData.LdifEntry]]:
                    """Parse LDIF file for DBT processing.

                    Args:
                        ldif_file_path: Path to LDIF file
                        parsing_config: LDIF parsing configuration

                    Returns:
                        r[Sequence[LdifEntry]]: Parsed LDIF entries or error

                    """
                    ...

                def transform_ldif_to_dbt_format(
                    self,
                    ldif_data: Sequence[t.LdifData.LdifEntry],
                    transformation_config: t.DbtLdifTransformation.TransformationConfig,
                ) -> p_meltano.Result[Sequence[t.LdifData.LdifEntry]]:
                    """Transform LDIF data to DBT-compatible format.

                    Args:
                        ldif_data: Raw LDIF data
                        transformation_config: Transformation parameters

                    Returns:
                        r[Sequence[LdifEntry]]: Transformed data or error

                    """
                    ...

                def validate_ldif_data_quality(
                    self,
                    data: Sequence[t.LdifData.LdifEntry],
                    quality_rules: t.LdifParsing.ValidationRules,
                ) -> p_meltano.Result[t.LdifProcessing.QualityValidation]:
                    """Validate LDIF data quality for DBT processing.

                    Args:
                        data: LDIF data to validate
                        quality_rules: Data quality validation rules

                    Returns:
                        r[QualityValidation]: Quality validation results or error

                    """
                    ...

                def export_ldif_to_warehouse(
                    self,
                    ldif_data: Sequence[t.LdifData.LdifEntry],
                    warehouse_config: t.LdifExport.ExportConfiguration,
                ) -> p_meltano.Result[t.JsonDict]:
                    """Export LDIF data to data warehouse for DBT processing.

                    Args:
                        ldif_data: LDIF data to export
                        warehouse_config: Data warehouse configuration

                    Returns:
                        r[t.JsonDict]: Export operation results or error

                    """
                    ...

            @runtime_checkable
            class ModelingProtocol(p_ldif.Service[object], Protocol):
                """Protocol for LDIF data modeling operations.

                Uses types from t.DbtLdifModel.
                NO imports of Models/Config per protocol rules.
                """

                def create_entry_dimension(
                    self,
                    ldif_entries: Sequence[t.LdifData.LdifEntry],
                    dimension_config: t.DbtLdifModel.LdifModelConfig,
                ) -> p_meltano.Result[t.DbtLdifModel.DimensionalModel]:
                    """Create entry dimension model from LDIF entry data.

                    Args:
                        ldif_entries: LDIF entry data
                        dimension_config: Dimension modeling configuration

                    Returns:
                        r[DimensionalModel]: Entry dimension model or error

                    """
                    ...

                def create_attribute_dimension(
                    self,
                    ldif_attributes: Sequence[t.LdifData.LdifAttributes],
                    dimension_config: t.DbtLdifModel.LdifModelConfig,
                ) -> p_meltano.Result[t.DbtLdifModel.DimensionalModel]:
                    """Create attribute dimension model from LDIF attribute data.

                    Args:
                        ldif_attributes: LDIF attribute data
                        dimension_config: Dimension modeling configuration

                    Returns:
                        r[DimensionalModel]: Attribute dimension model or error

                    """
                    ...

                def create_change_tracking_model(
                    self,
                    ldif_changes: Sequence[t.LdifData.LdifChangeRecord],
                    tracking_config: t.DbtLdifModel.LdifModelConfig,
                ) -> p_meltano.Result[t.DbtLdifModel.FactModel]:
                    """Create change tracking model from LDIF change data.

                    Args:
                        ldif_changes: LDIF change data
                        tracking_config: Change tracking configuration

                    Returns:
                        r[FactModel]: Change tracking model or error

                    """
                    ...

                def generate_fact_tables(
                    self,
                    dimensions: Sequence[t.DbtLdifModel.DimensionalModel],
                    fact_config: t.DbtLdifModel.LdifModelConfig,
                ) -> p_meltano.Result[Sequence[t.DbtLdifModel.FactModel]]:
                    """Generate fact tables from LDIF dimensions.

                    Args:
                        dimensions: LDIF dimension models
                        fact_config: Fact table configuration

                    Returns:
                        r[Sequence[FactModel]]: Generated fact tables or error

                    """
                    ...

            @runtime_checkable
            class TransformationProtocol(p_ldif.Service[object], Protocol):
                """Protocol for LDIF data transformation operations.

                Uses types from t.DbtLdifTransformation.
                NO imports of Models/Config per protocol rules.
                """

                def normalize_ldif_attributes(
                    self,
                    ldif_entries: Sequence[t.LdifData.LdifEntry],
                    normalization_rules: t.DbtLdifTransformation.DataNormalization,
                ) -> p_meltano.Result[Sequence[t.LdifData.LdifEntry]]:
                    """Normalize LDIF attributes for consistent data processing.

                    Args:
                        ldif_entries: Raw LDIF entries
                        normalization_rules: Attribute normalization rules

                    Returns:
                        r[Sequence[LdifEntry]]: Normalized LDIF data or error

                    """
                    ...

                def process_ldif_changesets(
                    self,
                    ldif_changes: Sequence[t.LdifData.LdifChangeRecord],
                    processing_config: t.LdifProcessing.BatchProcessing,
                ) -> p_meltano.Result[Sequence[t.LdifData.LdifChangeRecord]]:
                    """Process LDIF changeset data for analytics.

                    Args:
                        ldif_changes: LDIF changeset data
                        processing_config: Changeset processing configuration

                    Returns:
                        r[Sequence[LdifChangeRecord]]: Processed changeset data or error

                    """
                    ...

                def apply_business_rules(
                    self,
                    data: Sequence[t.LdifData.LdifEntry],
                    business_rules: t.DbtLdifTransformation.TransformationConfig,
                ) -> p_meltano.Result[Sequence[t.LdifData.LdifEntry]]:
                    """Apply business rules to LDIF data transformations.

                    Args:
                        data: LDIF data to transform
                        business_rules: Business transformation rules

                    Returns:
                        r[Sequence[LdifEntry]]: Transformed data or error

                    """
                    ...

                def generate_derived_attributes(
                    self,
                    ldif_data: Sequence[t.LdifData.LdifEntry],
                    derivation_config: t.DbtLdifTransformation.AttributeMapping,
                ) -> p_meltano.Result[Sequence[t.LdifData.LdifEntry]]:
                    """Generate derived attributes from LDIF base attributes.

                    Args:
                        ldif_data: Base LDIF data
                        derivation_config: Attribute derivation configuration

                    Returns:
                        r[Sequence[LdifEntry]]: Data with derived attributes or error

                    """
                    ...

            @runtime_checkable
            class MacroProtocol(p_ldif.Service[object], Protocol):
                """Protocol for DBT macro operations with LDIF data.

                Uses types from t.
                NO imports of Models/Config per protocol rules.
                """

                def generate_ldif_source_macro(
                    self,
                    source_config: t.DbtLdifModel.ModelDefinition,
                ) -> p_meltano.Result[str]:
                    """Generate DBT macro for LDIF data sources.

                    Args:
                        source_config: LDIF source configuration

                    Returns:
                        r[str]: Generated DBT macro or error

                    """
                    ...

                def create_ldif_test_macro(
                    self,
                    test_config: t.LdifParsing.ValidationRules,
                ) -> p_meltano.Result[str]:
                    """Create DBT test macro for LDIF data validation.

                    Args:
                        test_config: LDIF test configuration

                    Returns:
                        r[str]: Generated test macro or error

                    """
                    ...

                def generate_ldif_transformation_macro(
                    self,
                    transformation_config: t.DbtLdifTransformation.TransformationConfig,
                ) -> p_meltano.Result[str]:
                    """Generate DBT transformation macro for LDIF data.

                    Args:
                        transformation_config: Transformation configuration

                    Returns:
                        r[str]: Generated transformation macro or error

                    """
                    ...

                def create_ldif_snapshot_macro(
                    self,
                    snapshot_config: t.DbtLdifModel.LdifModelConfig,
                ) -> p_meltano.Result[str]:
                    """Create DBT snapshot macro for LDIF data versioning.

                    Args:
                        snapshot_config: Snapshot configuration

                    Returns:
                        r[str]: Generated snapshot macro or error

                    """
                    ...

            @runtime_checkable
            class QualityProtocol(p_ldif.Service[object], Protocol):
                """Protocol for LDIF data quality operations.

                Uses types from t.LdifProcessing.
                NO imports of Models/Config per protocol rules.
                """

                def validate_ldif_format_compliance(
                    self,
                    ldif_data: Sequence[t.LdifData.LdifEntry],
                    format_rules: t.LdifParsing.ValidationRules,
                ) -> p_meltano.Result[t.LdifProcessing.QualityValidation]:
                    """Validate LDIF data against format compliance rules.

                    Args:
                        ldif_data: LDIF data to validate
                        format_rules: Format compliance rules

                    Returns:
                        r[QualityValidation]: Format validation results or error

                    """
                    ...

                def check_data_completeness(
                    self,
                    data: Sequence[t.LdifData.LdifEntry],
                    completeness_config: t.LdifParsing.ValidationRules,
                ) -> p_meltano.Result[t.LdifProcessing.QualityValidation]:
                    """Check LDIF data completeness for DBT processing.

                    Args:
                        data: LDIF data to check
                        completeness_config: Completeness validation configuration

                    Returns:
                        r[QualityValidation]: Completeness check results or error

                    """
                    ...

                def detect_data_anomalies(
                    self,
                    data: Sequence[t.LdifData.LdifEntry],
                    anomaly_config: t.LdifParsing.ValidationRules,
                ) -> p_meltano.Result[Sequence[t.LdifData.LdifEntry]]:
                    """Detect anomalies in LDIF data for quality assurance.

                    Args:
                        data: LDIF data to analyze
                        anomaly_config: Anomaly detection configuration

                    Returns:
                        r[Sequence[LdifEntry]]: Detected anomalies or error

                    """
                    ...

                def generate_quality_report(
                    self,
                    quality_results: Sequence[t.LdifProcessing.QualityValidation],
                    report_config: t.LdifExport.ExportConfiguration,
                ) -> p_meltano.Result[t.JsonDict]:
                    """Generate data quality report for LDIF DBT processing.

                    Args:
                        quality_results: Quality validation results
                        report_config: Report generation configuration

                    Returns:
                        r[t.JsonDict]: Quality report or error

                    """
                    ...

            @runtime_checkable
            class PerformanceProtocol(p_ldif.Service[object], Protocol):
                """Protocol for DBT LDIF performance optimization operations.

                Uses types from t.LdifProcessing.
                NO imports of Models/Config per protocol rules.
                """

                def optimize_dbt_models(
                    self,
                    model_config: t.DbtLdifModel.LdifModelConfig,
                    performance_metrics: t.LdifProcessing.ProcessingMetrics,
                ) -> p_meltano.Result[t.JsonDict]:
                    """Optimize DBT models for LDIF data processing performance.

                    Args:
                        model_config: DBT model configuration
                        performance_metrics: Current performance metrics

                    Returns:
                        r[t.JsonDict]: Optimization recommendations or error

                    """
                    ...

                def cache_ldif_parsing(
                    self,
                    parsing_config: t.LdifParsing.ParserConfiguration,
                    cache_config: t.LdifProcessing.BatchProcessing,
                ) -> p_meltano.Result[bool]:
                    """Cache LDIF parsing operations for improved performance.

                    Args:
                        parsing_config: LDIF parsing configuration
                        cache_config: Caching configuration

                    Returns:
                        r[bool]: Caching setup success status

                    """
                    ...

                def monitor_dbt_performance(
                    self,
                    run_results: t.JsonDict,
                ) -> p_meltano.Result[t.LdifProcessing.ProcessingMetrics]:
                    """Monitor DBT performance with LDIF data processing.

                    Args:
                        run_results: DBT run results

                    Returns:
                        r[ProcessingMetrics]: Performance metrics or error

                    """
                    ...

                def optimize_ldif_parsing(
                    self,
                    parsing_config: t.LdifParsing.ParserConfiguration,
                ) -> p_meltano.Result[t.LdifProcessing.ProcessingMetrics]:
                    """Optimize LDIF parsing operations for DBT data processing.

                    Args:
                        parsing_config: LDIF parsing configuration

                    Returns:
                        r[ProcessingMetrics]: Parsing optimization results or error

                    """
                    ...

            @runtime_checkable
            class MonitoringProtocol(p_ldif.Service[object], Protocol):
                """Protocol for DBT LDIF monitoring operations.

                Uses types from t.LdifProcessing.
                NO imports of Models/Config per protocol rules.
                """

                def track_dbt_run_metrics(
                    self,
                    run_id: str,
                    metrics: t.LdifProcessing.ProcessingMetrics,
                ) -> p_meltano.Result[bool]:
                    """Track DBT run metrics for LDIF data processing.

                    Args:
                        run_id: DBT run identifier
                        metrics: Run metrics data

                    Returns:
                        r[bool]: Metric tracking success status

                    """
                    ...

                def monitor_ldif_data_freshness(
                    self,
                    freshness_config: t.LdifProcessing.BatchProcessing,
                ) -> p_meltano.Result[t.LdifProcessing.ProcessingMetrics]:
                    """Monitor LDIF data freshness for DBT processing.

                    Args:
                        freshness_config: Data freshness monitoring configuration

                    Returns:
                        r[ProcessingMetrics]: Data freshness status or error

                    """
                    ...

                def get_health_status(self) -> p_meltano.Result[t.JsonDict]:
                    """Get DBT LDIF integration health status.

                    Returns:
                        r[t.JsonDict]: Health status or error

                    """
                    ...

                def create_monitoring_dashboard(
                    self,
                    dashboard_config: t.LdifExport.ExportConfiguration,
                ) -> p_meltano.Result[t.JsonDict]:
                    """Create monitoring dashboard for DBT LDIF operations.

                    Args:
                        dashboard_config: Dashboard configuration

                    Returns:
                        r[t.JsonDict]: Dashboard creation result or error

                    """
                    ...


# Runtime alias for simplified usage
p = FlextDbtLdifProtocols

__all__: list[str] = [
    "FlextDbtLdifProtocols",
    "p",
]
