"""FlextDbtLdifUtilities - Unified DBT LDIF utilities service.

This module provides DBT LDIF utilities using flext-ldif APIs directly.
Uses types from typings.py and t, no dict[str, object].
Uses Python 3.13+ PEP 695 syntax and direct API calls.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import ClassVar

from flext_core import (
    FlextContainer,
    FlextLogger,
    r,
    u,
)
from flext_ldif import FlextLdif, FlextLdifModels

from flext_dbt_ldif.constants import FlextDbtLdifConstants
from flext_dbt_ldif.models import ColumnDefinition
from flext_dbt_ldif.typings import t

__all__: list[str] = ["FlextDbtLdifUtilities"]


class FlextDbtLdifUtilities(u):
    """Single unified utilities class for DBT LDIF data transformation operations.

    Provides complete DBT LDIF utilities for LDIF data transformation, DBT model generation,
    and LDIF-specific data processing without duplicating functionality.
    Uses flext-ldif APIs directly - no wrappers or manual parsing.

    This class consolidates all LDIF DBT operations:
    - LDIF file processing using flext-ldif.parse() directly
    - DBT schema generation for LDIF data structures
    - LDIF data transformation and validation using flext-ldif APIs
    - DBT model creation for LDIF analytics
    - LDIF-specific macro generation and optimization
    """

    # LDIF Processing constants (reusing from constants.py)
    LDIF_DEFAULT_BATCH_SIZE: ClassVar[int] = FlextDbtLdifConstants.DEFAULT_BATCH_SIZE
    LDIF_MAX_RECORD_SIZE: ClassVar[int] = FlextDbtLdifConstants.MAX_FILE_SIZE_GB
    LDIF_DEFAULT_ENCODING: ClassVar[str] = FlextDbtLdifConstants.DEFAULT_LDIF_ENCODING

    def __init__(self) -> None:
        """Initialize FlextDbtLdifUtilities service."""
        super().__init__()
        self._container = FlextContainer.get_global()
        self._logger = FlextLogger(__name__)
        self._ldif_api = FlextLdif()

    def execute(self) -> r[t.JsonDict]:
        """Execute the main DBT LDIF service operation.

        Returns:
            r[t.JsonDict]: Service status and capabilities

        """
        return r[t.JsonDict].ok({
            "status": "operational",
            "service": "flext-dbt-ldif-utilities",
            "capabilities": [
                "ldif_file_processing",
                "dbt_model_generation",
                "ldif_schema_mapping",
                "data_transformation",
                "macro_generation",
                "performance_optimization",
            ],
        })

    @property
    def logger(self) -> FlextLogger:
        """Get logger instance."""
        return self._logger

    @property
    def container(self) -> FlextContainer:
        """Get container instance."""
        return self._container

    class LdifFileProcessing:
        """LDIF file processing using flext-ldif APIs directly."""

        @staticmethod
        def parse_ldif_file(
            file_path: Path,
            encoding: str = FlextDbtLdifConstants.DEFAULT_LDIF_ENCODING,
        ) -> r[Sequence[FlextLdifModels.Entry]]:
            """Parse LDIF file using flext-ldif API directly.

            Args:
                file_path: Path to the LDIF file
                encoding: File encoding (defaults to UTF-8)

            Returns:
                r[Sequence[FlextLdifModels.Entry]]: Parsed LDIF entries or error

            """
            try:
                # Validate file exists
                if not file_path.exists():
                    return r[Sequence[FlextLdifModels.Entry]].fail(
                        f"LDIF file not found: {file_path}",
                    )

                # Validate extension
                if file_path.suffix.lower() != ".ldif":
                    return r[Sequence[FlextLdifModels.Entry]].fail(
                        f"Invalid LDIF file extension: {file_path}",
                    )

                # Use flext-ldif API directly - NO manual parsing
                ldif_api = FlextLdif()
                parse_result = ldif_api.parse(file_path, encoding=encoding)

                if not parse_result.success:
                    return r[Sequence[FlextLdifModels.Entry]].fail(
                        parse_result.error or "LDIF parsing failed",
                    )

                return r[Sequence[FlextLdifModels.Entry]].ok(
                    parse_result.value or [],
                )

            except Exception as e:
                return r[Sequence[FlextLdifModels.Entry]].fail(
                    f"LDIF file parsing failed: {e}",
                )

        @staticmethod
        def validate_ldif_structure(
            entries: Sequence[FlextLdifModels.Entry],
        ) -> r[t.LdifProcessing.QualityValidation]:
            """Validate LDIF entries structure for DBT compatibility.

            Args:
                entries: Sequence of FlextLdifModels.Entry objects

            Returns:
                r[QualityValidation]: Validation results or error

            """
            try:
                validation_results: t.LdifProcessing.QualityValidation = {
                    "is_valid": True,
                    "errors": [],
                    "warnings": [],
                    "statistics": {
                        "total_entries": len(entries),
                        "valid_entries": 0,
                        "unique_dns": 0,
                    },
                }

                # Check basic structure
                if not entries:
                    validation_results["errors"].append("No LDIF entries found")
                    validation_results["is_valid"] = False
                    return r[t.LdifProcessing.QualityValidation].ok(validation_results)

                # Validate entries using flext-ldif validation
                unique_dns: set[str] = set()
                valid_count = 0

                for entry in entries:
                    # Check DN uniqueness
                    dn = entry.dn.value
                    if dn in unique_dns:
                        validation_results["errors"].append(f"Duplicate DN found: {dn}")
                        validation_results["is_valid"] = False
                    else:
                        unique_dns.add(dn)

                    # Use flext-ldif validation
                    validation_result = entry.validate_business_rules()
                    if validation_result.success:
                        valid_count += 1

                validation_results["statistics"]["valid_entries"] = valid_count
                validation_results["statistics"]["unique_dns"] = len(unique_dns)

                return r[t.LdifProcessing.QualityValidation].ok(validation_results)

            except Exception as e:
                return r[t.LdifProcessing.QualityValidation].fail(
                    f"LDIF validation failed: {e}"
                )

    class DbtModelGeneration:
        """DBT model generation utilities for LDIF data.

        Uses flext-ldif Entry objects directly - no dict conversions.
        """

        @staticmethod
        def generate_ldif_staging_model(
            entries: Sequence[FlextLdifModels.Entry],
            model_name: str = "stg_ldif_entries",
        ) -> r[str]:
            """Generate DBT staging model for LDIF data.

            Args:
                entries: Sequence of FlextLdifModels.Entry objects
                model_name: Name of the DBT model

            Returns:
                r[str]: DBT model SQL or error

            """
            try:
                # Extract attribute names from entries
                attribute_names: set[str] = set()
                for entry in entries:
                    attribute_names.update(entry.attributes.keys())

                # Build column selections
                select_clauses = [
                    "    dn",
                    "    entry_number",
                    "    created_timestamp",
                ]

                for attr_name in sorted(attribute_names):
                    # Skip internal attributes
                    if attr_name.startswith("_"):
                        continue

                    # Check if multi-valued (using flext-ldif Entry methods)
                    # For now, assume all can be multi-valued
                    select_clauses.extend((
                        f"    {attr_name} as {attr_name}_array",
                        f"    array_to_string({attr_name}, ',') as {attr_name}_text",
                    ))

                # Use model_name in description (DBT template - safe SQL generation)
                # Note: This is a template string for DBT, not executable SQL
                # The f-string interpolation is safe as it's used for DBT templating
                model_sql = f"""{{{{
 config(
 materialized='view',
 tags=['ldif', 'staging'],
 description='Staging model for LDIF entries: {model_name}'
 )
}}}}

