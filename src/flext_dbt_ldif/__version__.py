"""Version information for FLEXT dbt LDIF."""

from __future__ import annotations

# Import directly from flext_core for type annotations

__version__ = "0.9.0"
__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())
