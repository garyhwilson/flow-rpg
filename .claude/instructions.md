# Flow RPG - Living Design Document

_Last Updated: November 12, 2025_

This document tracks ongoing design decisions, outstanding issues, and development priorities for the Flow RPG system. It serves as a continuity reference between development sessions and should be regularly updated and pruned as items are addressed.

## Current Project Status

- **Core Rules**: Split into modular files for improved development
- **Callings**: ✓ Fully modularized into structured directory
- **Archetypes**: ✓ Fully modularized (all 7 archetypes complete)
- **Species**: ✓ Fully modularized (all 4 species complete)
- **Equipment**: ✓ Fully modularized (all equipment types complete)
- **Spells**: ✓ Fully modularized (all 4 spell tiers complete)
- **Publication System**: ✓ Infrastructure complete for assembling books

## Active Development Priorities

1. **✓ Complete Archetype Modularization**

   - ✓ Create all archetype files following established template
   - ✓ Ensure consistent structure across all archetype documentation

2. **✓ Complete Species Modularization**

   - ✓ Apply same modular structure to species documentation
   - ✓ Maintain consistent cross-referencing with archetypes and callings
   - ✓ Create root files (introduction, GM guidelines, etc.)
   - ✓ Develop individual species files (human, elf, dwarf, halfling)

3. **✓ Complete Equipment Modularization**

   - ✓ Develop structured documentation for equipment systems
   - ✓ Create modular equipment structure (weapons, armor, adventuring gear, magical items)
   - ✓ Add quick reference guide

4. **✓ Complete Spell System Modularization**

   - ✓ Create modular structure for spell documentation
   - ✓ Organize spells by tier (cantrips, standard, advanced, master)
   - ✓ Develop spell root files (introduction, GM guidelines, system integration)
   - ✓ Create individual spell tier files
   - ✓ Add spell quick reference guide

5. **✓ Establish Publication System**

   - ✓ Create publication directory structure
   - ✓ Develop Python assembly script (assemble_book.py)
   - ✓ Create YAML manifest system for book definitions
   - ✓ Build Core Rulebook manifest
   - ✓ Create template files (title page, copyright)
   - ✓ Set up .gitignore for assembled output
   - ✓ Document publication workflow

## Outstanding Design Issues

### Balance Concerns

- **Guard Scaling**: At higher milestones, Guard may scale too quickly, making characters difficult to threaten

  - _Potential Solution_: Cap Guard scaling or introduce scaled threats

- **Halfling Weapon Damage**: The penalty may make Halflings non-viable in combat-focused roles

  - _Potential Solution_: Provide compensatory advantages or adjust penalty

- **Scholar Calling Dice Benefit**: The retroactive dice benefit may be too powerful

  - _Potential Solution_: Limit frequency or scope of benefit

- **Will Casting as Emergency Button**: Ability to cast at negative Flow may undermine Flow management
  - _Potential Solution_: Add consequences or limitations to Will casting at negative Flow

### System Integration Questions

- **Magic Access Requirement**: How does the Mind + Awareness ≥ +2 requirement affect archetypes like Clerics?

  - _Investigation Needed_: Review character creation examples to ensure viable paths

- **Stance/Calling Interaction**: Some Calling benefits may work too well with certain stances
  - _Investigation Needed_: Test combinations for balance issues

### Documentation Needs

- **Quick Start Rules**: Need condensed version for new players

  - _Status_: Not started

- **GM Screen Information**: Identify key references for quick lookup
  - _Status_: Not started

## Recently Addressed Items

- ✓ Established complete publication system for book assembly
- ✓ Completed spell system modularization (all 4 spell tiers)
- ✓ Completed equipment modularization (all equipment types)
- ✓ Completed all 4 species files with consistent structure
- ✓ Completed all 7 archetype files with consistent structure
- ✓ Calling Compendium split into modular structure
- ✓ Archetype modularization framework established
- ✓ Core Rules split into focused modules

## Design Principles Reference

These core principles should guide all design decisions:

1. **Elegance over Complexity**

   - Simple, unified resolution system
   - Minimal bookkeeping and calculation
   - Deep decision space without excessive rules

2. **Narrative-First with Tactical Depth**

   - Story drives mechanics, not vice versa
   - Tactical options for those who want them
   - Every rule supports the fiction

3. **Flow as Universal Resource**

   - Single resource unifying all subsystems
   - Dynamic economy creating dramatic pacing
   - Intuitive resource that mirrors character momentum

4. **Player Agency**
   - Meaningful choices in character building
   - Tactical decisions in combat
   - Narrative permissions granting special capabilities

## Project Organization

