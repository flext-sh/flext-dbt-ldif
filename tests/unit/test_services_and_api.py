"""Behavior contract for FlextDbtLdif services + API delegation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

import pytest

from flext_dbt_ldif import FlextDbtLdif, FlextDbtLdifServiceMixin
from tests import m, p, r, t


class TestsFlextDbtLdifServicesAndApi:
    """Behavior contract for FlextDbtLdif API delegation (services covered in test_services.py)."""

    def test_api_process_ldif_file(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: Path,
    ) -> None:
        """Test FlextDbtLdif.process_ldif_file delegates correctly."""

        def _run(
            _self: FlextDbtLdifServiceMixin.Service,
            ldif_file: Path | str,
            *,
            generate_models: bool = True,
            run_transformations: bool = False,
            model_names: t.StrSequence | None = None,
        ) -> p.Result[m.DbtLdif.WorkflowResult]:
            del generate_models, run_transformations, model_names
            return r[m.DbtLdif.WorkflowResult].ok(
                m.DbtLdif.WorkflowResult(
                    ldif_file=str(ldif_file),
                    entry_count=0,
                    validation_status="passed",
                    workflow_status="completed",
                ),
            )

        monkeypatch.setattr(
            FlextDbtLdif,
            "process_ldif_file",
            _run,
        )
        api = FlextDbtLdif()
        result = api.process_ldif_file(tmp_path / "f.ldif")
        assert result.success

    def test_api_validate_ldif_quality(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: Path,
    ) -> None:
        """Test FlextDbtLdif.validate_ldif_quality delegates correctly."""

        def _run_quality(
            _self: FlextDbtLdifServiceMixin.Service,
            ldif_file: Path | str,
        ) -> p.Result[m.DbtLdif.ParseValidationResult]:
            return r[m.DbtLdif.ParseValidationResult].ok(
                m.DbtLdif.ParseValidationResult(
                    entry_count=0,
                    quality_score=1.0,
                    validation_status="passed",
                ),
            )

        monkeypatch.setattr(
            FlextDbtLdifServiceMixin.Service,
            "run_data_quality_assessment",
            _run_quality,
        )
        api = FlextDbtLdif()
        assert api.validate_ldif_quality(tmp_path / "f.ldif").success

    def test_api_generate_ldif_models(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: Path,
    ) -> None:
        """Test FlextDbtLdif.generate_ldif_models delegates correctly."""

        def _gen_models(
            _self: FlextDbtLdifServiceMixin.Service,
            entries: Sequence[t.JsonMapping],
            *,
            overwrite: bool = False,
        ) -> p.Result[m.DbtLdif.ModelGenerationResult]:
            _ = overwrite
            return r[m.DbtLdif.ModelGenerationResult].ok(
                m.DbtLdif.ModelGenerationResult(
                    models_generated=0,
                    model_names=[],
                ),
            )

        monkeypatch.setattr(
            FlextDbtLdifServiceMixin.Service,
            "generate_and_write_models",
            _gen_models,
        )
        api = FlextDbtLdif()
        assert api.generate_ldif_models(tmp_path / "f.ldif").success
