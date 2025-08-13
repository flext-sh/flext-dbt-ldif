"""Compatibility facade: re-export dbt_models via models.py.

Standardizes imports to use flext_dbt_ldif.models across the codebase.
"""

from __future__ import annotations

from .dbt_models import *  # noqa: F403
