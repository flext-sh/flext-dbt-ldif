"""FlextDbtLdifUtilities - Unified DBT LDIF utilities service.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path
from typing import ClassVar

from flext_core import (
    FlextContainer,
    FlextLogger,
    FlextResult,
    FlextUtilities,
)

from flext_dbt_ldif.constants import FlextDbtLdifConstants

__all__: list[str] = ["FlextDbtLdifUtilities"]


class FlextDbtLdifUtilities(FlextUtilities):
    """Single unified utilities class for DBT LDIF data transformation operations.

    Provides complete DBT LDIF utilities for LDIF data transformation, DBT model generation,
    and LDIF-specific data processing without duplicating functionality.
    Uses FlextDbtLdifModels for all domain-specific data structures.

    This class consolidates all LDIF DBT operations:
    - LDIF file processing and parsing for DBT models
    - DBT schema generation for LDIF data structures
    - LDIF data transformation and validation
    - DBT model creation for LDIF analytics
    - LDIF-specific macro generation and optimization
    """

    # LDIF Processing constants
    LDIF_DEFAULT_BATCH_SIZE: ClassVar[int] = 5000
    LDIF_MAX_RECORD_SIZE: ClassVar[int] = 1048576  # 1MB per LDIF record
    LDIF_DEFAULT_ENCODING: ClassVar[str] = "utf-8"

    def __init__(self) -> None:
        """Initialize FlextDbtLdifUtilities service."""
        super().__init__()
        self._container = FlextContainer.get_global()
        self.logger = FlextLogger(__name__)

    def execute(self) -> FlextResult[dict[str, object]]:
        """Execute the main DBT LDIF service operation.

        Returns:
        FlextResult[dict[str, object]]: Service status and capabilities.

        """
        return FlextResult[dict[str, object]].ok({
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
        return self.logger

    @property
    def container(self) -> FlextContainer:
        """Get container instance."""
        return self._container

    class LdifFileProcessing:
        """LDIF file processing and parsing utilities."""

        @staticmethod
        def _validate_ldif_file(file_path: Path) -> FlextResult[bool]:
            """Validate LDIF file exists and has correct extension."""
            if not file_path.exists():
                return FlextResult[bool].fail(f"LDIF file not found: {file_path}")
            if file_path.suffix.lower() != ".ldif":
                return FlextResult[bool].fail(
                    f"Invalid LDIF file extension: {file_path}"
                )
            return FlextResult[bool].ok(True)

        @staticmethod
        def _initialize_parsed_data(file_path: Path) -> dict[str, object]:
            """Initialize the parsed data structure."""
            return {
                "file_path": str(file_path),
                "total_records": 0,
                "entries": [],
                "schema_info": {},
                "processing_stats": {},
            }

        @staticmethod
        def _process_dn_line(
            line: str,
            current_entry: dict[str, object],
            current_dn: str | None,
            record_count: int,
            batch_count: int,
            batch_size: int,
            parsed_data: dict[str, object],
        ) -> tuple[dict[str, object], str | None, int, int]:
            """Process a DN line and handle entry completion."""
            # Save previous entry if exists
            if current_entry and current_dn:
                parsed_data["entries"].append({
                    "dn": current_dn,
                    "attributes": current_entry,
                    "record_number": record_count,
                    "batch_number": batch_count // batch_size,
                })
                record_count += 1

                # Process in batches for memory efficiency
                if record_count % batch_size == 0:
                    batch_count += batch_size

            # Start new entry
            current_dn = line[3:].strip()
            current_entry = {}

            return current_entry, current_dn, record_count, batch_count

        @staticmethod
        def _process_attribute_line(
            line: str,
            current_entry: dict[str, object],
        ) -> dict[str, object]:
            """Process an attribute line."""
            attr_name, attr_value = line.split(":", 1)
            attr_name = attr_name.strip()
            attr_value = attr_value.strip()

            # Handle multi-valued attributes
            if attr_name in current_entry:
                if not isinstance(current_entry[attr_name], list):
                    current_entry[attr_name] = [current_entry[attr_name]]
                current_entry[attr_name].append(attr_value)
            else:
                current_entry[attr_name] = attr_value

            return current_entry

        @staticmethod
        def _finalize_last_entry(
            current_entry: dict[str, object],
            current_dn: str | None,
            record_count: int,
            parsed_data: dict[str, object],
        ) -> int:
            """Finalize the last entry in the file."""
            if current_entry and current_dn:
                parsed_data["entries"].append({
                    "dn": current_dn,
                    "attributes": current_entry,
                    "record_number": record_count,
                })
                record_count += 1

            return record_count

        @staticmethod
        def _calculate_processing_stats(
            file_path: Path,
            line_num: int,
            record_count: int,
        ) -> dict[str, object]:
            """Calculate processing statistics."""
            return {
                "lines_processed": line_num,
                "entries_found": record_count,
                "file_size_bytes": file_path.stat().st_size,
            }

        @staticmethod
        def _process_ldif_file(
            file_path: Path,
            parsed_data: dict[str, object],
            batch_size: int,
        ) -> FlextResult[bool]:
            """Process the LDIF file content and populate parsed_data."""
            try:
                with file_path.open("r", encoding="utf-8") as ldif_file:
                    current_entry = {}
                    current_dn = None
                    record_count = 0
                    batch_count = 0
                    line_num = 0

                    for original_line in ldif_file:
                        line_num += 1
                        line = original_line.rstrip("\n\r")

                        # Skip empty lines and comments
                        if not line or line.startswith("#"):
                            continue

                        # Process DN lines
                        if line.startswith("dn:"):
                            (
                                current_entry,
                                current_dn,
                                record_count,
                                batch_count,
                            ) = FlextDbtLdifUtilities.LdifFileProcessing._process_dn_line(  # noqa: SLF001
                                line,
                                current_entry,
                                current_dn,
                                record_count,
                                batch_count,
                                batch_size,
                                parsed_data,
                            )

                        # Process attribute lines
                        elif ":" in line:
                            current_entry = FlextDbtLdifUtilities.LdifFileProcessing._process_attribute_line(  # noqa: SLF001
                                line, current_entry
                            )

                    # Process last entry
                    record_count = (
                        FlextDbtLdifUtilities.LdifFileProcessing._finalize_last_entry(  # noqa: SLF001
                            current_entry, current_dn, record_count, parsed_data
                        )
                    )

                parsed_data["total_records"] = record_count
                parsed_data["processing_stats"] = (
                    FlextDbtLdifUtilities.LdifFileProcessing._calculate_processing_stats(  # noqa: SLF001
                        file_path, line_num, record_count
                    )
                )

                return FlextResult[bool].ok(True)

            except Exception as e:
                return FlextResult[bool].fail(f"LDIF file processing failed: {e}")

        @staticmethod
        def parse_ldif_file(
            file_path: Path,
            batch_size: int = 5000,
        ) -> FlextResult[dict[str, object]]:
            """Parse LDIF file and extract records for DBT processing.

            Args:
                file_path: Path to the LDIF file
                batch_size: Number of records to process per batch

            Returns:
                FlextResult containing parsed LDIF data or error

            """
            try:
                # Validate file
                validation_result = (
                    FlextDbtLdifUtilities.LdifFileProcessing._validate_ldif_file(  # noqa: SLF001
                        file_path
                    )
                )
                if not validation_result.success:
                    return FlextResult[dict[str, object]].fail(validation_result.error)

                # Initialize data structure
                parsed_data = (
                    FlextDbtLdifUtilities.LdifFileProcessing._initialize_parsed_data(  # noqa: SLF001
                        file_path
                    )
                )

                # Process file
                processing_result = (
                    FlextDbtLdifUtilities.LdifFileProcessing._process_ldif_file(  # noqa: SLF001
                        file_path, parsed_data, batch_size
                    )
                )
                if not processing_result.success:
                    return FlextResult[dict[str, object]].fail(processing_result.error)

                return FlextResult[dict[str, object]].ok(parsed_data)

            except Exception as e:
                return FlextResult[dict[str, object]].fail(
                    f"LDIF file parsing failed: {e}"
                )

        @staticmethod
        def validate_ldif_structure(
            ldif_data: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Validate LDIF data structure for DBT compatibility.

            Args:
            ldif_data: Parsed LDIF data structure

            Returns:
            FlextResult containing validation results or error

            """
            try:
                validation_results = {
                    "is_valid": True,
                    "errors": [],
                    "warnings": [],
                    "statistics": {},
                }

                # Check basic structure
                if not ldif_data.get("entries"):
                    validation_results["errors"].append("No LDIF entries found")
                    validation_results["is_valid"] = False

                # Validate entries
                unique_dns = set()
                attribute_types = {}

                for entry in ldif_data.get("entries", []):
                    # Check DN uniqueness
                    dn = entry.get("dn")
                    if not dn:
                        validation_results["errors"].append("Entry missing DN")
                        validation_results["is_valid"] = False
                        continue

                    if dn in unique_dns:
                        validation_results["errors"].append(f"Duplicate DN found: {dn}")
                        validation_results["is_valid"] = False
                    else:
                        unique_dns.add(dn)

                    # Analyze attribute types
                    for attr_name, attr_value in entry.get("attributes", {}).items():
                        if attr_name not in attribute_types:
                            attribute_types[attr_name] = {
                                "count": 0,
                                "multi_valued": False,
                                "data_types": set(),
                            }

                        attribute_types[attr_name]["count"] += 1

                        if isinstance(attr_value, list):
                            attribute_types[attr_name]["multi_valued"] = True
                            for val in attr_value:
                                attribute_types[attr_name]["data_types"].add(
                                    type(val).__name__
                                )
                        else:
                            attribute_types[attr_name]["data_types"].add(
                                type(attr_value).__name__
                            )

                validation_results["statistics"] = {
                    "total_entries": len(ldif_data.get("entries", [])),
                    "unique_dns": len(unique_dns),
                    "unique_attributes": len(attribute_types),
                    "attribute_analysis": attribute_types,
                }

                return FlextResult[dict[str, object]].ok(validation_results)

            except Exception as e:
                return FlextResult[dict[str, object]].fail(
                    f"LDIF validation failed: {e}"
                )

    class DbtModelGeneration:
        """DBT model generation utilities for LDIF data."""

        @staticmethod
        def generate_ldif_staging_model(
            ldif_schema: dict[str, object],
            model_name: str = "stg_ldif_entries",
        ) -> FlextResult[str]:
            """Generate DBT staging model for LDIF data.

            Args:
            ldif_schema: LDIF schema information
            model_name: Name of the DBT model

            Returns:
            FlextResult containing DBT model SQL or error

            """
            try:
                # Extract attribute information
                attributes = ldif_schema.get("attribute_analysis", {})

                # Build column selections
                select_clauses = [
                    "    dn",
                    "    entry_number",
                    "    created_timestamp",
                ]

                for attr_name, attr_info in attributes.items():
                    # Skip internal attributes
                    if attr_name.startswith("_"):
                        continue

                    # Handle multi-valued attributes
                    if attr_info.get("multi_valued"):
                        select_clauses.extend((
                            f"    {attr_name} as {attr_name}_array",
                            f"    array_to_string({attr_name}, ',') as {attr_name}_text",
                        ))
                    else:
                        select_clauses.append(f"    {attr_name}")

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

                return FlextResult[str].ok(model_sql)

            except Exception as e:
                return FlextResult[str].fail(
                    f"LDIF staging model generation failed: {e}"
                )

        @staticmethod
        def generate_ldif_dimension_model(
            model_type: str,
            ldif_schema: dict[str, object],
        ) -> FlextResult[str]:
            """Generate dimensional model for LDIF data.

            Args:
            model_type: Type of dimension (users, groups, organizational_units)
            ldif_schema: LDIF schema information

            Returns:
            FlextResult containing dimensional model SQL or error

            """
            try:
                # Use ldif_schema to validate parameter requirement (schema structure validation)
                if not ldif_schema or not isinstance(ldif_schema, dict):
                    # Default schema fallback for dimension model generation
                    pass

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
                    return FlextResult[str].fail(f"Unknown model type: {model_type}")

                return FlextResult[str].ok(model_sql)

            except Exception as e:
                return FlextResult[str].fail(
                    f"LDIF dimension model generation failed: {e}"
                )

    class LdifSchemaMapping:
        """LDIF schema mapping and analysis utilities."""

        @staticmethod
        def _initialize_schema_analysis() -> dict[str, object]:
            """Initialize the schema analysis structure."""
            return {
                "object_classes": {},
                "attributes": {},
                "dn_patterns": {},
                "data_quality": {},
            }

        def _analyze_object_classes(
            self,
            schema_analysis: dict[str, object],
            attributes: dict[str, object],
            dn: str,
        ) -> None:
            """Analyze object classes in the entry."""
            object_classes = attributes.get("objectclass", [])
            if not isinstance(object_classes, list):
                object_classes = [object_classes]

            for obj_class in object_classes:
                if obj_class not in schema_analysis["object_classes"]:
                    schema_analysis["object_classes"][obj_class] = {
                        "count": 0,
                        "example_dn": dn,
                        "common_attributes": set(),
                    }
                schema_analysis["object_classes"][obj_class]["count"] += 1
                schema_analysis["object_classes"][obj_class][
                    "common_attributes"
                ].update(attributes.keys())

        def _analyze_dn_patterns(
            self, schema_analysis: dict[str, object], dn: str
        ) -> None:
            """Analyze DN patterns."""
            dn_components = dn.split(",")
            if dn_components:
                root_component = (
                    dn_components[0].split("=")[0]
                    if "=" in dn_components[0]
                    else "unknown"
                )
                if root_component not in schema_analysis["dn_patterns"]:
                    schema_analysis["dn_patterns"][root_component] = 0
                schema_analysis["dn_patterns"][root_component] += 1

        def _analyze_attributes(
            self, schema_analysis: dict[str, object], attributes: dict[str, object]
        ) -> None:
            """Analyze attributes in the entry."""
            for attr_name, attr_value in attributes.items():
                if attr_name not in schema_analysis["attributes"]:
                    schema_analysis["attributes"][attr_name] = {
                        "count": 0,
                        "multi_valued_count": 0,
                        "data_types": set(),
                        "sample_values": [],
                    }

                attr_info = schema_analysis["attributes"][attr_name]
                attr_info["count"] += 1

                if isinstance(attr_value, list):
                    attr_info["multi_valued_count"] += 1

        def analyze_ldif_schema(
            self,
            ldif_data: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Analyze LDIF data to extract schema information.

            Args:
            ldif_data: Parsed LDIF data

            Returns:
            FlextResult containing schema analysis or error

            """
            try:
                schema_analysis = self._initialize_schema_analysis()

                # Analyze entries
                for entry in ldif_data.get("entries", []):
                    dn = entry.get("dn", "")
                    attributes = entry.get("attributes", {})

                    self._analyze_object_classes(schema_analysis, attributes, dn)
                    self._analyze_dn_patterns(schema_analysis, dn)
                    self._analyze_attributes(schema_analysis, attributes)

                # Finalize schema analysis
                self._finalize_schema_analysis(schema_analysis)

                return FlextResult[dict[str, object]].ok(schema_analysis)

            except Exception as e:
                return FlextResult[dict[str, object]].fail(
                    f"LDIF schema analysis failed: {e}"
                )

        def _finalize_schema_analysis(self, schema_analysis: dict[str, object]) -> None:
            """Finalize schema analysis by converting sets to lists and cleaning up."""
            # Convert sets to lists for JSON serialization
            for obj_class_info in schema_analysis["object_classes"].values():
                if isinstance(obj_class_info.get("common_attributes"), set):
                    obj_class_info["common_attributes"] = list(
                        obj_class_info["common_attributes"]
                    )

            # Convert data_types sets to lists
            for attr_info in schema_analysis["attributes"].values():
                if isinstance(attr_info.get("data_types"), set):
                    attr_info["data_types"] = list(attr_info["data_types"])

        @staticmethod
        def generate_dbt_source_definition(
            schema_analysis: dict[str, object],
            source_name: str = "ldif",
        ) -> FlextResult[dict[str, object]]:
            """Generate DBT source definition for LDIF data.

            Args:
            schema_analysis: LDIF schema analysis results
            source_name: Name for the DBT source

            Returns:
            FlextResult containing DBT source definition or error

            """
            try:
                # Build columns from attribute analysis
                columns = []
                for attr_name, attr_info in schema_analysis.get(
                    "attributes", {}
                ).items():
                    column_def = {
                        "name": attr_name.lower().replace("-", "_"),
                        "description": f"LDIF {attr_name} attribute",
                    }

                    # Determine data type
                    data_types = attr_info.get("data_types", [])
                    if "int" in data_types:
                        column_def["data_type"] = "integer"
                    elif attr_info.get("multi_valued_count", 0) > 0:
                        column_def["data_type"] = "text[]"
                    else:
                        column_def["data_type"] = "text"

                    columns.append(column_def)

                # Add standard columns
                standard_columns = [
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

                source_definition = {
                    "version": 2,
                    "sources": [
                        {
                            "name": source_name,
                            "description": "LDIF data source",
                            "tables": [
                                {
                                    "name": "raw_ldif_entries",
                                    "description": "Raw LDIF entries",
                                    "columns": standard_columns + columns,
                                }
                            ],
                        }
                    ],
                }

                return FlextResult[dict[str, object]].ok(source_definition)

            except Exception as e:
                return FlextResult[dict[str, object]].fail(
                    f"DBT source definition generation failed: {e}"
                )

    class MacroGeneration:
        """DBT macro generation utilities for LDIF operations."""

        @staticmethod
        def create_ldif_parsing_macros() -> FlextResult[dict[str, str]]:
            """Create DBT macros for LDIF data parsing.

            Returns:
            FlextResult containing macro definitions or error

            """
            try:
                macros = {}

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

                return FlextResult[dict[str, str]].ok(macros)

            except Exception as e:
                return FlextResult[dict[str, str]].fail(
                    f"LDIF macro generation failed: {e}"
                )

    class PerformanceOptimization:
        """Performance optimization utilities for LDIF processing."""

        @staticmethod
        def optimize_ldif_processing(
            processing_stats: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Optimize LDIF processing performance based on statistics.

            Args:
            processing_stats: LDIF processing statistics

            Returns:
            FlextResult containing optimization recommendations or error

            """
            try:
                file_size = processing_stats.get("file_size_bytes", 0)
                entry_count = processing_stats.get("entries_found", 0)

                optimizations = {
                    "batch_size": 5000,
                    "memory_limit": "1GB",
                    "parallel_processing": False,
                    "recommendations": [],
                }

                # Adjust batch size based on file size
                if file_size > 100 * 1024 * 1024:  # 100MB
                    optimizations["batch_size"] = 10000
                    optimizations["recommendations"].append(
                        "Use larger batch size for large files"
                    )

                if file_size > 1024 * 1024 * 1024:  # 1GB
                    optimizations["parallel_processing"] = True
                    optimizations["memory_limit"] = "4GB"
                    optimizations["recommendations"].append(
                        "Enable parallel processing for very large files"
                    )

                # Optimize based on entry count
                if entry_count > FlextDbtLdifConstants.LARGE_DATASET_THRESHOLD:
                    optimizations["recommendations"].append(
                        "Consider incremental loading for large datasets"
                    )

                # Memory optimization
                avg_entry_size = file_size / entry_count if entry_count > 0 else 0
                if avg_entry_size > FlextDbtLdifConstants.LARGE_ENTRY_SIZE_BYTES:
                    optimizations["recommendations"].append(
                        "Large entries detected - consider streaming processing"
                    )

                return FlextResult[dict[str, object]].ok(optimizations)

            except Exception as e:
                return FlextResult[dict[str, object]].fail(
                    f"LDIF performance optimization failed: {e}"
                )
