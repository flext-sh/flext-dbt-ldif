"""FLEXT DBT LDIF Configuration Module.

SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextConfig, FlextLogger, FlextTypes
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
    ldif_schema_mapping: ClassVar[FlextTypes.Core.Headers] = {
        "persons": "stg_persons",
        "groups": "stg_groups",
        "org_units": "stg_org_units",
        "domains": "stg_domains",
    }

    ldif_attribute_mapping: ClassVar[FlextTypes.Core.Headers] = {
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
    required_attributes: ClassVar[FlextTypes.Core.StringList] = ["dn", "objectClass"]
    validate_dns: bool = True
    max_dn_depth: int = 10

    # LDIF Entry Type Mapping
    entry_type_mapping: ClassVar[FlextTypes.Core.Headers] = {
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
        )

    def get_ldif_quality_config(self) -> FlextTypes.Core.Dict:
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


__all__: FlextTypes.Core.StringList = [
    "FlextDbtLdifConfig",
]
