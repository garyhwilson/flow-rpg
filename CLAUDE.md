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

## Documentation Presentation Standards

**CRITICAL**: How we present information is as important as what information we present. Traditional TTRPG documentation shows examples and lets patterns emerge naturally. Video game design documents categorize first and provide examples second. Flow RPG must follow TTRPG traditions.

### Examples-First Philosophy

**Always show concrete examples before theory or categorization:**

**RIGHT - Examples First:**
```markdown
## Captain Sera Blackthorn Hunts Heretics

Captain Sera Blackthorn leads the city's elite guard. She's hunting the party
because they're accused of stealing a sacred relic...

**Stats:** Guard 22, Vitality 30, Damage 2d6+1
**Tactics:** Coordinates squad to separate party members...

---

## The Red Cloak Gang Demands Tribute

Street thugs working for crime lord Vex. They're in it for money, not loyalty...

---

## Building Your Own Conflicts

Every adversary should be a character with a name, motivation, and personality...
```

**WRONG - Categories First:**
```markdown
## Opposition Patterns

### Organized Authority
This pattern represents law enforcement and military forces.
**Example:** Captain Sera Blackthorn

### Criminal Elements
This pattern represents criminal organizations.
**Example:** The Red Cloak Gang
```

**Why Examples-First Works:**
- GMs see what to do immediately (concrete examples)
- Patterns emerge naturally from studying examples
- Inspires creativity rather than constraining it
- Matches how traditional TTRPG books work (Monster Manual, Bestiary)
- Encourages adaptation over formula-following

### Avoid Video Game Taxonomy

**Forbidden taxonomic patterns:**

**Numbered Threat/Tier Systems:**
- "Threat 1: Henchmen", "Threat 2: Standard", "Threat 3: Champions", "Threat 4: Legendary"
- "Tier 1-5 Encounters", "Level 1-20 Appropriate Challenges"
- Formal numerical categorization of any kind

**Formal Type Systems as Primary Organization:**
- "Edge Categories: Combat Edges, Skill Edges, Flow Edges"
- "Opposition Patterns: Authority, Criminal, Wilderness, Supernatural"
- "NPC Types: Social, Combat, Specialist"

**Design Document Language:**
- Section headers like "Stat Guidance by Power Level"
- "Encounter Composition Guidelines"
- "Balance Formulas for Challenge Rating"

**MMO-Style Categorization:**
- Treating anything as interchangeable units in categories
- "Squad composition" thinking (1 Elite + 4 Henchmen)
- Formulaic approach to content creation

**Why Taxonomy Is Poison:**
- Makes documentation read like design docs, not game books
- Encourages formulaic thinking over creative adaptation
- Feels like video game wikis or D&D 4th Edition
- Restricts GM creativity to predefined categories
- Breaks immersion with artificial classifications

### Traditional TTRPG Presentation Patterns

**Follow these established TTRPG models:**

**D&D Monster Manual / Pathfinder Bestiary Approach:**
- Show specific creatures/NPCs with full details
- Provide 5-7 varied examples in each section
- Let GMs extrapolate patterns themselves
- Use natural language, not category labels
- Prioritize inspiration over instruction

**Good Section Headers:**
- "Creating Memorable Conflicts" (not "Opposition Patterns")
- "Available Edges" (not "Edge Categories")
- "Captain Sera Blackthorn Hunts Heretics" (not "Organized Authority Example")

**Good Organization:**
- Flat lists with concrete examples
- Descriptive phrases over formal type names ("Lesser adversaries" not "Henchmen Type")
- Guidance sections AFTER examples, not before
- Build examples showing how pieces fit together, not category definitions

**Good Presentation:**
- Named characters as primary examples
- Motivations and personality before mechanics
- Tactical variety shown through examples
- Story-first, mechanics-support approach

### Terminology Red Flags for Documentation

**These words as section headers suggest wrong approach:**

**Category/Type Language:**
- "Pattern" (as in "Opposition Patterns")
- "Category" (as in "Edge Categories")
- "Type" (as in "Enemy Types")
- "Classification" (as in "Threat Classifications")
- "Tier" (as in "Power Tiers")
- "Level" (as in "Challenge Levels")

**Okay in Body Text, Wrong as Headers:**
- These words are fine when describing things naturally
- "Different types of enemies" in a sentence = okay
- "Enemy Types" as a section header = wrong

**Better Alternatives:**
- "Creating [X]" instead of "[X] Categories"
- "Available [X]" instead of "[X] Types"
- "[Specific Named Example]" instead of "Example of [Category]"
- Natural groupings instead of formal classifications

### The Bestiary vs Design Doc Test

**When writing or reviewing documentation, ask:**

**"Is this a published game book or internal design documentation?"**

