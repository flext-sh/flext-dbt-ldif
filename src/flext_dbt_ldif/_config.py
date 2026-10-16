"""FlextDbtLdifConfig — frozen config singleton for flext-dbt-ldif (ADR-005 §7).

Model-less: business rules live in ``config/*.yaml`` under the ``DbtLdif:`` key and
are exposed through the open ``config.DbtLdif`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.DbtLdif.<domain>[<key>...]``.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_meltano import FlextMeltanoConfig, m

from flext_dbt_ldif._models.base import FlextDbtLdifModelsBase


class FlextDbtLdifConfig(FlextMeltanoConfig):
    """DbtLdif config auto-loaded model-less from ``config/*.yaml``."""

    DbtLdif: Annotated[
        FlextDbtLdifModelsBase.ConfigNamespace,
        m.Field(
            description="Open namespace exposing ``config/*.yaml`` under ``DbtLdif``.",
        ),
    ] = FlextDbtLdifModelsBase.ConfigNamespace()


config: FlextDbtLdifConfig = FlextDbtLdifConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_dbt_ldif import config``."""

__all__: list[str] = ["FlextDbtLdifConfig", "config"]
