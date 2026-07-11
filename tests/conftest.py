"""Test configuration and fixtures for flext-dbt-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from flext_tests import tf, tk

from flext_dbt_ldif import FlextDbtLdifSettings
from tests.utilities import u

if TYPE_CHECKING:
    from collections.abc import Generator


@pytest.fixture
def set_test_environment() -> Generator[None]:
    """Set test environment variables."""
    with (
        tf().temporary_directory() as temp_dir,
        u.Tests.env_vars_context({
            "FLEXT_ENV": "test",
            "FLEXT_LOG_LEVEL": "DEBUG",
            "DBT_PROFILES_DIR": temp_dir,
            "LDIF_TEST_MODE": "true",
        }),
    ):
        yield


@pytest.fixture(autouse=True)
def _reset_settings_singleton() -> Generator[None]:
    """Isolate the settings singleton so per-test construction never leaks globally."""
    # NOTE (multi-agent): mro-rn88 — constructing FlextDbtLdifSettings overwrites the
    # fetch_global() singleton; reset around each test to prevent cross-test pollution.
    FlextDbtLdifSettings.reset_for_testing()
    yield
    FlextDbtLdifSettings.reset_for_testing()


def pytest_sessionstart(session: pytest.Session) -> None:
    """Ensure shared Docker container is started for the test session."""
    _ = session
    docker_control = tk.shared(
        "flext-openldap-test",
        workspace_root=Path(__file__).resolve().parents[2],
    )
    result = docker_control.execute()
    if result.failure:
        pytest.skip(
            f"Failed to start LDAP container: {result.error}",
            allow_module_level=True,
        )


# NOTE (multi-agent, bead mro-d421): export fixtures/hooks so pyright sees them as
# accessed (reportUnusedFunction) — the autouse fixture is invoked implicitly by pytest.
__all__: list[str] = [
    "_reset_settings_singleton",
    "pytest_sessionstart",
    "set_test_environment",
]
