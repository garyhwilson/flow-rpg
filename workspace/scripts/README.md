# Scripts

This directory contains Python utilities for TTRPG development.

## Installation

```bash
pip install -r requirements.txt
```

## Available Scripts

### assemble_book.py

Assembles publication-ready markdown documents from modular source files based on YAML manifest definitions.

```bash
python scripts/assemble_book.py publications/manifests/example_book.yaml
```

**Features:**
- Manifest-driven book assembly
- Heading level adjustment
- Section exclusion
- Directory globbing for bulk file inclusion
- Optional TOC generation

### generate_docs.py

Generates markdown documentation from YAML source files using Jinja2 templates.

```bash
# Show available options
python scripts/generate_docs.py --help

# Generate example documentation
python scripts/generate_docs.py --example

# Validate YAML structure
python scripts/generate_docs.py --validate
```

**Features:**
- YAML to markdown conversion
- Jinja2 templating for flexible output
- Extensible generator pattern
- YAML validation

### validate_yaml_sync.py

Validates that YAML-SOURCE markers in markdown files point to valid YAML paths.

```bash
python scripts/validate_yaml_sync.py
```

**Features:**
- Scans markdown for YAML-SOURCE markers
- Verifies paths exist in YAML files
- Reports missing or invalid references

## YAML-SOURCE Marker Format

Mark mechanical content in markdown that comes from YAML:

```markdown
<!-- YAML-SOURCE: character.yaml > species > elf > bonus -->
Elves gain +1 to Agility
<!-- /YAML-SOURCE -->
```

The validation script will verify that `character.yaml` contains the path `species > elf > bonus`.
