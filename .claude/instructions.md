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
- **Monsters & NPCs**: ✓ Fully modularized (all threat levels + NPCs complete)
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

6. **✓ Complete Monster & NPC System**

   - ✓ Create monsters directory structure
   - ✓ Develop threat level system (1-4: Minions, Standard, Elite, Legendary)
   - ✓ Create monster root files (introduction, GM guidelines, system integration, quick reference)
   - ✓ Create threat level 1 monsters - 6 minion stat blocks
   - ✓ Create threat level 2 monsters - 4 standard enemy stat blocks
   - ✓ Create threat level 3 monsters - 6 elite enemy stat blocks
   - ✓ Create threat level 4 monsters - 5 legendary adversary stat blocks
   - ✓ Create NPC templates and guidelines
   - ✓ Integrate with Flow economy and PC systems

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

- ✓ Completed Monster & NPC system (all threat levels, 21 stat blocks, NPC templates)
- ✓ Added Writing Guidelines to prevent video game terminology
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

## Writing Guidelines

These guidelines ensure Flow RPG maintains appropriate tabletop RPG language and avoids video game terminology:

1. **Avoid Video Game Language**

   Flow RPG is a tabletop RPG, not a video game. Use appropriate TTRPG terminology:

   **Never Use:**
   - "Boss" (use: legendary adversary, major villain, archvillain)
   - "Elite" (use: champion, veteran, master)
   - "Tank" (use: defender, front-line fighter, guardian)
   - "DPS" (use: damage dealer, striker, attacker)
   - "Aggro" (use: draw attention, threaten, engage)
   - "AOE" (use: area effect, zone, burst)
   - "Proc" (use: trigger, activate, occurs)
   - "Cooldown" (use: recharge, rest required, once per scene)
   - "Buff/Debuff" (use: enhance, weaken, advantage, penalty)
   - "Mob" (use: creature, monster, enemy)
   - "Adds" (use: reinforcements, additional enemies)
   - "Trash" (use: minions, lesser enemies)
   - "Loot" (use: treasure, rewards, spoils)
   - "Respawn" (use: return, reform, regenerate)

   **Use Instead:**
   - Traditional TTRPG language
   - Natural English descriptions
   - Terms that fit fantasy fiction
   - Language that evokes tabletop play

2. **Natural Language Over Jargon**

   Prefer clear, descriptive language over gaming jargon when possible:
   - "The dragon attacks twice with its claws" not "The dragon has 2 claw attacks per turn"
   - "Recovers when you rest" not "Recharges on short rest"
   - "Once per encounter" not "1/encounter cooldown"

3. **Fiction-First Descriptions**

   Start with what it looks like in the fiction, then explain mechanics:
   - Good: "The paladin's holy aura protects nearby allies, granting them +2 to Guard while within Close range."
   - Bad: "AOE buff: +2 Guard to all friendlies within 10ft radius."

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
├── monsters/             # Monsters and NPCs
│   ├── 00_introduction.md
│   ├── 01_gm_guidelines.md
│   ├── 02_system_integration.md
│   ├── 03_quick_reference.md
│   └── monster_types/    # Creatures by threat level
│       ├── threat_1_minions.md
│       ├── threat_2_standard.md
│       ├── threat_3_elite.md
│       ├── threat_4_legendary.md
│       └── npcs.md
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

**Current Publications (All Ready):**
- **Core Rulebook** (775 KB) - Complete game
- **Player's Guide** (683 KB) - Player-facing content only
- **Game Master's Guide** (279 KB) - GM-facing content only
- **The Grimoire** (169 KB) - Magic system deep-dive
- **Quick Reference** (84 KB) - Printable at-table reference

**Generate All Publications:**
```bash
python scripts/assemble_book.py publications/manifests/core_rulebook.yaml
python scripts/assemble_book.py publications/manifests/players_guide.yaml
python scripts/assemble_book.py publications/manifests/gm_guide.yaml
python scripts/assemble_book.py publications/manifests/grimoire.yaml
python scripts/assemble_book.py publications/manifests/quick_reference.yaml
```

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

## Git Usage Guidelines for Claude

These guidelines help Claude actively support proper Git practices during work sessions.

### When Claude Should Prompt for Commits

I should remind you to review and commit changes when:

**1. After Completing a Discrete Task**
- Finished adding a new archetype/spell/calling
- Completed a section of documentation
- Fixed a specific bug or balance issue
- Finished a set of related edits

**2. Before Starting Major Changes**
- About to refactor a large system
- Planning to reorganize files
- Starting experimental changes
- Before trying alternative approaches

**3. After Significant Milestones**
- Completed a full system (e.g., all spells modularized)
- Finished a publication manifest
- Completed a session's work
- Before switching focus to different system

**4. Safety Checkpoints**
- Before making potentially destructive edits
- After creating many new files (rough guideline: 5-10+ files)
- When work session is ending
- Before long breaks in work

