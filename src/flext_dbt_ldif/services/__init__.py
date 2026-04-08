# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Services package."""

from __future__ import annotations

from flext_core.lazy import install_lazy_exports

_LAZY_IMPORTS = {
    "FlextDbtLdifCliService": (
        "flext_dbt_ldif.services.cli_service",
        "FlextDbtLdifCliService",
    ),
    "FlextDbtLdifClient": ("flext_dbt_ldif.services.client", "FlextDbtLdifClient"),
    "FlextDbtLdifCore": ("flext_dbt_ldif.services.core", "FlextDbtLdifCore"),
    "FlextDbtLdifError": ("flext_dbt_ldif.services.error", "FlextDbtLdifError"),
    "FlextDbtLdifServiceMixin": (
        "flext_dbt_ldif.services.service",
        "FlextDbtLdifServiceMixin",
    ),
    "FlextDbtLdifUnifiedService": (
        "flext_dbt_ldif.services.unified_service",
        "FlextDbtLdifUnifiedService",
    ),
    "cli_service": "flext_dbt_ldif.services.cli_service",
    "client": "flext_dbt_ldif.services.client",
    "core": "flext_dbt_ldif.services.core",
    "error": "flext_dbt_ldif.services.error",
    "service": "flext_dbt_ldif.services.service",
    "unified_service": "flext_dbt_ldif.services.unified_service",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
