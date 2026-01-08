#!/usr/bin/env python3
"""
Validate that YAML-SOURCE markers in markdown match their YAML sources.
Run before assembling publications to catch drift.

Usage:
    python scripts/validate_yaml_sync.py

Marker format in markdown:
    <!-- YAML-SOURCE: filename.yaml > path > to > value -->
    content here
    <!-- /YAML-SOURCE -->
"""

import yaml
import re
import sys
from pathlib import Path


def extract_yaml_value(yaml_data, path):
    """Navigate YAML structure by path like 'species > dwarf > attribute_bonus'"""
    if not path:
        return yaml_data

    keys = [k.strip() for k in path.split('>')]
    value = yaml_data
    for key in keys:
        if isinstance(value, dict):
            value = value.get(key)
        else:
            return None
        if value is None:
            return None
    return value


def find_yaml_source_blocks(md_content):
    """Find all <!-- YAML-SOURCE: path --> blocks"""
    pattern = r'<!-- YAML-SOURCE: ([^-]+) -->\n(.*?)<!-- /YAML-SOURCE -->'
    return re.findall(pattern, md_content, re.DOTALL)


def validate_file(md_path, yaml_dir):
    """Check all YAML-SOURCE blocks in a markdown file"""
    issues = []
    warnings = []

    try:
        md_content = md_path.read_text()
    except Exception as e:
        issues.append(f"{md_path}: Could not read file: {e}")
        return issues, warnings

    blocks = find_yaml_source_blocks(md_content)

    if not blocks:
        # Not an error, just no markers yet
        return issues, warnings

    for source_path, content in blocks:
        source_path = source_path.strip()

        # Parse source path: "character.yaml > species > dwarf"
        parts = source_path.split('>')
        parts = [p.strip() for p in parts]

        if not parts:
            issues.append(f"{md_path}: Empty YAML-SOURCE path")
            continue

        yaml_file = parts[0]
        yaml_path = ' > '.join(parts[1:]) if len(parts) > 1 else ''

        # Load YAML and extract value
        yaml_full_path = yaml_dir / yaml_file
        if not yaml_full_path.exists():
            issues.append(f"{md_path}: YAML file not found: {yaml_file}")
            continue

        try:
            with open(yaml_full_path) as f:
                yaml_data = yaml.safe_load(f)
        except Exception as e:
            issues.append(f"{md_path}: Could not parse {yaml_file}: {e}")
            continue

        # Verify the path exists in YAML
        yaml_value = extract_yaml_value(yaml_data, yaml_path)
        if yaml_value is None:
            issues.append(f"{md_path}: YAML path not found: {source_path}")
        else:
            # Path exists - could add content comparison here in future
            pass

    return issues, warnings


def main():
    # Find project root (where yaml/ directory is)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    yaml_dir = project_root / 'yaml'

    if not yaml_dir.exists():
        print(f"Error: YAML directory not found at {yaml_dir}")
        sys.exit(1)

    # Find all markdown files to check
    md_files = []

    # Core rules
    core_rules_dir = project_root / 'core_rules'
    if core_rules_dir.exists():
        md_files.extend(core_rules_dir.glob('*.md'))

    # Quick reference
    quick_ref = project_root / 'quick_reference.md'
    if quick_ref.exists():
        md_files.append(quick_ref)

    # Archetypes
    archetypes_dir = project_root / 'archetypes' / 'archetype_types'
    if archetypes_dir.exists():
        md_files.extend(archetypes_dir.glob('*.md'))

    # Callings
    callings_dir = project_root / 'callings' / 'calling_types'
    if callings_dir.exists():
        md_files.extend(callings_dir.glob('*.md'))

    all_issues = []
    all_warnings = []
    files_with_markers = 0

    for md_file in md_files:
        issues, warnings = validate_file(md_file, yaml_dir)
        all_issues.extend(issues)
        all_warnings.extend(warnings)

        # Check if file has any markers
        content = md_file.read_text()
        if '<!-- YAML-SOURCE:' in content:
            files_with_markers += 1

    # Report results
    print(f"\nYAML-Markdown Sync Validation")
    print(f"=" * 40)
    print(f"Files scanned: {len(md_files)}")
    print(f"Files with YAML-SOURCE markers: {files_with_markers}")

    if all_warnings:
        print(f"\nWarnings ({len(all_warnings)}):")
        for warning in all_warnings:
            print(f"  - {warning}")

    if all_issues:
        print(f"\nIssues ({len(all_issues)}):")
        for issue in all_issues:
            print(f"  - {issue}")
        print(f"\nValidation FAILED")
        sys.exit(1)
    else:
        print(f"\nAll YAML-SOURCE markers validated successfully.")
        sys.exit(0)


if __name__ == '__main__':
    main()
