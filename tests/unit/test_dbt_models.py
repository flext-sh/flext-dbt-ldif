"""Behavioral tests for FLEXT DBT LDIF unified service and model contract.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path

import pytest

from flext_dbt_ldif import FlextDbtLdifSettings
from flext_dbt_ldif.services.unified_service import FlextDbtLdifUnifiedService
from tests import c, m, t, tm


class TestsFlextDbtLdifDbtModels:
    """Public-contract tests for FlextDbtLdifUnifiedService and DbtModel."""

    @pytest.fixture
    @staticmethod
    def service() -> FlextDbtLdifUnifiedService.UnifiedService:
        """Provide a service instance backed by global settings.

        Returns:
            The resulting ``FlextDbtLdifUnifiedService.UnifiedService``.

        """
        return FlextDbtLdifUnifiedService.UnifiedService(
            settings=FlextDbtLdifSettings.fetch_global(),
        )

    # -- service construction -------------------------------------------------

    @staticmethod
    def test_service_exposes_configured_project_dir_and_default_name(
        tmp_path: Path,
    ) -> None:
        """Constructor arguments surface through public fields."""
        gen = FlextDbtLdifUnifiedService.UnifiedService(
            settings=FlextDbtLdifSettings.fetch_global(),
            project_dir=tmp_path,
        )
        tm.that(gen.project_dir, eq=tmp_path)
        tm.that(gen.name, eq=c.DbtLdif.GENERATOR_SERVICE_NAME)

    # -- execute --------------------------------------------------------------

    @staticmethod
    def test_execute_returns_ready_metadata_payload(
        service: FlextDbtLdifUnifiedService.UnifiedService,
    ) -> None:
        """Execute succeeds and reports the ready status contract."""
        result = service.execute()
        tm.ok(result)
        data: t.JsonMapping = result.unwrap()
        tm.that(data["name"], eq=c.DbtLdif.GENERATOR_SERVICE_NAME)
        tm.that(data["status"], eq=c.DbtLdif.WORKFLOW_STATUS_READY)

    @staticmethod
    def test_execute_metadata_reflects_project_dir(tmp_path: Path) -> None:
        """Execute payload echoes the configured project directory."""
        gen = FlextDbtLdifUnifiedService.UnifiedService(
            settings=FlextDbtLdifSettings.fetch_global(),
            project_dir=tmp_path,
        )
        data = gen.execute().unwrap()
        tm.that(data["project_dir"], eq=str(tmp_path))

    # -- staging generation ---------------------------------------------------

    @staticmethod
    def test_generate_staging_models_emits_view_model_for_entries(
        service: FlextDbtLdifUnifiedService.UnifiedService,
    ) -> None:
        """Non-empty entries yield exactly one staging view model."""
        entries: t.SequenceOf[t.JsonMapping] = [{"dn": "cn=test,dc=example,dc=org"}]
        models = service.generate_staging_models(entries).unwrap()
        tm.that(len(models), eq=1)
        model = models[0]
        tm.that(model.name, eq=c.DbtLdif.STAGING_MODEL_NAME)
        tm.that(model.dbt_model_type, eq=c.DbtLdif.DBT_MODEL_TYPE_STAGING)
        tm.that(model.materialization, eq=c.DbtLdif.DBT_MATERIALIZATION_VIEW)
        tm.that(model.description, eq=c.DbtLdif.STAGING_MODEL_DESCRIPTION)

    @staticmethod
    def test_generate_staging_models_returns_empty_without_entries(
        service: FlextDbtLdifUnifiedService.UnifiedService,
    ) -> None:
        """Empty entries yield an empty, successful result."""
        result = service.generate_staging_models([])
        tm.ok(result)
        tm.that(result.unwrap(), eq=[])

    # -- analytics generation -------------------------------------------------

    @staticmethod
    def test_generate_analytics_models_emits_table_model_from_staging(
        service: FlextDbtLdifUnifiedService.UnifiedService,
    ) -> None:
        """A staging model produces one analytics table model."""
        staging_model = m.DbtLdif.DbtModel(
            name=c.DbtLdif.STAGING_MODEL_NAME,
            dbt_model_type=c.DbtLdif.DBT_MODEL_TYPE_STAGING,
            ldif_source=c.DbtLdif.LDIF_SOURCE_NAME,
            materialization=c.DbtLdif.DBT_MATERIALIZATION_VIEW,
            sql_content="select 1",
            description=c.DbtLdif.STAGING_MODEL_DESCRIPTION,
            columns=[],
            dependencies=[],
        )
        models = service.generate_analytics_models([staging_model]).unwrap()
        tm.that(len(models), eq=1)
        model = models[0]
        tm.that(model.name, eq=c.DbtLdif.ANALYTICS_MODEL_NAME)
        tm.that(model.dbt_model_type, eq=c.DbtLdif.DBT_MODEL_TYPE_ANALYTICS)
        tm.that(model.materialization, eq=c.DbtLdif.DBT_MATERIALIZATION_TABLE)
        tm.that(model.description, eq=c.DbtLdif.ANALYTICS_MODEL_DESCRIPTION)
        tm.that(model.dependencies, has=c.DbtLdif.STAGING_MODEL_NAME)

    @staticmethod
    def test_generate_analytics_models_returns_empty_without_staging(
        service: FlextDbtLdifUnifiedService.UnifiedService,
    ) -> None:
        """No staging models yields an empty, successful result."""
        result = service.generate_analytics_models([])
        tm.ok(result)
        tm.that(result.unwrap(), eq=[])

    # -- model contract -------------------------------------------------------

    @staticmethod
    def test_dbt_model_defaults_and_public_fields() -> None:
        """Optional fields default and required fields echo through the public API."""
        model = m.DbtLdif.DbtModel(
            name="test_model",
            dbt_model_type=c.DbtLdif.DBT_MODEL_TYPE_STAGING,
            ldif_source=c.DbtLdif.LDIF_SOURCE_NAME,
            sql_content="select 1",
        )
        tm.that(model.name, eq="test_model")
        tm.that(model.materialization, eq=c.DbtLdif.DBT_MATERIALIZATION_VIEW)
        tm.that(model.description, eq="")
        tm.that(list(model.columns), eq=[])
        tm.that(list(model.dependencies), eq=[])
        tm.that(model.ldif_source, eq=c.DbtLdif.LDIF_SOURCE_NAME)
        tm.that(model.sql_content, eq="select 1")

    @staticmethod
    @pytest.mark.parametrize(
        ("field", "kwargs"),
        [
            ("name", {"name": "  "}),
            ("ldif_source", {"ldif_source": "  "}),
            ("sql_content", {"sql_content": "  "}),
        ],
    )
    def test_blank_required_field_rejected_at_construction(
        field: str,
        kwargs: t.StrMapping,
    ) -> None:
        """Blank required fields (t.StrippedStr) fail validation naming the field."""
        with pytest.raises(c.ValidationError) as exc_info:
            m.DbtLdif.DbtModel.model_validate({
                "name": "test_model",
                "dbt_model_type": c.DbtLdif.DBT_MODEL_TYPE_STAGING,
                "ldif_source": c.DbtLdif.LDIF_SOURCE_NAME,
                "sql_content": "select 1",
                **kwargs,
            })
        tm.that(str(exc_info.value), has=field)
