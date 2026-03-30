# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

from tests.unit import _LAZY_IMPORTS as _CHILD_LAZY_0

if TYPE_CHECKING:
    from tests.conftest import *
    from tests.constants import *
    from tests.models import *
    from tests.protocols import *
    from tests.typings import *
    from tests.unit import *
    from tests.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    **_CHILD_LAZY_0,
    "FlextDbtLdifTestConstants": "tests.constants",
    "FlextDbtLdifTestModels": "tests.models",
    "FlextDbtLdifTestProtocols": "tests.protocols",
    "FlextDbtLdifTestTypes": "tests.typings",
    "FlextDbtLdifTestUtilities": "tests.utilities",
    "c": ["tests.constants", "FlextDbtLdifTestConstants"],
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": "flext_tests",
    "dbt_ldif_profile": "tests.conftest",
    "dbt_ldif_project_config": "tests.conftest",
    "docker_control": "tests.conftest",
    "e": "flext_tests",
    "ensure_shared_docker_container": "tests.conftest",
    "h": "flext_tests",
    "ldif_source_config": "tests.conftest",
    "m": ["tests.models", "FlextDbtLdifTestModels"],
    "models": "tests.models",
    "p": ["tests.protocols", "FlextDbtLdifTestProtocols"],
    "protocols": "tests.protocols",
    "pytest_configure": "tests.conftest",
    "r": "flext_tests",
    "s": "flext_tests",
    "sample_ldif_entries": "tests.conftest",
    "set_test_environment": "tests.conftest",
    "shared_ldap_container": "tests.conftest",
    "t": ["tests.typings", "FlextDbtLdifTestTypes"],
    "typings": "tests.typings",
    "u": ["tests.utilities", "FlextDbtLdifTestUtilities"],
    "unit": "tests.unit",
    "utilities": "tests.utilities",
    "x": "flext_tests",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
