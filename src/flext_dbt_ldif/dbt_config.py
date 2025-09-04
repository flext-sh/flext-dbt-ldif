"""DBT configuration for LDIF transformations.

Provides configuration management for DBT LDIF projects using flext-core patterns.
Integrates with flext-ldif for data processing and flext-meltano for DBT execution.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Any, ClassVar

from flext_core import FlextConfig, FlextLogger, FlextResult
from flext_ldif import FlextLDIFConfig
from flext_meltano.config import FlextMeltanoConfig

logger = FlextLogger(__name__)


class FlextDbtLdifConfig(FlextConfig):
    """Configuration for DBT LDIF transformations.

    Combines LDIF processing settings with DBT execution configuration.
    Uses composition to integrate flext-ldif and flext-meltano configurations.
    """

    # LDIF Processing Settings (from flext-ldif)
    ldif_file_path: str = ""
    ldif_encoding: str = "utf-8"
    ldif_max_file_size: int = 100 * 1024 * 1024  # 100MB
    ldif_validate_syntax: bool = True
    ldif_validate_schemas: bool = True

    # DBT Execution Settings (from flext-meltano)
    dbt_project_dir: str = "."
    dbt_profiles_dir: str = "."
    dbt_target: str = "dev"
    dbt_threads: int = 1
    dbt_log_level: str = "info"

    # LDIF-specific DBT Settings
    ldif_schema_mapping: ClassVar[dict[str, str]] = {
        "persons": "stg_persons",
        "groups": "stg_groups",
        "org_units": "stg_org_units",
        "domains": "stg_domains",
    }

    ldif_attribute_mapping: ClassVar[dict[str, str]] = {
        "cn": "common_name",
        "uid": "user_id",
        "mail": "email",
        "memberOf": "member_of",
        "objectClass": "object_class",
        "ou": "organizational_unit",
        "dc": "domain_component",
    }

    # Data Quality Settings
    min_quality_threshold: float = 0.8
    required_attributes: ClassVar[list[str]] = ["dn", "objectClass"]
    validate_dns: bool = True
    max_dn_depth: int = 10

    # LDIF Entry Type Mapping
    entry_type_mapping: ClassVar[dict[str, str]] = {
        "person": "persons",
        "organizationalPerson": "persons",
        "inetOrgPerson": "persons",
        "user": "persons",
        "group": "groups",
        "groupOfNames": "groups",
        "groupOfUniqueNames": "groups",
        "organizationalUnit": "org_units",
        "organization": "org_units",
        "domain": "domains",
        "dcObject": "domains",
    }

    def get_ldif_config(self) -> FlextLDIFConfig:
        """Get LDIF configuration for flext-ldif integration."""
        return FlextLDIFConfig(
            max_entries=20000,
            max_entry_size=self.ldif_max_file_size,
            strict_validation=self.ldif_validate_syntax,
            input_encoding=self.ldif_encoding,
            output_encoding=self.ldif_encoding,
        )

    def get_meltano_config(self) -> FlextMeltanoConfig:
        """Get Meltano configuration for flext-meltano integration."""
        return FlextMeltanoConfig(
            project_root=self.dbt_project_dir,
            environment="dev",
            dbt_project_dir=self.dbt_project_dir,
            dbt_profiles_dir=self.dbt_profiles_dir,
            dbt_target=self.dbt_target,
            dbt_threads=self.dbt_threads,
            log_level=self.dbt_log_level,
        )

    def validate_config(self) -> FlextResult[bool]:
        """Validate configuration using flext-core patterns.
        
        Returns:
            FlextResult indicating whether configuration is valid
        """
        try:
            errors: list[str] = []
            
            # Validate LDIF settings
            if self.ldif_max_file_size <= 0:
                errors.append("ldif_max_file_size must be positive")
            
            if self.max_dn_depth <= 0:
                errors.append("max_dn_depth must be positive")
                
            if not (0.0 <= self.min_quality_threshold <= 1.0):
                errors.append("min_quality_threshold must be between 0.0 and 1.0")
            
            # Validate DBT settings  
            if self.dbt_threads <= 0:
                errors.append("dbt_threads must be positive")
                
            if self.dbt_log_level not in ["debug", "info", "warn", "error"]:
                errors.append("dbt_log_level must be debug, info, warn, or error")
            
            # Validate required attributes
            if not self.required_attributes:
                errors.append("required_attributes cannot be empty")
                
            if errors:
                error_msg = "; ".join(errors)
                logger.error("Configuration validation failed: %s", error_msg)
                return FlextResult[bool].fail(f"Configuration validation failed: {error_msg}")
                
            logger.info("Configuration validation passed")
            return FlextResult[bool].ok(True)
            
        except Exception as e:
            logger.exception("Error during configuration validation")
            return FlextResult[bool].fail(f"Configuration validation error: {e}")

    def to_dict(self) -> dict[str, Any]:
        """Convert configuration to dictionary for serialization."""
        return {
            # LDIF settings
            "ldif_file_path": self.ldif_file_path,
            "ldif_encoding": self.ldif_encoding,
            "ldif_max_file_size": self.ldif_max_file_size,
            "ldif_validate_syntax": self.ldif_validate_syntax,
            "ldif_validate_schemas": self.ldif_validate_schemas,
            # DBT settings
            "dbt_project_dir": self.dbt_project_dir,
            "dbt_profiles_dir": self.dbt_profiles_dir,
            "dbt_target": self.dbt_target,
            "dbt_threads": self.dbt_threads,
            "dbt_log_level": self.dbt_log_level,
            # Quality settings
            "min_quality_threshold": self.min_quality_threshold,
            "validate_dns": self.validate_dns,
            "max_dn_depth": self.max_dn_depth,
            # Mappings (as read-only)
            "ldif_schema_mapping": dict(self.ldif_schema_mapping),
            "ldif_attribute_mapping": dict(self.ldif_attribute_mapping),
            "entry_type_mapping": dict(self.entry_type_mapping),
            "required_attributes": list(self.required_attributes),
        }

    def get_ldif_quality_config(self) -> dict[str, object]:
        """Get data quality configuration for LDIF validation."""
        return {
            "min_quality_threshold": self.min_quality_threshold,
            "required_attributes": self.required_attributes,
            "validate_dns": self.validate_dns,
            "max_dn_depth": self.max_dn_depth,
        }

    def get_entry_type_for_object_class(self, object_class: str) -> str | None:
        """Get entry type mapping for a given object class."""
        return self.entry_type_mapping.get(object_class.lower())

    def get_schema_for_entry_type(self, entry_type: str) -> str | None:
        """Get DBT schema name for a given entry type."""
        return self.ldif_schema_mapping.get(entry_type)


__all__: list[str] = [
    "FlextDbtLdifConfig",
]
