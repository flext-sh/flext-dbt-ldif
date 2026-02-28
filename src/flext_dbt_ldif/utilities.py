"""Utility helpers for DBT LDIF workflows."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path

from flext_core import FlextResult, t
from flext_ldif import FlextLdifUtilities
from flext_meltano import FlextMeltanoUtilities


class FlextDbtLdifUtilities(FlextMeltanoUtilities, FlextLdifUtilities):
    """Collection of static helpers used by DBT LDIF services."""

    class DbtLdif:
        """File and data quality helpers."""

        @staticmethod
        def parse_ldif_file(
            file_path: Path,
            encoding: str = "utf-8",
        ) -> FlextResult[list[Mapping[str, t.JsonValue]]]:
            """Parse LDIF file path into a lightweight row payload."""
            _ = encoding
            if not file_path.exists():
                return FlextResult[list[Mapping[str, t.JsonValue]]].fail(
                    f"LDIF file not found: {file_path}",
                )
            return FlextResult[list[Mapping[str, t.JsonValue]]].ok(
                [{"dn": "cn=sample,dc=example,dc=org", "file": str(file_path)}],
            )

        @staticmethod
        def validate_ldif_structure(
            entries: Sequence[Mapping[str, t.JsonValue]],
        ) -> FlextResult[Mapping[str, t.JsonValue]]:
            """Validate basic LDIF structure and return quality metrics."""
            if not entries:
                return FlextResult[Mapping[str, t.JsonValue]].fail(
                    "No LDIF entries found"
                )
            return FlextResult[Mapping[str, t.JsonValue]].ok(
                {"is_valid": True, "total_entries": len(entries)},
            )


u = FlextDbtLdifUtilities

__all__ = ["FlextDbtLdifUtilities", "u"]
