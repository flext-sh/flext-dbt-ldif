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
    "c": ("flext_core.constants", "FlextConstants"),
    "cli_service": "flext_dbt_ldif.services.cli_service",
    "client": "flext_dbt_ldif.services.client",
    "core": "flext_dbt_ldif.services.core",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "error": "flext_dbt_ldif.services.error",
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("flext_core.models", "FlextModels"),
    "p": ("flext_core.protocols", "FlextProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "service": "flext_dbt_ldif.services.service",
    "t": ("flext_core.typings", "FlextTypes"),
    "u": ("flext_core.utilities", "FlextUtilities"),
    "unified_service": "flext_dbt_ldif.services.unified_service",
    "x": ("flext_core.mixins", "FlextMixins"),
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
