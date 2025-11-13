# Templates Directory

This directory contains the infrastructure for generating documentation from YAML sources.

## Directory Structure

```
templates/
├── generators/          # Jinja2 templates for mechanics
│   ├── callings.jinja
│   ├── armor.jinja
│   ├── spells.jinja
│   └── ...
├── narrative/          # Hand-written flavor text
│   ├── calling_lore.md
│   ├── magic_traditions.md
│   └── ...
└── output/             # Generated markdown (gitignored)
    ├── calling_mechanics.md
    ├── armor_mechanics.md
    └── ...
```

## Usage

### Generators Directory
Contains Jinja2 templates that transform YAML data into markdown documentation. Each template focuses on mechanical content, pulling data from the YAML files.

Example: `callings.jinja` reads from `yaml/character.yaml` and generates formatted calling documentation.

### Narrative Directory
Contains hand-written narrative content that doesn't change with mechanical rebalancing:
- Lore and flavor text
- Setting descriptions
- Example narratives
- Thematic explanations

These files can be referenced by templates or included in publications directly.

### Output Directory
Generated markdown files appear here. This directory is gitignored because the content is generated from YAML sources, not authored directly.

To regenerate: `python scripts/generate_docs.py --all`

## Workflow

1. **Edit YAML** → Single source of truth for all mechanics
2. **Run Generator** → `python scripts/generate_docs.py --callings` (or --all)
3. **Review Output** → Check `templates/output/` for generated files
4. **Iterate** → Adjust YAML or templates, regenerate

## Why This Structure?

- **YAML as Single Source** - All mechanical data lives in one place
- **Fast Iteration** - Change numbers in YAML, regenerate instantly
- **Separation of Concerns** - Mechanics (YAML) separate from presentation (templates)
- **Version Control** - Track meaningful changes (YAML edits) not formatting
- **Automation Ready** - Generated files can feed into publication assembly
