"""Base model definitions for DBT LDIF — MRO composition of parent model namespaces.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifModels


class FlextModelsDbtLdifBase(FlextLdifModels):
    """MRO facade composing the LDIF model namespace for DBT LDIF."""


__all__: list[str] = ["FlextModelsDbtLdifBase"]
