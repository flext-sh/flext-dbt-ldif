# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import install_lazy_exports

_LAZY_IMPORTS = {
    "test_api_surface": "tests.unit.test_api_surface",
    "test_cli": "tests.unit.test_cli",
    "test_core": "tests.unit.test_core",
    "test_dbt_client": "tests.unit.test_dbt_client",
    "test_dbt_models": "tests.unit.test_dbt_models",
    "test_services": "tests.unit.test_services",
    "test_services_and_api": "tests.unit.test_services_and_api",
    "test_version": "tests.unit.test_version",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
