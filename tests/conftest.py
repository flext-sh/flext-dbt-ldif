"""Test configuration and fixtures for flext-dbt-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Generator
from pathlib import Path

import pytest
from flext_tests import tf, tk

from tests.utilities import u


@pytest.fixture(scope="session")
def docker_control() -> tk:
    """Provide tk instance for container management."""
    return tk.shared(
        "flext-openldap-test",
        workspace_root=Path(__file__).resolve().parents[2],
    )


@pytest.fixture(scope="session")
def shared_ldap_container(docker_control: tk) -> str:
    """Start and maintain flext-openldap-test container."""
    result = docker_control.execute()
    if result.failure:
        pytest.skip(f"Failed to start LDAP container: {result.error}")
    return "flext-openldap-test"


@pytest.fixture(autouse=True)
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


@pytest.fixture(scope="session", autouse=True)
def ensure_shared_docker_container(shared_ldap_container: str) -> None:
    """Ensure shared Docker container is started for the test session."""
    _ = shared_ldap_container
