"""Test configuration and fixtures for flext-dbt-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Generator
from pathlib import Path

import pytest
from flext_tests import tf, tk

from flext_dbt_ldif import FlextDbtLdifSettings
from tests import u


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


@pytest.fixture
def settings() -> FlextDbtLdifSettings:
    """Provide a typed FlextDbtLdifSettings instance with a sample LDIF path."""
    FlextDbtLdifSettings.reset_for_testing()
    return FlextDbtLdifSettings(
        DbtLdif=FlextDbtLdifSettings._DbtLdif(ldif_file_path="/tmp/sample.ldif"),
    )


def pytest_runtest_setup(item: pytest.Item) -> None:
    """Reset the settings singleton before each test."""
    _ = item
    # NOTE (multi-agent): mro-rn88 — constructing FlextDbtLdifSettings overwrites the
    # fetch_global() singleton; reset around each test to prevent cross-test pollution.
    FlextDbtLdifSettings.reset_for_testing()


def pytest_runtest_teardown(item: pytest.Item) -> None:
    """Reset the settings singleton after each test."""
    _ = item
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


# NOTE (multi-agent, bead mro-d421): export pytest hooks and fixtures so pyright
# sees the plugin surface as accessed.
__all__: list[str] = [
    "pytest_runtest_setup",
    "pytest_runtest_teardown",
    "pytest_sessionstart",
    "set_test_environment",
]
