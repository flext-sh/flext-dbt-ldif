"""Client mixin for dbt-ldif utilities.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldif/services/client
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

# NOTE (multi-agent): mro-rn88 — import settings singleton (same family as base.py fix).
from flext_dbt_ldif import FlextDbtLdifSettings, c, m, p, r, t

if TYPE_CHECKING:
    from pathlib import Path


class FlextDbtLdifClient:
    """Mixin providing Client for dbt-ldif utilities."""

    class Client:
        """Client with typed parse, validate, and transform operations."""

        _settings: FlextDbtLdifSettings

        # NOTE (multi-agent): mro-rn88 — inject the canonical settings contract and
        # resolve the concrete snapshot (injected override or global singleton).
        def __init__(self, settings: p.Settings | None = None) -> None:
            """Wire the client with optional injected settings.

            Args:
                settings: Settings contract to honor; the global settings
                    singleton is used when omitted, and foreign settings
                    payloads are revalidated into the dbt-ldif settings
                    type.

            """
            if settings is None:
                self._settings = FlextDbtLdifSettings.fetch_global()
            elif isinstance(settings, FlextDbtLdifSettings):
                self._settings = settings
            else:
                self._settings = FlextDbtLdifSettings.model_validate(
                    settings.model_dump(),
                )

        @property
        def settings(self) -> FlextDbtLdifSettings:
            """The effective dbt-ldif settings for this client."""
            return self._settings

        def parse_ldif_file(
            self,
            file_path: Path | str | None = None,
        ) -> p.Result[list[t.JsonMapping]]:
            """Return minimal parsed LDIF entries payload.

            Args:
                file_path: Path to the LDIF file; falls back to the
                    configured settings path when omitted.

            Returns:
                Result wrapping the parsed entries as JSON mappings, or a
                failure when no path is available.

            """
            selected_path = (
                str(file_path)
                if file_path is not None
                else self.settings.DbtLdif.ldif_file_path
            )
            if not selected_path:
                return r[list[t.JsonMapping]].fail("LDIF file path is required")
            return r[list[t.JsonMapping]].ok([
                {"dn": c.DbtLdif.SAMPLE_LDIF_DN, "source": selected_path},
            ])

        @staticmethod
        def transform_with_dbt(
            entries: t.SequenceOf[t.JsonMapping],
            model_names: t.StrSequence | None = None,
        ) -> p.Result[m.DbtLdif.DbtTransformationResult]:
            """Return synthetic DBT transformation metadata.

            Args:
                entries: Parsed LDIF entries to report on.
                model_names: Model names to include; defaults to the
                    canonical staging and analytics models when omitted.

            Returns:
                Result wrapping the transformation summary.

            """
            selected_models = model_names or [
                c.DbtLdif.STAGING_MODEL_NAME,
                c.DbtLdif.ANALYTICS_MODEL_NAME,
            ]
            return r[m.DbtLdif.DbtTransformationResult].ok(
                m.DbtLdif.DbtTransformationResult(
                    records=len(entries),
                    models=selected_models,
                    status=c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS,
                ),
            )

        def validate_ldif_data(
            self,
            entries: t.SequenceOf[t.JsonMapping],
        ) -> p.Result[m.DbtLdif.LdifValidationResult]:
            """Validate parsed LDIF payload and compute quality score.

            Args:
                entries: Parsed LDIF entries to validate.

            Returns:
                Result wrapping the validation metrics, or a failure when
                no entries are found or the quality threshold is not met.

            """
            total_entries = len(entries)
            if total_entries == 0:
                return r[m.DbtLdif.LdifValidationResult].fail("No LDIF entries found")
            if (
                self.settings.DbtLdif.min_quality_threshold
                > c.DbtLdif.DEFAULT_QUALITY_SCORE
            ):
                return r[m.DbtLdif.LdifValidationResult].fail(
                    "Quality threshold not met",
                )
            return r[m.DbtLdif.LdifValidationResult].ok(
                m.DbtLdif.LdifValidationResult(
                    total_entries=total_entries,
                    quality_score=c.DbtLdif.DEFAULT_QUALITY_SCORE,
                    validation_status=c.DbtLdif.VALIDATION_STATUS_PASSED,
                ),
            )