**When NOT to Prompt:**
- In the middle of a multi-step task
- During active brainstorming/planning
- When user explicitly says "don't commit yet"
- For trivial typo fixes (batch these together)

### Helping Write Commit Messages

When prompting for a commit, I should:

**1. Summarize What Changed**
- List files modified/created
- Describe the changes briefly
- Group related changes

**2. Propose Commit Message**
- Suggest specific, descriptive message
- Follow conventional commits format when appropriate
- Include "why" not just "what"
- Use imperative mood ("Add" not "Added")

**3. Example Format:**
```
I've completed [X]. Ready to commit?

Suggested commit message:
"Add Monk archetype with ki point system

- Created monk.md with complete archetype documentation
- Added ki points as alternative resource to Flow
- Integrated with existing combat stance system
- Updated archetype quick reference"

Files changed:
- archetypes/archetype_types/monk.md (new)
- archetypes/03_quick_reference.md (modified)
```

### Pre-Commit Verification

Before suggesting a commit, I should verify:

- [ ] No broken cross-references introduced
- [ ] Consistent formatting maintained
- [ ] No placeholder text left ([TODO], [Your Name], etc.)
- [ ] Files are in correct locations
- [ ] Related files are updated together (e.g., content + quick reference)
- [ ] No assembled publications being committed (should be gitignored)

If issues found, fix them before suggesting commit.

### Git Workflow Rules for Claude

**1. Always Suggest Review Commands First**
```bash
# Before commit, suggest these
git status
git diff
```

**2. Never Suggest These Commands** (unless user explicitly requests):
- `git push --force` (destructive)
- `git reset --hard` (destructive)
- `git clean -fd` (destructive)
- `git commit --amend` (unless last commit not pushed)
- `git rebase` on main branch (risky)

**3. Always Suggest Proper Sequence**:
```bash
# Review
git status
git diff

# Commit
git add .
git commit -m "Descriptive message"

# Push
git push
```

**4. Warn About These Situations**:
- Committing without reviewing changes first
- Very large commits (>20 files) - suggest breaking up
- Committing assembled publications (should be gitignored)
- Committing with vague messages
- Mixing unrelated changes in single commit

### Commit Message Standards

**Encourage This Format:**

```bash
# Good - Specific and clear
git commit -m "Add Monk archetype with ki point system"

# Better - Includes context
git commit -m "Add Monk archetype with ki point system

- Created complete Monk archetype documentation
- Ki points as alternative resource to Flow
- Unarmed combat specialization
- Integrated with existing stance system"
```

**Prevent These:**

```bash
# Too vague
git commit -m "updates"
git commit -m "fixed stuff"
git commit -m "more changes"

# Too generic
git commit -m "Updated files"
git commit -m "Changes"
```

**If user provides vague message, suggest improvement:**
```
That message is a bit vague. How about:
"Fix Fireball damage calculation in advanced_spells.md"

This makes it clear what changed and why when reviewing history.
```

### Session Management

**At Session Start:**
```bash
# Check for uncommitted changes
git status
```
- If uncommitted changes exist, ask if user wants to commit them first
- If on wrong branch, notify user

**During Session:**
- Commit after each completed task (not mid-task)
- Batch small related changes together
- Don't interrupt flow with too-frequent commit prompts
- Group related file changes into single commit

**At Session End:**
```
We've completed [list of tasks]. Before ending:

1. Review changes: git status && git diff
2. Commit work: git add . && git commit -m "[suggested message]"
3. Push to GitHub: git push

This ensures your work is backed up and tracked.
```

Always remind to commit any uncommitted work at session end.

### When to Suggest Branching

I should recommend creating a branch for:

**1. Experimental Changes**
- Testing major balance changes
- Trying alternative system designs
- Prototyping new mechanics

**2. Large Refactors**
- Restructuring multiple files
- Renaming systems
- Major reorganization

**3. Optional Content**
- New archetypes being playtested
- Alternative spell lists
- Variant rules

**Suggested Workflow:**
```bash
# Create feature branch
git checkout -b feature/monk-archetype

# Work and commit as normal
git add .
git commit -m "Add Monk archetype (experimental)"

# Push branch
git push -u origin feature/monk-archetype

# When ready to merge:
git checkout main
git merge feature/monk-archetype
git branch -d feature/monk-archetype
```

**Keep on Main Branch:**
- Bug fixes
- Typo corrections
- Balance tweaks
- Documentation improvements
- Regular content additions

### Error Prevention

I should actively warn about:

**1. Large File Commits**
- If assembled books aren't gitignored
- Binary files being added accidentally
- Very large documents (>1MB)

