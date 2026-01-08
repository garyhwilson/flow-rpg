#!/usr/bin/env python3
"""
TTRPG Documentation Generator

Generates markdown documentation from YAML source files using Jinja2 templates.
Enables rapid iteration on game mechanics while maintaining narrative context.

Usage:
    python generate_docs.py --help        # Show available options
    python generate_docs.py --all         # Generate all documentation
    python generate_docs.py --validate    # Validate YAML consistency
    python generate_docs.py --example     # Generate example documentation

This is a template script. Add your own generator methods for your game system.
"""

import argparse
import sys
from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from typing import Dict, Any, List, Optional


# =============================================================================
# PATH CONFIGURATION
# =============================================================================

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
YAML_DIR = PROJECT_ROOT / 'yaml'
TEMPLATE_DIR = PROJECT_ROOT / 'templates'
OUTPUT_DIR = TEMPLATE_DIR / 'output'


# =============================================================================
# GENERATOR CLASS
# Extend this class with methods for your game system's documentation
# =============================================================================

class TTRPGGenerator:
    """
    Main generator class for TTRPG documentation.

    Add new generator methods following this pattern:

    def generate_spells(self):
        '''Generate spell documentation.'''
        template = self.env.get_template('spells.jinja')
        spells = self.yaml_data.get('magic', {}).get('spells', [])
        output = template.render(spells=spells)
        self._write_output('spells.md', output)
    """

    def __init__(self):
        """Initialize the generator with Jinja2 environment."""
        self.yaml_data = {}

        # Create Jinja2 environment
        generators_dir = TEMPLATE_DIR / 'generators'
        if generators_dir.exists():
            self.env = Environment(
                loader=FileSystemLoader(generators_dir),
                autoescape=select_autoescape(),
                trim_blocks=True,
                lstrip_blocks=True
            )
        else:
            self.env = None
            print(f"Warning: Template directory not found at {generators_dir}")

        # Ensure output directory exists
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    def load_yaml(self, filename: str) -> Dict[str, Any]:
        """Load a YAML file and return parsed data."""
        yaml_path = YAML_DIR / filename
        if not yaml_path.exists():
            print(f"  Warning: {filename} not found at {yaml_path}")
            return {}

        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        print(f"  Loaded {filename}")
        return data

    def load_all_yaml(self):
        """
        Load all YAML files.

        Customize this method for your project's YAML structure.
        """
        print("Loading YAML files...")

        # Load your project's YAML files here
        yaml_files = [
            'index.yaml',
            'example_system.yaml',
            # Add your YAML files:
            # 'core_rules.yaml',
            # 'character.yaml',
            # 'equipment.yaml',
            # etc.
        ]

        for filename in yaml_files:
            key = filename.replace('.yaml', '')
            self.yaml_data[key] = self.load_yaml(filename)

    def _write_output(self, filename: str, content: str):
        """Write generated content to output file."""
        output_path = OUTPUT_DIR / filename
        with open(output_path, 'w') as f:
            f.write(content)
        print(f"  Generated {output_path}")

    # =========================================================================
    # VALIDATION
    # =========================================================================

    def validate_yaml(self) -> bool:
        """
        Validate YAML data for consistency.

        Customize this method with your project's validation rules.
        """
        print("\nValidating YAML data...")
        errors = []
        warnings = []

        # Example validation: check index.yaml has required fields
        if 'index' in self.yaml_data:
            index = self.yaml_data['index']

            if 'title' not in index:
                errors.append("index.yaml missing 'title' field")

            if 'version' not in index:
                warnings.append("index.yaml missing 'version' field")

        # Add your validation rules here
        # Example:
        # if 'character' in self.yaml_data:
        #     if 'species' not in self.yaml_data['character']:
        #         errors.append("character.yaml missing 'species' section")

        # Report results
        if warnings:
            print(f"\nWarnings ({len(warnings)}):")
            for warning in warnings:
                print(f"  - {warning}")

        if errors:
            print(f"\nErrors ({len(errors)}):")
            for error in errors:
                print(f"  - {error}")
            return False

        print("  Validation passed")
        return True

    # =========================================================================
    # GENERATOR METHODS
    # Add your generator methods below
    # =========================================================================

    def generate_example(self):
        """
        Generate example documentation.

        This demonstrates the generator pattern. Replace with your own generators.
        """
        if not self.env:
            print("  Error: Jinja2 environment not initialized")
            return

        try:
            template = self.env.get_template('example.jinja')
        except Exception as e:
            print(f"  Error loading template: {e}")
            return

        # Get data from YAML
        index_data = self.yaml_data.get('index', {})
        example_data = self.yaml_data.get('example_system', {})

        # Render template
        output = template.render(
            title=index_data.get('title', 'Untitled'),
            version=index_data.get('version', '0.0'),
            system=example_data
        )

        self._write_output('example_output.md', output)

    def generate_all(self):
        """Generate all documentation."""
        print("\nGenerating all documentation...")

        # Add calls to all your generator methods here
        self.generate_example()

        # Example:
        # self.generate_species()
        # self.generate_classes()
        # self.generate_spells()
        # self.generate_equipment()

        print("\nGeneration complete!")


# =============================================================================
# COMMAND LINE INTERFACE
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Generate TTRPG documentation from YAML files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python generate_docs.py --all         # Generate all documentation
    python generate_docs.py --validate    # Validate YAML structure
    python generate_docs.py --example     # Generate example documentation

Add your own --flags by extending the argument parser and generator class.
        """
    )

    # Core options
    parser.add_argument('--all', action='store_true',
                        help='Generate all documentation')
    parser.add_argument('--validate', action='store_true',
                        help='Validate YAML data consistency')
    parser.add_argument('--example', action='store_true',
                        help='Generate example documentation')

    # Add your generator options here:
    # parser.add_argument('--species', action='store_true',
    #                     help='Generate species documentation')
    # parser.add_argument('--classes', action='store_true',
    #                     help='Generate class documentation')

    args = parser.parse_args()

    # If no arguments, show help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    # Initialize generator and load YAML
    generator = TTRPGGenerator()
    generator.load_all_yaml()

    # Handle validation
    if args.validate:
        success = generator.validate_yaml()
        sys.exit(0 if success else 1)

    # Handle generation
    if args.all:
        generator.generate_all()
    elif args.example:
        generator.generate_example()

    # Add your generator handlers here:
    # if args.species:
    #     generator.generate_species()


if __name__ == '__main__':
    main()
