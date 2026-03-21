"""Auto-generated centralized models."""

from __future__ import annotations

from flext_core.typings import FlextTypes as t
from pydantic import RootModel


class FlextAutoConstants:
    pass


class FlextAutoProtocols:
    pass


class FlextAutoUtilities:
    pass


class FlextAutoModels:
    pass


c = FlextAutoConstants
p = FlextAutoProtocols
u = FlextAutoUtilities
m = FlextAutoModels


class EntryContainerListAdapter(RootModel[list[dict[str, t.ContainerValue]]]):
    """Adapter for validating a list of LDIF entry containers."""


class EntryListAdapter(RootModel[list[dict[str, t.ContainerValue]]]):
    """Adapter for validating a list of LDIF entries."""
