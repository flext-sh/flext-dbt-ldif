"""Version information for FLEXT dbt LDIF."""

from __future__ import annotations

# 🚨 ARCHITECTURAL COMPLIANCE: Using DI container
from flext_dbt_ldif.infrastructure.di_container import (
    get_base_config,
    get_domain_entity,
    get_domain_value_object,
    get_field,
    get_service_result,
)

ServiceResult = get_service_result()
DomainEntity = get_domain_entity()
Field = get_field()
DomainValueObject = get_domain_value_object()
BaseConfig = get_base_config()

__version__ = get_version()
__version_info__ = get_version_info()
