"""Unit tests for DBT client functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from flext_dbt_ldif import FlextDbtLdifClient, FlextDbtLdifSettings
from tests import t


class TestFlextDbtLdifClient:
    """Test cases for FlextDbtLdifClient."""

    def test_initialization_default(self) -> None:
        """Test client initialization with default settings."""
        client = FlextDbtLdifClient.Client()
        assert client.config is not None

    def test_initialization_with_config(self) -> None:
        """Test client initialization with explicit config."""
        config = FlextDbtLdifSettings.get_global()
        client = FlextDbtLdifClient.Client(config)
        assert client.config is config

    def test_parse_ldif_file_ok(self, tmp_path: Path) -> None:
        """Test parsing LDIF file returns success."""
        client = FlextDbtLdifClient.Client()
        result = client.parse_ldif_file(tmp_path / "dummy.ldif")
        assert result.success
        assert isinstance(result.value, list)
        assert result.value

    def test_parse_ldif_file_no_path(self) -> None:
        """Test parsing without file path fails when config path is empty."""
        config = FlextDbtLdifSettings.get_global()
        client = FlextDbtLdifClient.Client(config)
        result = client.parse_ldif_file()
        assert result.failure
        assert "required" in (result.error or "").lower()

    def test_validate_ldif_data_ok(self) -> None:
        """Test validating LDIF data with entries."""
        client = FlextDbtLdifClient.Client()
        entries: Sequence[t.ContainerValueMapping] = [
            {"dn": "cn=test,dc=example,dc=org", "source": "test.ldif"},
        ]
        result = client.validate_ldif_data(entries)
        assert result.success
        data = result.value
        assert data is not None
        assert data.total_entries == 1
        quality_score = data.quality_score
        assert isinstance(quality_score, float)
        assert 0.99 < quality_score < 1.01
        assert data.validation_status == "passed"

    def test_validate_ldif_data_empty(self) -> None:
        """Test validating empty entries fails."""
        client = FlextDbtLdifClient.Client()
        result = client.validate_ldif_data([])
        assert result.failure

    def test_transform_with_dbt_ok(self) -> None:
        """Test transforming with DBT returns metadata."""
        client = FlextDbtLdifClient.Client()
        entries: Sequence[t.ContainerValueMapping] = [
            {"dn": "cn=test,dc=example,dc=org"},
        ]
        result = client.transform_with_dbt(entries, ["m1", "m2"])
        assert result.success
        data = result.value
        assert data is not None
        assert data.records == 1
        assert data.models == ["m1", "m2"]
        assert data.status == "success"

    def test_transform_with_dbt_default_models(self) -> None:
        """Test transform uses default models when none specified."""
        client = FlextDbtLdifClient.Client()
        result = client.transform_with_dbt([], None)
        assert result.success
        data = result.value
        assert data is not None
        assert "stg_ldif_entries" in data.models

    def test_run_full_pipeline_ok(self, tmp_path: Path) -> None:
        """Test running full pipeline with valid file."""
        client = FlextDbtLdifClient.Client()
        result = client.run_full_pipeline(tmp_path / "f.ldif", ["m1"])
        assert result.success
        data = result.value
        assert data is not None
        assert data.pipeline_status == "completed"
        assert data.parsed_entries == 1
        assert data.validation_status == "passed"
        assert data.transformation_status == "success"

    def test_run_full_pipeline_no_path(self) -> None:
        """Test pipeline fails when no file path and config path is empty."""
        config = FlextDbtLdifSettings.get_global()
        client = FlextDbtLdifClient.Client(config)
        result = client.run_full_pipeline()
        assert result.failure
