# Flow RPG - Living Design Document

_Last Updated: November 14, 2025_

This document tracks ongoing design decisions, outstanding issues, and development priorities for the Flow RPG system. It serves as a continuity reference between development sessions and should be regularly updated and pruned as items are addressed.

**Technical Reference**: For system architecture, mathematical constraints, and recently fixed issues, see [CLAUDE.md](../CLAUDE.md).

## Current Project Status

- **Core Rules**: ✓ Split into modular files for improved development
- **Callings**: ✓ Fully modularized into structured directory
- **Archetypes**: ✓ Fully modularized (all 7 archetypes complete)
- **Species**: ✓ Fully modularized (all 4 species complete)
- **Equipment**: ✓ Fully modularized (all equipment types complete)
- **Spells**: ✓ Fully modularized (all 4 spell tiers complete)
- **Monsters & NPCs**: ✓ Fully modularized (all threat levels + NPCs complete)
- **Publication System**: ✓ Infrastructure complete for assembling books
- **YAML Conversion**: ✓ Complete (all game systems in structured YAML)
- **Playtesting Phase 1-3**: ✓ Complete (critical fixes, balance tuning, accessibility improvements)

## Active Development Priorities

**All initial development priorities completed!** The system is now in structured YAML format with all core systems implemented and playtested fixes applied (Phase 1-3).

### Completed Initiatives

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
   - ✓ Develop threat level system (1-4: Henchmen, Standard, Champions, Legendary)
   - ✓ Create monster root files (introduction, GM guidelines, system integration, quick reference)
   - ✓ Create threat level 1 monsters - 6 henchman stat blocks
   - ✓ Create threat level 2 monsters - 4 standard enemy stat blocks
   - ✓ Create threat level 3 monsters - 6 champion enemy stat blocks
   - ✓ Create threat level 4 monsters - 5 legendary adversary stat blocks
   - ✓ Create NPC templates and guidelines
   - ✓ Integrate with Flow economy and PC systems

7. **✓ YAML System Conversion**
   - ✓ Convert all Markdown to structured YAML
   - ✓ Establish YAML schema for all game components
   - ✓ Create Python documentation generator
   - ✓ Maintain dual YAML/Markdown workflow

8. **✓ Playtesting Fixes - Phase 1 (Critical Fixes)**
   - ✓ Champion action economy (2 attacks max to prevent TPK)
   - ✓ Deepen Expertise timing (requires 3 consecutive minor milestones)
   - ✓ Documentation corrections (Guard formula, skill tier modifiers)

9. **✓ Playtesting Fixes - Phase 2 (Balance Tuning)**
   - ✓ Flow generation limit (once per round)
   - ✓ High Flow bonus removal (flat +6 maximum)
   - ✓ TN scaling guidance (TN 10-12 for late game challenges)
   - ✓ GM Flow examples and guidance

10. **✓ Playtesting Fixes - Phase 3 (Accessibility & Polish)**
    - ✓ Simplified rules for new players (examples.yaml)
    - ✓ Default build paths to reduce option paralysis (advancement.yaml)
    - ✓ Optional GM Flow pool guidance (gm_tools.yaml)

## Outstanding Design Issues

### Balance Concerns

- **Will Casting as Emergency Button**: Ability to cast at negative Flow may undermine Flow management
  - _Potential Solution_: Add consequences or limitations to Will casting at negative Flow
  - _Status_: Needs playtesting with new Flow generation rules (once per round limit now in place)

- **Calling Ability Power Levels**: Some calling abilities may be stronger than others
  - Champion's +1 Flow per round in Aggressive (when protecting) is very strong
  - Sentinel's +1 Guard per Flow gain could stack rapidly
  - Scholar's banking 2 Flow between scenes is unique but situational
  - _Status_: Needs comparative playtesting
  - _Note_: Less urgent now with bounded accuracy +5 cap and Flow generation limit

### Missing Subsystems

Critical gameplay systems not yet documented:

- **Multiclassing Rules**: No system for characters training in multiple archetypes
  - _Status_: Not started
  - _Priority_: High (common player request)

- **Crafting System**: Craft skill exists but no crafting rules
  - _Status_: Not started
  - _Priority_: Medium

- **Social Conflict Resolution**: Social skills exist but no social conflict mechanics
  - _Status_: Not started
  - _Priority_: Medium (three social skills need framework)

