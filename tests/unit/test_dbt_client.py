"""Behavioral tests for the FlextDbtLdifClient public contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path

import pytest
from flext_tests import tm

from flext_dbt_ldif import FlextDbtLdifSettings, settings
from flext_dbt_ldif.services.client import FlextDbtLdifClient
from tests import c, m, t


class TestsFlextDbtLdifClient:
    """Behavioral contract of FlextDbtLdifClient.Client public operations."""

    # ---- construction contract -------------------------------------------

    @staticmethod
    def test_default_construction_yields_usable_global_settings() -> None:
        """A client built without settings exposes usable global settings."""
        client = FlextDbtLdifClient.Client()
        tm.that(client.settings, is_=FlextDbtLdifSettings)

    @staticmethod
    def test_explicit_settings_are_the_ones_used() -> None:
        """Explicit settings are the settings the client operates on."""
        client = FlextDbtLdifClient.Client(settings)
        assert client.settings is settings

    # ---- parse_ldif_file contract ----------------------------------------

    @staticmethod
    def test_parse_with_explicit_path_returns_entry_tagged_with_source(
        tmp_path: Path,
    ) -> None:
        """Parsing echoes the requested path as the entry source."""
        path = tmp_path / "dummy.ldif"
        result = FlextDbtLdifClient.Client().parse_ldif_file(path)

        entries = result.unwrap()
        tm.that(entries, eq=[{"dn": c.DbtLdif.SAMPLE_LDIF_DN, "source": str(path)}])

    @staticmethod
    def test_parse_is_idempotent_for_same_path(tmp_path: Path) -> None:
        """Parsing the same path twice yields equal payloads."""
        client = FlextDbtLdifClient.Client()
        path = tmp_path / "same.ldif"

        tm.that(
            client.parse_ldif_file(path).unwrap(),
            eq=(client.parse_ldif_file(path).unwrap()),
        )

    @staticmethod
    def test_parse_without_path_and_empty_settings_fails_with_reason() -> None:
        """Absent path plus empty settings path is a required-input failure."""
        client = FlextDbtLdifClient.Client(FlextDbtLdifSettings.fetch_global())
        result = client.parse_ldif_file()

        tm.fail(result)
        tm.that((result.error or "").lower(), has="required")

    # ---- validate_ldif_data contract -------------------------------------

    @staticmethod
    @pytest.mark.parametrize("entry_count", [1, 3, 10])
    def test_validation_reports_entry_count_and_passing_status(
        entry_count: int,
    ) -> None:
        """Non-empty entries validate as passed with matching totals."""
        entries: t.SequenceOf[t.JsonMapping] = [
            {"dn": f"cn=n{i},dc=example,dc=org", "source": "in.ldif"}
            for i in range(entry_count)
        ]
        data = FlextDbtLdifClient.Client().validate_ldif_data(entries).unwrap()

        tm.that(data, is_=m.DbtLdif.LdifValidationResult)
        tm.that(data.total_entries, eq=entry_count)
        tm.that(data.validation_status, eq=c.DbtLdif.VALIDATION_STATUS_PASSED)
        tm.that(data.quality_score, eq=pytest.approx(c.DbtLdif.DEFAULT_QUALITY_SCORE))

    @staticmethod
    def test_validation_of_empty_entries_fails_with_reason() -> None:
        """Empty entries cannot validate and explain why."""
        result = FlextDbtLdifClient.Client().validate_ldif_data([])

        tm.fail(result)
        tm.that((result.error or "").lower(), has="no ldif entries")

    # ---- transform_with_dbt contract -------------------------------------

    @staticmethod
    def test_transform_reports_record_count_and_requested_models() -> None:
        """Transform metadata reflects inputs and reports success."""
        entries: t.SequenceOf[t.JsonMapping] = [{"dn": "cn=t,dc=example,dc=org"}]
        data = (
            FlextDbtLdifClient
            .Client()
            .transform_with_dbt(entries, ["m1", "m2"])
            .unwrap()
        )

        tm.that(data.records, eq=1)
        tm.that(list(data.models), eq=["m1", "m2"])
        tm.that(data.status, eq=c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS)

    @staticmethod
    def test_transform_without_models_uses_default_staging_and_analytics() -> None:
        """Omitting model names falls back to the default model set."""
        data = FlextDbtLdifClient.Client().transform_with_dbt([], None).unwrap()

        tm.that(
            list(data.models),
            eq=[c.DbtLdif.STAGING_MODEL_NAME, c.DbtLdif.ANALYTICS_MODEL_NAME],
        )
        tm.that(data.records, eq=0)

    # ---- run_full_pipeline contract --------------------------------------

    @staticmethod
    def test_pipeline_completes_and_aggregates_stage_statuses(
        tmp_path: Path,
    ) -> None:
        """A valid path drives parse+validate+transform to a completed result."""
        result = FlextDbtLdifClient.Client().run_full_pipeline(
            tmp_path / "f.ldif", ["m1"],
        )
        data = result.unwrap()

        tm.that(data, is_=m.DbtLdif.PipelineResult)
        tm.that(data.pipeline_status, eq=c.DbtLdif.WORKFLOW_STATUS_COMPLETED)
        tm.that(data.parsed_entries, eq=1)
        tm.that(data.validation_status, eq=c.DbtLdif.VALIDATION_STATUS_PASSED)
        tm.that(data.transformation_status, eq=c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS)

    @staticmethod
    def test_pipeline_propagates_parse_failure() -> None:
        """A parse failure short-circuits the whole pipeline as a failure."""
        client = FlextDbtLdifClient.Client(FlextDbtLdifSettings.fetch_global())
        result = client.run_full_pipeline()

        tm.fail(result)
        tm.that((result.error or "").lower(), has="required")

    # ---- result composition contract -------------------------------------

    @staticmethod
    def test_parse_result_chains_into_validation_via_flat_map(
        tmp_path: Path,
    ) -> None:
        """Parse -> validate composes as monadic r[T] without manual unwrap."""
        client = FlextDbtLdifClient.Client()
        chained = client.parse_ldif_file(tmp_path / "c.ldif").flat_map(
            client.validate_ldif_data,
        )

        tm.ok(chained)
        tm.that(chained.unwrap().total_entries, eq=1)

    @staticmethod
    def test_transform_result_serializes_public_state_via_model_dump() -> None:
        """Public model state is exposed through model_dump for consumers."""
        data = (
            FlextDbtLdifClient
            .Client()
            .transform_with_dbt([{"dn": "cn=a"}], ["only"])
            .unwrap()
        )
        dumped = data.model_dump()

        tm.that(dumped["records"], eq=1)
        tm.that(list(dumped["models"]), eq=["only"])
        tm.that(dumped["status"], eq=c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS)
