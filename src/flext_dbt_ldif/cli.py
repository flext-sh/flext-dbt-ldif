"""Command-line interface for FLEXT dbt LDIF.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import sys
from typing import NoReturn

from flext_core import FlextResult, FlextLogger
from flext_cli import FlextCliApi, FlextCliConfig

from flext_dbt_ldif import __version__

logger = FlextLogger(__name__)


class FlextDbtLdifCliService:
    """FLEXT dbt LDIF CLI service using flext-cli foundation exclusively."""
    
    def __init__(self) -> None:
        """Initialize CLI service with flext-cli patterns."""
        self._cli_api = FlextCliApi()
        self._config = FlextCliConfig()
        
    def display_info(self) -> FlextResult[str]:
        """Display package info using flext-cli."""
        info_data = {
            "name": "FLEXT dbt LDIF",
            "version": __version__,
            "description": "Advanced LDAP Data Analytics and Transformations",
            "features": [
                "Programmatic dbt model generation",
                "LDIF data processing and analytics", 
                "Advanced SQL pattern generation",
                "PostgreSQL optimized transformations"
            ]
        }
        
        # Use flext-cli to format and display data
        try:
            formatted_data = self._cli_api.format_data(info_data)
            if formatted_data is not None:
                print(f"FLEXT dbt LDIF v{__version__}")
                print("Advanced LDAP Data Analytics and Transformations")
                print("\nFeatures:")
                for feature in info_data["features"]:
                    print(f"• {feature}")
                return FlextResult[str].ok("Package information displayed successfully")
            else:
                # Fallback display
                print(f"FLEXT dbt LDIF v{__version__}")
                print("Advanced LDAP Data Analytics and Transformations")
                return FlextResult[str].ok("Package information displayed (fallback)")
        except Exception as e:
            # Safe fallback without Rich
            print(f"FLEXT dbt LDIF v{__version__}")
            print("Advanced LDAP Data Analytics and Transformations")
            return FlextResult[str].ok("Package information displayed (simple)")
    
    def display_generate_message(self) -> FlextResult[str]:
        """Display generate message using flext-cli."""
        try:
            # Try flext-cli formatting
            result = self._cli_api.format_data({"message": "Model generation functionality coming soon!"})
            print("Model generation functionality coming soon!")
            print("This will generate dbt models programmatically.")
            return FlextResult[str].ok("Generate message displayed")
        except Exception:
            # Fallback display
            print("Model generation functionality coming soon!")
            print("This will generate dbt models programmatically.")
            return FlextResult[str].ok("Generate message displayed (fallback)")
    
    def display_validate_message(self) -> FlextResult[str]:
        """Display validate message using flext-cli."""
        try:
            # Try flext-cli formatting
            result = self._cli_api.format_data({"message": "Model validation functionality coming soon!"})
            print("Model validation functionality coming soon!")
            print("This will validate generated dbt models.")
            return FlextResult[str].ok("Validate message displayed")
        except Exception:
            # Fallback display
            print("Model validation functionality coming soon!")
            print("This will validate generated dbt models.")
            return FlextResult[str].ok("Validate message displayed (fallback)")


def info() -> None:
    """Show package information."""
    cli_service = FlextDbtLdifCliService()
    result = cli_service.display_info()
    if result.is_failure:
        print(f"Error: {result.error}")


def generate() -> None:
    """Generate dbt models from LDIF schema definitions."""
    cli_service = FlextDbtLdifCliService()
    result = cli_service.display_generate_message()
    if result.is_failure:
        print(f"Error: {result.error}")


def validate() -> None:
    """Validate dbt models and configurations."""
    cli_service = FlextDbtLdifCliService()
    result = cli_service.display_validate_message()
    if result.is_failure:
        print(f"Error: {result.error}")


def main() -> NoReturn:
    """Main CLI entry point for flext-dbt-ldif."""
    try:
        # Simple command dispatching without Click
        import sys
        
        if len(sys.argv) > 1:
            command = sys.argv[1]
            if command == "info":
                info()
            elif command == "generate":
                generate()
            elif command == "validate":
                validate()
            else:
                print("Available commands: info, generate, validate")
                sys.exit(1)
        else:
            print("FLEXT dbt LDIF - Advanced LDAP Data Analytics and Transformations")
            print("Available commands: info, generate, validate")
        
        sys.exit(0)
        
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        sys.exit(1)
    except (OSError, RuntimeError, ValueError) as e:
        logger.error(f"CLI error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
