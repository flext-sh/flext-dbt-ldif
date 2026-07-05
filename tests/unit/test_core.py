"""Behavioral unit tests for FlextDbtLdifCore public contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path

import pytest

from flext_dbt_ldif import c, t
from flext_dbt_ldif.services.core import FlextDbtLdifCore

__all__ = ["TestsFlextDbtLdifCore"]


class TestsFlextDbtLdifCore:
    """Behavioral contract for FlextDbtLdifCore.Core helpers."""

    def test_model_generator_defaults_project_dir_to_cwd(self) -> None:
        """Default project_dir resolves to the current working directory."""
        gen = FlextDbtLdifCore.Core.ModelGenerator()
        assert gen.project_dir == Path.cwd()

    def test_model_generator_honors_custom_project_dir(self, tmp_path: Path) -> None:
        """A supplied project_dir is exposed unchanged on the public field."""
        gen = FlextDbtLdifCore.Core.ModelGenerator(project_dir=tmp_path)
        assert gen.project_dir == tmp_path

    def test_generate_staging_models_returns_named_staging_metadata(self) -> None:
        """Staging metadata carries the canonical staging name and description."""
        gen = FlextDbtLdifCore.Core.ModelGenerator()
        models = gen.generate_staging_models()
        assert [m["name"] for m in models] == [c.DbtLdif.STAGING_MODEL_NAME]
        assert models[0]["description"] == c.DbtLdif.STAGING_MODEL_DESCRIPTION

    def test_generate_analytics_models_returns_named_analytics_metadata(self) -> None:
        """Analytics metadata carries the canonical analytics name and description."""
        gen = FlextDbtLdifCore.Core.ModelGenerator()
        models = gen.generate_analytics_models()
        assert [m["name"] for m in models] == [c.DbtLdif.ANALYTICS_MODEL_NAME]
        assert models[0]["description"] == c.DbtLdif.ANALYTICS_MODEL_DESCRIPTION

    def test_generate_models_are_deterministic_across_calls(self) -> None:
        """Repeated generation yields identical metadata (idempotent contract)."""
        gen = FlextDbtLdifCore.Core.ModelGenerator()
        assert gen.generate_staging_models() == gen.generate_staging_models()
        assert gen.generate_analytics_models() == gen.generate_analytics_models()

    @pytest.mark.parametrize(
        ("entries", "expected_total", "expected_unique"),
        [
            pytest.param([], 0, 0, id="empty"),
            pytest.param(
                [{"dn": "cn=user1,dc=example,dc=com"}],
                1,
                1,
                id="single-entry",
            ),
            pytest.param(
                [
                    {"dn": "cn=user1,ou=users,dc=example,dc=com"},
                    {"dn": "cn=user2,ou=users,dc=example,dc=com"},
                ],
                2,
                2,
                id="distinct-dns",
            ),
            pytest.param(
                [
                    {"dn": "cn=user1,dc=example,dc=com"},
                    {"dn": "cn=user1,dc=example,dc=com"},
                ],
                2,
                1,
                id="duplicate-dns",
            ),
            pytest.param(
                [{"cn": "no-dn-key"}, {"cn": "also-missing"}],
                2,
                1,
                id="missing-dn-collapses-to-single-empty-key",
            ),
        ],
    )
    def test_analyze_entry_patterns_reports_totals_and_unique_dns(
        self,
        entries: t.SequenceOf[t.StrMapping],
        expected_total: int,
        expected_unique: int,
    ) -> None:
        """Analysis succeeds and reports entry totals and distinct DN counts."""
        analytics = FlextDbtLdifCore.Core.Analytics()
        result = analytics.analyze_entry_patterns(entries)
        assert result.success
        data = result.unwrap()
        assert data["total_entries"] == expected_total
        assert data["unique_dns"] == expected_unique

    def test_analyze_entry_patterns_result_supports_map_combinator(self) -> None:
        """The r[T] outcome chains through map without losing success state."""
        analytics = FlextDbtLdifCore.Core.Analytics()
        entries: t.SequenceOf[t.StrMapping] = [{"dn": "cn=a,dc=x"}]
        total = (
            analytics
            .analyze_entry_patterns(entries)
            .map(lambda payload: payload["total_entries"])
            .unwrap()
        )
        assert total == 1
