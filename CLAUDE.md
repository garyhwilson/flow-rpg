# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Workflow & Development Tracking**: For active development priorities, outstanding issues, session history, and git workflow, see [.claude/instructions.md](.claude/instructions.md).

## Repository Overview

This repository contains **Flow RPG Sweet Spot Edition**, a tabletop RPG system designed for 8-12 session campaigns with bounded accuracy mechanics. The system is implemented in two parallel formats:

1. **YAML structured data** (yaml/ directory) - Machine-readable game rules
2. **Markdown narrative** (core_rules/, callings/, etc.) - Human-readable documentation

Both formats contain the same game system but serve different purposes: YAML for tooling/automation, Markdown for publication.

## Design Philosophy: TTRPG Not Video Game

**CRITICAL**: This is a tabletop roleplaying game, not a video game. Every design decision, term, and mechanic must reflect TTRPG principles, not MMO/video game patterns.

### The Video Game Trap

Video game design patterns are fundamentally incompatible with TTRPG play:

**Forbidden Patterns**:
- Formulaic stat scaling (e.g., "Guard = 8 + milestones × 2")
- Enemy "types" or "tiers" as interchangeable units
- "Squad composition" language (e.g., "1 Elite + 4 Henchmen")
- Role trinity thinking (Tank/Healer/DPS)
- "Encounter balance" calculations
- Treating adversaries as stat blocks without personality

**What This Looks Like in Practice**:
- WRONG: "For a Medium encounter, use 2 Standards OR 4 Henchmen + 1 Standard"
- RIGHT: "Captain Vex (experienced Guard officer) might bring 3-5 soldiers depending on the situation"

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

### Red Flags vs Green Flags

When reviewing or creating content, watch for these indicators:

**Red Flags (Video Game Thinking)**:
- Words like: boss, minion, elite squad, raid, aggro, DPS
- Phrases like: "encounter composition", "threat level", "stat block template"
- Mathematical scaling formulas tied to character level/milestones
- "Balance guidelines" that treat enemies as interchangeable units
- Role-based design (controller, striker, defender, etc.)

**Green Flags (TTRPG Thinking)**:
- Named characters with motivations: "Captain Vex wants revenge"
- Situational guidance: "A squad of guards typically has..."
- Story-first design: "What would make sense for this villain?"
- Emphasis on consequences over mechanics
- GM empowerment over rigid rules

### How to Audit Content

When writing or reviewing any game content, ask:

1. **Does this sound like a tabletop game or World of Warcraft?**
2. **Are we describing characters or stat blocks?**
3. **Is the GM empowered to make narrative choices, or forced to follow formulas?**
4. **Would this language appear in D&D/Fate/PbtA, or in an MMO wiki?**

If it sounds like video game design, rewrite it with TTRPG principles.

## Core Architecture

### Dual-Format System

**YAML Files** (`yaml/` directory):
- Complete game rules as structured data
- 10 component files referenced by `index.yaml`
- Used for validation, tooling, and future digital implementations
- **Master files**: All balance fixes and playtesting changes happen here first

**Markdown Files** (multiple directories):
- Narrative documentation of the same system
- Organized for human reading and publication
- Assembled into books via `scripts/assemble_book.py`
- Should mirror YAML content but in prose form

### Key Design Principle: Bounded Accuracy

The system uses a **hard +5 total modifier cap** (attribute +3, skill +2, edges +1) to maintain meaningful dice rolls throughout 8-12 session campaigns. This is enforced mathematically:

- At +0 modifier vs TN 8: 58% success (challenging)
- At +5 modifier vs TN 8: 97.2% success (nearly automatic)
- **Critical**: GMs must use TN 10-12 for late-game challenges (sessions 7-12)

This cap is THE fundamental constraint - do not suggest changes that break it.

## Essential Commands

### Assemble Publications

```bash
# Install dependencies (first time only)
pip install pyyaml

# Assemble specific book from YAML manifests
python scripts/assemble_book.py publications/manifests/core_rulebook.yaml
python scripts/assemble_book.py publications/manifests/players_guide.yaml
python scripts/assemble_book.py publications/manifests/gm_guide.yaml

# Output appears in: publications/assembled/
```

### Generate Documentation from YAML

```bash
# Convert YAML files to markdown documentation
python scripts/generate_docs.py

# This syncs yaml/ content to markdown files
```

## Critical YAML Files

When making balance changes, **always edit YAML first**, then sync to markdown:

### Core System Files (yaml/ directory)

1. **index.yaml** - Master reference, version info, design philosophy
2. **core_rules.yaml** - Resolution mechanics, Flow system, attributes, skills
3. **advancement.yaml** - Milestone system, edges, build paths, power progression
4. **gm_tools.yaml** - Encounter building, enemy templates, TN scaling guidance
5. **combat.yaml** - Stance system, health, death saves
6. **magic.yaml** - Spell system, casting mechanics
7. **character.yaml** - Species, archetypes, callings, creation process
8. **techniques.yaml** - Combat techniques, metamagic, abilities
9. **equipment.yaml** - Weapons, armor, gear
10. **examples.yaml** - Pre-gen characters, quick-start rules, play examples

### Recently Fixed Issues (DO NOT REVERT)

**Phase 1 - Critical Fixes**:
- Powerful adversary action economy: Maximum 2 attacks per round (gm_tools.yaml:133-167)
- Deepen Expertise: Requires 3 consecutive minors, not 2 (advancement.yaml:67-76)
- Example characters: All Guard/skill values corrected (examples.yaml)

