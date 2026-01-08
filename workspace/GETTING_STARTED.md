# Getting Started with TTRPG Development

This guide explains how to use this template for developing tabletop RPG systems.

## Table of Contents

1. [Environment Setup](#environment-setup)
2. [Understanding the Dual-Format System](#understanding-the-dual-format-system)
3. [YAML-First Development Workflow](#yaml-first-development-workflow)
4. [Modular Content Structure](#modular-content-structure)
5. [Publication Assembly](#publication-assembly)
6. [YAML-SOURCE Markers](#yaml-source-markers)
7. [Best Practices](#best-practices)

---

## Environment Setup

### Requirements

- Python 3.6 or higher
- pip (Python package manager)

### Installation

```bash
# Navigate to your project directory
cd /path/to/your/project

# Install dependencies
pip install -r scripts/requirements.txt

# Or install individually
pip install pyyaml jinja2
```

### Verify Installation

```bash
# Test the assembly script
python scripts/assemble_book.py publications/manifests/example_book.yaml

# Check the output
cat publications/assembled/example_book.md
```

---

## Understanding the Dual-Format System

This template uses two parallel formats for game content:

### YAML Files (`yaml/` directory)
- **Purpose**: Machine-readable source of truth for mechanics
- **Contains**: Rules, formulas, stats, structured game data
- **Used for**: Validation, tooling, consistency checking
- **Edit these FIRST** when making mechanical changes

### Markdown Files (content directories)
- **Purpose**: Human-readable documentation for publication
- **Contains**: Narrative descriptions, examples, flavor text
- **Used for**: Reading, playtesting, publication assembly
- **Edit these** for prose and presentation changes

### Why Both?

The YAML files ensure mechanical consistency across your system. The markdown files provide rich, readable documentation. The publication system combines markdown files into complete books, while validation ensures the markdown stays in sync with YAML.

---

## YAML-First Development Workflow

When making changes to your game system:

### Mechanical Changes (stats, formulas, rules)

1. **Edit the YAML file** in `yaml/` directory
2. **Update corresponding markdown** to match
3. **Run validation**: `python scripts/validate_yaml_sync.py`
4. **Assemble publications** to review

### Narrative Changes (descriptions, examples)

1. **Edit markdown directly** (no YAML involved)
2. **Keep changes outside YAML-SOURCE markers**
3. **Assemble publications** to review

### The Golden Rule

> **Never edit mechanical values in markdown without first updating the YAML source file.**

---

## Modular Content Structure

Use this 4-file pattern for major content categories:

```
content_category/
├── 00_introduction.md       # Overview and purpose
├── 01_gm_guidelines.md      # How GMs should use this content
├── 02_system_integration.md # How this connects to other systems
├── 03_quick_reference.md    # Tables and summaries
└── content_types/           # Individual items
    ├── item_a.md
    ├── item_b.md
    └── item_c.md
```

### Benefits

- **Consistent organization** across all content types
- **Flexible publication** - include what you need per book
- **Easy navigation** - predictable file locations
- **GM support** - dedicated guidance section for each system

### Example Categories

- Character classes/archetypes
- Species/ancestry/heritage options
- Spell systems and spell lists
- Equipment and gear
- Monsters and adversaries
- Setting regions or factions

---

## Publication Assembly

The manifest system lets you assemble different books from the same source files.

### Creating a Manifest

Create a YAML file in `publications/manifests/`:

```yaml
title: "Player's Handbook"
version: "1.0"
output_file: "publications/assembled/players_handbook.md"

sections:
  - title: "Getting Started"
    content:
      - file: "core_rules/00_introduction.md"
      - file: "core_rules/01_basic_mechanics.md"

  - title: "Character Creation"
    content:
      - file: "content_modules/00_introduction.md"
      - files_from_directory: "content_modules/content_types/*.md"
        sort: alphabetical
```

### Assembling a Book

```bash
python scripts/assemble_book.py publications/manifests/your_manifest.yaml
```

### Manifest Features

| Feature | Usage | Purpose |
|---------|-------|---------|
| `file:` | Single file inclusion | Include one file |
| `files_from_directory:` | Glob pattern | Include multiple files |
| `heading_level_adjust:` | +1 or -1 | Promote/demote headings |
| `exclude_sections:` | List of titles | Skip sections from file |
| `rename_to:` | New title | Rename first heading |
| `section_header:` | Title text | Add divider heading |

See `publications/manifests/README.md` for complete documentation.

---

## YAML-SOURCE Markers

Mark mechanical content that comes from YAML files:

```markdown
<!-- YAML-SOURCE: character.yaml > species > elf > attribute_bonus -->
Elves gain +1 to Grace
<!-- /YAML-SOURCE -->
```

### Benefits

- **Validation**: Script can check these match YAML
- **Clarity**: Know what content needs YAML updates
- **Maintenance**: Find all places affected by mechanical changes

### Validation

```bash
python scripts/validate_yaml_sync.py
```

This scans markdown files for YAML-SOURCE markers and verifies the paths exist in the corresponding YAML files.

---

## Best Practices

### From Experience Building TTRPG Systems

1. **YAML is source of truth** - Always edit YAML first for mechanics
2. **Modularize early** - Use the 4-file pattern from the start
3. **Examples over theory** - Show concrete examples before explaining rules
4. **Named characters** - Use specific NPCs, not generic "Enemy Type A"
5. **Flat lists** - Avoid complex taxonomies and category systems

### Avoiding Common Pitfalls

- **Don't duplicate mechanics** - If it's in YAML, reference it, don't copy it
- **Don't over-categorize** - Let patterns emerge from examples
- **Don't use video game terms** - "Boss", "minion", "elite", "threat level" feel wrong in TTRPG
- **Don't create formulas** - Give ranges and guidelines, not rigid calculations

### Writing Style

- **Inspire, don't prescribe** - Show GMs possibilities
- **Characters have names** - Captain Vex, not "Standard Guard"
- **Story before stats** - Who they are matters more than numbers
- **Trust the GM** - They know their table better than any formula

---

## Next Steps

1. Read [CLAUDE.md](CLAUDE.md) for design philosophy guidance
2. Review example files in each directory
3. Start defining your core mechanics in `yaml/index.yaml`
4. Build out your first content module
5. Create a manifest and assemble your first publication

Good luck with your TTRPG system!
