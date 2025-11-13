# SPELLS - INTRODUCTION

## Overview

Magic in Flow RPG represents one of the most revolutionary aspects of the system: a unified casting framework where spells adapt to the caster's approach rather than being locked to a single tradition. This modular documentation covers the complete spell system, from basic cantrips to legendary master spells.

## Core Magic Philosophy

### The Flow of Magic

Magic is fundamentally tied to the Flow that permeates reality. Spellcasters learn to channel this Flow through various approaches, shaping it according to their own strengths and perspectives. Unlike traditional magic systems where each caster type has unique spells, here the same spells can be cast through different mental and spiritual approaches, creating diverse effects.

### Flexible Casting System

The revolutionary aspect of this magic system is that spells aren't tied to a single casting attribute:

- **Casting Roll:** 2d6 + [Chosen Attribute] + Sorcery
- **Attribute Choice:** Player chooses which attribute to use based on their approach to casting
- **Power Source:** Spend Flow to fuel spells
- **Each Attribute Provides Different Benefits:** The same spell produces different effects based on the attribute used

### The Four Casting Approaches

#### Mind + Sorcery: The Wizard's Way
- **Mechanical Benefits:** Precision, control, avoiding allies, calculated effects
- **Narrative Flavor:** Academic magic, formulaic casting, spellbooks
- **Example:** Casting Fireball with Mind lets you exclude specific targets from the blast

#### Awareness + Sorcery: The Sorcerer's Way
- **Mechanical Benefits:** Maximum damage, sensing weaknesses, magical detection
- **Narrative Flavor:** Instinctive magic, raw power, natural talent
- **Example:** Casting Fireball with Awareness deals maximum damage output

#### Will + Sorcery: The Divine/Pact Way
- **Mechanical Benefits:** Cast at negative Flow, maintain concentration, push through adversity
- **Narrative Flavor:** Channeling external power, faith magic, patron bonds
- **Example:** Casting Fireball with Will works even when you're at negative Flow

#### Presence + Sorcery: The Bard's Way
- **Mechanical Benefits:** Social effects, fear/inspiration, affecting groups
- **Narrative Flavor:** Reality-shaping through force of personality, performative magic
- **Example:** Casting Fireball with Presence causes survivors to flee in terror

## Magic Access Requirements

Magic access is determined by your archetype and attributes:

**Universal Rule:** If your archetype provides the Sorcery skill, you can cast spells regardless of your attributes.
- This applies to Wizards, Clerics, Bards, and Paladins
- Your archetype training overrides the normal attribute requirements
- Represents formal magical education and practice

**Alternative Access:** Characters without a spellcasting archetype can learn magic if:
- **Mind + Awareness ≥ +2** (Arcane magic)
- **Will + Presence ≥ +2** (Divine magic)
- **Awareness + Will ≥ +2** (Primal magic)

This creates meaningful choices for non-caster archetypes while ensuring spellcasting archetypes can fulfill their role.

### Mage Sight (Innate to All Casters)

All characters who meet the magic access requirement possess Mage Sight, an innate ability to perceive magic:

- **Out of Combat:** Detect magic within Near zone, no roll needed
- **In Defensive Stance:** Can use instead of building Flow
- **Automatic:** Not a spell or cantrip, just natural perception
- **Enhanced by Awareness:** Awareness +3 or higher can identify spell types and magical signatures

## Spell Categories

Spells are divided into five tiers based on power level and Flow cost:

### Tier 0: Cantrips (Generate +1 Flow on Success)
- Simple magics that build momentum rather than consuming it
- Successfully casting a cantrip generates +1 Flow
- Available to all casters from the start
- Examples: Spark, Light, Mage Armor, Prestidigitation

### Tier 1: Basic Spells (0 Flow Cost)
- Fundamental spells that maintain Flow equilibrium
- The bread and butter of magical combat and utility
- No Flow cost, making them reliable and sustainable
- Examples: Bolt, Shield, Charm, Blur, Detect Magic

