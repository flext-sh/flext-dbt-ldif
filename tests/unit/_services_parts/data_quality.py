"""Data quality service test mixin."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_tests import tm
from tests import c

if TYPE_CHECKING:
    from pathlib import Path

    from flext_dbt_ldif.services.service import FlextDbtLdifServiceMixin


class TestsFlextDbtLdifServicesDataQuality:
    """Data quality service behavior."""

    def test_run_data_quality_assessment(
        self, svc: FlextDbtLdifServiceMixin.Service, tmp_path: Path
    ) -> None:
        """Data quality assessment parses, validates, and reports entry metrics."""
        target = tmp_path / "f.ldif"
        target.write_text(
            "dn: cn=test,dc=example,dc=org\nobjectClass: top\n\n", encoding="utf-8"
        )

        result = svc.run_data_quality_assessment(target)

        tm.ok(result)
        data = result.unwrap()
        tm.that(data, none=False)
        tm.that(data.entry_count, eq=1)
        tm.that(data.quality_score, eq=c.DbtLdif.DEFAULT_QUALITY_SCORE)
        tm.that(data.validation_status, eq=c.DbtLdif.VALIDATION_STATUS_PASSED)


__all__: list[str] = ["TestsFlextDbtLdifServicesDataQuality"]
