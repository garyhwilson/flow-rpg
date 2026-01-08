# Core Rules

This directory contains the fundamental rules of your game system.

## Structure

Organize your core rules into numbered files for easy reference and publication:

```
core_rules/
├── 00_introduction.md      # What is this game?
├── 01_basic_mechanics.md   # Dice, resolution, core concepts
├── 02_character_creation.md # Making a character
├── 03_combat.md            # Fighting and action
├── 04_magic.md             # Spellcasting (if applicable)
├── 05_advancement.md       # Character growth
├── 06_equipment.md         # Gear and items
└── 07_gm_guide.md          # Running the game
```

## Tips

1. **Start with mechanics** - Define how dice work before everything else
2. **Be concise** - Players should find rules quickly
3. **Use examples** - Show, don't just tell
4. **Cross-reference** - Link between sections where concepts overlap

## YAML Integration

For mechanical content that should stay in sync with YAML, use markers:

```markdown
<!-- YAML-SOURCE: core_rules.yaml > resolution > target_numbers -->
**Target Numbers:**
- Easy: 5
- Normal: 10
- Hard: 15
<!-- /YAML-SOURCE -->
```
