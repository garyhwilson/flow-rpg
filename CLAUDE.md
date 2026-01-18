# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Workflow & Development Tracking**: For active development priorities, outstanding issues, session history, and git workflow, see [.claude/instructions.md](.claude/instructions.md).

## Repository Overview

This repository contains **Autumn Phoenix RPG**, a tabletop RPG system designed for 30-50 session campaigns with bounded accuracy mechanics. The system is implemented in two parallel formats:

1. **YAML structured data** (yaml/ directory) - Machine-readable game rules, source of truth for mechanics
2. **Markdown narrative** (core_rules/, callings/, etc.) - Human-readable documentation for publication

Both formats contain the same game system. YAML is authoritative for mechanical values; Markdown mirrors it in prose form.

## Design Philosophy: TTRPG Not Video Game

**CRITICAL**: This is a tabletop roleplaying game, not a video game. Every design decision, term, and mechanic must reflect TTRPG principles, not MMO/video game patterns.

### Forbidden Patterns

Video game design patterns are fundamentally incompatible with TTRPG play:

- Formulaic stat scaling (e.g., "Guard = 8 + milestones × 2")
- Enemy "types" or "tiers" as interchangeable units
- "Squad composition" language (e.g., "1 Elite + 4 Henchmen")
- Role trinity thinking (Tank/Healer/DPS)
- "Encounter balance" calculations
- Treating adversaries as stat blocks without personality
- Words like: boss, minion, elite squad, raid, aggro, DPS
- Phrases like: "encounter composition", "threat level", "stat block template"
- Numbered threat/tier systems ("Threat 1: Henchmen", "Tier 1-5 Encounters")
- Category-first organization ("Opposition Patterns", "Edge Categories", "NPC Types")

**WRONG**: "For a Medium encounter, use 2 Standards OR 4 Henchmen + 1 Standard"
**RIGHT**: "Captain Vex (experienced Guard officer) might bring 3-5 soldiers depending on the situation"

### Required TTRPG Approach

**Named adversaries with motivations**:
- Every significant opponent should have a name and reason for opposing the PCs
- Stats serve the story, not the other way around
- GMs should create specific individuals, not fill "roles"

**Narrative-driven opposition**:
- Scene difficulty comes from circumstances, not stat block math
- Consequences matter more than hit points
- Social and environmental challenges are as important as combat

**GM judgment over formulas**:
- Provide ranges and examples, not rigid formulas
- Emphasize "create what feels right for your story"
- Trust GMs to balance their own campaigns

### The Test

When writing or reviewing any game content, ask:

1. Does this sound like a tabletop game or World of Warcraft?
2. Are we describing characters or stat blocks?
3. Is the GM empowered to make narrative choices, or forced to follow formulas?
4. Would this language appear in D&D/Fate/PbtA, or in an MMO wiki?

If it sounds like video game design, rewrite it with TTRPG principles.

## Documentation Standards: Examples First

Traditional TTRPG documentation shows examples and lets patterns emerge naturally. Video game design documents categorize first and provide examples second. Autumn Phoenix follows TTRPG traditions.

**RIGHT - Examples First:**

```markdown
## Captain Sera Blackthorn Hunts Heretics

Captain Sera Blackthorn leads the city's elite guard...
**Stats:** Guard 22, Vitality 30, Damage 2d6+1

---

## The Red Cloak Gang Demands Tribute

Street thugs working for crime lord Vex...

---

## Building Your Own Conflicts

Every adversary should be a character with a name, motivation, and personality...
```

**WRONG - Categories First:**

```markdown
## Opposition Patterns

### Organized Authority
This pattern represents law enforcement...
**Example:** Captain Sera Blackthorn
```

**Why this matters:**
- GMs see what to do immediately (concrete examples)
- Patterns emerge naturally from studying examples
- Matches how traditional TTRPG books work (Monster Manual, Bestiary)
- Inspires creativity rather than constraining it

**Practical guidelines:**
1. Start with 5-7 concrete, named examples
2. Add guidance section AFTER examples
3. Use natural language groupings ("Lesser adversaries" not "Henchmen Type")
4. Ask: "Does this read like a published game book or internal design documentation?"

## Core Architecture

### Dual-Format System

**YAML Files** (`yaml/` directory):
- Complete game rules as structured data
- 10 component files referenced by `index.yaml`
- **Source of truth**: All mechanical values live here

**Markdown Files** (multiple directories):
- Narrative documentation for publication
- Assembled into books via `scripts/assemble_book.py`
- Must match YAML for mechanical content