select
{chr(10).join(select_clauses)}
from {{{{ source('ldif', 'raw_ldif_entries') }}}}
where dn is not null
"""

                return r[str].ok(model_sql)

            except Exception as e:
                return r[str].fail(
                    f"LDIF staging model generation failed: {e}",
                )

        @staticmethod
        def generate_ldif_dimension_model(
            model_type: FlextDbtLdifConstants.DbtTargetLiteral,
            _entries: Sequence[FlextLdifModels.Entry] | None = None,
        ) -> r[str]:
            """Generate dimensional model for LDIF data.

            Args:
                model_type: Type of dimension (users, groups, organizational_units)
                _entries: Optional entries for future validation (currently unused)

            Returns:
                r[str]: Dimensional model SQL or error

            """
            try:
                if model_type == "users":
                    model_sql = """{{
 config(
 materialized='table',
 tags=['ldif', 'dimension', 'users'],
 description='User dimension from LDIF data'
 )
}}}}

select
 {{ dbt_utils.surrogate_key(['dn']) }} as user_sk,
 dn as user_dn,
 coalesce(cn, uid, samaccountname) as username,
 givenname as first_name,
 sn as last_name,
 mail as email,
 telephonenumber as phone,
 title as job_title,
 department,
 manager,
 case
 when useraccountcontrol is not null then
 case when useraccountcontrol::int & 2 = 0 then true else false end
 else true
 end as is_active,
 created_timestamp,
 current_timestamp as updated_timestamp