**Published Game Book (RIGHT):**
- "Captain Vex is a veteran mercenary commander who leads through respect, not fear. Her soldiers are loyal because she protects them..."
- Shows what GMs need: inspiration and guidelines
- Reads like fantasy fiction with mechanics attached
- Emphasizes story and character
- Provides ranges and examples, not formulas

**Internal Design Doc (WRONG):**
- "Threat 3 (Champion): Use when party has 6-8 milestones. Formula: Guard = 40 + (milestones × 8)"
- Shows what designers need: balance formulas and categorization
- Reads like technical specifications
- Emphasizes math and systems
- Provides rigid formulas and type definitions

**The Test:**
- Would this appear in a D&D or Pathfinder book? (Good)
- Would this appear in an MMO strategy guide or game wiki? (Bad)
- Does it inspire me to create my own content? (Good)
- Does it tell me to follow a formula? (Bad)

### Red Flags vs Green Flags for Documentation

**Red Flags (Wrong Approach):**
- Section organized by categories/types/patterns
- Numbered tier/threat/level systems
- Examples listed under category headers
- "Stat blocks by power level" thinking
- Formulas and balance calculations prominent
- Theory before examples
- Feels like filling out a template

**Green Flags (Right Approach):**
- Section organized by concrete examples
- Natural language descriptions
- Categories emerge from studying examples
- Named characters with personalities
- Guidelines and ranges, not formulas
- Examples before theory
- Feels like reading a story collection

### Case Studies: Recent Fixes

**These recent issues illustrate the problems:**

**"Paragon Paths" (advancement.yaml):**
- D&D 4th Edition terminology that snuck in
- Formal categorization system for character advancement
- Fixed by folding into mythic_edge with concrete examples

**"Opposition Patterns" (encounters.md):**
- Video game taxonomy (Organized Authority, Criminal Elements, etc.)
- Categories first, examples second
- Fixed by replacing with 5 named conflicts (Captain Sera Blackthorn, Red Cloak Gang, etc.)

**"Threat Levels" (monsters_reference.md):**
- MMO-style numbered threat system (Threat 1-4)
- Formal type classifications (Henchmen, Standard, Champions, Legendary)
- Fixed by deleting file entirely - moved to descriptive language in context

**"Edge Categories" (edges_mechanics.md):**
- Explicit categorization (Combat Edges, Skill Edges, Flow Edges, etc.)
- Category headers with examples under each
- Fixed by presenting flat list with build examples

**What These Have in Common:**
- All imposed video game/design doc structure
- All prioritized categorization over examples
- All felt like 4th Edition D&D or MMO wikis
- All fixed by examples-first approach

### Practical Guidelines

**When creating new documentation:**

1. **Start with 5-7 concrete, named examples**
   - Captain Sera Blackthorn, not "Example of Organized Authority"
   - Specific builds showing edge combinations, not "Edge Categories"
   - Named spells with flavor, not "Spell Type: Evocation"

2. **Add guidance section AFTER examples**
   - "Building Your Own Conflicts" comes after the 5 conflict examples
   - "Customizing Your Build" comes after the example builds
   - Theory emerges from examples, not vice versa

3. **Use natural language groupings if you must group**
   - "Lesser adversaries" not "Henchmen Type"
   - "Dangerous in groups" not "Threat Level 1"
   - Descriptive phrases, not formal type names

4. **Always ask: "Bestiary or Design Doc?"**
   - If it reads like a design doc, rewrite it
   - If you can't tell, show it to someone who plays TTRPGs
   - When in doubt, add more named examples

5. **Audit for category thinking**
   - Search for "Pattern", "Category", "Type" as section headers
   - Check if examples come after theory
   - Verify you're showing, not telling
   - Make sure it inspires rather than prescribes

**When reviewing existing documentation:**

1. **Look for taxonomic organization**
   - Are things organized by type/category/pattern?
   - Do section headers use classification language?
   - Is theory presented before examples?

2. **Check presentation order**
   - Examples should come first
   - Guidance should follow examples
   - Theory should emerge from studying examples

3. **Verify TTRPG voice**
   - Does it sound like D&D/Pathfinder?
   - Or does it sound like WoW/design docs?
   - Would a veteran TTRPG player recognize this as tabletop content?

4. **Test the inspiration factor**
   - Does this make me want to create my own content?
   - Or does it make me want to follow a formula?
   - Am I inspired or constrained?

### Integration with Video Game Content Warnings

**These presentation standards complement the existing video game content warnings:**

**Video Game Content Warnings (existing):** Focus on terminology and mechanical patterns
- Forbids boss/minion/elite/tank/DPS language
- Prevents formulaic stat scaling
- Stops squad composition thinking

**Documentation Presentation Standards (this section):** Focus on organization and structure
- Forbids category-first organization
- Prevents taxonomic thinking
- Stops design-doc presentation

**Together they ensure:** Flow RPG reads like a traditional TTRPG book, not a video game design document or MMO strategy guide.

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
