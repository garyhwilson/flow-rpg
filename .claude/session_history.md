# Flow RPG - Session History

This document tracks all development session notes in chronological order. Each session records major accomplishments, design decisions, and files modified.

## Session Notes

_11/12/25 Session (Balance Fixes)_:

- **Implemented comprehensive balance fixes based on playtest feedback:**
- **Guard Calculation Rebalanced**: Changed formula from 5 + Might to 7 + Might
  - Narrows starting range from 7 points (3-10) to 5 points (5-10)
  - Makes low-Might characters (rogues, wizards) more viable
  - Updated: core_rules/03_character_creation.md, core_rules/04_combat_system.md
- **Halfling Species Fixed**: Removed punitive -1 melee damage penalty
  - New Small but Mighty: Movement + stealth bonus instead
  - Updated: core_rules/03_character_creation.md
- **Spell Flow Generation Added**: Offensive spells generate +1 Flow in Aggressive stance
  - Fixes spellcaster Flow economy issue
  - Updated: spells/00_introduction.md, spells/02_system_integration.md
- **Armor System Rebalanced**:
  - Medium armor: Reduced Sorcery penalty from -2 to -1
  - Heavy armor: Changed from "cannot cast" to -4 Sorcery penalty
  - Enables armored caster concepts (especially elves)
  - Updated: equipment/equipment_types/armor.md
- **Calling Inconsistencies Resolved**: Standardized Champion, Scholar, Sentinel
  - Champion: Protecting others in Aggressive generates +1 Flow/round
  - Scholar: Banks 2 Flow between scenes from knowledge actions
  - Sentinel: Gains +1 Guard when gaining Flow from any source
  - Updated: core_rules/03_character_creation.md
- **Skill System Clarified**: Added Physical Skill Decision Tree
  - Clear examples for when to use Combat/Athletics/Finesse/Stealth/Survival
  - Includes attribute pairing guidance
  - Updated: core_rules/02_basic_mechanics.md
- **Outstanding Design Issues Updated**:
  - Documented missing subsystems (multiclassing, crafting, social conflict, etc.)
  - Added new balance concerns discovered (species trait consistency, calling power levels)
  - Updated Recently Addressed Items with all fixes
  - Updated: .claude/instructions.md
- **Files Modified**: 7 core system files updated with balance improvements

_11/12/25 Session (Evening)_:

- Fixed Shield spell Mind version mechanical benefit
- Replaced vague "sometimes prevents damage entirely" with clear tactical advantage
- Mind version can now shield two adjacent targets (within Near of each other) for -1 Flow total
- Provides meaningful efficiency benefit through optimized energy distribution
- Updated standard_spells.md with new mechanics and GM notes
- Each Shield attribute version now has distinct, meaningful value proposition:
  - Mind: Efficiency (cover 2 targets for 1 Flow)
  - Awareness: Information (warning of attacks)
  - Will: Persistence (works when unconscious)
  - Presence: Control (demoralizes attackers)
- Confirmed spellcasting requirements: Mind + Awareness ≥ +2 still in place
- Added "Session Workflow for Claude" section to ensure consistent documentation practices
- Established mandatory session notes updates and success criteria

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

_11/12/25 Session (Mathematical Rebalancing)_:

- **Implemented comprehensive mathematical rebalancing across entire Flow RPG system**
- **Addressed 10 Core System Problems**:
  1. Flow economy too volatile (-6 to +10 range excessive)
  2. Skill progression unclear and unbalanced
  3. Guard formula created non-viable low-Might characters
  4. Vitality scaling insufficient at higher levels
  5. Death spiral too punishing
  6. Spell costs unbalanced across tiers
  7. Spellcasting access too restrictive
  8. Calling Flow benefits too rare/unreliable
  9. Armor system too restrictive (blocked armored casters)
  10. Damage scaling unclear

**Phase 1 - Core Rules (7 files modified)**:
- **Flow System Rebalanced**: Changed range from -6 to +10 down to -3 to +6
  - Tighter economy, more predictable resource management
  - Updated: basic_mechanics.md, character_creation.md, combat_system.md
- **7-Tier Skill System Implemented**: Untrained (-2), Novice (-1), Competent (+0), Professional (+2), Expert (+4), Master (+6), Legendary (+8)
  - Clear progression path with meaningful differences between tiers
  - Updated: basic_mechanics.md, character_creation.md
- **Guard Formula Changed**: From 5 + Might to 8 + Higher(Might, Grace) + (Milestones × 2)
  - Makes all character types viable in combat
  - Updated: character_creation.md, combat_system.md
- **Vitality Formula Enhanced**: 10 + Will + (Major Milestones × 3)
  - Better scaling at higher levels
  - Updated: character_creation.md
- **Death Saves Added**: 2d6 + Will at -1, -2, -3 Vitality to avoid death
  - Reduces death spiral, creates dramatic moments
  - Updated: combat_system.md
- **Damage Scaling Clarified**: +1 damage per 2 milestones, weapon die upgrades at 5/10/15
  - Clear progression for martial characters
  - Updated: advancement.md, combat_system.md

