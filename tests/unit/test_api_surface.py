"""Behavioral contract tests for the FLEXT DBT LDIF public API surface.

Exercises observable behavior through the public facades only: parse /
validate / transform results, ``r[T]`` success and failure outcomes, and
public model state via ``model_dump``. No private attributes, no internal
collaborator spying.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from flext_dbt_ldif import (
    FlextDbtLdif,
    FlextDbtLdifSettings,
    __version__,
    c,
)
from flext_dbt_ldif.services.client import FlextDbtLdifClient
from flext_dbt_ldif.services.service import FlextDbtLdifServiceMixin

type Settings = FlextDbtLdifSettings
type Client = FlextDbtLdifClient.Client


class TestsFlextDbtLdifApiSurface:
    """Behavior contract for the public DBT LDIF API surface."""

    @pytest.fixture
    def settings(self) -> Settings:
        """Settings with a concrete LDIF path and a permissive threshold."""
        # NOTE (multi-agent): mro-rn88 — project fields nest under the DbtLdif namespace.
        return FlextDbtLdifSettings(
            DbtLdif={
                "ldif_file_path": "/tmp/sample.ldif",
                "min_quality_threshold": 0.5,
            },
        )

    @pytest.fixture
    def client(self, settings: Settings) -> Client:
        """Client bound to the test settings."""
        return FlextDbtLdifClient.Client(settings)

    def test_version_is_nonempty_string(self) -> None:
        """The package advertises a non-empty version string."""
        assert isinstance(__version__, str)
        assert __version__

    def test_parse_uses_configured_path_when_none_given(
        self,
        client: Client,
    ) -> None:
        """Parsing with no argument falls back to the configured LDIF path."""
        result = client.parse_ldif_file()

        assert result.success
        entries = result.value
        assert entries == [
            {"dn": c.DbtLdif.SAMPLE_LDIF_DN, "source": "/tmp/sample.ldif"},
        ]

    def test_parse_prefers_explicit_path_over_settings(
        self,
        client: Client,
    ) -> None:
        """An explicit path overrides the configured default."""
        result = client.parse_ldif_file("/data/other.ldif")

        assert result.success
        assert result.value[0]["source"] == "/data/other.ldif"

    def test_parse_fails_when_no_path_available(self) -> None:
        """Empty settings path with no argument yields a failure result."""
        client = FlextDbtLdifClient.Client(
            FlextDbtLdifSettings(
                DbtLdif={"ldif_file_path": "", "min_quality_threshold": 0.5}
            ),
        )

        result = client.parse_ldif_file()

        assert result.failure
        assert result.error == "LDIF file path is required"

    def test_validate_reports_quality_for_populated_entries(
        self,
        client: Client,
    ) -> None:
        """Validation of one entry passes with the default quality score."""
        result = client.validate_ldif_data(
            [{"dn": c.DbtLdif.SAMPLE_LDIF_DN, "source": "x"}],
        )

        assert result.success
        assert result.value.model_dump() == {
            "total_entries": 1,
            "quality_score": c.DbtLdif.DEFAULT_QUALITY_SCORE,
            "validation_status": c.DbtLdif.VALIDATION_STATUS_PASSED,
        }

    def test_validate_fails_on_empty_entries(self, client: Client) -> None:
        """Validation of an empty payload is a failure, not an empty success."""
        result = client.validate_ldif_data([])

        assert result.failure
        assert result.error == "No LDIF entries found"

    def test_validate_passes_at_maximum_threshold_boundary(self) -> None:
        """Threshold equal to the achievable score is the passing boundary.

        ``min_quality_threshold`` is capped at 1.0 by the settings contract
        (``le=1.0``), so the "threshold not met" branch is unreachable through
        the public API; equality with DEFAULT_QUALITY_SCORE is the boundary and
        must still pass.
        """
        client = FlextDbtLdifClient.Client(
            FlextDbtLdifSettings(
                ldif_file_path="/tmp/sample.ldif",
                min_quality_threshold=1.0,
            ),
        )

        result = client.validate_ldif_data([{"dn": "cn=a"}])

        assert result.success
        assert result.value.quality_score == c.DbtLdif.DEFAULT_QUALITY_SCORE

    @pytest.mark.parametrize(
        ("model_names", "expected_models"),
        [
            (None, ["stg_ldif_entries", "analytics_ldif_insights"]),
            (["only_model"], ["only_model"]),
            (["a", "b", "c"], ["a", "b", "c"]),
        ],
    )
    def test_transform_reports_records_and_selected_models(
        self,
        client: Client,
        model_names: list[str] | None,
        expected_models: list[str],
    ) -> None:
        """Transform echoes record count and the selected model names."""
        entries = [{"dn": "cn=a"}, {"dn": "cn=b"}]

        result = client.transform_with_dbt(entries, model_names)

        assert result.success
        payload = result.value.model_dump()
        assert payload["records"] == len(entries)
        assert list(payload["models"]) == expected_models
        assert payload["status"] == c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS

    def test_full_pipeline_composes_parse_validate_transform(
        self,
        client: Client,
    ) -> None:
        """The full pipeline aggregates each stage into a completed status."""
        result = client.run_full_pipeline()

        assert result.success
        assert result.value.model_dump() == {
            "parsed_entries": 1,
            "validation_status": c.DbtLdif.VALIDATION_STATUS_PASSED,
            "transformation_status": c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS,
            "pipeline_status": c.DbtLdif.WORKFLOW_STATUS_COMPLETED,
        }

    def test_full_pipeline_propagates_parse_failure(self) -> None:
        """A parse failure short-circuits the pipeline as a failure."""
        client = FlextDbtLdifClient.Client(
            FlextDbtLdifSettings(
                DbtLdif={"ldif_file_path": "", "min_quality_threshold": 0.5}
            ),
        )

        result = client.run_full_pipeline()

        assert result.failure
        assert result.error == "LDIF file path is required"

    def test_service_parse_and_validate_reports_entry_count(
        self,
        settings: Settings,
    ) -> None:
        """The service one-shot parse+validate reports counts and status."""
        service = FlextDbtLdifServiceMixin.Service(settings)

        result = service.parse_and_validate_ldif("/tmp/sample.ldif")

        assert result.success
        assert result.value.model_dump() == {
            "entry_count": 1,
            "quality_score": c.DbtLdif.DEFAULT_QUALITY_SCORE,
            "validation_status": c.DbtLdif.VALIDATION_STATUS_PASSED,
        }

    def test_facade_execute_returns_settings(self, settings: Settings) -> None:
        """The facade ``execute`` yields a successful settings result."""
        facade = FlextDbtLdif(settings)

        result = facade.execute()

        assert result.success
        assert isinstance(result.value, FlextDbtLdifSettings)

    def test_facade_service_is_bound_workflow_service(
        self,
        settings: Settings,
    ) -> None:
        """The facade exposes a usable bound Service via its public property."""
        facade = FlextDbtLdif(settings)

        result = facade.service.parse_and_validate_ldif("/tmp/sample.ldif")

        assert result.success
        assert result.value.entry_count == 1

    def test_fetch_instance_is_shared_singleton(self) -> None:
        """``fetch_instance`` returns the same shared facade each call."""
        assert FlextDbtLdif.fetch_instance() is FlextDbtLdif.fetch_instance()

    def test_process_ldif_file_runs_end_to_end_workflow(
        self,
        settings: Settings,
    ) -> None:
        """Processing a file drives the end-to-end workflow to a result."""
        facade = FlextDbtLdif(settings)

        result = facade.process_ldif_file("/tmp/sample.ldif")

        assert result.success
        payload = result.value.model_dump()
        assert payload["entry_count"] == 1
        assert payload["validation_status"] == c.DbtLdif.VALIDATION_STATUS_PASSED


__all__: list[str] = ["TestsFlextDbtLdifApiSurface"]
