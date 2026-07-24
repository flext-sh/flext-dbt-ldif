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
from flext_tests import tm

from flext_dbt_ldif import FlextDbtLdif, FlextDbtLdifSettings, __version__
from flext_dbt_ldif.services.client import FlextDbtLdifClient
from flext_dbt_ldif.services.service import FlextDbtLdifServiceMixin
from tests import c

type Settings = FlextDbtLdifSettings
type Client = FlextDbtLdifClient.Client


class TestsFlextDbtLdifApiSurface:
    """Behavior contract for the public DBT LDIF API surface."""

    @pytest.fixture
    def client(self, settings: Settings) -> Client:
        """Client bound to the test settings."""
        return FlextDbtLdifClient.Client(settings)

    def test_version_is_nonempty_string(self) -> None:
        """The package advertises a non-empty version string."""
        tm.that(__version__, is_=str)
        assert __version__

    def test_parse_uses_configured_path_when_none_given(self, client: Client) -> None:
        """Parsing with no argument falls back to the configured LDIF path."""
        result = client.parse_ldif_file()

        tm.ok(result)
        entries = result.value
        tm.that(
            entries, eq=[{"dn": c.DbtLdif.SAMPLE_LDIF_DN, "source": "/tmp/sample.ldif"}]
        )

    def test_parse_prefers_explicit_path_over_settings(self) -> None:
        """An explicit path overrides the configured default."""
        client = FlextDbtLdifClient.Client(
            FlextDbtLdifSettings(
                DbtLdif=FlextDbtLdifSettings._DbtLdif(ldif_file_path="")
            )
        )
        result = client.parse_ldif_file("/data/other.ldif")

        tm.ok(result)
        tm.that(result.value[0]["source"], eq="/data/other.ldif")

        result = client.parse_ldif_file()

        tm.fail(result)
        tm.that(result.error, eq="LDIF file path is required")

    def test_validate_reports_quality_for_populated_entries(
        self, client: Client
    ) -> None:
        """Validation of one entry passes with the default quality score."""
        result = client.validate_ldif_data([
            {"dn": c.DbtLdif.SAMPLE_LDIF_DN, "source": "x"}
        ])

        tm.ok(result)
        tm.that(
            result.value.model_dump(),
            eq={
                "total_entries": 1,
                "quality_score": c.DbtLdif.DEFAULT_QUALITY_SCORE,
                "validation_status": c.DbtLdif.VALIDATION_STATUS_PASSED,
            },
        )

    def test_validate_fails_on_empty_entries(self, client: Client) -> None:
        """Validation of an empty payload is a failure, not an empty success."""
        result = client.validate_ldif_data([])

        tm.fail(result)
        tm.that(result.error, eq="No LDIF entries found")

    def test_validate_passes_at_maximum_threshold_boundary(self) -> None:
        """Threshold equal to the achievable score is the passing boundary.

        ``min_quality_threshold`` is capped at 1.0 by the settings contract
        (``le=1.0``), so the "threshold not met" branch is unreachable through
        the public API; equality with DEFAULT_QUALITY_SCORE is the boundary and
        must still pass.
        """
        client = FlextDbtLdifClient.Client(
            FlextDbtLdifSettings(
                ldif_file_path="/tmp/sample.ldif", min_quality_threshold=1.0
            )
        )

        result = client.validate_ldif_data([{"dn": "cn=a"}])

        tm.ok(result)
        tm.that(result.value.quality_score, eq=c.DbtLdif.DEFAULT_QUALITY_SCORE)

    @pytest.mark.parametrize(
        ("model_names", "expected_models"),
        [
            (None, ["stg_ldif_entries", "analytics_ldif_insights"]),
            (["only_model"], ["only_model"]),
            (["a", "b", "c"], ["a", "b", "c"]),
        ],
    )
    def test_transform_reports_records_and_selected_models(
        self, client: Client, model_names: list[str] | None, expected_models: list[str]
    ) -> None:
        """Transform echoes record count and the selected model names."""
        entries = [{"dn": "cn=a"}, {"dn": "cn=b"}]

        result = client.transform_with_dbt(entries, model_names)

        tm.ok(result)
        payload = result.value.model_dump()
        tm.that(payload["records"], eq=len(entries))
        tm.that(list(payload["models"]), eq=expected_models)
        tm.that(payload["status"], eq=c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS)

    def test_full_pipeline_composes_parse_validate_transform(
        self, client: Client
    ) -> None:
        """The full pipeline aggregates each stage into a completed status."""
        result = client.run_full_pipeline()

        tm.ok(result)
        tm.that(
            result.value.model_dump(),
            eq={
                "parsed_entries": 1,
                "validation_status": c.DbtLdif.VALIDATION_STATUS_PASSED,
                "transformation_status": c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS,
                "pipeline_status": c.DbtLdif.WORKFLOW_STATUS_COMPLETED,
            },
        )

    def test_full_pipeline_propagates_parse_failure(self) -> None:
        """A parse failure short-circuits the pipeline as a failure."""
        client = FlextDbtLdifClient.Client(
            FlextDbtLdifSettings(
                DbtLdif=FlextDbtLdifSettings._DbtLdif(
                    ldif_file_path="", min_quality_threshold=0.5
                )
            )
        )

        result = client.run_full_pipeline()

        tm.fail(result)
        tm.that(result.error, eq="LDIF file path is required")

    def test_service_parse_and_validate_reports_entry_count(
        self, settings: Settings
    ) -> None:
        """The service one-shot parse+validate reports counts and status."""
        service = FlextDbtLdifServiceMixin.Service(settings)

        result = service.parse_and_validate_ldif("/tmp/sample.ldif")

        tm.ok(result)
        tm.that(
            result.value.model_dump(),
            eq={
                "entry_count": 1,
                "quality_score": c.DbtLdif.DEFAULT_QUALITY_SCORE,
                "validation_status": c.DbtLdif.VALIDATION_STATUS_PASSED,
            },
        )

    def test_facade_execute_returns_settings(self, settings: Settings) -> None:
        """The facade ``execute`` yields a successful settings result."""
        facade = FlextDbtLdif(settings)

        result = facade.execute()

        tm.ok(result)
        tm.that(result.value, is_=FlextDbtLdifSettings)

    def test_facade_service_is_bound_workflow_service(self, settings: Settings) -> None:
        """The facade exposes a usable bound Service via its public property."""
        facade = FlextDbtLdif(settings)

        result = facade.service.parse_and_validate_ldif("/tmp/sample.ldif")

        tm.ok(result)
        tm.that(result.value.entry_count, eq=1)

    def test_fetch_instance_is_shared_singleton(self) -> None:
        """``fetch_instance`` returns the same shared facade each call."""
        assert FlextDbtLdif.fetch_instance() is FlextDbtLdif.fetch_instance()

    def test_process_ldif_file_runs_end_to_end_workflow(
        self, settings: Settings
    ) -> None:
        """Processing a file drives the end-to-end workflow to a result."""
        facade = FlextDbtLdif(settings)

        result = facade.process_ldif_file("/tmp/sample.ldif")

        tm.ok(result)
        payload = result.value.model_dump()
        tm.that(payload["entry_count"], eq=1)
        tm.that(payload["validation_status"], eq=c.DbtLdif.VALIDATION_STATUS_PASSED)


__all__: list[str] = ["TestsFlextDbtLdifApiSurface"]