- **Exploration Procedures**: Survival/Investigate skills need exploration framework
  - _Status_: Not started
  - _Priority_: Low (can use general scene resolution)

- **Rest and Recovery Mechanics**: How do characters recover Flow, Guard, and Vitality?
  - _Status_: Partially documented, needs expansion
  - _Priority_: High (fundamental to gameplay)

- **Wealth and Economy**: No pricing beyond weapons/armor, no wealth tracking system
  - _Status_: Not started
  - _Priority_: Medium (GMs need guidelines)

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

### Playtesting Phase 1-3 Fixes (11/14/25)

**Phase 1 - Critical Fixes:**
- ✓ **Champion Action Economy** (advancement.yaml:752-763): Limited to 2 attacks per round to prevent TPK
- ✓ **Deepen Expertise Timing** (advancement.yaml:609-616): Now requires 3 consecutive minor milestones (was ambiguous)
- ✓ **Guard Formula Correction** (core_rules.yaml:412-420): Documented as `12 + max(Might, Grace, Will)` (not `8 + attribute + milestones`)
- ✓ **Skill Tier Modifiers** (core_rules.yaml:372-381): Clarified Professional = +1 (not +2), Expert = +2

**Phase 2 - Balance Tuning:**
- ✓ **Flow Generation Limit** (core_rules.yaml:458-465): Maximum once per round to prevent runaway economy
- ✓ **High Flow Bonus Removal** (core_rules.yaml:455-456): Removed +2 bonus at 6+ Flow, now flat +6 maximum
- ✓ **TN Scaling Guidance** (gm_tools.yaml:64-110): Added guidance for TN 10-12 challenges at late game (+5 cap sweet spot)
- ✓ **GM Flow Examples** (gm_tools.yaml:34-63): Added complete worked examples for spending GM Flow pool

**Phase 3 - Accessibility & Polish:**
- ✓ **Simplified Rules** (examples.yaml:24-93): Created quick-start variant for first 1-2 sessions
- ✓ **Default Build Paths** (advancement.yaml:862-982): Added 6 pre-planned advancement paths to reduce option paralysis
- ✓ **Optional GM Flow** (gm_tools.yaml:162-200): Made GM Flow pool explicitly optional with guidance for when to skip it

### Earlier Addressed Items (Pre-YAML)

- ✓ **Guard Calculation Rebalanced** (11/12/25): Changed from 5 + Might to 7 + Might, narrowing viability gap
- ✓ **Halfling Small but Mighty Fixed** (11/12/25): Removed punitive -1 damage penalty, added stealth benefit
- ✓ **Spell Flow Generation Added** (11/12/25): Offensive spells now generate +1 Flow in Aggressive stance
- ✓ **Armor Penalties Reduced** (11/12/25): Medium armor -1 Sorcery (was -2), Heavy armor -4 (was prohibition)
- ✓ **Calling Inconsistencies Resolved** (11/12/25): Standardized Champion, Scholar, Sentinel abilities
- ✓ **Skill Decision Tree Added** (11/12/25): Clarified when to use Combat/Athletics/Finesse
- ✓ **Shield Spell Mind Version Fixed** (11/12/25): Now protects two adjacent targets efficiently
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

5. **Bounded Accuracy (+5 Cap)**
   - Total modifier cap of +5 (attribute +3, skill +2, edges +1)
   - Maintains meaningful dice rolls throughout progression
   - Sweet spot: At +5 vs TN 8 = 97.2% (too easy), vs TN 10 = 72.2% (meaningful), vs TN 12 = 41.7% (hard)
   - Late game challenges should use TN 10-12, not higher modifiers
   - Guard doesn't automatically scale with milestones (12 + max attribute)
   - See CLAUDE.md for detailed mathematical constraints

## CRITICAL: This Is A Tabletop RPG, Not A Video Game

**This section must be reviewed before ANY content creation or modification.**

Flow RPG is a traditional tabletop roleplaying game. Every design decision, piece of content, and word choice must reflect TTRPG principles, not video game (especially MMO) patterns. This is not negotiable.

### The Video Game Trap

Video game design patterns are fundamentally incompatible with TTRPG play and must be actively rejected:

**Forbidden Video Game Patterns:**
- **Formulaic stat scaling** - e.g., "Guard = 8 + milestones × 2"
- **Enemy types/tiers as units** - Treating adversaries as interchangeable stat blocks
- **Squad composition formulas** - e.g., "1 Champion + 4 Henchmen = Medium difficulty"
- **Role trinity thinking** - Tank/Healer/DPS archetypes
- **Balance calculations** - Mathematical encounter budgets and CR systems
- **Scripted encounters** - Phase transitions, timed waves, enrage timers
- **Stat blocks without character** - Enemies as numbers, not people

**Why These Patterns Are Poison:**
- MMO patterns assume computer-controlled enemies with scripted AI
- TTRPGs have intelligent GMs making dynamic narrative decisions
- Video games require mathematical balance for fair matchmaking
- TTRPGs balance through GM judgment and story appropriateness
- Video game terminology breaks immersion for tabletop players
- MMO thinking restricts GM creativity and player agency

### Required TTRPG Approach

**Every adversary is a character with a name and motivation:**
- Don't create "a Champion" - create "Captain Vex, who wants revenge for his fallen squad"
- Stats serve the story, never the other way around
- GMs create specific individuals, not fill encounter slots
- Personality and motivation come BEFORE mechanics

**Narrative-driven opposition:**
- Scene difficulty emerges from circumstances, not stat calculations
- Consequences and stakes matter more than hit points
- Social and environmental challenges are as important as combat
- Story determines what's appropriate, not balance formulas

**GM judgment over rigid rules:**
- Provide guidance ranges and examples, not formulas
- Trust GMs to create what feels right for their story
- Emphasize adaptation to table needs
- Flexibility is a feature, not a bug

### Forbidden Terminology (Comprehensive List)

**NEVER use these video game terms:**

Combat & Enemies:
- "Boss" → Use: legendary adversary, major villain, archvillain
- "Elite" → Use: champion, veteran, master
- "Minion" → Use: henchman, lesser enemy, follower
- "Mob" → Use: creature, enemy, adversary
- "Adds" → Use: reinforcements, additional enemies
- "Trash" → Use: minor threats, fodder (sparingly)
- "Pull" → Use: engage, attack, draw out
- "Wipe" → Use: party defeat, overwhelming loss
- "Aggro" → Use: draw attention, threaten, engage

Roles & Classes:
- "Tank" → Use: defender, guardian, protector
- "DPS" → Use: damage dealer, striker, attacker
- "Healer" → Use: support, medic (if modern), cleric
- "Support" → Use: ally, helper (context-dependent)

Abilities & Effects:
- "AOE" → Use: area effect, zone, burst
- "Proc" → Use: trigger, activate, occurs
- "Cooldown" → Use: recharge, rest required, once per scene
- "Buff/Debuff" → Use: enhance, weaken, advantage, penalty
- "CC" (crowd control) → Use: restraint, hindrance, disable
- "DOT" (damage over time) → Use: ongoing damage, poison, burning

Rewards & Progression:
- "Loot" → Use: treasure, rewards, spoils
- "Drop" → Use: carried, possesses
- "XP/EXP" → Use: advancement, growth (we use milestones)
- "Grinding" → Use: practice, training
- "Farming" → Never applicable in TTRPG

Encounter Design:
- "Encounter" → Use: conflict, scene, confrontation
- "Wave" → Use: reinforcements, second group
- "Phase" → Use: the enemy changes tactics, adapts
- "Enrage" → Use: desperation, fury (as character emotion)
- "Respawn" → Use: return, reform, regenerate

### How to Audit Content

**Before creating or modifying any content, ask:**

1. **Does this sound like a tabletop game or World of Warcraft?**
   - If it sounds like an MMO wiki page, rewrite it
   - Would this appear in D&D, Fate, or Powered by the Apocalypse?

2. **Are we describing characters or stat blocks?**
   - Every significant enemy needs a name and motivation
   - Personality should be clear even in mechanical descriptions

3. **Is the GM empowered to make narrative choices?**
   - Are we providing guidance or rigid formulas?
   - Can the GM adapt to their specific story?
   - Is player creativity supported or constrained?

4. **Would veteran TTRPG players recognize this as tabletop content?**
   - Does it evoke fantasy fiction or video game mechanics?
   - Is the language natural or full of gaming jargon?

**Red Flags vs Green Flags:**

Red Flags (Video Game):
- Mathematical scaling formulas
- "Opposition types" and "squad composition"
- Role-based character design
- "Encounter balance guidelines"
- Timed or scripted events
- Treating enemies as interchangeable units

