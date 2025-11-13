# YAML-First Development Workflow

## Overview

This project uses YAML as the single source of truth for all game mechanics. Markdown documentation is generated from YAML using Jinja2 templates.

## Quick Start

### Prerequisites

```bash
# Activate virtual environment (first time setup)
python3 -m venv venv
source venv/bin/activate
pip install jinja2 pyyaml
```

### Generate Documentation

```bash
# Activate virtual environment
source venv/bin/activate

# Generate all documentation
python scripts/generate_docs.py --all

# Generate specific systems
python scripts/generate_docs.py --callings
python scripts/generate_docs.py --armor
python scripts/generate_docs.py --spells

# Validate YAML consistency
python scripts/generate_docs.py --validate
```

## Directory Structure

```
Flow RPG/drafts/
├── yaml/                          # Single source of truth for mechanics
│   ├── character.yaml            # Callings, species, archetypes
│   ├── equipment.yaml            # Weapons, armor, gear
│   ├── magic.yaml                # Spells and casting
│   └── ...
│
├── templates/
│   ├── generators/               # Jinja2 templates
│   │   ├── callings.jinja
│   │   ├── armor.jinja
│   │   └── spells.jinja
│   ├── narrative/                # Hand-written flavor text
│   └── output/                   # Generated markdown (gitignored)
│       ├── calling_mechanics.md
│       ├── armor_mechanics.md
│       └── spell_mechanics.md
│
└── scripts/
    └── generate_docs.py          # Generator script
```

## Workflow

### 1. Edit Mechanics in YAML

All mechanical changes happen in YAML files:

```yaml
# Example: Rebalancing a calling in yaml/character.yaml
callings:
  advocate:
    flow_benefit:
      trigger: "When you or ally reveals truth"
      effect: "Gain +1 Flow"
      limit: "No limit per scene"
```

### 2. Validate Changes

```bash
python scripts/generate_docs.py --validate
```

This checks:
- All callings have required fields
- Armor types are complete
- YAML syntax is valid

### 3. Generate Documentation

```bash
python scripts/generate_docs.py --all
```

Generates markdown files in `templates/output/` from YAML data.

### 4. Review Generated Output

Check `templates/output/` for generated markdown:
- `calling_mechanics.md` - All calling mechanics
- `armor_mechanics.md` - Armor system reference
- `spell_mechanics.md` - Complete spell list

### 5. Iterate

Make changes to YAML, regenerate, review. Repeat.

## Why This Approach?

### Single Source of Truth
- All mechanics live in YAML
- No duplication across files
- Change once, updates everywhere

### Fast Iteration
- Rebalance numbers in seconds
- Regenerate all docs instantly
- See changes immediately

### Separation of Concerns
- **YAML:** Pure mechanical data
- **Templates:** Presentation and formatting
- **Narrative:** Hand-written flavor text (separate files)

### Version Control Benefits
- Track meaningful changes (mechanics, not formatting)
- Diff shows actual balance changes
- Easy to revert specific mechanical tweaks

### Automation Ready
- Machine-readable data format
- Can generate character sheets, apps, tools
- Programmatic validation of balance

## Template Development

Templates use Jinja2 syntax to transform YAML into markdown:

```jinja
{% for calling_id, calling in callings.items() %}
## {{ calling.name }}
*"{{ calling.core_drive }}"*

### Flow Benefit: {{ calling.flow_benefit.name }}
- **Trigger:** {{ calling.flow_benefit.trigger }}
- **Effect:** {{ calling.flow_benefit.effect }}
{% endfor %}
```

### Creating New Templates

1. Add template to `templates/generators/`
2. Use Jinja2 syntax to access YAML data
3. Add generator function to `scripts/generate_docs.py`
4. Test with `--validate` and generation commands

## Common Tasks

### Rebalance a Calling
1. Edit `yaml/character.yaml`
2. Find the calling under `callings:`
3. Change trigger, effect, or limit
4. Run: `python scripts/generate_docs.py --callings`
5. Review: `templates/output/calling_mechanics.md`

### Adjust Armor Values
1. Edit `yaml/equipment.yaml`
2. Find armor under `armor.types`
3. Change DR, penalties, or benefits
4. Run: `python scripts/generate_docs.py --armor`
5. Review: `templates/output/armor_mechanics.md`

### Modify Spell Effects
1. Edit `yaml/magic.yaml`
2. Find spell under appropriate tier
3. Change damage, range, or attribute variations
4. Run: `python scripts/generate_docs.py --spells`
5. Review: `templates/output/spell_mechanics.md`

### Batch Changes
1. Edit multiple YAML files
2. Run: `python scripts/generate_docs.py --all --validate`
3. Check validation passes
4. Review all generated files

## Tips

### Keep YAML Clean
- Consistent indentation (2 spaces)
- Descriptive keys and values
- Comments for complex mechanics
- Validate after every major change

### Template Best Practices
- Focus on mechanics in templates
- Put narrative in separate files
- Test templates with minimal data first
- Add error handling for missing fields

### Git Workflow
- Commit YAML changes with clear messages
- Don't commit `templates/output/` (gitignored)
- Templates are source files (commit them)
- Document major mechanical changes in commit messages

## Troubleshooting

### "No module named 'jinja2'"
```bash
source venv/bin/activate
pip install jinja2 pyyaml
```

### "Template not found"
Check that templates exist in `templates/generators/`

### "No data found"
Verify YAML structure matches what generator expects. Check YAML keys.

### Validation Errors
Read error messages carefully. They point to specific missing fields or incorrect structure.

### Empty Output
Check that YAML file exists and has correct structure. Verify generator is looking at right keys.

## Future Expansion

This workflow can be extended to generate:
- Character sheets (interactive forms)
- Quick reference cards (printable PDFs)
- Digital tools (web apps, Discord bots)
- Balance analysis (automated calculations)
- Publication-ready documents (combine with existing assembly system)

The YAML foundation makes all of this possible with minimal effort.

---

*This workflow enables rapid iteration on game mechanics while maintaining a clear, maintainable codebase.*
