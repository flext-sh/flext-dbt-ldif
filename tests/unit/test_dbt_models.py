"""Behavioral tests for FLEXT DBT LDIF unified service and model contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from flext_tests import tm

from flext_dbt_ldif import FlextDbtLdifSettings
from flext_dbt_ldif.services.unified_service import FlextDbtLdifUnifiedService
from tests import c, m, p, t

if TYPE_CHECKING:
    from pathlib import Path


class TestsFlextDbtLdifDbtModels:
    """Public-contract tests for FlextDbtLdifUnifiedService and DbtModel."""

    @pytest.fixture
    def service(self) -> FlextDbtLdifUnifiedService.UnifiedService:
        """Provide a service instance backed by global settings."""
        return FlextDbtLdifUnifiedService.UnifiedService(
            settings=FlextDbtLdifSettings.fetch_global()
        )

    @staticmethod
    def _make_model(
        *,
        name: str = "test_model",
        ldif_source: str = "ldif_entries",
        sql_content: str = "select 1",
    ) -> p.DbtLdif.DbtModel:
        """Build a DbtModel via its public constructor."""
        return m.DbtLdif.DbtModel(
            name=name,
            dbt_model_type="staging",
            ldif_source=ldif_source,
            sql_content=sql_content,
            columns=[],
            dependencies=[],
        )

    # -- service construction -------------------------------------------------

    def test_service_exposes_configured_project_dir_and_default_name(
        self, tmp_path: Path
    ) -> None:
        """Constructor arguments surface through public fields."""
        gen = FlextDbtLdifUnifiedService.UnifiedService(
            settings=FlextDbtLdifSettings.fetch_global(), project_dir=tmp_path
        )
        tm.that(gen.project_dir, eq=tmp_path)
        tm.that(gen.name, eq="ldif_generator")

    # -- execute --------------------------------------------------------------

    def test_execute_returns_ready_metadata_payload(
        self, service: FlextDbtLdifUnifiedService.UnifiedService
    ) -> None:
        """Execute succeeds and reports the ready status contract."""
        result = service.execute()
        tm.ok(result)
        data: t.JsonMapping = result.unwrap()
        tm.that(data["name"], eq="ldif_generator")
        tm.that(data["status"], eq="ready")

    def test_execute_metadata_reflects_project_dir(self, tmp_path: Path) -> None:
        """Execute payload echoes the configured project directory."""
        gen = FlextDbtLdifUnifiedService.UnifiedService(
            settings=FlextDbtLdifSettings.fetch_global(), project_dir=tmp_path
        )
        data = gen.execute().unwrap()
        tm.that(data["project_dir"], eq=str(tmp_path))

    # -- staging generation ---------------------------------------------------

    def test_generate_staging_models_emits_view_model_for_entries(
        self, service: FlextDbtLdifUnifiedService.UnifiedService
    ) -> None:
        """Non-empty entries yield exactly one staging view model."""
        entries: t.SequenceOf[t.JsonMapping] = [{"dn": "cn=test,dc=example,dc=org"}]
        models = service.generate_staging_models(entries).unwrap()
        tm.that(len(models), eq=1)
        model = models[0]
        tm.that(model.name, eq="stg_ldif_entries")
        tm.that(model.dbt_model_type, eq="staging")
        tm.that(model.materialization, eq="view")

    def test_generate_staging_models_returns_empty_without_entries(
        self, service: FlextDbtLdifUnifiedService.UnifiedService
    ) -> None:
        """Empty entries yield an empty, successful result."""
        result = service.generate_staging_models([])
        tm.ok(result)
        tm.that(result.unwrap(), eq=[])

    # -- analytics generation -------------------------------------------------

    def test_generate_analytics_models_emits_table_model_from_staging(
        self, service: FlextDbtLdifUnifiedService.UnifiedService
    ) -> None:
        """A staging model produces one analytics table model."""
        staging_model = self._make_model(name="stg_ldif_entries")
        models = service.generate_analytics_models([staging_model]).unwrap()
        tm.that(len(models), eq=1)
        model = models[0]
        tm.that(model.name, eq="analytics_ldif_insights")
        tm.that(model.dbt_model_type, eq="analytics")
        tm.that(model.materialization, eq="table")

    def test_generate_analytics_models_returns_empty_without_staging(
        self, service: FlextDbtLdifUnifiedService.UnifiedService
    ) -> None:
        """No staging models yields an empty, successful result."""
        result = service.generate_analytics_models([])
        tm.ok(result)
        tm.that(result.unwrap(), eq=[])

    # -- model contract -------------------------------------------------------

    def test_dbt_model_defaults_exposed_via_public_api(self) -> None:
        """Optional fields default to their documented values."""
        model = self._make_model()
        tm.that(model.name, eq="test_model")
        tm.that(model.materialization, eq="view")
        tm.that(model.description, eq="")
        tm.that(list(model.columns), eq=[])
        tm.that(list(model.dependencies), eq=[])

    def test_complete_model_constructs_via_public_api(self) -> None:
        """A fully populated model constructs successfully through its public API."""
        model = self._make_model()
        tm.that(model.name, eq="test_model")
        tm.that(model.ldif_source, eq="ldif_entries")
        tm.that(model.sql_content, eq="select 1")

    @pytest.mark.parametrize(
        ("field", "kwargs"),
        [
            ("name", {"name": "  "}),
            ("ldif_source", {"ldif_source": "  "}),
            ("sql_content", {"sql_content": "  "}),
        ],
    )
    def test_blank_required_field_rejected_at_construction(
        self, field: str, kwargs: dict[str, str]
    ) -> None:
        """Blank required fields (t.StrippedStr) fail validation naming the field."""
        with pytest.raises(c.ValidationError) as exc_info:
            self._make_model(**kwargs)
        tm.that(str(exc_info.value), has=field)


__all__ = ["TestsFlextDbtLdifDbtModels"]
