"""Base model definitions for DBT LDIF — MRO composition of parent model namespaces.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifModels
from flext_meltano import m


class FlextDbtLdifModelsBase(FlextLdifModels):
    """MRO facade composing the LDIF model namespace for DBT LDIF."""

    class ConfigNamespace(m.BaseModel):
        """Open, frozen namespace exposing every ``config/*.yaml`` domain."""

        model_config = m.ConfigDict(extra="allow", frozen=True)


__all__: list[str] = ["FlextDbtLdifModelsBase"]