from {{ ref('stg_ldif_entries') }}
where array_to_string(objectclass_array, ',') ilike '%person%'
 or array_to_string(objectclass_array, ',') ilike '%user%'
"""

                elif model_type == "groups":
                    model_sql = """{{
 config(
 materialized='table',
 tags=['ldif', 'dimension', 'groups'],
 description='Group dimension from LDIF data'
 )
}}}}

select
 {{ dbt_utils.surrogate_key(['dn']) }} as group_sk,
 dn as group_dn,
 cn as group_name,
 description as group_description,
 case
 when array_to_string(objectclass_array, ',') ilike '%security%' then 'security'
 when array_to_string(objectclass_array, ',') ilike '%distribution%' then 'distribution'
 else 'other'
 end as group_type,
 member_array as members,
 created_timestamp,
 current_timestamp as updated_timestamp
from {{ ref('stg_ldif_entries') }}
where array_to_string(objectclass_array, ',') ilike '%group%'
"""

                elif model_type == "organizational_units":
                    model_sql = """{{
 config(
 materialized='table',
 tags=['ldif', 'dimension', 'organizational_units'],
 description='Organizational Unit dimension from LDIF data'
 )
}}}}

select
 {{ dbt_utils.surrogate_key(['dn']) }} as ou_sk,
 dn as ou_dn,
 ou as ou_name,
 description as ou_description,
 street as address,
 l as city,
 st as state,
 postalcode as postal_code,
 c as country,
 created_timestamp,
 current_timestamp as updated_timestamp
