"""Behavioral tests for the FlextDbtLdifClient public contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

# NOTE (multi-agent): mro-rn88 — import settings singleton (same family as base.py fix).
from flext_dbt_ldif import FlextDbtLdifSettings, c, m, settings
from flext_dbt_ldif.services.client import FlextDbtLdifClient

if TYPE_CHECKING:
    from pathlib import Path

    from tests.typings import t

__all__: list[str] = [
    "TestsFlextDbtLdifClient",
]


class TestsFlextDbtLdifClient:
    """Behavioral contract of FlextDbtLdifClient.Client public operations."""

    # ---- construction contract -------------------------------------------

    def test_default_construction_yields_usable_global_settings(self) -> None:
        """A client built without settings exposes usable global settings."""
        client = FlextDbtLdifClient.Client()
        assert isinstance(client.settings, FlextDbtLdifSettings)

    def test_explicit_settings_are_the_ones_used(self) -> None:
        """Explicit settings are the settings the client operates on."""
        client = FlextDbtLdifClient.Client(settings)
        assert client.settings is settings

    # ---- parse_ldif_file contract ----------------------------------------

    def test_parse_with_explicit_path_returns_entry_tagged_with_source(
        self,
        tmp_path: Path,
    ) -> None:
        """Parsing echoes the requested path as the entry source."""
        path = tmp_path / "dummy.ldif"
        result = FlextDbtLdifClient.Client().parse_ldif_file(path)

        entries = result.unwrap()
        assert entries == [
            {"dn": c.DbtLdif.SAMPLE_LDIF_DN, "source": str(path)},
        ]

    def test_parse_is_idempotent_for_same_path(self, tmp_path: Path) -> None:
        """Parsing the same path twice yields equal payloads."""
        client = FlextDbtLdifClient.Client()
        path = tmp_path / "same.ldif"

        assert client.parse_ldif_file(path).unwrap() == (
            client.parse_ldif_file(path).unwrap()
        )

    def test_parse_without_path_and_empty_settings_fails_with_reason(self) -> None:
        """Absent path plus empty settings path is a required-input failure."""
        client = FlextDbtLdifClient.Client(FlextDbtLdifSettings.fetch_global())
        result = client.parse_ldif_file()

        assert result.failure
        assert "required" in (result.error or "").lower()

    # ---- validate_ldif_data contract -------------------------------------

    @pytest.mark.parametrize("entry_count", [1, 3, 10])
    def test_validation_reports_entry_count_and_passing_status(
        self,
        entry_count: int,
    ) -> None:
        """Non-empty entries validate as passed with matching totals."""
        entries: t.SequenceOf[t.JsonMapping] = [
            {"dn": f"cn=n{i},dc=example,dc=org", "source": "in.ldif"}
            for i in range(entry_count)
        ]
        data = FlextDbtLdifClient.Client().validate_ldif_data(entries).unwrap()

        assert isinstance(data, m.DbtLdif.LdifValidationResult)
        assert data.total_entries == entry_count
        assert data.validation_status == c.DbtLdif.VALIDATION_STATUS_PASSED
        assert data.quality_score == pytest.approx(c.DbtLdif.DEFAULT_QUALITY_SCORE)

    def test_validation_of_empty_entries_fails_with_reason(self) -> None:
        """Empty entries cannot validate and explain why."""
        result = FlextDbtLdifClient.Client().validate_ldif_data([])

        assert result.failure
        assert "no ldif entries" in (result.error or "").lower()

    # ---- transform_with_dbt contract -------------------------------------

    def test_transform_reports_record_count_and_requested_models(self) -> None:
        """Transform metadata reflects inputs and reports success."""
        entries: t.SequenceOf[t.JsonMapping] = [{"dn": "cn=t,dc=example,dc=org"}]
        data = (
            FlextDbtLdifClient
            .Client()
            .transform_with_dbt(entries, ["m1", "m2"])
            .unwrap()
        )

        assert data.records == 1
        assert list(data.models) == ["m1", "m2"]
        assert data.status == c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS

    def test_transform_without_models_uses_default_staging_and_analytics(
        self,
    ) -> None:
        """Omitting model names falls back to the default model set."""
        data = FlextDbtLdifClient.Client().transform_with_dbt([], None).unwrap()

        assert list(data.models) == [
            c.DbtLdif.STAGING_MODEL_NAME,
            c.DbtLdif.ANALYTICS_MODEL_NAME,
        ]
        assert data.records == 0

    # ---- run_full_pipeline contract --------------------------------------

    def test_pipeline_completes_and_aggregates_stage_statuses(
        self,
        tmp_path: Path,
    ) -> None:
        """A valid path drives parse+validate+transform to a completed result."""
        result = FlextDbtLdifClient.Client().run_full_pipeline(
            tmp_path / "f.ldif",
            ["m1"],
        )
        data = result.unwrap()

        assert isinstance(data, m.DbtLdif.PipelineResult)
        assert data.pipeline_status == c.DbtLdif.WORKFLOW_STATUS_COMPLETED
        assert data.parsed_entries == 1
        assert data.validation_status == c.DbtLdif.VALIDATION_STATUS_PASSED
        assert data.transformation_status == c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS

    def test_pipeline_propagates_parse_failure(self) -> None:
        """A parse failure short-circuits the whole pipeline as a failure."""
        client = FlextDbtLdifClient.Client(FlextDbtLdifSettings.fetch_global())
        result = client.run_full_pipeline()

        assert result.failure
        assert "required" in (result.error or "").lower()

    # ---- result composition contract -------------------------------------

    def test_parse_result_chains_into_validation_via_flat_map(
        self,
        tmp_path: Path,
    ) -> None:
        """Parse -> validate composes as monadic r[T] without manual unwrap."""
        client = FlextDbtLdifClient.Client()
        chained = client.parse_ldif_file(tmp_path / "c.ldif").flat_map(
            client.validate_ldif_data,
        )

        assert chained.success
        assert chained.unwrap().total_entries == 1

    def test_transform_result_serializes_public_state_via_model_dump(self) -> None:
        """Public model state is exposed through model_dump for consumers."""
        data = (
            FlextDbtLdifClient
            .Client()
            .transform_with_dbt([{"dn": "cn=a"}], ["only"])
            .unwrap()
        )
        dumped = data.model_dump()

        assert dumped["records"] == 1
        assert list(dumped["models"]) == ["only"]
        assert dumped["status"] == c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS
