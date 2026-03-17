"""Auto-generated centralized models."""

from __future__ import annotations

from pydantic import RootModel, TypeAdapter


class FlextAutoConstants:
    pass


class FlextAutoTypes:
    pass


class FlextAutoProtocols:
    pass


class FlextAutoUtilities:
    pass


class FlextAutoModels:
    pass


c = FlextAutoConstants
t = FlextAutoTypes
p = FlextAutoProtocols
u = FlextAutoUtilities
m = FlextAutoModels


class _EntryContainerListAdapter(
    RootModel[TypeAdapter(list[dict[str, t.ContainerValue]])]
):
    pass


class _EntryListAdapter(RootModel[TypeAdapter(list[dict[str, t.ContainerValue]])]):
    pass