### Tier 2: Advanced Spells (-1 Flow Cost)
- Powerful effects that require minimal momentum investment
- Moderate Flow cost enables frequent use
- Significant battlefield impact
- Examples: Fireball, Heal, Fly, Invisibility, Web

### Tier 3: Expert Spells (-2 Flow Cost)
- Major magical effects requiring significant focus
- Higher Flow investment for dramatic results
- Game-changing capabilities
- Examples: Lightning Bolt, Teleport, Polymorph, Scrying, Wall of Fire

### Tier 4: Master Spells (-3 Flow Cost)
- Reality-altering magic at the peak of mortal capability
- Requires substantial Flow but delivers legendary effects
- Can fundamentally change encounters
- Examples: Time Stop, Dominate, Meteor Swarm, True Resurrection, Wish

## Armor and Casting

Wearing armor while casting spells affects your spellcasting ability:

- **No Armor:** +1 bonus to Sorcery checks (unrestricted magical flow)
- **Light Armor:** No penalty (compatible with spellcasting)
- **Medium Armor:** -1 to Sorcery checks (minor restriction)
- **Heavy Armor:** -3 to Sorcery checks (difficult but possible)

This rebalancing allows armored spellcasters (like Clerics and Paladins) to function effectively while maintaining meaningful trade-offs. Certain species traits and abilities can further reduce these penalties.

## Spells and Flow Generation

Spellcasters generate Flow through multiple methods, ensuring they participate actively in the Flow economy:

**Cantrips Generate Flow:**
- Successfully casting any cantrip generates +1 Flow
- This makes cantrips excellent for building momentum
- No Flow cost means you're always gaining when successful

**Aggressive Stance:**
- When you successfully cast an offensive spell that deals damage, gain +1 Flow
- Applies to all damage-dealing spells (Spark, Bolt, Fireball, etc.)
- Combines with cantrip Flow generation for Spark

**Taking Damage:**
- When you take damage (regardless of armor), gain +1 Flow
- Helps spellcasters recover from being targeted
- Universal Flow generation for all character types

**Critical Success:**
- Rolling 13+ on any casting roll generates +1 Flow
- Rewards high-skill casting

**Example Flow Economy:** A wizard casts Spark (cantrip) in Aggressive Stance and hits. They gain +1 Flow from cantrip success and +1 Flow from Aggressive successful attack, for a total of +2 Flow. Later, they cast Fireball (-1 Flow) and hit, spending 1 Flow but gaining 1 Flow back from Aggressive, for net 0 Flow cost.

## Spell Failure

When you roll 6 or less on a casting roll:
- Spell fails, generates +1 Flow for enemy
- Each attribute produces different failure manifestations:
  - **Mind failures:** Miscalculation causes minor paradox
  - **Awareness failures:** Magical backlash, sense overload
  - **Will failures:** Power source rejects you temporarily
  - **Presence failures:** Reality refuses to bend, embarrassing

## Using This Documentation

This spell documentation is organized into several sections:

- **[00_introduction.md](00_introduction.md)** (this file) - Core concepts and overview
- **[01_gm_guidelines.md](01_gm_guidelines.md)** - Running magic in your game
- **[02_system_integration.md](02_system_integration.md)** - How magic interacts with other systems
- **[03_quick_reference.md](03_quick_reference.md)** - Fast lookup for spells and mechanics
- **spell_tiers/** - Individual spell tier documentation
  - [cantrips.md](spell_tiers/cantrips.md)
  - [standard_spells.md](spell_tiers/standard_spells.md)
  - [advanced_spells.md](spell_tiers/advanced_spells.md)
  - [master_spells.md](spell_tiers/master_spells.md)

## Design Philosophy

The spell system adheres to Flow RPG's core design principles:

1. **Elegance over Complexity** - One unified casting mechanic instead of multiple subsystems
2. **Narrative-First with Tactical Depth** - Same spell, different narrative based on approach
3. **Flow as Universal Resource** - Magic fully integrated into the Flow economy
4. **Player Agency** - Choose how to cast each spell based on the situation

---

*This spell system represents the flexible, narrative-driven approach to magic that defines Flow RPG. Every casting choice creates a unique story while maintaining mechanical clarity and balance.*
