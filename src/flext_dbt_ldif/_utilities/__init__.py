# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Internal utilities subpackage."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_dbt_ldif.simple_api import FlextDbtLdif

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextDbtLdif": ["flext_dbt_ldif.simple_api", "FlextDbtLdif"],
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
