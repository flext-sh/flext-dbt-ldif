"""Command-line interface for FLEXT dbt LDIF.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import NoReturn

import click
from rich.console import Console
from flext_core import FlextLogger

from flext_dbt_ldif import __version__
from .dbt_config import FlextDbtLdifConfig
from .dbt_exceptions import FlextDbtLdifError
from .simple_api import generate_ldif_models, process_ldif_file, validate_ldif_quality

console = Console()
logger = FlextLogger(__name__)


@click.group()
@click.version_option(version=__version__, prog_name="flext-data.dbt.flext-dbt-ldif")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.pass_context
def cli(ctx: click.Context, *, verbose: bool) -> None:
    """FLEXT dbt LDIF - Advanced LDAP Data Analytics and Transformations."""
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose


@cli.command()
def info() -> None:
    """Show package information."""
    console.print(f"[bold blue]FLEXT dbt LDIF[/bold blue] v{__version__}")
    console.print("Advanced LDAP Data Analytics and Transformations")
    console.print("")
    console.print("[bold]Features:[/bold]")
    console.print("• Programmatic dbt model generation")
    console.print("• LDIF data processing and analytics")
    console.print("• Advanced SQL pattern generation")
    console.print("• PostgreSQL optimized transformations")


@cli.command()
@click.argument("ldif_file", type=click.Path(exists=True, path_type=Path))
@click.option("--project-dir", "-p", type=click.Path(path_type=Path), help="DBT project directory")
@click.option("--generate-models/--no-generate-models", default=True, help="Generate DBT models")
@click.option("--run-transformations/--no-run-transformations", default=False, help="Run DBT transformations")
@click.pass_context
def process(
    ctx: click.Context,
    ldif_file: Path,
    project_dir: Path | None,
    generate_models: bool,
    run_transformations: bool,
) -> None:
    """Process an LDIF file with DBT transformations."""
    verbose = ctx.obj.get("verbose", False)
    
    if verbose:
        console.print(f"[bold blue]Processing LDIF file:[/bold blue] {ldif_file}")
        console.print(f"Project directory: {project_dir or 'current directory'}")
        console.print(f"Generate models: {generate_models}")
        console.print(f"Run transformations: {run_transformations}")
    
    try:
        result = process_ldif_file(
            ldif_file=ldif_file,
            project_dir=project_dir,
            generate_models=generate_models,
            run_transformations=run_transformations,
        )
        
        if result.success:
            console.print("[bold green]✓[/bold green] LDIF processing completed successfully")
            if verbose and result.value:
                data = result.value
                console.print(f"Steps completed: {data.get('steps_completed', [])}")
                console.print(f"Status: {data.get('workflow_status', 'unknown')}")
        else:
            console.print(f"[bold red]✗[/bold red] LDIF processing failed: {result.error}")
            sys.exit(1)
            
    except Exception as e:
        logger.exception("Unexpected error in CLI process command")
        console.print(f"[bold red]✗[/bold red] Unexpected error: {e}")
        sys.exit(1)


@cli.command()
@click.argument("ldif_file", type=click.Path(exists=True, path_type=Path))
@click.pass_context
def validate(ctx: click.Context, ldif_file: Path) -> None:
    """Validate LDIF data quality."""
    verbose = ctx.obj.get("verbose", False)
    
    if verbose:
        console.print(f"[bold blue]Validating LDIF file:[/bold blue] {ldif_file}")
    
    try:
        result = validate_ldif_quality(ldif_file)
        
        if result.success:
            data = result.value or {}
            quality_summary = data.get("quality_summary", {})
            score = quality_summary.get("overall_score", 0.0)
            threshold_met = quality_summary.get("threshold_met", False)
            
            status_icon = "✓" if threshold_met else "⚠"
            status_color = "green" if threshold_met else "yellow"
            
            console.print(f"[bold {status_color}]{status_icon}[/bold {status_color}] Quality score: {score:.2f}")
            
            if verbose:
                file_info = data.get("file_info", {})
                console.print(f"Total entries: {file_info.get('total_entries', 0)}")
                console.print(f"Risk level: {quality_summary.get('risk_level', 'unknown')}")
                
        else:
            console.print(f"[bold red]✗[/bold red] Validation failed: {result.error}")
            sys.exit(1)
            
    except Exception as e:
        logger.exception("Unexpected error in CLI validate command")
        console.print(f"[bold red]✗[/bold red] Unexpected error: {e}")
        sys.exit(1)


@cli.command()
@click.argument("ldif_file", type=click.Path(exists=True, path_type=Path))
@click.option("--project-dir", "-p", type=click.Path(path_type=Path), help="DBT project directory")
@click.option("--overwrite", is_flag=True, help="Overwrite existing models")
@click.pass_context
def generate(
    ctx: click.Context,
    ldif_file: Path,
    project_dir: Path | None,
    overwrite: bool,
) -> None:
    """Generate DBT models from LDIF schema."""
    verbose = ctx.obj.get("verbose", False)
    
    if verbose:
        console.print(f"[bold blue]Generating models for:[/bold blue] {ldif_file}")
        console.print(f"Project directory: {project_dir or 'current directory'}")
        console.print(f"Overwrite existing: {overwrite}")
    
    try:
        result = generate_ldif_models(
            ldif_file=ldif_file,
            project_dir=project_dir,
            overwrite=overwrite,
        )
        
        if result.success:
            data = result.value or {}
            console.print("[bold green]✓[/bold green] Model generation completed successfully")
            if verbose:
                console.print(f"Total models generated: {data.get('total_models', 0)}")
                console.print(f"Staging models: {data.get('staging_models', 0)}")
                console.print(f"Analytics models: {data.get('analytics_models', 0)}")
        else:
            console.print(f"[bold red]✗[/bold red] Model generation failed: {result.error}")
            sys.exit(1)
            
    except Exception as e:
        logger.exception("Unexpected error in CLI generate command")
        console.print(f"[bold red]✗[/bold red] Unexpected error: {e}")
        sys.exit(1)


@cli.command()
@click.option("--format", "output_format", type=click.Choice(["json", "yaml", "table"]), default="table", help="Output format")
@click.pass_context  
def config(ctx: click.Context, output_format: str) -> None:
    """Show current configuration and validate it."""
    verbose = ctx.obj.get("verbose", False)
    
    try:
        config_obj = FlextDbtLdifConfig()
        validation_result = config_obj.validate_config()
        
        if output_format == "json":
            import json
            config_dict = config_obj.to_dict()
            console.print(json.dumps(config_dict, indent=2))
        elif output_format == "yaml":
            import yaml
            config_dict = config_obj.to_dict()
            console.print(yaml.dump(config_dict, default_flow_style=False))
        else:  # table format
            console.print("[bold blue]FLEXT DBT LDIF Configuration[/bold blue]")
            console.print()
            
            if validation_result.success:
                console.print("[bold green]✓[/bold green] Configuration is valid")
            else:
                console.print(f"[bold red]✗[/bold red] Configuration validation failed: {validation_result.error}")
            
            if verbose:
                console.print()
                console.print("[bold]LDIF Settings:[/bold]")
                console.print(f"  Max file size: {config_obj.ldif_max_file_size:,} bytes")
                console.print(f"  Encoding: {config_obj.ldif_encoding}")
                console.print(f"  Validate syntax: {config_obj.ldif_validate_syntax}")
                console.print(f"  Validate schemas: {config_obj.ldif_validate_schemas}")
                
                console.print()
                console.print("[bold]DBT Settings:[/bold]")
                console.print(f"  Project directory: {config_obj.dbt_project_dir}")
                console.print(f"  Profiles directory: {config_obj.dbt_profiles_dir}")
                console.print(f"  Target: {config_obj.dbt_target}")
                console.print(f"  Threads: {config_obj.dbt_threads}")
                console.print(f"  Log level: {config_obj.dbt_log_level}")
                
                console.print()
                console.print("[bold]Quality Settings:[/bold]")
                console.print(f"  Min quality threshold: {config_obj.min_quality_threshold}")
                console.print(f"  Max DN depth: {config_obj.max_dn_depth}")
                console.print(f"  Validate DNs: {config_obj.validate_dns}")
            
    except Exception as e:
        logger.exception("Error showing configuration")
        console.print(f"[bold red]✗[/bold red] Error: {e}")
        sys.exit(1)


def main() -> NoReturn:
    """Main CLI entry point for flext-dbt-ldif."""
    try:
        cli()
    except KeyboardInterrupt:
        console.print("\n[bold red]Interrupted by user[/bold red]")
        sys.exit(1)
    except (OSError, RuntimeError, ValueError) as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