```
flow-rpg/
├── core_rules/           # Core system files
│   ├── 01_introduction.md
│   ├── 02_basic_mechanics.md
│   └── ...
├── callings/             # Character motivation system
│   ├── 00_introduction.md
│   ├── calling_types/    # Individual callings
│   └── growth_patterns/  # Evolution and combinations
├── archetypes/           # Character profession system
│   ├── 00_introduction.md
│   ├── 01_gm_guidelines.md
│   ├── 02_system_integration.md
│   ├── 03_quick_reference.md
│   └── archetype_types/  # Individual archetypes
│       ├── fighter.md
│       ├── wizard.md
│       ├── cleric.md
│       ├── rogue.md
│       ├── ranger.md
│       ├── bard.md
│       └── paladin.md
├── species/              # Character heritage system
│   ├── 00_introduction.md
│   ├── 01_gm_guidelines.md
│   ├── 02_system_integration.md
│   ├── 03_quick_reference.md
│   └── species_types/    # Individual species
│       ├── human.md
│       ├── elf.md
│       ├── dwarf.md
│       └── halfling.md
├── equipment/            # Items and gear
│   ├── 00_introduction.md
│   ├── 01_gm_guidelines.md
│   ├── 02_system_integration.md
│   ├── 03_quick_reference.md
│   └── equipment_types/  # Individual equipment categories
│       ├── weapons.md
│       ├── armor.md
│       ├── adventuring_gear.md
│       └── magical_items.md
├── spells/               # Magic system
│   ├── 00_introduction.md
│   ├── 01_gm_guidelines.md
│   ├── 02_system_integration.md
│   ├── 03_quick_reference.md
│   └── spell_tiers/      # Individual spell tiers
│       ├── cantrips.md
│       ├── standard_spells.md
│       ├── advanced_spells.md
│       └── master_spells.md
├── publications/         # Publication assembly system
│   ├── manifests/        # YAML book definitions
│   │   └── core_rulebook.yaml
│   ├── templates/        # Reusable content
│   │   ├── title_page.md
│   │   └── copyright.md
│   ├── custom_content/   # Book-specific additions
│   ├── assembled/        # OUTPUT: Generated books (gitignored)
│   └── README.md         # Publication system documentation
└── scripts/
    └── assemble_book.py  # Book assembly script
```

## Publication System Workflow

The project now includes a complete publication assembly system:

**To Assemble a Book:**
```bash
# From project root
python scripts/assemble_book.py publications/manifests/core_rulebook.yaml
```

**System Features:**
- YAML manifests define book structure
- Python script automatically assembles from modular sources
- Output to `publications/assembled/` (gitignored)
- Template system for front matter
- On-demand generation only

**See:** `publications/README.md` for detailed documentation

**Current Books:**
- Core Rulebook (complete manifest ready)

**Planned Books:**
- Player's Guide
- Game Master's Guide
- Grimoire: Advanced Magic
- Additional supplements

## Git & GitHub Workflow

The project is ready for version control with Git and GitHub:

**Setup Instructions:**
- Complete setup guide: `GIT_SETUP.md`
- Repository files created: `README.md`, `LICENSE.md`, `CONTRIBUTING.md`
- `.gitignore` configured to exclude assembled publications

**Daily Workflow:**
```bash
# Review changes
git status
git diff

# Commit changes
git add .
git commit -m "Descriptive message"

# Push to GitHub
git push
```

**Commit Message Guidelines:**
- Use clear, specific descriptions
- Explain why, not just what
- Group related changes together
- Reference issues when applicable

**Example Commit Messages:**
```bash
# Good
git commit -m "Add Monk archetype with ki point system"
git commit -m "Fix Fireball damage calculation in spell tier files"
git commit -m "Rebalance Guard scaling at high levels"

# Poor (too vague)
git commit -m "Updates"
git commit -m "Fixed stuff"
```

**Repository Structure:**
- `main` branch: Stable, tested content
- Feature branches: Experimental changes (optional)
- Releases: Major milestones (v0.1, v1.0, etc.)

**GitHub Features:**
- **Issues:** Track bugs, balance concerns, design questions
- **Projects:** Organize development priorities
- **Discussions:** Community Q&A and feedback
- **Releases:** Mark playtest versions and milestones

**See:** `GIT_SETUP.md` for complete setup instructions

## Future Enhancements

- **Character Generator Tool**: Interactive tool for character creation
- **Scenario Builder**: Structured approach to adventure design using Flow
- **Monster Creation System**: Standardized approach to creating balanced threats
- **Additional Publication Manifests**: Player's Guide, GM Guide, Grimoire, etc.

## Session Notes

_11/12/25 Session (Continued 4)_:

- Prepared project for GitHub version control
- Created comprehensive README.md for repository front page
- Created LICENSE.md with multiple license options
- Created CONTRIBUTING.md with playtesting and feedback guidelines
- Created GIT_SETUP.md with complete Git/GitHub setup instructions
- Updated Living Design Document with Git workflow
- Project ready for initial Git commit and GitHub push

_11/12/25 Session (Continued 3)_:

- Established complete publication assembly system
- Created Python script (assemble_book.py) for automatic book generation
- Implemented YAML manifest system for book definitions
- Created Core Rulebook manifest (complete structure)
- Set up publication directory structure and templates
- Created .gitignore for assembled output
- Documented publication workflow in publications/README.md
- Updated Living Design Document

_11/12/25 Session (Continued 2)_:

- Completed spell system modularization (all 4 spell tiers)
- Created all spell root files (introduction, GM guidelines, system integration)
- Created individual spell tier files (cantrips, standard, advanced, master)
- Created spell quick reference guide
- Updated Living Design Document
- All major systems now fully modularized!

_11/12/25 Session (Continued)_:

- Completed equipment modularization (all 4 equipment types)
- Created equipment quick reference guide
- Updated Living Design Document

_11/12/25 Session_:

- Completed all species modularization (all 4 species)
- Started equipment modularization
- Updated Living Design Document

_11/11/25 Session_:

- Completed Calling modularization
- Started Archetype modularization with Fighter and Wizard examples
- Created initial Living Design Document

---

_Note: This document should be updated at the beginning and end of each development session to maintain continuity._
