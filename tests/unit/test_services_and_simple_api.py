"""Test services and simple API functionality.

This module tests the services and simple API functionality of flext-dbt-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

import pytest
from flext_core import FlextResult

from flext_dbt_ldif.dbt_services import FlextDbtLdifService
from flext_dbt_ldif.simple_api import (
    generate_ldif_models,
    process_ldif_file,
    validate_ldif_quality,
)

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def service(tmp_path: Path) -> FlextDbtLdifService:
    """Create a test service."""
    return FlextDbtLdifService(project_dir=tmp_path)


def test_parse_and_validate_ldif_ok(
    monkeypatch: pytest.MonkeyPatch, service: FlextDbtLdifService, tmp_path: Path,
) -> None:
    """Test parsing and validating LDIF."""
    monkeypatch.setattr(
        service.client,
        "parse_ldif_file",
        lambda ldif_file: FlextResult.ok([]),  # type: ignore[no-any-return]
    )
    monkeypatch.setattr(
        service.client,
        "validate_ldif_data",
        lambda entries: FlextResult.ok({"quality_score": 0.91}),  # type: ignore[no-any-return]
    )

    result = service.parse_and_validate_ldif(tmp_path / "x.ldif")
    assert result.success
    data = result.data or {}
    assert data.get("status") == "validated"


def test_generate_and_write_models_ok(
    monkeypatch: pytest.MonkeyPatch, service: FlextDbtLdifService,
) -> None:
    """Test generating and writing models."""

    def _gen_stg(entries: list[object]) -> FlextResult[list[Any]]:
        return FlextResult.ok([cast("Any", object())])

    def _gen_an(models: list[Any]) -> FlextResult[list[Any]]:
        return FlextResult.ok([cast("Any", object())])

    def _write(
        models: list[Any], *, overwrite: bool = False,
    ) -> FlextResult[dict[str, object]]:
        return FlextResult.ok({"written_files": ["f.sql", "f.yml"], "output_dir": "."})

    monkeypatch.setattr(service.model_generator, "generate_staging_models", _gen_stg)
    monkeypatch.setattr(service.model_generator, "generate_analytics_models", _gen_an)
    monkeypatch.setattr(service.model_generator, "write_models_to_disk", _write)

    result = service.generate_and_write_models(cast("list[object]", []))
    assert result.success
    assert isinstance(result.data, dict)


def test_simple_api_helpers(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Test simple API helpers."""

    def _run(
        self: FlextDbtLdifService,
        ldif_file: Path | str,
        *,
        generate_models: bool = True,
        run_transformations: bool = False,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, object]]:
        return FlextResult.ok({"ok": True})

    monkeypatch.setattr(FlextDbtLdifService, "run_complete_workflow", _run)

    assert process_ldif_file(tmp_path / "f.ldif").success

    # Patch validation path to avoid real file read
    def _run_quality(
        self: FlextDbtLdifService, ldif_file: Path | str,
    ) -> FlextResult[dict[str, object]]:
        return FlextResult.ok({"ok": True})

    monkeypatch.setattr(
        FlextDbtLdifService, "run_data_quality_assessment", _run_quality,
    )
    assert validate_ldif_quality(tmp_path / "f.ldif").success

    def _parse_val(
        self: FlextDbtLdifService, ldif_file: Path | str,
    ) -> FlextResult[dict[str, object]]:
        return FlextResult.ok({"entries": []})

    def _gen_models(
        self: FlextDbtLdifService, entries: list[object], *, overwrite: bool = False,
    ) -> FlextResult[dict[str, object]]:
        return FlextResult.ok({"total_models": 0})

    monkeypatch.setattr(FlextDbtLdifService, "parse_and_validate_ldif", _parse_val)
    monkeypatch.setattr(FlextDbtLdifService, "generate_and_write_models", _gen_models)

    assert generate_ldif_models(tmp_path / "f.ldif").success
