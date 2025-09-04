"""Test DBT client functionality.

This module tests the DBT client functionality of flext-dbt-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path
from typing import cast

import pytest
from flext_core import FlextResult

from flext_dbt_ldif import FlextDbtLdifClient, FlextDbtLdifConfig
from flext_dbt_ldif.dbt_exceptions import (
    FlextDbtLdifConfigurationError,
    FlextDbtLdifProcessingError,
)


@pytest.fixture
def client() -> FlextDbtLdifClient:
    """Create a test client."""
    return FlextDbtLdifClient(FlextDbtLdifConfig())


def test_client_initialization_validates_config() -> None:
    """Test that client initialization validates configuration."""
    # Invalid configuration should raise exception
    invalid_config = FlextDbtLdifConfig(ldif_max_file_size=-1)
    
    with pytest.raises(FlextDbtLdifConfigurationError):
        FlextDbtLdifClient(invalid_config)


def test_parse_ldif_file_with_nonexistent_file_raises_exception(
    client: FlextDbtLdifClient,
) -> None:
    """Test that parsing nonexistent file raises appropriate exception."""
    nonexistent_path = Path("/nonexistent/file.ldif")
    
    with pytest.raises(FlextDbtLdifProcessingError) as exc_info:
        client.parse_ldif_file(nonexistent_path)
    
    assert "FILE_NOT_FOUND" in str(exc_info.value)
    assert "not found" in str(exc_info.value)


def test_parse_ldif_file_ok(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    client: FlextDbtLdifClient,
) -> None:
    """Test parsing LDIF file."""

    def _parse_file(_self: object, _path: Path) -> FlextResult[list[object]]:
        return FlextResult[list[object]].ok([])

    # Create a dummy file to avoid FILE_NOT_FOUND error
    dummy_file = tmp_path / "dummy.ldif"
    dummy_file.write_text("dn: cn=test\nobjectClass: person\n")

    monkeypatch.setattr(
        client,
        "_ldif_api",
        type("X", (), {"parse_file": _parse_file})(),
    )
    
    # Now this returns the entries directly, not a FlextResult
    entries = client.parse_ldif_file(dummy_file)
    assert isinstance(entries, list)


def test_validate_ldif_data_ok(
    monkeypatch: pytest.MonkeyPatch,
    client: FlextDbtLdifClient,
) -> None:
    """Test validating LDIF data."""

    def _validate(
        _self: object, _entries: list[object]
    ) -> FlextResult[dict[str, object]]:
        return FlextResult[dict[str, object]].ok({})

    def _stats(_self: object, _entries: list[object]) -> FlextResult[dict[str, object]]:
        return FlextResult[dict[str, object]].ok({"quality_score": 0.95})

    api = type("API", (), {"validate": _validate, "get_entry_statistics": _stats})()
    monkeypatch.setattr(client, "_ldif_api", api)

    # Now this returns the validation metrics directly, not a FlextResult
    validation_metrics = client.validate_ldif_data([])
    assert validation_metrics.get("quality_score") == 0.95
    assert validation_metrics.get("validation_status") == "passed"


def test_transform_with_dbt_ok(
    monkeypatch: pytest.MonkeyPatch,
    client: FlextDbtLdifClient,
) -> None:
    """Test transforming with DBT."""

    def _prep(
        _self: FlextDbtLdifClient,
        _entries: list[object],
    ) -> FlextResult[dict[str, object]]:
        return FlextResult[dict[str, object]].ok({"prepared": True})

    # Mock the dbt_hub to avoid real initialization
    mock_hub = type("MockHub", (), {
        "run_models": lambda *args, **kwargs: FlextResult[dict[str, object]].ok({"success": True}),
        "run_all": lambda *args, **kwargs: FlextResult[dict[str, object]].ok({"success": True}),
    })()

    monkeypatch.setattr(FlextDbtLdifClient, "_prepare_ldif_data_for_dbt", _prep)
    monkeypatch.setattr(client, "_dbt_hub", mock_hub)

    result = client.transform_with_dbt([], ["m1", "m2"])
    assert result.success
    assert isinstance(result.value, dict)


def test_run_full_pipeline_ok(
    monkeypatch: pytest.MonkeyPatch,
    client: FlextDbtLdifClient,
    tmp_path: Path,
) -> None:
    """Test running full pipeline."""

    def _parse(
        _self: FlextDbtLdifClient,
        _file: Path | str | None = None,
    ) -> list[object]:
        return []

    def _validate(
        _self: FlextDbtLdifClient,
        _entries: list[object],
    ) -> dict[str, object]:
        return {"quality_score": 0.9}

    def _transform(
        _self: FlextDbtLdifClient,
        _entries: list[object],
        _models: list[str] | None,
    ) -> FlextResult[dict[str, object]]:
        return FlextResult[dict[str, object]].ok({"ran": True})

    monkeypatch.setattr(FlextDbtLdifClient, "parse_ldif_file", _parse)
    monkeypatch.setattr(FlextDbtLdifClient, "validate_ldif_data", _validate)
    monkeypatch.setattr(FlextDbtLdifClient, "transform_with_dbt", _transform)

    result = client.run_full_pipeline(tmp_path / "f.ldif", ["m1"])
    assert result.success
    data = result.value or {}
    assert data.get("pipeline_status") == "completed"
