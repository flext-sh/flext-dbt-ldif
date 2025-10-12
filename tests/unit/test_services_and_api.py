"""Test services and API for FLEXT DBT LDIF.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path
from typing import cast

import pytest
from flext_core import FlextCore

from flext_dbt_ldif import (
    FlextDbtLdifService,
    generate_ldif_models,
    process_ldif_file,
    validate_ldif_quality,
)


@pytest.fixture
def service(tmp_path: Path) -> FlextDbtLdifService:
    """Create a test service."""
    return FlextDbtLdifService(project_dir=tmp_path)


def test_parse_and_validate_ldif_ok(
    monkeypatch: pytest.MonkeyPatch,
    service: FlextDbtLdifService,
    tmp_path: Path,
) -> None:
    """Test parsing and validating LDIF."""
    monkeypatch.setattr(
        service.client,
        "parse_ldif_file",
        lambda _ldif_file: FlextCore.Result[FlextCore.Types.List].ok([]),
    )
    monkeypatch.setattr(
        service.client,
        "validate_ldif_data",
        lambda _entries: FlextCore.Result[FlextCore.Types.Dict].ok({
            "quality_score": 0.91
        }),
    )

    result = service.parse_and_validate_ldif(tmp_path / "x.ldif")
    assert result.is_success
    data = result.value or {}
    assert data.get("status") == "validated"


def test_generate_and_write_models_ok(
    monkeypatch: pytest.MonkeyPatch,
    service: FlextDbtLdifService,
) -> None:
    """Test generating and writing models."""

    def _gen_stg(
        _entries: FlextCore.Types.List,
    ) -> FlextCore.Result[FlextCore.Types.List]:
        return FlextCore.Result[FlextCore.Types.List].ok([cast("object", object())])

    def _gen_an(
        _models: FlextCore.Types.List,
    ) -> FlextCore.Result[FlextCore.Types.List]:
        return FlextCore.Result[FlextCore.Types.List].ok([cast("object", object())])

    def _write(
        _models: FlextCore.Types.List,
        *,
        _overwrite: bool = False,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        return FlextCore.Result[FlextCore.Types.Dict].ok(
            {
                "written_files": ["f.sql", "f.yml"],
                "output_dir": ".",
            },
        )

    monkeypatch.setattr(service.model_generator, "generate_staging_models", _gen_stg)
    monkeypatch.setattr(service.model_generator, "generate_analytics_models", _gen_an)
    monkeypatch.setattr(service.model_generator, "write_models_to_disk", _write)

    result = service.generate_and_write_models(cast("FlextCore.Types.List", []))
    assert result.is_success
    assert isinstance(result.value, dict)


def test_monkeypatch(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Test simple API helpers."""

    def _run(
        _self: FlextDbtLdifService,
        _ldif_file: Path | str,
        *,
        _generate_models: bool = True,
        _run_transformations: bool = False,
        _model_names: FlextCore.Types.StringList | None = None,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        return FlextCore.Result[FlextCore.Types.Dict].ok({"ok": True})

    monkeypatch.setattr(FlextDbtLdifService, "run_complete_workflow", _run)

    assert process_ldif_file(tmp_path / "f.ldif").is_success

    # Patch validation path to avoid real file read
    def _run_quality(
        _self: FlextDbtLdifService,
        _ldif_file: Path | str,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        return FlextCore.Result[FlextCore.Types.Dict].ok({"ok": True})

    monkeypatch.setattr(
        FlextDbtLdifService,
        "run_data_quality_assessment",
        _run_quality,
    )
    assert validate_ldif_quality(tmp_path / "f.ldif").is_success

    def _parse_val(
        _self: FlextDbtLdifService,
        _ldif_file: Path | str,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        return FlextCore.Result[FlextCore.Types.Dict].ok({"entries": []})

    def _gen_models(
        _self: FlextDbtLdifService,
        _entries: FlextCore.Types.List,
        *,
        _overwrite: bool = False,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        return FlextCore.Result[FlextCore.Types.Dict].ok({"total_models": 0})

    monkeypatch.setattr(FlextDbtLdifService, "parse_and_validate_ldif", _parse_val)
    monkeypatch.setattr(FlextDbtLdifService, "generate_and_write_models", _gen_models)

    assert generate_ldif_models(tmp_path / "f.ldif").is_success
