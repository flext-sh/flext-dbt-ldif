"""Unit tests for DBT client functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path
from typing import cast

import pytest
from flext_core import FlextCore

from flext_dbt_ldif import FlextDbtLdifClient, FlextDbtLdifConfig


@pytest.fixture
def client() -> FlextDbtLdifClient:
    """Create a test client."""
    return FlextDbtLdifClient(FlextDbtLdifConfig())


def test_parse_ldif_file_ok(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    client: FlextDbtLdifClient,
) -> None:
    """Test parsing LDIF file."""

    def _parse_file(
        _self: object, __path: Path
    ) -> FlextCore.Result[FlextCore.Types.List]:
        return FlextCore.Result[FlextCore.Types.List].ok([])

    monkeypatch.setattr(
        client,
        "_ldif_api",
        type("X", (), {"parse_file": _parse_file})(),
    )
    result = client.parse_ldif_file(tmp_path / "dummy.ldif")
    assert result.is_success
    assert isinstance(result.value, list)


def test_validate_ldif_data_ok(
    monkeypatch: pytest.MonkeyPatch,
    client: FlextDbtLdifClient,
) -> None:
    """Test validating LDIF data."""

    def _validate(
        _self: object,
        _entries: FlextCore.Types.List,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        return FlextCore.Result[FlextCore.Types.Dict].ok({})

    def _stats(
        _self: object,
        _entries: FlextCore.Types.List,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        return FlextCore.Result[FlextCore.Types.Dict].ok({"quality_score": 0.95})

    api = type("API", (), {"validate": _validate, "get_entry_statistics": _stats})()
    monkeypatch.setattr(client, "_ldif_api", api)

    result = client.validate_ldif_data(cast("FlextCore.Types.List", []))
    assert result.is_success
    data = result.value or {}
    assert data.get("quality_score") == 0.95
    assert data.get("validation_status") == "passed"


def test_transform_with_dbt_ok(
    monkeypatch: pytest.MonkeyPatch,
    client: FlextDbtLdifClient,
) -> None:
    """Test transforming with DBT."""

    def _prep(
        _self: FlextDbtLdifClient,
        _entries: FlextCore.Types.List,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        return FlextCore.Result[FlextCore.Types.Dict].ok({"prepared": True})

    monkeypatch.setattr(FlextDbtLdifClient, "_prepare_ldif_data_for_dbt", _prep)
    # Preload hub to avoid real initialization
    client._dbt_hub = cast("object", object())

    result = client.transform_with_dbt(cast("FlextCore.Types.List", []), ["m1", "m2"])
    assert result.is_success
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
    ) -> FlextCore.Result[FlextCore.Types.List]:
        return FlextCore.Result[FlextCore.Types.List].ok([])

    def _validate(
        _self: FlextDbtLdifClient,
        _entries: FlextCore.Types.List,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        return FlextCore.Result[FlextCore.Types.Dict].ok({"quality_score": 0.9})

    def _transform(
        _self: FlextDbtLdifClient,
        _entries: FlextCore.Types.List,
        _models: FlextCore.Types.StringList | None,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        return FlextCore.Result[FlextCore.Types.Dict].ok({"ran": True})

    monkeypatch.setattr(FlextDbtLdifClient, "parse_ldif_file", _parse)
    monkeypatch.setattr(FlextDbtLdifClient, "validate_ldif_data", _validate)
    monkeypatch.setattr(FlextDbtLdifClient, "transform_with_dbt", _transform)

    result = client.run_full_pipeline(tmp_path / "f.ldif", ["m1"])
    assert result.is_success
    data = result.value or {}
    assert data.get("pipeline_status") == "completed"
