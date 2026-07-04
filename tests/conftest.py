"""Test configuration and fixtures for flext-dbt-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from flext_tests import tf, tk

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
