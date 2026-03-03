"""Test services and API for FLEXT DBT LDIF.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path

import pytest
from flext_core import FlextResult

from flext_dbt_ldif import (
    FlextDbtLdif,
    FlextDbtLdifService,
    t,
)
from flext_dbt_ldif.models import FlextDbtLdifModels


@pytest.fixture
def service(tmp_path: Path) -> FlextDbtLdifService:
    """Create a test service."""
    return FlextDbtLdifService(project_dir=tmp_path)


def test_parse_and_validate_ldif_ok(
    monkeypatch: pytest.MonkeyPatch,
    service: FlextDbtLdifService,
    tmp_path: Path,
) -> None:
    """Test parsing and validating LDIF via service."""
    entries: list[dict[str, t.ContainerValue]] = [{"dn": "cn=test,dc=example,dc=org"}]
    monkeypatch.setattr(
        service.client,
        "parse_ldif_file",
        lambda _ldif_file: FlextResult[list[dict[str, t.ContainerValue]]].ok(entries),
    )
    monkeypatch.setattr(
        service.client,
        "validate_ldif_data",
        lambda _entries: FlextResult[dict[str, t.ContainerValue]].ok({
            "quality_score": 0.91,
        }),
    )

    result = service.parse_and_validate_ldif(tmp_path / "x.ldif")
    assert result.is_success
    data = result.value or {}
    assert "entries" in data
    assert data["entry_count"] == 1


def test_generate_and_write_models_ok(
    monkeypatch: pytest.MonkeyPatch,
    service: FlextDbtLdifService,
) -> None:
    """Test generating and writing models via service."""
    staging_model = FlextDbtLdifModels.DbtModel(
        name="stg_ldif_entries",
        dbt_model_type="staging",
        ldif_source="ldif_entries",
        sql_content="select * from raw",
    )
    analytics_model = FlextDbtLdifModels.DbtModel(
        name="analytics_ldif_insights",
        dbt_model_type="analytics",
        ldif_source="ldif_entries",
        sql_content="select * from stg",
    )

    gen = service.model_generator
    object.__setattr__(
        gen,
        "generate_staging_models",
        lambda _e: FlextResult[list[FlextDbtLdifModels.DbtModel]].ok([staging_model]),
    )
    object.__setattr__(
        gen,
        "generate_analytics_models",
        lambda _m: FlextResult[list[FlextDbtLdifModels.DbtModel]].ok([analytics_model]),
    )

    entries: list[dict[str, t.ContainerValue]] = [{"dn": "cn=test,dc=example,dc=org"}]
    result = service.generate_and_write_models(entries)
    assert result.is_success
    data = result.value or {}
    assert data["models_generated"] == 2


def test_api_process_ldif_file(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """Test FlextDbtLdif.process_ldif_file delegates correctly."""

    def _run(
        _self: FlextDbtLdifService,
        ldif_file: Path | str,
        *,
        generate_models: bool = True,
        run_transformations: bool = False,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, t.ContainerValue]]:
        return FlextResult[dict[str, t.ContainerValue]].ok({"ok": True})

    monkeypatch.setattr(FlextDbtLdifService, "run_complete_workflow", _run)

    api = FlextDbtLdif()
    result = api.process_ldif_file(tmp_path / "f.ldif")
    assert result.is_success


def test_api_validate_ldif_quality(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """Test FlextDbtLdif.validate_ldif_quality delegates correctly."""

    def _run_quality(
        _self: FlextDbtLdifService,
        _ldif_file: Path | str,
    ) -> FlextResult[dict[str, t.ContainerValue]]:
        return FlextResult[dict[str, t.ContainerValue]].ok({"ok": True})

    monkeypatch.setattr(
        FlextDbtLdifService,
        "run_data_quality_assessment",
        _run_quality,
    )

    api = FlextDbtLdif()
    assert api.validate_ldif_quality(tmp_path / "f.ldif").is_success


def test_api_generate_ldif_models(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """Test FlextDbtLdif.generate_ldif_models delegates correctly."""

    def _parse_val(
        _self: FlextDbtLdifService,
        _ldif_file: Path | str,
    ) -> FlextResult[dict[str, t.ContainerValue]]:
        return FlextResult[dict[str, t.ContainerValue]].ok({"entries": []})

    def _gen_models(
        _self: FlextDbtLdifService,
        _entries: list[dict[str, t.ContainerValue]],
        *,
        overwrite: bool = False,
    ) -> FlextResult[dict[str, t.ContainerValue]]:
        return FlextResult[dict[str, t.ContainerValue]].ok({"total_models": 0})

    monkeypatch.setattr(FlextDbtLdifService, "parse_and_validate_ldif", _parse_val)
    monkeypatch.setattr(FlextDbtLdifService, "generate_and_write_models", _gen_models)

    api = FlextDbtLdif()
    assert api.generate_ldif_models(tmp_path / "f.ldif").is_success
