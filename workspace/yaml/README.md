# YAML Source Files

This directory contains the structured YAML data that serves as the **source of truth** for all game mechanics.

## Philosophy

YAML files define the mechanical truth of your game system. Markdown files provide narrative context and publication-ready documentation. When these differ, YAML is correct.

## File Structure

```
yaml/
├── index.yaml          # Master reference (version, metadata, design philosophy)
├── example_system.yaml # Example structure for game systems
└── [your files].yaml   # Add your game system files
```

## Suggested File Organization

Organize YAML files by major game system:

| File | Contents |
|------|----------|
| `index.yaml` | Version, metadata, design philosophy, file references |
| `core_rules.yaml` | Dice mechanics, attributes, skills, resolution |
| `character.yaml` | Species, classes, creation process |
| `combat.yaml` | Action economy, health, damage, tactics |
| `magic.yaml` | Spells, casting, magical traditions |
| `advancement.yaml` | Progression, abilities, milestones |
| `equipment.yaml` | Weapons, armor, gear |
| `gm_tools.yaml` | Adversary creation, encounter design, tables |

## YAML Schema Conventions

### Top-Level Structure

```yaml
# Metadata
_meta:
  file: "filename.yaml"
  description: "What this file contains"
  last_updated: "2024-01-01"

# Main content sections
section_name:
  subsection:
    key: value
```

### Common Patterns

**Lists with details:**
```yaml
species:
  elf:
    name: "Elf"
    description: "Graceful and long-lived"
    attribute_bonus: "Agility +1"
    special_ability: "Low-light vision"
```

**Formulas and mechanics:**
```yaml
derived_stats:
  health:
    formula: "10 + Constitution modifier"
    description: "How much damage you can take"
```

**Tiered content:**
```yaml
spells:
  tier_1:
    - name: "Magic Missile"
      cost: 1
      effect: "1d4+1 force damage"
  tier_2:
    - name: "Fireball"
      cost: 3
      effect: "6d6 fire damage in area"
```

## Linking to Markdown

Use YAML-SOURCE markers in markdown to track mechanical content:

```markdown
<!-- YAML-SOURCE: character.yaml > species > elf > attribute_bonus -->
Elves gain +1 to Agility
<!-- /YAML-SOURCE -->
```

Run `python scripts/validate_yaml_sync.py` to verify these markers.

## Best Practices

1. **Edit YAML first** for any mechanical changes
2. **Use descriptive keys** that match how you talk about the content
3. **Include descriptions** for complex mechanics
4. **Keep related content together** in the same file
5. **Use `_meta` sections** for file-level metadata
6. **Validate often** to catch sync issues early
