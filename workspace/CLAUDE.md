# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Workflow & Development Tracking**: For active development priorities, outstanding issues, session history, and git workflow, see [.claude/instructions.md](.claude/instructions.md).

## Repository Overview

This repository contains **[Your TTRPG System Name]**, a tabletop RPG system. The system is implemented in two parallel formats:

1. **YAML structured data** (yaml/ directory) - Machine-readable game rules
2. **Markdown narrative** (core_rules/, content_modules/, etc.) - Human-readable documentation

Both formats contain the same game system but serve different purposes: YAML for tooling/automation, Markdown for publication.

<!--
==============================================================================
PROJECT-SPECIFIC CONFIGURATION
Add your system-specific rules, constraints, and critical values here.
==============================================================================
-->

## Project-Specific Rules

<!-- Add your system's critical constraints here. Examples:
- Core dice mechanic and target numbers
- Modifier caps or bounded accuracy rules
- Character advancement structure
- Any "do not change" rules from playtesting
-->

*Add your system-specific rules and constraints here.*

<!--
==============================================================================
TTRPG DESIGN PHILOSOPHY
The following sections apply to ALL tabletop RPG projects.
Do not remove or modify these - they prevent common design mistakes.
==============================================================================
-->

## Design Philosophy: TTRPG Not Video Game

**CRITICAL**: This is a tabletop roleplaying game, not a video game. Every design decision, term, and mechanic must reflect TTRPG principles, not MMO/video game patterns.

### The Video Game Trap

Video game design patterns are fundamentally incompatible with TTRPG play:

**Forbidden Patterns**:
- Formulaic stat scaling (e.g., "Defense = 8 + level x 2")
- Enemy "types" or "tiers" as interchangeable units
- "Squad composition" language (e.g., "1 Elite + 4 Minions")
- Role trinity thinking (Tank/Healer/DPS)
- "Encounter balance" calculations
- Treating adversaries as stat blocks without personality

**What This Looks Like in Practice**:
- WRONG: "For a Medium encounter, use 2 Standards OR 4 Minions + 1 Standard"
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
- Mathematical scaling formulas tied to character level
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

**CRITICAL**: How we present information is as important as what information we present. Traditional TTRPG documentation shows examples and lets patterns emerge naturally. Video game design documents categorize first and provide examples second. Your game must follow TTRPG traditions.

### Examples-First Philosophy

**Always show concrete examples before theory or categorization:**

**RIGHT - Examples First:**
```markdown
## Captain Sera Blackthorn Hunts Heretics

Captain Sera Blackthorn leads the city's elite guard. She's hunting the party
because they're accused of stealing a sacred relic...

**Stats:** Defense 22, Health 30, Damage 2d6+1
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
- "Threat 1: Minions", "Threat 2: Standard", "Threat 3: Champions", "Threat 4: Legendary"
- "Tier 1-5 Encounters", "Level 1-20 Appropriate Challenges"
- Formal numerical categorization of any kind

**Formal Type Systems as Primary Organization:**
- "Ability Categories: Combat Abilities, Skill Abilities, Special Abilities"
- "Opposition Patterns: Authority, Criminal, Wilderness, Supernatural"
- "NPC Types: Social, Combat, Specialist"

**Design Document Language:**
- Section headers like "Stat Guidance by Power Level"
- "Encounter Composition Guidelines"
- "Balance Formulas for Challenge Rating"

**MMO-Style Categorization:**
- Treating anything as interchangeable units in categories
- "Squad composition" thinking (1 Elite + 4 Minions)
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
- "Available Abilities" (not "Ability Categories")
- "Captain Sera Blackthorn Hunts Heretics" (not "Organized Authority Example")

**Good Organization:**
- Flat lists with concrete examples
- Descriptive phrases over formal type names ("Lesser adversaries" not "Minion Type")
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
- "Category" (as in "Ability Categories")
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
- "Threat 3 (Champion): Use when party has 6-8 sessions. Formula: Defense = 40 + (sessions x 8)"
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

### Practical Guidelines

**When creating new documentation:**

1. **Start with 5-7 concrete, named examples**
   - Captain Sera Blackthorn, not "Example of Organized Authority"
   - Specific builds showing ability combinations, not "Ability Categories"
   - Named spells with flavor, not "Spell Type: Evocation"

2. **Add guidance section AFTER examples**
   - "Building Your Own Conflicts" comes after the 5 conflict examples
   - "Customizing Your Build" comes after the example builds
   - Theory emerges from examples, not vice versa

3. **Use natural language groupings if you must group**
   - "Lesser adversaries" not "Minion Type"
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

<!--
==============================================================================
TECHNICAL ARCHITECTURE
==============================================================================
-->

## Core Architecture

### Dual-Format System

**YAML Files** (`yaml/` directory):
- Complete game rules as structured data
- Component files referenced by `index.yaml`
- Used for validation, tooling, and future digital implementations
- **Master files**: All balance fixes and changes happen here first

**Markdown Files** (content directories):
- Narrative documentation of the same system
- Organized for human reading and publication
- Assembled into books via `scripts/assemble_book.py`
- Should mirror YAML content but in prose form

## Essential Commands

### Assemble Publications

```bash
# Install dependencies (first time only)
pip install -r scripts/requirements.txt

