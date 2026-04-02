# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Services package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_dbt_ldif.services import (
        cli_service,
        client,
        core,
        error,
        service,
        unified_service,
    )
    from flext_dbt_ldif.services.cli_service import FlextDbtLdifCliService
    from flext_dbt_ldif.services.client import FlextDbtLdifClient
    from flext_dbt_ldif.services.core import FlextDbtLdifCore
    from flext_dbt_ldif.services.error import FlextDbtLdifError
    from flext_dbt_ldif.services.service import FlextDbtLdifServiceMixin, logger
    from flext_dbt_ldif.services.unified_service import FlextDbtLdifUnifiedService

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextDbtLdifCliService": "flext_dbt_ldif.services.cli_service",
    "FlextDbtLdifClient": "flext_dbt_ldif.services.client",
    "FlextDbtLdifCore": "flext_dbt_ldif.services.core",
    "FlextDbtLdifError": "flext_dbt_ldif.services.error",
    "FlextDbtLdifServiceMixin": "flext_dbt_ldif.services.service",
    "FlextDbtLdifUnifiedService": "flext_dbt_ldif.services.unified_service",
    "cli_service": "flext_dbt_ldif.services.cli_service",
    "client": "flext_dbt_ldif.services.client",
    "core": "flext_dbt_ldif.services.core",
    "error": "flext_dbt_ldif.services.error",
    "logger": "flext_dbt_ldif.services.service",
    "service": "flext_dbt_ldif.services.service",
    "unified_service": "flext_dbt_ldif.services.unified_service",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
