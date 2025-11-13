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

- **Guard Scaling**: ~~At higher milestones, Guard may scale too quickly~~ PARTIALLY ADDRESSED
  - Changed base formula from 5 + Might to 7 + Might
  - Narrows starting range from 7 points (3-10) to 5 points (5-10)
  - Still scales with milestones - may need testing at higher levels

- **Will Casting as Emergency Button**: Ability to cast at negative Flow may undermine Flow management
  - _Potential Solution_: Add consequences or limitations to Will casting at negative Flow
  - _Status_: Needs playtesting with new Flow generation rules

- **Species Trait Consistency**: Halfling traits differ between character_creation.md and species/halfling.md
  - Character creation has: Lucky, Brave Heart, Small but Mighty
  - Species file has: Communal Support, Inconspicuous, Homefield Advantage, Lucky
  - Attribute bonuses also differ (+1 Will/Presence choice vs +2 Presence, +1 Grace, -2 Might)
  - _Action Needed_: Standardize halfling traits across files

- **Calling Ability Power Levels**: Some calling abilities may be stronger than others
  - Champion's +1 Flow per round in Aggressive (when protecting) is very strong
  - Sentinel's +1 Guard per Flow gain could stack rapidly
  - Scholar's banking 2 Flow between scenes is unique but situational
  - _Status_: Needs comparative playtesting

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

4. **Forbidden Video Game Patterns**

   Flow RPG is a traditional tabletop RPG, not an MMO or video game. Avoid these video game design patterns:

   **Never Use:**
   - "Escalation" mechanics (automatic difficulty increases over time)
   - "Wave spawning" (timed enemy reinforcements)
   - "Adds" (additional enemies appearing on timers)
   - "Holy Trinity" role design (Tank/Healer/DPS)
   - "Aggro tables" or threat mechanics
   - "Enrage timers" (forced time limits)
   - "Phase transitions" (scripted boss behavior changes)
   - "Wipes" (use: party defeat, overwhelming loss)
   - "Pull" (use: engage, attack, draw out)
   - "Kiting" (use: fighting retreat, hit-and-run tactics)

   **Design Rationale:**
   - MMO patterns assume computer-controlled enemies with scripted behaviors
   - Tabletop RPGs have intelligent GMs making dynamic decisions
   - Video game balance assumes perfect information and consistent execution
   - TTRPG balance accounts for improvisation and narrative circumstances

5. **Combat Design Principles**

   Combat stances and tactical options should emphasize **situational choices**, not role-based character archetypes:

   **Good - Tactical Guidance:**
   - "Use Aggressive stance when you need to end fights quickly or press a tactical advantage"
   - "Defensive stance generates Flow reliably through being targeted"
   - "This ability works best when facing overwhelming offense"

   **Bad - Role-Based Thinking:**
   - "Tanks should use Defensive stance"
   - "DPS characters want Aggressive stance"
   - "This is the healer's main ability"

   **Why This Matters:**
   - Stances are tactical responses to situations, not character identities
   - Any character might use any stance depending on circumstances
   - Role-based language restricts player creativity and agency
   - Situational language empowers dynamic tactical decisions

6. **Encounter Design Principles**

   Encounters should be **narrative-based and GM-driven**, not timed or scripted:

   **Good - Dynamic and Narrative:**
   - "GM may introduce complications using Flow pool"
   - "Reinforcements arrive when dramatically appropriate"
   - "Elite adapts tactics when strategy fails"
   - "Environmental hazards respond to fiction"

   **Bad - Timed and Scripted:**
   - "Wave 2 spawns after 3 rounds"
   - "Boss enters phase 2 at 50% HP"
   - "Adds appear every 4 rounds"
   - "Enrage timer at round 10"

   **Why This Matters:**
   - GMs can respond to player creativity and table dynamics
   - Encounters remain flexible to narrative circumstances
   - No "correct" solution or optimal strategy
   - Dramatic pacing emerges from play, not predetermined scripts

7. **YAML Documentation Standards**

   When working with YAML source files:

   - **Always validate** after making changes: `python scripts/generate_docs.py --all`
   - **Regenerate all templates** when YAML changes affect multiple files
   - **Check cross-references** between YAML and generated markdown
   - **Test assembly** of affected publications after major changes
   - **Maintain consistency** in terminology across all YAML files

8. **Language Audit Requirements**

   When reviewing or modifying content:

   - **Search comprehensively** for video game terminology across all files
   - **Check YAML first** - it's the source of truth for generated content
   - **Verify generated docs** after cleaning up YAML
   - **Update both mechanics and descriptions** - don't just reword, redesign if needed
   - **Document changes** in session notes with files modified

   Common audit triggers:
   - Adding new enemy types or encounter mechanics
   - Creating combat abilities or tactical options
   - Writing GM guidance for running encounters
   - Describing character roles or party composition

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
