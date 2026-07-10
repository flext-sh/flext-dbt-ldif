"""FlextDbtLdifConfig — frozen config singleton for flext-dbt-ldif (ADR-005 §7).

Model-less: business rules live in ``config/*.yaml`` under the ``DbtLdif:`` key and
are exposed through the open ``config.DbtLdif`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.DbtLdif.<domain>[<key>...]``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from flext_meltano import FlextMeltanoConfig


class _DbtLdifNamespace(BaseModel):
    """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

    model_config = ConfigDict(extra="allow", frozen=True)


class FlextDbtLdifConfig(FlextMeltanoConfig):
    """DbtLdif config auto-loaded model-less from ``config/*.yaml``."""

    DbtLdif: _DbtLdifNamespace = _DbtLdifNamespace()


config: FlextDbtLdifConfig = FlextDbtLdifConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_dbt_ldif import config``."""

__all__: list[str] = ["FlextDbtLdifConfig", "config"]
