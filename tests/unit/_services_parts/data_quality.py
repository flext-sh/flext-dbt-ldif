"""Data quality service test mixin."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

import pytest
from flext_tests import r

from flext_dbt_ldif.services.service import FlextDbtLdifServiceMixin
from tests.models import m
from tests.protocols import p
from tests.typings import t


class TestsFlextDbtLdifServicesDataQuality:
    """Data quality service behavior."""

    def test_run_data_quality_assessment(
        self,
        monkeypatch: pytest.MonkeyPatch,
        svc: FlextDbtLdifServiceMixin.Service,
        tmp_path: Path,
    ) -> None:
        """Test data quality assessment delegates to parse_and_validate."""
        entries: t.SequenceOf[t.JsonMapping] = [
            {"dn": "cn=test,dc=example,dc=org"},
        ]

        def _parse_ldif_file(
            _fp: Path | str,
        ) -> p.Result[Sequence[t.JsonMapping]]:
            return r[Sequence[t.JsonMapping]].ok(entries)

        def _validate_ldif_data(
            entries: t.SequenceOf[t.JsonMapping],
        ) -> p.Result[m.DbtLdif.LdifValidationResult]:
            return r[m.DbtLdif.LdifValidationResult].ok(
                m.DbtLdif.LdifValidationResult(
                    total_entries=1,
                    quality_score=0.88,
                    validation_status="passed",
                ),
            )

        monkeypatch.setattr(svc.client, "parse_ldif_file", _parse_ldif_file)
        monkeypatch.setattr(svc.client, "validate_ldif_data", _validate_ldif_data)

        result = svc.run_data_quality_assessment(tmp_path / "f.ldif")
        assert result.success
        data = result.value
        assert data is not None
        assert data.entry_count == 1


__all__: list[str] = ["TestsFlextDbtLdifServicesDataQuality"]