**Phase 2 - Balance Tuning**:
- Flow generation: "Taking damage" limited to once per round (core_rules.yaml:176-180)
- High Flow bonus: Removed "+1 to all rolls" at Flow 4-6 (core_rules.yaml:160-167)
- TN scaling: Comprehensive guidance for GMs (gm_tools.yaml:507-573)

**Phase 3 - Accessibility**:
- Simplified rules for first sessions (examples.yaml:24-93)
- Default build paths to reduce option paralysis (advancement.yaml:862-982)
- Optional GM Flow pool with guidance (gm_tools.yaml:162-200)

## Key Mathematical Constraints

### Success Rates (2d6 + modifier vs TN)

At +5 cap vs TN 8: 97.2% (nearly automatic - only fail on 1,1)
At +5 cap vs TN 10: 72.2% (meaningful challenge)
At +5 cap vs TN 12: 41.7% (hard challenge)

### Guard Formula

**NEW**: `12 + max(Might, Grace, Will)`
**OLD** (removed): `8 + attribute + milestones`

Do not use the old formula - all examples have been corrected.

### Skill Tiers

- Untrained: -2
- Novice: +0 (not -1)
- Competent: 0
- Professional: +1 (not +2)
- Expert: +2 (max, not +3)

### Flow Range

-3 to +6 (not -5 to +10 from older versions)

## Working with Playtesting Results

This system underwent exhaustive playtesting that identified and fixed critical issues. When analyzing balance:

1. **Trust the math**: Success rates are calculated, not estimated
2. **Major threat conflicts**: Test with 2 attack maximum, not 3
3. **Progression timing**: +5 cap should hit Session 4-6, not Session 3
4. **TN scaling**: Late game (sessions 7-12) requires TN 10-12 for challenges

## Publication Workflow

When updating game content:

1. **Edit YAML files** in yaml/ directory (source of truth for mechanics)
2. **Run generate_docs.py** to sync changes to markdown (if script supports this)
3. **Update markdown manually** if needed for narrative/examples
4. **Assemble books** using manifests when ready to review full documents
5. **Test assembled output** before considering it final

## Directory Structure Worth Knowing

```
drafts/
├── yaml/                    # YAML structured rules (EDIT HERE FIRST)
│   ├── index.yaml          # Master reference
│   ├── core_rules.yaml     # Resolution & Flow mechanics
│   ├── advancement.yaml    # Milestones, build paths
│   ├── gm_tools.yaml       # Adversary guidance, TN scaling
│   └── [6 other component files]
├── scripts/
│   ├── assemble_book.py    # Build publications from manifests
│   └── generate_docs.py    # Convert YAML to markdown
├── publications/
│   ├── manifests/          # YAML files defining book structure
│   ├── templates/          # Reusable content (title pages, etc.)
│   └── assembled/          # OUTPUT: Generated books (gitignored)
├── core_rules/             # Markdown narrative (9 sections)
├── callings/               # 9 calling types + introduction
└── [other markdown directories]
```

## Common Tasks

### Adding New Content

**New spell**:
1. Add to `yaml/magic.yaml` in appropriate tier
2. Update spell count in `index.yaml`
3. Add narrative description to `core_rules/05_magic_system.md`
4. Reassemble grimoire: `python scripts/assemble_book.py publications/manifests/grimoire.yaml`

**New adversary**:
1. Start with narrative concept (who they are, what they want)
2. Use stat guidance from `gm_tools.yaml` as starting point
3. Adjust based on story needs - stats serve the narrative
4. Give them a name and motivation, not just a stat block

**Balance change**:
1. Edit YAML file (e.g., `advancement.yaml` for milestone options)
2. Update design notes in `index.yaml` if philosophy changed
3. Sync to markdown documentation
4. Update examples if mechanics changed

### Verifying Balance

**Check modifier caps**:
```yaml
# In advancement.yaml or character.yaml
total_modifier_maximum: "+5"
formula: "Attribute + Skill + Edges ≤ 5"
```

**Check Guard formula**:
```yaml
# In core_rules.yaml or examples.yaml
guard: "12 + max(Might, Grace, Will)"  # CORRECT
# NOT: "8 + attribute + milestones"     # OLD/WRONG
```

**Check powerful adversary action economy**:
```yaml
# In gm_tools.yaml
critical_rule: "Champions can make MAXIMUM 2 ATTACKS per round"
```

## Design Philosophy

From `index.yaml` - keep these principles in mind:

1. **Bounded accuracy that ACTUALLY works** - Hard +5 cap required
2. **8-12 sessions is the sweet spot** - Campaign concludes at peak power
3. **TN scaling is mandatory** - GMs must use TN 10-12 at sessions 7-12
4. **Horizontal growth after cap** - Players gain versatility, not raw power
5. **Archetypes are optional** - Custom Build is equally viable

## What Not to Change

- The +5 total modifier cap (breaks bounded accuracy)
- Champion/powerful adversary 2-attack maximum (causes TPK with 3 attacks)
- Deepen Expertise 3-minor requirement (2 minors hits cap too early)
- Guard formula (12 + max, not 8 + attribute)
- Flow range -3 to +6 (other ranges tested and rejected)
- Skill tier modifiers (Professional = +1, not +2)

These were all extensively playtested and mathematically validated.
