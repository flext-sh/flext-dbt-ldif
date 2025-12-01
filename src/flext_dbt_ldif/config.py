"""FLEXT DBT LDIF Configuration Module.

This module provides DBT LDIF configuration using Pydantic 2 BaseModel.
Uses types from constants.py and typings.py, no dict[str, object].
Uses Python 3.13+ PEP 695 syntax and Pydantic 2 advanced features.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import ClassVar, Self

from flext_core import FlextConfig, FlextLogger, FlextResult
from flext_ldif import FlextLdifConfig
from flext_meltano import FlextMeltanoConfig
from pydantic import ConfigDict, Field, field_validator, model_validator

from flext_dbt_ldif.constants import FlextDbtLdifConstants
from flext_dbt_ldif.typings import FlextDbtLdifTypes

logger = FlextLogger(__name__)


@FlextConfig.auto_register("dbt_ldif")
class FlextDbtLdifConfig(FlextConfig.AutoConfig):
    """Single Pydantic 2 BaseModel class for flext-dbt-ldif using AutoConfig pattern.

    **ARCHITECTURAL PATTERN**: Zero-Boilerplate Auto-Registration

    This class uses FlextConfig.AutoConfig for automatic:
    - Singleton pattern (thread-safe)
    - Namespace registration (accessible via config.dbt_ldif)
    - Test reset capability (_reset_instance)

    Follows standardized pattern:
    - Extends FlextConfig.AutoConfig (BaseModel) for nested config pattern
    - No nested classes within Config
    - All defaults from FlextDbtLdifConstants
    - Uses Pydantic 2.11+ features (field_validator, model_validator)
    - Uses types from constants.py and typings.py
    - NO dict[str, object] - uses specific types

    **Usage**:
        # Get singleton instance
        config = FlextDbtLdifConfig.get_instance()

        # Or via FlextConfig namespace
        from flext_core import FlextConfig
        config = FlextConfig.get_global_instance()
        dbt_ldif_config = config.dbt_ldif
    """

    model_config = ConfigDict(
        case_sensitive=False,
        extra="allow",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
        frozen=False,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "title": "FLEXT DBT LDIF Configuration",
            "description": "DBT LDIF configuration using AutoConfig pattern",
        },
    )

    # =========================================================================
    # LDIF PROCESSING SETTINGS - Using types from constants.py
    # =========================================================================

    ldif_file_path: str = Field(
        default="",
        description="Path to LDIF file for processing",
    )
    """Path to LDIF file for processing."""

    ldif_encoding: str = Field(
        default=FlextDbtLdifConstants.DEFAULT_LDIF_ENCODING,
        description="LDIF file encoding",
    )
    """LDIF file encoding."""

    ldif_max_file_size: int = Field(
        default=FlextDbtLdifConstants.MAX_FILE_SIZE_GB,
        ge=FlextDbtLdifConstants.MIN_FILE_SIZE_KB,
        le=FlextDbtLdifConstants.MAX_FILE_SIZE_GB,
        description="Maximum LDIF file size in bytes",
    )
    """Maximum LDIF file size in bytes."""

    ldif_validate_syntax: bool = Field(
        default=True,
        description="Validate LDIF syntax during processing",
    )
    """Validate LDIF syntax during processing."""

    ldif_validate_schemas: bool = Field(
        default=True,
        description="Validate LDIF schemas during processing",
    )
    """Validate LDIF schemas during processing."""

    # =========================================================================
    # DBT EXECUTION SETTINGS - Using types from constants.py
    # =========================================================================

    dbt_project_dir: str = Field(
        default=".",
        description="DBT project directory path",
    )
    """DBT project directory path."""

    dbt_profiles_dir: str = Field(
        default=FlextDbtLdifConstants.DEFAULT_DBT_PROFILES_DIR,
        description="DBT profiles directory path",
    )
    """DBT profiles directory path."""

    dbt_target: FlextDbtLdifConstants.Literals.DbtTargetLiteral = Field(
        default=FlextDbtLdifConstants.DEFAULT_DBT_TARGET,
        description="DBT target environment",
    )
    """DBT target environment."""

    dbt_threads: int = Field(
        default=FlextDbtLdifConstants.DEFAULT_BATCH_SIZE // 1000,
        ge=1,
        le=16,
        description="Number of DBT threads",
    )
    """Number of DBT threads."""

    dbt_log_level: FlextDbtLdifConstants.Literals.DbtLogLevelLiteral = Field(
        default=FlextDbtLdifConstants.DbtLogLevels.INFO,
        description="DBT log level",
    )
    """DBT log level."""

    # =========================================================================
    # LDIF-SPECIFIC DBT SETTINGS - Using Mapping types
    # =========================================================================

    ldif_schema_mapping: ClassVar[Mapping[str, str]] = {
        "persons": "stg_persons",
        "groups": "stg_groups",
        "org_units": "stg_org_units",
        "domains": "stg_domains",
    }
    """Mapping of LDIF entry types to DBT schema names."""

    ldif_attribute_mapping: ClassVar[Mapping[str, str]] = {
        "cn": "common_name",
        "uid": "user_id",
        "mail": "email",
        "memberOf": "member_of",
        "objectClass": "object_class",
        "ou": "organizational_unit",
        "dc": "domain_component",
    }
    """Mapping of LDIF attribute names to DBT column names."""

    # =========================================================================
    # DATA QUALITY SETTINGS
    # =========================================================================

    min_quality_threshold: float = Field(
        default=0.8,
        ge=0.0,
        le=1.0,
        description="Minimum data quality threshold",
    )
    """Minimum data quality threshold."""

    required_attributes: ClassVar[Sequence[str]] = [
        "dn",
        "objectClass",
    ]
    """Required LDIF attributes for validation."""

    validate_dns: bool = Field(
        default=True,
        description="Validate LDIF distinguished names",
    )
    """Validate LDIF distinguished names."""

    max_dn_depth: int = Field(
        default=FlextDbtLdifConstants.PERFORMANCE_THRESHOLD_MODEL_COUNT_INCREMENTAL // 2,
        ge=1,
        le=50,
        description="Maximum DN depth for validation",
    )
    """Maximum DN depth for validation."""

    # =========================================================================
    # LDIF ENTRY TYPE MAPPING - Using Mapping types
    # =========================================================================

    entry_type_mapping: ClassVar[Mapping[str, str]] = {
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
    """Mapping of LDIF object classes to entry types."""

    # =========================================================================
    # PROJECT IDENTIFICATION
    # =========================================================================

    project_name: str = Field(
        default="flext-dbt-ldif",
        description="Project name",
    )
    """Project name."""

    project_version: str = Field(
        default="0.9.0",
        description="Project version",
    )
    """Project version."""

    # =========================================================================
    # PYDANTIC 2.11 FIELD VALIDATORS
    # =========================================================================

    @field_validator("dbt_target")
    @classmethod
    def validate_dbt_target(
        cls,
        v: str,
    ) -> FlextDbtLdifConstants.Literals.DbtTargetLiteral:
        """Validate DBT target environment."""
        valid_targets = {
            "dev",
            "development",
            "staging",
            "prod",
            "production",
            "test",
            "local",
        }
        if v not in valid_targets:
            valid_targets_str = ", ".join(sorted(valid_targets))
            msg = f"Invalid DBT target: {v}. Must be one of: {valid_targets_str}"
            raise ValueError(msg)
        return v  # type: ignore[return-value]

    @field_validator("ldif_encoding")
    @classmethod
    def validate_ldif_encoding(cls, v: str) -> str:
        """Validate LDIF encoding."""
        valid_encodings = {"utf-8", "utf-16", "ascii", "latin-1"}
        if v.lower() not in valid_encodings:
            valid_encodings_str = ", ".join(sorted(valid_encodings))
            msg = f"Invalid LDIF encoding: {v}. Must be one of: {valid_encodings_str}"
            raise ValueError(msg)
        return v.lower()

    @field_validator("ldif_file_path")
    @classmethod
    def validate_ldif_file_path(cls, v: str) -> str:
        """Validate LDIF file path."""
        if v and not v.endswith(".ldif"):
            msg = f"LDIF file path must end with .ldif extension: {v}"
            raise ValueError(msg)
        return v

    @model_validator(mode="after")
    def validate_ldif_configuration_consistency(self) -> Self:
        """Validate LDIF configuration consistency."""
        # Validate file path if specified
        if self.ldif_file_path:
            file_path = Path(self.ldif_file_path)
            if (
                file_path.exists()
                and file_path.stat().st_size > self.ldif_max_file_size
            ):
                msg = (
                    f"LDIF file size exceeds maximum allowed: "
                    f"{self.ldif_max_file_size} bytes"
                )
                raise ValueError(msg)

        return self

    # =========================================================================
    # BUSINESS RULES VALIDATION
    # =========================================================================

    def validate_business_rules(self) -> FlextResult[bool]:
        """Validate DBT LDIF specific business rules."""
        try:
            # Validate LDIF configuration
            if self.ldif_file_path and Path(self.ldif_file_path).suffix != ".ldif":
                return FlextResult[bool].fail("LDIF file must have .ldif extension")

            # Validate DBT configuration
            if not self.dbt_project_dir:
                return FlextResult[bool].fail("DBT project directory is required")

            # Validate file size limits
            if self.ldif_max_file_size < FlextDbtLdifConstants.MIN_FILE_SIZE_KB:
                return FlextResult[bool].fail("LDIF max file size must be at least 1KB")

            if self.ldif_max_file_size > FlextDbtLdifConstants.MAX_FILE_SIZE_GB:
                return FlextResult[bool].fail("LDIF max file size cannot exceed 1GB")

            return FlextResult[bool].ok(True)
        except Exception as e:
            return FlextResult[bool].fail(f"Business rules validation failed: {e}")

    # =========================================================================
    # INTEGRATION METHODS - Return typed configurations
    # =========================================================================

    def get_ldif_config(self) -> FlextLdifConfig:
        """Get LDIF configuration for flext-ldif integration."""
        return FlextLdifConfig(
            ldif_max_entries=20000,
            ldif_strict_validation=self.ldif_validate_syntax,
            ldif_encoding=self.ldif_encoding,  # type: ignore[arg-type]
        )

    def get_meltano_config(self) -> FlextMeltanoConfig:
        """Get Meltano configuration for flext-meltano integration."""
        # Convert string to proper Environment string value
        environment_mapping: Mapping[str, str] = {
            "dev": "development",
            "development": "development",
            "staging": "staging",
            "prod": "production",
            "production": "production",
            "test": "test",
            "local": "local",
        }

        environment_value = environment_mapping.get(
            self.dbt_target.lower(),
            "development",
        )

        return FlextMeltanoConfig(
            project_root=Path(self.dbt_project_dir),
            environment=environment_value,
        )

    def get_ldif_quality_config(
        self,
    ) -> FlextDbtLdifTypes.LdifParsing.ValidationRules:
        """Get data quality configuration for LDIF validation.

        Returns:
            ValidationRules mapping with quality configuration

        """
        return {
            "min_quality_threshold": self.min_quality_threshold,
            "required_attributes": list(self.required_attributes),
            "validate_dns": self.validate_dns,
            "max_dn_depth": self.max_dn_depth,
        }

    def get_entry_type_for_object_class(self, object_class: str) -> str | None:
        """Get entry type mapping for a given object class."""
        return self.entry_type_mapping.get(object_class.lower())

    def get_schema_for_entry_type(self, entry_type: str) -> str | None:
        """Get DBT schema name for a given entry type."""
        return self.ldif_schema_mapping.get(entry_type)

    # =========================================================================
    # FACTORY METHODS - Using AutoConfig singleton pattern
    # =========================================================================

    @classmethod
    def create_for_environment(
        cls,
        environment: str | None = None,
        **overrides: object,
    ) -> FlextDbtLdifConfig:
        """Create configuration for specific environment using AutoConfig singleton pattern.

        Args:
            environment: Environment name (unused, kept for API compatibility)
            **overrides: Configuration overrides (unused, kept for API compatibility)

        Returns:
            FlextDbtLdifConfig singleton instance

        """
        _ = environment  # Unused parameter kept for API compatibility
        _ = overrides  # Unused parameter kept for API compatibility
        return cls.get_instance()

    @classmethod
    def create_default(cls) -> FlextDbtLdifConfig:
        """Create default configuration instance using AutoConfig singleton pattern."""
        return cls.get_instance()

    @classmethod
    def create_for_development(cls) -> FlextDbtLdifConfig:
        """Create configuration optimized for development using AutoConfig singleton pattern."""
        instance = cls.get_instance()
        # Update instance with dev defaults if needed
        instance.ldif_validate_syntax = False
        instance.dbt_target = "dev"  # type: ignore[assignment]
        instance.dbt_threads = 1
        instance.dbt_log_level = "debug"  # type: ignore[assignment]
        instance.ldif_max_file_size = 10 * 1024 * 1024  # 10MB for dev
        return instance

    @classmethod
    def create_for_production(cls) -> FlextDbtLdifConfig:
        """Create configuration optimized for production using AutoConfig singleton pattern."""
        instance = cls.get_instance()
        # Update instance with prod defaults if needed
        instance.ldif_validate_syntax = True
        instance.ldif_validate_schemas = True
        instance.dbt_target = "production"  # type: ignore[assignment]
        instance.dbt_threads = 8
        instance.dbt_log_level = "info"  # type: ignore[assignment]
        instance.ldif_max_file_size = 500 * 1024 * 1024  # 500MB for prod
        return instance

    @classmethod
    def create_for_testing(cls) -> FlextDbtLdifConfig:
        """Create configuration optimized for testing using AutoConfig singleton pattern."""
        instance = cls.get_instance()
        # Update instance with test defaults if needed
        instance.ldif_file_path = "./test_data/sample.ldif"
        instance.ldif_encoding = "utf-8"
        instance.ldif_validate_syntax = True
        instance.dbt_target = "test"  # type: ignore[assignment]
        instance.dbt_threads = 1
        instance.dbt_log_level = "debug"  # type: ignore[assignment]
        instance.ldif_max_file_size = 1024 * 1024  # 1MB for tests
        instance.min_quality_threshold = 0.5
        return instance

    @classmethod
    def reset_global_instance(cls) -> None:
        """Reset the global FlextDbtLdifConfig instance (mainly for testing)."""
        # Use the AutoConfig reset mechanism
        cls._reset_instance()


__all__: list[str] = [
    "FlextDbtLdifConfig",
]