Green Flags (TTRPG):
- Named characters with clear motivations
- Situational guidance: "A squad typically has..."
- Story-first design: "What makes sense for this villain?"
- Emphasis on consequences over mechanics
- GM empowerment and flexibility
- Characters as people, not stat blocks

### Content Audit Triggers

**These situations require extra vigilance:**
- Adding new enemy types or adversary guidance
- Creating combat abilities or tactical options
- Writing GM guidance for running conflicts
- Describing character roles or party dynamics
- Designing challenges or obstacles
- Writing advancement or progression systems

**When in doubt:**
1. Check CLAUDE.md "Design Philosophy: TTRPG Not Video Game" section
2. Search the content for forbidden terms
3. Read it aloud - does it sound like fantasy fiction or a game wiki?
4. Ask: "Would Gary Gygax or Matt Colville write it this way?"

### Additional Writing Standards

**YAML Documentation Standards:**

When working with YAML source files:
- **Always validate** after making changes: `python scripts/generate_docs.py --all`
- **Regenerate all templates** when YAML changes affect multiple files
- **Check cross-references** between YAML and generated markdown
- **Test assembly** of affected publications after major changes
- **Maintain consistency** in terminology across all YAML files

**Language Audit Requirements:**

When reviewing or modifying content:
- **Search comprehensively** for video game terminology across all files
- **Check YAML first** - it's the source of truth for generated content
- **Verify generated docs** after cleaning up YAML
- **Update both mechanics and descriptions** - don't just reword, redesign if needed
- **Document changes** in session notes with files modified

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

## Session Workflow for Claude

These guidelines ensure continuity and proper documentation across development sessions.

### At Session Start

**1. Review Current State**
```bash
# Check for uncommitted changes
git status
```

**2. Review Instructions Document**
- Read any new entries in Outstanding Design Issues
- Check Active Development Priorities
- Review most recent Session Notes

**3. Create Todo List for Session**
- Use TodoWrite to track major tasks for this session
- Always include "Update .claude/instructions.md session notes" as final task
- Mark tasks in_progress as you work on them
- Complete tasks immediately after finishing

### During Session

**1. Task Management**
- Use TodoWrite for complex, multi-step work
- Keep exactly one task in_progress at a time
- Mark tasks completed immediately after finishing
- Don't batch completions

**2. Documentation**
- Note any new design issues discovered
- Track important decisions made
- Document balance concerns that arise
- Capture new guidelines or patterns

**3. Git Workflow**
- Provide git commands after completing discrete tasks
- Suggest commits before major changes
- Never execute git commands unless explicitly requested
- Follow commit message guidelines

### At Session End (MANDATORY)

**1. Update Session Notes**
- **ALWAYS add new session entry to this document**
- Include date and session identifier
- List all major work completed
- Document design decisions made
- Note any new issues discovered
- Update project status if milestones completed

**2. Verify Completeness**
- All todos marked as completed
- No placeholder text left in files
- Cross-references are valid
- Files in correct locations

**3. Provide Git Commands**
```bash
# Review all changes
git status
git diff

# Commit with descriptive message
git add .
git commit -m "Descriptive message"

# Push to remote
git push
```

**4. Session Notes Template**
```markdown
_MM/DD/YY Session (Identifier)_:

- [Major accomplishment 1]
- [Major accomplishment 2]
- [Design decision made]
- [New issue discovered]
- [Files modified/created]
```

### Common Failure Modes to Avoid

**Forgetting Session Notes:**
- If session ends without updating Session Notes, this is a FAILURE
- Session notes are MANDATORY, not optional
- Use TodoWrite to track this task throughout session

**Incomplete Git Workflow:**
- Always provide git commands at session end
- Review what changed before committing
- Use descriptive commit messages
- Never leave uncommitted work without explicit user approval

**Poor Task Tracking:**
- Forgetting to mark todos as completed
- Leaving todos in_progress when done
- Not using TodoWrite for complex work
- Batching multiple task completions

### Success Criteria

A successful session includes:
- ✓ New session notes added to instructions.md
- ✓ All todos marked completed
- ✓ Git commands provided for uncommitted changes
- ✓ Design issues documented
- ✓ Files properly organized
- ✓ Cross-references validated

## Session Notes

**Session history has been moved to [session_history.md](session_history.md) to keep this document focused and manageable.**

All development session notes are tracked chronologically in the session history document. Continue to add new session notes there at the end of each work session.

---

_Note: This document should be updated at the beginning and end of each development session to maintain continuity._