# Assemble specific book from YAML manifests
python scripts/assemble_book.py publications/manifests/example_book.yaml

# Output appears in: publications/assembled/
```

### Generate Documentation from YAML

```bash
# Convert YAML files to markdown documentation
python scripts/generate_docs.py --help

# Generate specific content
python scripts/generate_docs.py --example
```

### Validate YAML-Markdown Sync

```bash
# Check that YAML-SOURCE markers match their YAML sources
python scripts/validate_yaml_sync.py

# Run before assembling to catch documentation drift
python scripts/validate_yaml_sync.py && python scripts/assemble_book.py publications/manifests/example_book.yaml
```

## YAML-Markdown Sync Workflow

The YAML files are the **source of truth** for all mechanical values (formulas, costs, modifiers, etc.). Markdown files contain both mechanical content (which must match YAML) and narrative content (which is hand-written).

### YAML-SOURCE Markers

Mechanical content in markdown files can be marked with HTML comments to indicate it comes from YAML:

```markdown
<!-- YAML-SOURCE: character.yaml > derived_values > defense -->
**Defense:** 10 + Agility modifier
<!-- /YAML-SOURCE -->
```

### Editing Rules

**When making MECHANICAL changes:**
1. Edit the YAML file first (source of truth)
2. Find the corresponding section in markdown
3. Update the markdown to match
4. Run validation script
5. Reassemble publications

**When making NARRATIVE changes:**
1. Edit markdown directly (no YAML involved)
2. Keep edits outside of YAML-SOURCE markers
3. Reassemble publications

**Rule:** Never edit mechanical values in markdown without first updating the YAML source file.

### Preventing Documentation Drift

Common drift issues to watch for:
- Formula discrepancies between YAML and markdown
- Modifier values that don't match
- Costs or requirements that differ

When in doubt, check the YAML file - it's always the authoritative source.

## Directory Structure

```
project/
├── yaml/                    # YAML structured rules (EDIT HERE FIRST)
│   ├── index.yaml          # Master reference
│   └── [component files]   # Your game systems
├── scripts/
│   ├── assemble_book.py    # Build publications from manifests
│   ├── generate_docs.py    # Convert YAML to markdown
│   └── validate_yaml_sync.py # Check sync between formats
├── publications/
│   ├── manifests/          # YAML files defining book structure
│   ├── templates/          # Reusable content (title pages, etc.)
│   └── assembled/          # OUTPUT: Generated books (gitignored)
├── core_rules/             # Core rulebook content
└── content_modules/        # Modular content (classes, species, etc.)
```

## Common Tasks

### Adding New Content

**New game element (spell, ability, item, etc.)**:
1. Add to appropriate `yaml/*.yaml` file
2. Add narrative description to corresponding markdown
3. Reassemble relevant publication

**New adversary/NPC**:
1. Start with narrative concept (who they are, what they want)
2. Use stat guidance from your system as starting point
3. Adjust based on story needs - stats serve the narrative
4. Give them a name and motivation, not just a stat block

**Balance change**:
1. Edit YAML file first
2. Update design notes in `index.yaml` if philosophy changed
3. Sync to markdown documentation
4. Update examples if mechanics changed

## Publication Workflow

When updating game content:

1. **Edit YAML files** in yaml/ directory (source of truth for mechanics)
2. **Run generate_docs.py** to sync changes to markdown (if using generation)
3. **Update markdown manually** for narrative content
4. **Run validation** to check sync
5. **Assemble books** using manifests when ready to review full documents
