"""Test configuration and fixtures for flext-dbt-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import os
import tempfile
from collections.abc import Generator

import pytest

from flext_tests import FlextTestDocker


@pytest.fixture(scope="session")
def docker_control() -> FlextTestDocker:
    """Provide FlextTestDocker instance for container management."""
    return FlextTestDocker()


@pytest.fixture(scope="session")
def shared_ldap_container(
    docker_control: FlextTestDocker,
) -> Generator[str]:
    """Start and maintain flext-openldap-test container.

    Container auto-starts if not running and remains running after tests.
    """
    result = docker_control.start_container("flext-openldap-test")
    if result.is_failure:
        pytest.skip(f"Failed to start LDAP container: {result.error}")

    yield "flext-openldap-test"

    # Keep container running after tests
    docker_control.stop_container("flext-openldap-test", remove=False)


# Import shared fixtures from docker directory


# Test environment setup
@pytest.fixture(autouse=True)
def set_test_environment() -> Generator[None]:
    """Set test environment variables."""
    os.environ["FLEXT_ENV"] = "test"
    os.environ["FLEXT_LOG_LEVEL"] = "debug"
    temp_dir = tempfile.mkdtemp(prefix="dbt_profiles_")
    os.environ["DBT_PROFILES_DIR"] = temp_dir
    os.environ["LDIF_TEST_MODE"] = "true"
    yield
    # Cleanup
    os.environ.pop("FLEXT_ENV", None)
    os.environ.pop("FLEXT_LOG_LEVEL", None)
    os.environ.pop("DBT_PROFILES_DIR", None)
    os.environ.pop("LDIF_TEST_MODE", None)


# Shared LDAP container fixture
@pytest.fixture(scope="session", autouse=True)
def ensure_shared_docker_container(shared_ldap_container: object) -> None:
    """Ensure shared Docker container is started for the test session.

    This fixture automatically starts the shared LDAP container if not running,
    and ensures it's available for all tests in the session.
    """
    # Suppress unused parameter warning - fixture is used for side effects
    _ = shared_ldap_container
    # The shared_ldap_container fixture will be invoked automatically
    # and will start/stop the container for the entire test session


# dbt LDIF configuration fixtures
@pytest.fixture
def dbt_ldif_profile() -> FlextTypes.Core.Dict:
    """Dbt LDIF profile configuration for testing."""
    return {
        "config": {
            "partial_parse": True,
            "printer_width": 120,
            "send_anonymous_usage_stats": False,
            "use_colors": True,
        },
        "test": {
            "outputs": {
                "default": {
                    "type": "postgres",  # Using postgres as target for
                    # transformed LDIF data
                    "host": "localhost",
                    "port": 5432,
                    "database": "ldif_warehouse",
                    "schema": "ldif_transformed",
                    "user": "dbt_ldif_user",
                    "password": "dbt_ldif_pass",
                    "threads": 4,
                    "keepalives_idle": 0,
                    "search_path": "ldif_transformed",
                },
            },
            "target": "default",
        },
    }


@pytest.fixture
def dbt_ldif_project_config() -> FlextTypes.Core.Dict:
    """Dbt LDIF project configuration for testing."""
    return {
        "name": "flext_dbt_ldif_test",
        "version": "0.7.0",
        "profile": "test",
        "model-paths": ["models"],
        "analysis-paths": ["analyses"],
        "test-paths": ["tests"],
        "seed-paths": ["seeds"],
        "macro-paths": ["macros"],
        "snapshot-paths": ["snapshots"],
        "docs-paths": ["docs"],
        "asset-paths": ["assets"],
        "target-path": "target",
        "clean-targets": ["target", "dbt_packages"],
        "require-dbt-version": ">=1.8.0",
        "model_config": {
            "materialized": "table",
            "ldif": {
                "enable_ldif_functions": True,
                "ldap_server": "localhost:3390",  # Use shared container port
                "base_dn": "dc=flext,dc=local",  # Use shared container domain
            },
        },
        "vars": {
            "ldif_base_dn": "dc=flext,dc=local",  # Use shared container domain
            "ldif_users_ou": "ou=people",  # Use shared container OU structure
            "ldif_groups_ou": "ou=groups",  # Use shared container OU structure
            "enable_ldif_validation": True,
        },
    }


# LDIF source fixtures
@pytest.fixture
def ldif_source_config(shared_ldap_config: dict) -> FlextTypes.Core.Dict:
    """LDIF source configuration for testing using shared container."""
    _ = shared_ldap_config  # Acknowledge parameter usage
    return {
        "server": "localhost",
        "port": 3390,  # Use shared container port
        "base_dn": "dc=flext,dc=local",  # Use shared container domain
        "bind_dn": "cn=REDACTED_LDAP_BIND_PASSWORD,dc=flext,dc=local",  # Use shared container REDACTED_LDAP_BIND_PASSWORD DN
        "bind_password": "REDACTED_LDAP_BIND_PASSWORD123",  # Use shared container password
        "use_ssl": False,
        "use_tls": False,
        "timeout": 30,
        "search_scope": "SUBTREE",
    }


@pytest.fixture
def sample_ldif_entries() -> list[FlextTypes.Core.Dict]:
    """Sample LDIF entries for testing using shared container domain."""
    return [
        {
            "dn": "cn=john.doe,ou=people,dc=flext,dc=local",
            "attributes": {
                "cn": ["john.doe"],
                "uid": ["jdoe"],
                "mail": ["john.doe@internal.invalid"],
                "givenName": ["John"],
                "sn": ["Doe"],
                "employeeNumber": ["12345"],
                "departmentNumber": ["IT"],
                "title": ["Software Engineer"],
                "telephoneNumber": ["+1-555-1234"],
                "objectClass": ["inetOrgPerson", "organizationalPerson", "person"],
            },
        },
        {
            "dn": "cn=jane.smith,ou=people,dc=flext,dc=local",
            "attributes": {
                "cn": ["jane.smith"],
                "uid": ["jsmith"],
                "mail": ["jane.smith@internal.invalid"],
                "givenName": ["Jane"],
                "sn": ["Smith"],
                "employeeNumber": ["12346"],
                "departmentNumber": ["HR"],
                "title": ["HR Manager"],
                "telephoneNumber": ["+1-555-5678"],
                "objectClass": ["inetOrgPerson", "organizationalPerson", "person"],
            },
        },
        {
            "dn": "cn=developers,ou=groups,dc=flext,dc=local",
            "attributes": {
                "cn": ["developers"],
                "description": ["Software Developers Group"],
                "member": [
                    "cn=john.doe,ou=people,dc=flext,dc=local",
                    "cn=bob.johnson,ou=people,dc=flext,dc=local",
                ],
                "objectClass": ["groupOfNames"],
            },
        },
    ]


# Pytest markers for test categorization
def pytest_configure(config: pytest.Config) -> None:
    """Configure pytest markers."""
    config.addinivalue_line("markers", "unit: Unit tests")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "e2e: End-to-end tests")
    config.addinivalue_line("markers", "dbt: dbt-specific tests")
    config.addinivalue_line("markers", "ldif: LDIF integration tests")
    config.addinivalue_line("markers", "transformation: Data transformation tests")
    config.addinivalue_line("markers", "validation: Data validation tests")
    config.addinivalue_line("markers", "performance: Performance tests")
    config.addinivalue_line("markers", "slow: Slow tests")