### Key Design Principle: Bounded Accuracy

The system uses a **hard +5 total modifier cap** (attribute +3, skill +2) to maintain meaningful dice rolls throughout 30-50 session campaigns:

- At +0 modifier vs TN 8: 42% success
- At +5 modifier vs TN 8: 97.2% success (nearly automatic)
- **Critical**: GMs must use TN 10-12 for late-game challenges

## Essential Commands

```bash
# Assemble publications
python scripts/assemble_book.py publications/manifests/core_rulebook.yaml
python scripts/assemble_book.py publications/manifests/players_guide.yaml
python scripts/assemble_book.py publications/manifests/gm_guide.yaml

# Generate docs from YAML
python scripts/generate_docs.py

# Validate YAML-Markdown sync
python scripts/validate_yaml_sync.py
```

## YAML-Markdown Sync Workflow

YAML files are the **source of truth** for mechanical values. Markdown contains both mechanical content (must match YAML) and narrative content (hand-written).

**When making MECHANICAL changes:**
1. Edit the YAML file first
2. Update the markdown to match
3. Run validation script
4. Reassemble publications

**When making NARRATIVE changes:**
1. Edit markdown directly
2. Reassemble publications

**Rule:** Never edit mechanical values in markdown without first updating the YAML source file.

## Core YAML Files

1. **index.yaml** - Master reference, version info
2. **core_rules.yaml** - Resolution mechanics, Momentum, attributes, skills
3. **advancement.yaml** - XP/Ranks system, build paths
4. **gm_tools.yaml** - Encounter building, TN scaling guidance
5. **combat.yaml** - Stance system, health, death saves
6. **magic.yaml** - Spell system, casting mechanics
7. **character.yaml** - Species, archetypes, callings
8. **techniques.yaml** - Combat techniques, metamagic
9. **equipment.yaml** - Weapons, armor, gear
10. **examples.yaml** - Pre-gen characters, quick-start rules

## Key Mathematical Constraints

### Modifier Cap
- **Total maximum:** +5 (Attribute +3 + Skill +2)
- Specialties only add if room remains under cap

### Success Rates (2d6 + modifier vs TN)
- At +5 vs TN 8: 97.2% (only fail on snake eyes)
- At +5 vs TN 10: 83% (reliable)
- At +5 vs TN 12: 58% (challenging)

### Guard Formula
`12 + max(Might, Grace, Will)`

### Skill Tiers
- Untrained: -2
- Novice: -1
- Competent: 0
- Professional: +1
- Expert: +2 (max)

### Momentum Range
-3 to +6

### Campaign Structure
- **5 Ranks:** Novice → Seasoned → Veteran → Heroic → Legendary
- **Advancement:** 5 XP = 1 Advance, 4 Advances per Rank
- **+5 cap reached:** Typically at Veteran rank (sessions 11-15)
- **TN scaling:** GMs increase TNs as characters grow

## Directory Structure

```
drafts/
├── yaml/                    # YAML structured rules (EDIT HERE FIRST)
├── scripts/
│   ├── assemble_book.py    # Build publications from manifests
│   └── generate_docs.py    # Convert YAML to markdown
├── publications/
│   ├── manifests/          # YAML files defining book structure
│   ├── templates/          # Reusable content
│   └── assembled/          # OUTPUT: Generated books (gitignored)
├── core_rules/             # Markdown narrative
├── callings/               # Calling documentation
└── [other markdown directories]
```

## Validated Design Decisions

These decisions emerged from playtesting and mathematical validation:

| Decision | Rationale |
|----------|-----------|
| +5 modifier cap | Maintains bounded accuracy |
| Powerful adversary 2-attack max | 3 attacks causes TPK |
| Guard = 12 + max(Might, Grace, Will) | Replaces milestone-scaling formula |
| Momentum range -3 to +6 | Other ranges tested and rejected |
| Skill tiers (Professional = +1, Expert = +2) | Prevents early cap |
| TN scaling mandatory | +5 vs TN 8 is 97% - not a challenge |

## Common Tasks

**New adversary:**
1. Start with narrative concept (who they are, what they want)
2. Use stat guidance from `gm_tools.yaml` as starting point
3. Give them a name and motivation, not just a stat block

**Balance change:**
1. Edit YAML file first
2. Update design notes in `index.yaml` if philosophy changed
3. Sync to markdown documentation
4. Update examples if mechanics changed