from {{ ref('stg_ldif_entries') }}
where array_to_string(objectclass_array, ',') ilike '%organizationalunit%'
"""

                else:
                    return r[str].fail(f"Unknown model type: {model_type}")

                return r[str].ok(model_sql)

            except Exception as e:
                return r[str].fail(
                    f"LDIF dimension model generation failed: {e}",
                )

    class LdifSchemaMapping:
        """LDIF schema mapping and analysis utilities.

        Uses flext-ldif Entry objects directly - no dict conversions.
        """

        @staticmethod
        def analyze_ldif_schema(
            entries: Sequence[FlextLdifModels.Entry],
        ) -> r[t.LdifParsing.ParsedData]:
            """Analyze LDIF entries to extract schema information.

            Args:
                entries: Sequence of FlextLdifModels.Entry objects

            Returns:
                r[ParsedData]: Schema analysis or error

            """
            try:
                schema_analysis: t.LdifParsing.ParsedData = {
                    "object_classes": {},
                    "attributes": {},
                    "dn_patterns": {},
                    "data_quality": {},
                }

                # Analyze entries using flext-ldif Entry objects
                for entry in entries:
                    dn = entry.dn.value
                    attributes = entry.attributes

                    # Analyze object classes
                    object_classes = entry.get_object_classes()
                    for obj_class in object_classes:
                        if obj_class not in schema_analysis["object_classes"]:
                            schema_analysis["object_classes"][obj_class] = {
                                "count": 0,
                                "example_dn": dn,
                                "common_attributes": [],
                            }
                        schema_analysis["object_classes"][obj_class]["count"] += 1
                        schema_analysis["object_classes"][obj_class][
                            "common_attributes"
                        ].extend(list(attributes.keys()))

                    # Analyze DN patterns
                    dn_components = dn.split(",")
                    if dn_components:
                        root_component = (
                            dn_components[0].split("=")[0]
                            if "=" in dn_components[0]
                            else "unknown"
                        )
                        schema_analysis["dn_patterns"][root_component] = (
                            schema_analysis["dn_patterns"].get(root_component, 0) + 1
                        )

                    # Analyze attributes
                    for attr_name, attr_value in attributes.items():
                        if attr_name not in schema_analysis["attributes"]:
                            schema_analysis["attributes"][attr_name] = {
                                "count": 0,
                                "multi_valued_count": 0,
                                "data_types": [],
                                "sample_values": [],
                            }

                        attr_info = schema_analysis["attributes"][attr_name]
                        attr_info["count"] += 1

                        if isinstance(attr_value, list):
                            attr_info["multi_valued_count"] += 1

                return r[t.LdifParsing.ParsedData].ok(
                    schema_analysis,
                )

            except Exception as e:
                return r[t.LdifParsing.ParsedData].fail(
                    f"LDIF schema analysis failed: {e}",
                )

        @staticmethod
        def generate_dbt_source_definition(
            entries: Sequence[FlextLdifModels.Entry],
            source_name: str = "ldif",
        ) -> r[t.JsonDict]:
            """Generate DBT source definition for LDIF data.

            Args:
                entries: Sequence of FlextLdifModels.Entry objects
                source_name: Name for the DBT source

            Returns:
                r[t.JsonDict]: DBT source definition or error

            """
            try:
                # Analyze schema first
                schema_result = (
                    FlextDbtLdifUtilities.LdifSchemaMapping.analyze_ldif_schema(entries)
                )
                if not schema_result.success:
                    return r[t.JsonDict].fail(schema_result.error)

                schema_analysis = schema_result.value

                # Build columns from attribute analysis
                columns: list[ColumnDefinition] = []
                for attr_name, attr_info in schema_analysis.get(
                    "attributes",
                    {},
                ).items():
                    column_def: ColumnDefinition = {
                        "name": attr_name.lower().replace("-", "_"),
                        "description": f"LDIF {attr_name} attribute",
                    }

                    # Determine data type
                    data_types = attr_info.get("data_types", [])
                    if "int" in str(data_types):
                        column_def["data_type"] = "integer"
                    elif attr_info.get("multi_valued_count", 0) > 0:
                        column_def["data_type"] = "text[]"
                    else:
                        column_def["data_type"] = "text"

                    columns.append(column_def)

                # Add standard columns
                standard_columns: list[ColumnDefinition] = [
                    {
                        "name": "dn",
                        "description": "Distinguished Name",
                        "data_type": "text",
                    },
                    {
                        "name": "entry_number",
                        "description": "Entry sequence number",
                        "data_type": "integer",
                    },
                    {
                        "name": "created_timestamp",
                        "description": "Entry creation timestamp",
                        "data_type": "timestamp",
                    },
                ]

                source_definition: t.JsonDict = {
                    "version": 2,
                    "sources": [
                        {
                            "name": source_name,
                            "description": "LDIF data source",
                            "tables": [
                                {
                                    "name": "raw_ldif_entries",
                                    "description": "Raw LDIF entries",
                                    "columns": [
                                        {
                                            "name": col["name"],
                                            "description": col["description"],
                                            "data_type": col["data_type"],
                                        }
                                        for col in standard_columns + columns
                                    ],
                                },
                            ],
                        },
                    ],
                }

                return r[t.JsonDict].ok(source_definition)

            except Exception as e:
                return r[t.JsonDict].fail(
                    f"DBT source definition generation failed: {e}",
                )

    class MacroGeneration:
        """DBT macro generation utilities for LDIF operations."""

        @staticmethod
        def create_ldif_parsing_macros() -> r[Mapping[str, str]]:
            """Create DBT macros for LDIF data parsing.

            Returns:
                r[Mapping[str, str]]: Macro definitions or error

            """
            try:
                macros: dict[str, str] = {}

                # DN parsing macro
                macros["parse_ldif_dn"] = """-- Parse LDIF Distinguished Name components
{% macro parse_ldif_dn(dn_column, component='cn') %}
    case
        when {{ dn_column }} is null then null
        when position('{{ component }}=' in lower({{ dn_column }})) = 0 then null
        else trim(both '"' from
            split_part(
                split_part(
                    lower({{ dn_column }}),
                    '{{ component }}=',
                    2
                ),
                ',',
                1
            )
        )
    end
{% endmacro %}"""

                # Multi-valued attribute extraction
                macros[
                    "extract_ldif_multivalue"
                ] = """-- Extract first value from LDIF multi-valued attribute
{% macro extract_ldif_multivalue(column_name, index=1) %}
 case
 when {{ column_name }} is null then null
 when array_length({{ column_name }}, 1) is null then {{ column_name }}
 when array_length({{ column_name }}, 1) >= {{ index }} then {{ column_name }}[{{ index }}]
 else null
 end
{% endmacro %}"""

                # LDIF timestamp normalization
                macros[
                    "normalize_ldif_timestamp"
                ] = """-- Normalize LDIF timestamp to standard format
{% macro normalize_ldif_timestamp(timestamp_column) %}
 case
 when {{ timestamp_column }} is null then null
 when length({{ timestamp_column }}) = 14 then
 -- LDIF GeneralizedTime format: YYYYMMDDHHMMSSZ
 to_timestamp(
 substring({{ timestamp_column }} from 1 for 14),
 'YYYYMMDDHH24MISS'
 )
 else
 -- Try standard timestamp parsing
 try_cast({{ timestamp_column }} as timestamp)
 end
{% endmacro %}"""

                return r[Mapping[str, str]].ok(macros)

            except Exception as e:
                return r[Mapping[str, str]].fail(
                    f"LDIF macro generation failed: {e}",
                )

    class PerformanceOptimization:
        """Performance optimization utilities for LDIF processing."""

        @staticmethod
        def optimize_ldif_processing(
            entries: Sequence[FlextLdifModels.Entry],
            file_path: Path | None = None,
        ) -> r[t.LdifProcessing.BatchProcessing]:
            """Optimize LDIF processing performance based on entry count and file size.

            Args:
                entries: Sequence of FlextLdifModels.Entry objects
                file_path: Optional file path for size calculation

            Returns:
                r[BatchProcessing]: Optimization recommendations or error

            """
            try:
                entry_count = len(entries)
                file_size = (
                    file_path.stat().st_size if file_path and file_path.exists() else 0
                )

                optimizations: t.LdifProcessing.BatchProcessing = {
                    "batch_size": FlextDbtLdifConstants.DEFAULT_BATCH_SIZE,
                    "memory_limit": "1GB",
                    "parallel_processing": False,
                    "recommendations": [],
                }

                # Adjust batch size based on file size
                if file_size > 100 * 1024 * 1024:  # 100MB
                    optimizations["batch_size"] = 10000
                    optimizations["recommendations"].append(
                        "Use larger batch size for large files",
                    )

                if file_size > 1024 * 1024 * 1024:  # 1GB
                    optimizations["parallel_processing"] = True
                    optimizations["memory_limit"] = "4GB"
                    optimizations["recommendations"].append(
                        "Enable parallel processing for very large files",
                    )

                # Optimize based on entry count
                if entry_count > FlextDbtLdifConstants.LARGE_DATASET_THRESHOLD:
                    optimizations["recommendations"].append(
                        "Consider incremental loading for large datasets",
                    )

                # Memory optimization
                avg_entry_size = file_size / entry_count if entry_count > 0 else 0
                if avg_entry_size > FlextDbtLdifConstants.LARGE_ENTRY_SIZE_BYTES:
                    optimizations["recommendations"].append(
                        "Large entries detected - consider streaming processing",
                    )

                return r[t.LdifProcessing.BatchProcessing].ok(
                    optimizations,
                )

            except Exception as e:
                return r[t.LdifProcessing.BatchProcessing].fail(
                    f"LDIF performance optimization failed: {e}"
                )