**Phase 2 - Magic System (6 files modified)**:
- **Spell Tier Costs Rebalanced**: Tier 0 (+1 Flow), Tier 1 (0 Flow), Tier 2 (-1 Flow), Tier 3 (-2 Flow), Tier 4 (-3 Flow)
  - Cantrips generate Flow, making spellcasters more sustainable
  - Tier 1 spells free, reducing barrier to entry
  - Higher tier costs scale reasonably
  - Updated: introduction.md, cantrips.md, standard_spells.md, advanced_spells.md, master_spells.md
- **Spellcasting Override Added**: If archetype grants Sorcery skill, can cast regardless of attributes
  - Wizard/Cleric no longer need Mind + Awareness ≥ +2
  - Arcane/divine traditions use different attributes
  - Updated: introduction.md, system_integration.md
- **Spell Damage Scaling**: +1 damage per 3 milestones for attack spells
  - Keeps casters competitive at higher levels
  - Updated: system_integration.md

**Phase 3 - Archetypes (6 files modified)**:
- **All Archetypes Updated with Novice Skills**: Every archetype now grants Novice (-1) proficiency in 6-7 skills
  - Ensures basic competence in archetype-relevant skills
  - Updated: fighter.md, ranger.md, paladin.md, rogue.md, wizard.md, cleric.md
- **Spellcasting Archetypes Override**: Wizard/Cleric explicitly state "can cast regardless of attributes"
  - Removes attribute gating for dedicated spellcasters
  - Updated: wizard.md, cleric.md
- **Rogue Dual Professional**: Rogues get Professional (+2) in two skills instead of one
  - Reflects specialized expertise
  - Updated: rogue.md
- **Fighter/Paladin/Ranger Edges**: Added Edge at 1/5/10 milestones
  - Gives martial classes tactical options
  - Updated: fighter.md, paladin.md, ranger.md

**Phase 4 - Calling Files (9 files modified)**:
- **All Calling Flow Benefits Redesigned for Reliability**:
  - **Advocate**: Truth revelation triggers (Investigation/Empathy checks) instead of "expose corruption once per scene"
  - **Guardian**: Ally takes damage (once per round) instead of "ally drops below half Vitality once per scene"
  - **Exemplar**: +1 bonus Flow on any critical success instead of complex goal system
  - **Seeker**: Novel approach +3 Flow (once per scene) instead of vague "act against expectations"
  - **Scholar**: Start scenes at +1 Flow instead of banking system
  - **Sentinel**: When you/ally attacked (once per round) instead of Guard conversion
  - **Enthusiast**: Adjacent ally gains +1 Flow when you do instead of voluntary transfer
  - **Champion**: Successful attacks while allies threatened instead of "protecting in Aggressive once per round"
  - **Mediator**: First conflict resolution per scene instead of "defuse without violence once per scene"
  - Updated: All 9 calling files in calling_types/

**Phase 5 - Armor System (1 file modified)**:
- **No Armor Benefits Added**: +1 Flow when taking damage, +1 Sorcery, extra movement zone
  - Makes unarmored a deliberate tactical choice, not just "can't afford armor"
- **Light Armor Rebalanced**: DR 1, no penalties, +1 initiative/movement
  - Versatile choice for many character types
- **Medium Armor Rebalanced**: DR 2, -1 Grace, -1 Sorcery (removed Flow restriction), +1 Guard per scene
  - Viable for armored casters (especially elves)
- **Heavy Armor Rebalanced**: DR 4, -2 Grace, -1 Flow generation, -3 Sorcery (removed casting prohibition and stance restriction), immune to forced movement
  - Can now cast in heavy armor (difficult but possible)
  - Can use all stances
  - Distinct tactical identity
  - Updated: armor.md

**Files Modified (43 total)**:
- Core Rules: 7 files (introduction, basic_mechanics, character_creation, combat_system, advancement, magic, running_the_game)
- Spells: 6 files (introduction, system_integration, cantrips, standard_spells, advanced_spells, master_spells)
- Archetypes: 6 files (fighter, ranger, paladin, rogue, wizard, cleric)
- Callings: 9 files (all 9 calling types)
- Equipment: 1 file (armor)
- GM Guidelines: 14 files (spell tiers GM notes)

**Design Impact**:
- Flow economy more predictable and manageable
- All character concepts viable (including armored casters)
- Spellcasters sustainable without constant resource starvation
- Martial characters have clear progression
- Calling Flow benefits trigger frequently enough to be meaningful
- Armor provides distinct tactical choices, not just numerical progression
- Death spiral reduced, creating more dramatic combat
- Skill progression clear and balanced

**Outstanding Issues Partially Addressed**:
- Guard Scaling: Formula improved, still needs high-level playtesting
- Calling Power Levels: All rebalanced to trigger frequently
- Spellcasting Access: Attribute gating removed for spellcasting archetypes
- Armor Casting Restrictions: Heavy armor can now cast (-3 penalty)

---

_Note: This document contains the complete development history. Add new session notes at the bottom in chronological order._
