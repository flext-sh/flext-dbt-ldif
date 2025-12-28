"""Unit tests for DBT client functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path

import pytest
from flext_core import FlextTypes as t, FlextResult

from flext_dbt_ldif import FlextDbtLdifClient, FlextDbtLdifSettings


@pytest.fixture
def client() -> FlextDbtLdifClient:
    """Create a test client."""
    return FlextDbtLdifClient(FlextDbtLdifSettings())


def test_parse_ldif_file_ok(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    client: FlextDbtLdifClient,
) -> None:
    """Test parsing LDIF file."""

    def _parse_file(_self: object, __path: Path) -> FlextResult[list[t.GeneralValueType]]:
        return FlextResult[list[t.GeneralValueType]].ok([])

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
        _entries: list[t.GeneralValueType],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        return FlextResult[dict[str, t.GeneralValueType]].ok({})

    def _stats(
        _self: object,
        _entries: list[t.GeneralValueType],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        return FlextResult[dict[str, t.GeneralValueType]].ok({"quality_score": 0.95})

    api = type("API", (), {"validate": _validate, "get_entry_statistics": _stats})()
    monkeypatch.setattr(client, "_ldif_api", api)

    empty_entries: list[t.GeneralValueType] = []
    result = client.validate_ldif_data(empty_entries)
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
        _entries: list[t.GeneralValueType],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        return FlextResult[dict[str, t.GeneralValueType]].ok({"prepared": True})

    monkeypatch.setattr(FlextDbtLdifClient, "_prepare_ldif_data_for_dbt", _prep)
    # Preload hub to avoid real initialization
    client._dbt_hub = object()  # type: ignore[assignment]

    empty_entries: list[t.GeneralValueType] = []
    result = client.transform_with_dbt(empty_entries, ["m1", "m2"])
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
    ) -> FlextResult[list[t.GeneralValueType]]:
        return FlextResult[list[t.GeneralValueType]].ok([])

    def _validate(
        _self: FlextDbtLdifClient,
        _entries: list[t.GeneralValueType],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        return FlextResult[dict[str, t.GeneralValueType]].ok({"quality_score": 0.9})

    def _transform(
        _self: FlextDbtLdifClient,
        _entries: list[t.GeneralValueType],
        _models: list[str] | None,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        return FlextResult[dict[str, t.GeneralValueType]].ok({"ran": True})

    monkeypatch.setattr(FlextDbtLdifClient, "parse_ldif_file", _parse)
    monkeypatch.setattr(FlextDbtLdifClient, "validate_ldif_data", _validate)
    monkeypatch.setattr(FlextDbtLdifClient, "transform_with_dbt", _transform)

    result = client.run_full_pipeline(tmp_path / "f.ldif", ["m1"])
    assert result.is_success
    data = result.value or {}
    assert data.get("pipeline_status") == "completed"
