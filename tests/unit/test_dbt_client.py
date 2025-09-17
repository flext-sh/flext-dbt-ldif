"""Unit tests for DBT client functionality."""

from __future__ import annotations

from pathlib import Path
from typing import cast

import pytest

from flext_core import FlextResult, FlextTypes
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

    def _parse_file(_self: object, __path: Path) -> FlextResult[FlextTypes.Core.List]:
        return FlextResult[None].ok([])

    monkeypatch.setattr(
        client,
        "_ldif_api",
        type("X", (), {"parse_file": _parse_file})(),
    )
    result = client.parse_ldif_file(tmp_path / "dummy.ldif")
    assert result.success
    assert isinstance(result.value, list)


def test_validate_ldif_data_ok(
    monkeypatch: pytest.MonkeyPatch,
    client: FlextDbtLdifClient,
) -> None:
    """Test validating LDIF data."""

    def _validate(
        _self: object, _entries: FlextTypes.Core.List
    ) -> FlextResult[FlextTypes.Core.Dict]:
        return FlextResult[None].ok(None)

    def _stats(
        _self: object, _entries: FlextTypes.Core.List
    ) -> FlextResult[FlextTypes.Core.Dict]:
        return FlextResult[None].ok({"quality_score": 0.95})

    api = type("API", (), {"validate": _validate, "get_entry_statistics": _stats})()
    monkeypatch.setattr(client, "_ldif_api", api)

    result = client.validate_ldif_data(cast("FlextTypes.Core.List", []))
    assert result.success
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
        _entries: FlextTypes.Core.List,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        return FlextResult[None].ok({"prepared": True})

    monkeypatch.setattr(FlextDbtLdifClient, "_prepare_ldif_data_for_dbt", _prep)
    # Preload hub to avoid real initialization
    client._dbt_hub = cast("object", object())

    result = client.transform_with_dbt(cast("FlextTypes.Core.List", []), ["m1", "m2"])
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
    ) -> FlextResult[FlextTypes.Core.List]:
        return FlextResult[None].ok([])

    def _validate(
        _self: FlextDbtLdifClient,
        _entries: FlextTypes.Core.List,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        return FlextResult[FlextTypes.Core.Dict].ok({"quality_score": 0.9})

    def _transform(
        _self: FlextDbtLdifClient,
        _entries: FlextTypes.Core.List,
        _models: FlextTypes.Core.StringList | None,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        return FlextResult[None].ok({"ran": True})

    monkeypatch.setattr(FlextDbtLdifClient, "parse_ldif_file", _parse)
    monkeypatch.setattr(FlextDbtLdifClient, "validate_ldif_data", _validate)
    monkeypatch.setattr(FlextDbtLdifClient, "transform_with_dbt", _transform)

    result = client.run_full_pipeline(tmp_path / "f.ldif", ["m1"])
    assert result.success
    data = result.value or {}
    assert data.get("pipeline_status") == "completed"
