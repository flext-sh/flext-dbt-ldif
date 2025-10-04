"""FLEXT DBT LDIF Configuration Module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path
from typing import ClassVar, Self

from flext_core import FlextConfig, FlextLogger, FlextResult
from flext_ldif import FlextLdifConfig
from flext_meltano.config import FlextMeltanoConfig
from pydantic import Field, field_validator, model_validator
from pydantic_settings import SettingsConfigDict

from flext_dbt_ldif.constants import FlextDbtLdifConstants
from flext_dbt_ldif.typings import FlextDbtLdifTypes

logger = FlextLogger(__name__)


class FlextDbtLdifConfig(FlextConfig):
    """Single Pydantic 2 Settings class for flext-dbt-ldif extending FlextConfig.

    Follows standardized pattern:
    - Extends FlextConfig from flext-core
    - No nested classes within Config
    - All defaults from FlextDbtLdifConstants
    - Uses enhanced singleton pattern with inverse dependency injection
    - Uses Pydantic 2.11+ features (field_validator, model_validator)
    """

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_DBT_LDIF_",
        case_sensitive=False,
        extra="allow",
        validate_assignment=True,
        str_strip_whitespace=True,
        json_schema_extra={
            "title": "FLEXT DBT LDIF Configuration",
            "description": "DBT LDIF configuration extending FlextConfig",
        },
    )

    # LDIF Processing Settings (from flext-ldif) using Field and proper defaults
    ldif_file_path: str = Field(
        default="", description="Path to LDIF file for processing"
    )
    ldif_encoding: str = Field(
        default=FlextDbtLdifConstants.DEFAULT_LDIF_ENCODING,
        description="LDIF file encoding",
    )
    ldif_max_file_size: int = Field(
        default=FlextDbtLdifConstants.MAX_FILE_SIZE_GB,
        ge=FlextDbtLdifConstants.MIN_FILE_SIZE_KB,
        le=FlextDbtLdifConstants.MAX_FILE_SIZE_GB,
        description="Maximum LDIF file size in bytes",
    )
    ldif_validate_syntax: bool = Field(
        default=True, description="Validate LDIF syntax during processing"
    )
    ldif_validate_schemas: bool = Field(
        default=True, description="Validate LDIF schemas during processing"
    )

    # DBT Execution Settings (from flext-meltano) using Field
    dbt_project_dir: str = Field(default=".", description="DBT project directory path")
    dbt_profiles_dir: str = Field(
        default=FlextDbtLdifConstants.DEFAULT_DBT_PROFILES_DIR,
        description="DBT profiles directory path",
    )
    dbt_target: str = Field(
        default=FlextDbtLdifConstants.DEFAULT_DBT_TARGET,
        description="DBT target environment",
    )
    dbt_threads: int = Field(
        default=FlextDbtLdifConstants.DEFAULT_BATCH_SIZE // 1000,
        ge=1,
        le=16,
        description="Number of DBT threads",
    )
    dbt_log_level: str = Field(default="info", description="DBT log level")

    # LDIF-specific DBT Settings
    ldif_schema_mapping: ClassVar[FlextDbtLdifTypes.Core.Dict] = {
        "persons": "stg_persons",
        "groups": "stg_groups",
        "org_units": "stg_org_units",
        "domains": "stg_domains",
    }

    ldif_attribute_mapping: ClassVar[FlextDbtLdifTypes.Core.Dict] = {
        "cn": "common_name",
        "uid": "user_id",
        "mail": "email",
        "memberOf": "member_of",
        "objectClass": "object_class",
        "ou": "organizational_unit",
        "dc": "domain_component",
    }

    # Data Quality Settings
    min_quality_threshold: float = Field(
        default=0.8, ge=0.0, le=1.0, description="Minimum data quality threshold"
    )
    required_attributes: ClassVar[FlextDbtLdifTypes.Core.List] = [
        "dn",
        "objectClass",
    ]
    validate_dns: bool = Field(
        default=True, description="Validate LDIF distinguished names"
    )
    max_dn_depth: int = Field(
        default=FlextDbtLdifConstants.PERFORMANCE_THRESHOLD_MODEL_COUNT_INCREMENTAL
        // 2,
        ge=1,
        le=50,
        description="Maximum DN depth for validation",
    )

    # LDIF Entry Type Mapping
    entry_type_mapping: ClassVar[FlextDbtLdifTypes.Core.Dict] = {
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

    # Project Identification
    project_name: str = Field(
        default="flext-dbt-ldif",
        description="Project name",
    )

    project_version: str = Field(
        default="0.9.0",
        description="Project version",
    )

    # Pydantic 2.11 field validators
    @field_validator("dbt_target")
    @classmethod
    def validate_dbt_target(cls, v: str) -> str:
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
        return v

    @field_validator("dbt_log_level")
    @classmethod
    def validate_dbt_log_level(cls, v: str) -> str:
        """Validate DBT log level."""
        valid_levels = {"debug", "info", "warn", "error", "none"}
        if v.lower() not in valid_levels:
            valid_levels_str = ", ".join(sorted(valid_levels))
            msg = f"Invalid DBT log level: {v}. Must be one of: {valid_levels_str}"
            raise ValueError(msg)
        return v.lower()

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
                msg = f"LDIF file size exceeds maximum allowed: {self.ldif_max_file_size} bytes"
                raise ValueError(msg)

        return self

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate DBT LDIF specific business rules."""
        try:
            # Validate LDIF configuration
            if self.ldif_file_path and Path(self.ldif_file_path).suffix != ".ldif":
                return FlextResult[None].fail("LDIF file must have .ldif extension")

            # Validate DBT configuration
            if not self.dbt_project_dir:
                return FlextResult[None].fail("DBT project directory is required")

            # Validate file size limits
            if self.ldif_max_file_size < FlextDbtLdifConstants.MIN_FILE_SIZE_KB:
                return FlextResult[None].fail("LDIF max file size must be at least 1KB")

            if self.ldif_max_file_size > FlextDbtLdifConstants.MAX_FILE_SIZE_GB:
                return FlextResult[None].fail("LDIF max file size cannot exceed 1GB")

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Business rules validation failed: {e}")

    def get_ldif_config(self) -> FlextLdifConfig:
        """Get LDIF configuration for flext-ldif integration."""
        return FlextLdifConfig(
            ldif_max_entries=20000,
            ldif_max_file_size_mb=self.ldif_max_file_size // (1024 * 1024),
            ldif_strict_validation=self.ldif_validate_syntax,
            ldif_encoding=self.ldif_encoding,
        )

    def get_meltano_config(self) -> FlextMeltanoConfig:
        """Get Meltano configuration for flext-meltano integration."""
        # Convert string to proper Environment string value
        environment_mapping: dict[str, FlextDbtLdifTypes.Config.Environment] = {
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

    def get_ldif_quality_config(self) -> FlextDbtLdifTypes.Core.Dict:
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

    @classmethod
    def create_for_environment(
        cls, environment: str, **overrides: object
    ) -> FlextDbtLdifConfig:
        """Create configuration for specific environment using enhanced singleton pattern."""
        return cls.get_or_create_shared_instance(
            project_name="flext-dbt-ldif", environment=environment, **overrides
        )

    @classmethod
    def create_default(cls) -> FlextDbtLdifConfig:
        """Create default configuration instance using enhanced singleton pattern."""
        return cls.get_or_create_shared_instance(project_name="flext-dbt-ldif")

    @classmethod
    def create_for_development(cls) -> FlextDbtLdifConfig:
        """Create configuration optimized for development using enhanced singleton pattern."""
        return cls.get_or_create_shared_instance(
            project_name="flext-dbt-ldif",
            ldif_validate_syntax=False,
            dbt_target="dev",
            dbt_threads=1,
            dbt_log_level="debug",
            ldif_max_file_size=10 * 1024 * 1024,  # 10MB for dev
        )

    @classmethod
    def create_for_production(cls) -> FlextDbtLdifConfig:
        """Create configuration optimized for production using enhanced singleton pattern."""
        return cls.get_or_create_shared_instance(
            project_name="flext-dbt-ldif",
            ldif_validate_syntax=True,
            ldif_validate_schemas=True,
            dbt_target="production",
            dbt_threads=8,
            dbt_log_level="info",
            ldif_max_file_size=500 * 1024 * 1024,  # 500MB for prod
        )

    @classmethod
    def create_for_testing(cls) -> FlextDbtLdifConfig:
        """Create configuration optimized for testing using enhanced singleton pattern."""
        return cls.get_or_create_shared_instance(
            project_name="flext-dbt-ldif",
            ldif_file_path="./test_data/sample.ldif",
            ldif_encoding="utf-8",
            ldif_validate_syntax=True,
            dbt_target="test",
            dbt_threads=1,
            dbt_log_level="debug",
            ldif_max_file_size=1024 * 1024,  # 1MB for tests
            min_quality_threshold=0.5,
        )

    @classmethod
    def get_global_instance(cls) -> FlextDbtLdifConfig:
        """Get the global singleton instance using enhanced FlextConfig pattern."""
        return cls.get_or_create_shared_instance(project_name="flext-dbt-ldif")

    @classmethod
    def reset_global_instance(cls) -> None:
        """Reset the global FlextDbtLdifConfig instance (mainly for testing)."""
        # Use the enhanced FlextConfig reset mechanism
        cls.reset_shared_instance()


__all__: FlextDbtLdifTypes.Core.List = [
    "FlextDbtLdifConfig",
]