**2. Sensitive Information**
- Email addresses in content (use placeholders)
- Personal information
- API keys or tokens (shouldn't be in this project, but watch for it)

**3. File Organization**
- Files in wrong directories
- Inconsistent naming conventions
- Missing related updates

**4. Commit Quality**
- Mixing multiple unrelated changes
- Incomplete features being committed
- Broken cross-references

### Example Interaction

**Good Flow:**
```
User: "Let's add a Monk archetype"
Claude: [Creates monk.md with complete documentation]

Claude: "I've completed the Monk archetype with ki point mechanics.
Before we continue, let's commit this work:

git status  # Review what changed

Suggested commit:
git add drafts/archetypes/archetype_types/monk.md
git commit -m 'Add Monk archetype with ki point system

- Created complete Monk archetype documentation
- Ki points as alternative resource to Flow
- Unarmed combat specialization
- Integrated with existing stance system'

Ready to commit, or would you like to review the changes first?"
```

**Preventing Problems:**
```
User: "Commit these changes"
Claude: "Before committing, I notice:
- The assembled Core Rulebook (775KB) is included in changes
- This should be gitignored (it's regenerated from sources)

Let me verify the .gitignore is working correctly first."
```

### Commit Frequency Guidelines

**Good Rhythm:**
- 1 commit per completed task/feature
- 3-5 commits per work session (rough guideline)
- Commit before ending session (always)

**Too Frequent:**
- Committing every file edit
- Committing incomplete work
- Micro-commits for trivial changes

**Too Infrequent:**
- Working for hours without commits
- Mixing many unrelated changes
- Risk losing work if something goes wrong

**Balance:** Commit when something discrete and meaningful is complete.

## Future Enhancements

- **Character Generator Tool**: Interactive tool for character creation
- **Scenario Builder**: Structured approach to adventure design using Flow
- **Monster Creation System**: Standardized approach to creating balanced threats
- **Additional Publication Manifests**: Player's Guide, GM Guide, Grimoire, etc.

## Session Notes

_11/12/25 Session (Continued 5)_:

- Completed full publication suite (5 publications total)
- Created Player's Guide manifest (683 KB - player-facing only)
- Created Game Master's Guide manifest (279 KB - GM-facing only)
- Created Spell Grimoire manifest (169 KB - magic deep-dive)
- Created Quick Reference manifest (84 KB - printable reference)
- Created publication-specific title pages
- Successfully assembled all 5 publications
- Updated publications/README.md with complete book list
- Updated Living Design Document
- Added Git Usage Guidelines for Claude to enforce proper Git practices

_11/12/25 Session (Continued 4)_:

- Prepared project for GitHub version control
- Created comprehensive README.md for repository front page
- Created LICENSE.md with multiple license options
- Created CONTRIBUTING.md with playtesting and feedback guidelines
- Created GIT_SETUP.md with complete Git/GitHub setup instructions
- Updated Living Design Document with Git workflow
- Project ready for initial Git commit and GitHub push

_11/12/25 Session (Continued 6)_:

- Cleaned up video game terminology throughout monster system
- Replaced all "Boss" references with "legendary adversary" (contextual)
- Replaced all "Elite" references with "Champion" (threat level 3)
- Renamed threat_3_elite.md → threat_3_champion.md
- Updated all manifest files with new terminology
- Added "Elite" to prohibited terms in Writing Guidelines
- Successfully tested all assemblies:
  - core_rulebook.md: 899 KB
  - gm_guide.md: 391 KB
  - monster_manual.md: 109 KB
- Monster system now uses proper TTRPG language throughout

_11/12/25 Session (Continued 5)_:

- Integrated monster content into publication system
- Updated core_rulebook.yaml to include all monster content (Part VII)
- Updated gm_guide.yaml with complete monster compendium (Part II)
- Created monster_manual.yaml manifest (standalone bestiary)
- Created monster_manual_title.md template
- Successfully assembled all publications with monster content:
  - core_rulebook.md: 899 KB (was 775 KB)
  - gm_guide.md: 391 KB (was 279 KB)
  - monster_manual.md: 109 KB (new)
- Updated publications/README.md with new Monster Manual publication
- All 6 publications now complete and tested

_11/12/25 Session (Continued 4)_:

- Completed Monster & NPC system modularization
- Created all monster root files (introduction, GM guidelines, system integration, quick reference)
- Created threat level 1 monsters: 6 minion stat blocks (goblin, bandit, zombie, rat, skeleton, cultist)
- Created threat level 2 monsters: 4 standard enemy stat blocks (orc, dire wolf, goblin shaman, animated armor)
- Created threat level 3 monsters: 6 elite enemy stat blocks (ogre, battle mage, young dragon, vampire spawn, stone golem, werewolf)
- Created threat level 4 monsters: 5 legendary adversary stat blocks (adult dragon, lich, beholder, demon lord, archmage)
- Created comprehensive NPC templates and guidelines
- Added Writing Guidelines section to prevent video game terminology (no "boss", "tank", "DPS", etc.)
- Fixed all references from "boss" to "legendary adversary" throughout monster system
- Updated Living Design Document with complete monster system
- Total: 21 complete stat blocks plus NPC system

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
