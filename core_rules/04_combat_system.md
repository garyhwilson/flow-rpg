# COMBAT SYSTEM

## Stance-Based Combat

Rather than using traditional initiative rolls, this game uses a stance system that determines turn order based on tactical choices. Each round, you choose one of three stances that reflect your approach to the fight.

### The Three Stances

**Aggressive Stance**
_"Strike first, strike hard"_

- **Turn Order:** Act first
- **Momentum Generation:** +1 Momentum on successful attacks
- **Damage Bonus:** +1 to all damage rolls
- **Defense Penalty:** -1 to defense rolls
- **Movement:** Must move toward nearest enemy if able
- **Special Ability:** Charge - Move 2+ zones and attack for +2 damage

**Balanced Stance**
_"Adapt and overcome"_

- **Turn Order:** Act second
- **Momentum Generation:** +1 Momentum on any roll of 8+ (natural, before modifiers)
- **Damage:** Normal
- **Defense:** Normal
- **Movement:** Complete freedom
- **Special Ability:** Once per combat, switch stance as a free action

**Defensive Stance**
_"Patience and protection"_

- **Turn Order:** Act last (choosing your moment)
- **Momentum Generation:** +1 when attacked (once per round), +1 on successful defense
- **Damage Penalty:** -1 to damage rolls
- **Defense Bonus:** +4 to defense rolls
- **Damage Reduction:** 2 (reduces incoming damage)
- **Movement:** Can disengage without penalty
- **Special Ability:** Counterattack on critical defense success

### Stance Switching Rules

Stance switching is now **free** (no Momentum cost). You can change your stance at the start of each round based on tactical needs. The Balanced stance special ability allows one additional stance change during combat as a free action.

### Turn Order Specifics

1. **Aggressive stance characters** act first (pressing the attack)
2. **Balanced stance characters** act second
3. **Defensive stance characters** act last (waiting to react)

Within each stance group, highest Grace acts first, with ties favoring players over NPCs.

---

## Momentum Zones & Positioning

Combat occurs across abstract distance zones that determine engagement and weapon effectiveness.

### The Three Core Zones

**Engaged**

- In melee with specific opponents
- Melee weapons operate normally
- Cannot use bows or other ranged weapons
- Switching weapons is free
- Cannot move past enemies without special abilities

**Close**

- One move from any engagement
- Throwing weapons operate at optimal range
- Bows and ranged weapons operate normally
- Can move into Engaged zone as normal movement
- Enemies can't directly attack you with melee weapons

**Far**

- Two moves from any engagement
- Optimal for bows and ranged attacks
- Melee fighters cannot attack targets at Far range
- Spells may still reach depending on description
- Safe from immediate melee threats

### Movement Between Zones

- **Standard Movement:** One zone per round
- **Double Movement:** Two zones if taking no other action
- **Engagement:** Moving into the same zone as an enemy puts you in Engaged position
- **Disengagement:** Moving from Engaged to Close requires specific stance or abilities

### Stance Effects on Movement

**Aggressive Stance Movement:**

- Moving Far → Close → Engaged generates +1 Momentum per zone crossed
- Cannot disengage from enemies without switching stance
- Must close to Engaged if possible (seeking combat)

**Balanced Stance Movement:**

- Normal movement (one zone per round)
- Can choose to engage or disengage as preferred
- Can move two zones if taking no other action

**Defensive Stance Movement:**

- Can disengage from Engaged to Close freely
- Gains +1 Momentum when enemies close to Engaged with you
- Can maintain preferred distance more easily

### Ranged Combat by Zone

- **Engaged:** Cannot use bows, -2 penalty with thrown weapons
- **Close:** Thrown weapons gain +1 Momentum, bows work normally
- **Far:** Optimal for bows (+1 damage), thrown weapons cannot reach

---

## Health System

Characters have two health resources that work together to model both minor and serious injuries.

### Guard

Guard represents your ability to avoid serious harm through armor, dodging, tactical positioning, and mental fortitude.

- **Formula:** 12 + max(Might, Grace, Will)
- **Function:** Ablative defense that absorbs damage first
- **Recovery:** Fully restored between scenes
- **In-Combat Recovery:** Can use Rally action to recover 1d6 Guard (once per scene)

**Why Three Options?**
Using the highest of Might, Grace, or Will allows tough fighters (high Might), agile defenders (high Grace), and mentally resilient characters (high Will) to all be effective. This is especially important for casters who typically have high Will but low physical attributes.

> **Note:** Guard is NOT a target number for attacks. Attacks always roll against TN 8 (or higher per GM guidance). Guard is an HP pool that absorbs damage from successful hits.

**Archetype Bonuses:**
Some archetypes provide additional Guard through their features:

- **Divine Grace** (Paladin, Cleric): +4 Guard
- **Arcane Battery** (Wizard): +2 Guard

### Vitality

Vitality represents your core health and ability to withstand serious injury.

- **Formula:** 10 + Will
- **Function:** Core health representing serious injury
- **Consequences:** Damage to Vitality often causes lasting effects
- **Critical Point:** At 0 Vitality, you fall unconscious and begin dying

**Increasing Vitality:**
Vitality can be increased through advance choices (see Advancement), but does not scale automatically. This keeps death meaningful throughout the campaign.

### Damage Resolution

1. Attacker rolls damage (typically weapon dice + modifiers)
2. Subtract armor damage reduction (if any)
3. Remaining damage is applied to Guard first
4. Once Guard is depleted, further damage reduces Vitality
5. At 0 Vitality, character falls unconscious and begins dying

### Death & Dying Rules

When reduced to 0 Vitality, you fall unconscious and begin dying.

**Death Saves:** Roll 2d6 + Will at the start of each turn:

- **5 or less:** Lose 1 Vitality (getting worse)
- **6-7:** Stable for this round (holding on)
- **8-10:** Stabilize at 0 Vitality (unconscious but stable)
- **11+:** Regain consciousness at 1 Vitality (heroic recovery)

**Death:** Occurs at -3 Vitality (down from -5)
**Stabilization:** Medicine check (TN 8) or any magical healing
**Recovery:** Regain 1 Vitality per hour of rest after stabilization

---

## Combat Actions

### Basic Actions

**Attack**

- Roll 2d6 + Attribute + Combat
- Typically Might + Combat for melee, Grace + Combat for ranged
- Target number 8 (standard difficulty)
- On hit, roll weapon damage (usually 2d6 + modifiers)

**Defend**

- Roll 2d6 + Grace + Combat
- Success adds +2 Guard until your next turn
- Critical success grants +1 Momentum

**Maneuver**

- Roll 2d6 + appropriate Attribute + Skill
- Reposition, create advantage, or alter battlefield
- Success often grants +1 Momentum or creates opportunity

**Rally**

- Spend action to recover 1d6 Guard
- Once per scene only
- Does not require a roll

### Reactions

**Counter**

- When attacked in Defensive stance, spend 1 Momentum
- Roll opposed Combat check
- Success negates attack and may grant counterattack

**Interpose**

- When adjacent ally is attacked, spend 1 Momentum
- Become the target instead
- Must be in Defensive stance

---

## Combat Techniques

### Access Philosophy

- Basic combat available to all
- Advanced techniques require Momentum thresholds
- Acquisition through advances (earned via XP)
- NO attribute gates for combat (anyone can learn any technique)

### Basic Techniques (Anyone can attempt)

- Strike: Standard attack action
- Defend: Increase Guard temporarily
- Maneuver: Create tactical advantage
- Rally: Recover Guard mid-combat (once per scene)

### Novice Techniques (Available to All)

- **Riposte:** After successful Defend, immediately Strike
- **Press Advantage:** +1d6 damage when Momentum positive
- **Defensive Stance Mastery:** Trade offense for stronger defense
- **Quick Recovery:** Regain Guard between rounds

### Seasoned Techniques (Require Seasoned Rank)

- **Whirlwind Strike:** Hit all adjacent enemies
- **Perfect Parry:** Negate all damage from one source
- **Devastating Blow:** Double damage dice
- **Combat Momentum:** Extra Momentum on critical success

### Heroic Techniques (Require Heroic Rank)

- **Unstoppable Assault:** Cannot miss
- **Death Blow:** Instant kill if target below 50% Vitality
- **Battlefield Control:** Dictate positioning of multiple combatants

---

## Signature Moves

At Seasoned rank and beyond, you can use an advance to create a personal Signature Move that represents your character's unique fighting style.

### Creating a Signature Move

- Combines existing abilities in a unique way
- Costs 1 less Momentum than normal (minimum 0)
- Must have narrative description and name
- Should reflect character's Calling and style

### Example Signature Moves

- **"Divine Hammer"** - Spark spell that heals adjacent ally
- **"Smoke & Mirrors"** - Deceive check creates illusory duplicates
- **"Reality Tear"** - Bolt spell that reduces target's defense
- **"Guardian's Stand"** - Perfect defense that generates Momentum for allies

---

## Armor & Weapons

### Armor System

**Light Armor** (leather, padded)

- **Damage Reduction:** -1
- **No penalties**
- **Examples:** Leather armor, padded jerkin

**Medium Armor** (chain, scale)

- **Damage Reduction:** -2
- **Penalty:** -1 to Grace-based rolls (including Grace + Combat)
- **Cannot generate Momentum from movement** (no charging bonus)
- **Examples:** Chain shirt, scale mail

**Heavy Armor** (plate)

- **Damage Reduction:** -4
- **Penalty:** -2 to Grace-based rolls
- **Stance Restriction:** Cannot use Aggressive stance
- **Examples:** Full plate, heavy field plate

**Shields**

- **Small Shield:** +1 Guard
- **Large Shield:** +2 Guard, -1 to Grace when attacking

_Note: Armor reduces damage before it applies to Guard. Shields increase Guard total._

### Weapon Types

**Light Weapons** (dagger, club)

- **Damage:** 2d6
- **Special:** +1 to Finesse actions
- **Examples:** Dagger, club, short sword

**Medium Weapons** (sword, mace)

- **Damage:** 2d6+1
- **Balanced:** No special bonuses or penalties
- **Examples:** Longsword, mace, battle axe

**Heavy Weapons** (greatsword, maul)

- **Damage:** 2d6+2
- **Penalty:** -1 Grace
- **Examples:** Greatsword, maul, greataxe

**Reach Weapons** (spear, polearm)

- **Damage:** 2d6
- **Special:** Can attack from Close range
- **Examples:** Spear, halberd, pike

**Ranged Weapons** (bow, crossbow)

- **Damage:** 2d6
- **Special:** -2 penalty in melee (Engaged)
- **Examples:** Shortbow, longbow, crossbow

### Weapon Damage Rules

- **Base Damage:** Determined by weapon type
- **Exploding Dice:** Any 6 rolled is rolled again and added (uncapped)
- **Critical Hit:** On attack roll of 13+, +1d6 damage

---

## Social Combat

Social conflicts use the same stance system as physical combat, creating a consistent mechanical framework.

### Social Stances

**Aggressive (Social)**

- Direct argument, intimidation, forceful persuasion
- Generate +1 Momentum on successful Social checks
- Act first in social exchanges
- More vulnerable to counterarguments

**Balanced (Social)**

- Negotiation, finding common ground
- Normal Momentum generation
- Act second in social exchanges
- Adaptable to different approaches

**Defensive (Social)**

- Listening, gathering information, cautious responses
- Generate +1 Momentum when learning important secrets
- Act last in social exchanges
- Harder to persuade but less influential

### Social Health: Composure

- **Formula:** Will + Presence + 5
- **Function:** Represents social resilience and resolve
- **Consequences:** When reduced to 0, character is convinced, flees, or surrenders
- **Recovery:** Fully restored between scenes

### Social Damage

- **Formula:** Typically 1d6 + Presence or other relevant attribute
- **Application:** Reduces target's Composure
- **Critical Success:** Additional impact on target's beliefs or actions

---

## Example Combat Round

**Setup:** Elena (Cleric, Balanced stance), Magnus (Fighter, Aggressive stance), and Lyra (Wizard, Defensive stance) face off against a hobgoblin captain and two archers.

**Turn Order:**

1. Magnus (Aggressive stance)
2. Hobgoblin Captain (Aggressive stance)
3. Elena (Balanced stance)
4. Lyra (Defensive stance)
5. Hobgoblin Archers (Defensive stance)

**Round 1:**

1. **Magnus (Momentum +1):** In Aggressive stance, closes from Far to Engaged with the captain (+1 Momentum for charging), attacks with longsword. Rolls 2d6+4: 9 - hits for 2d6+1: 8 damage. Captain's armor reduces by 2, taking 6 to Guard.

2. **Hobgoblin Captain (Momentum 0):** Already Engaged with Magnus, attacks with battleaxe. Rolls 7 - hits for 7 damage. Magnus's medium armor reduces by 2, taking 5 to Guard.

3. **Elena (Momentum 0):** In Balanced stance at Close range, casts Shield on Magnus using Mind + Sorcery. Rolls 10 - success, granting Magnus +2 Guard.

4. **Lyra (Momentum 0):** In Defensive stance at Far range, casts Bolt at an archer using Awareness + Sorcery. Rolls 13 - critical success (+1 Momentum), dealing 9 damage. Archer's light armor reduces by 1, taking 8 damage (reducing Guard to 0 and 3 to Vitality).

5. **Hobgoblin Archers (Momentum 0):** In Defensive stance at Far range, both fire at Lyra. First rolls 5 - miss. Second rolls 9 - hits for 7 damage. Lyra has no armor, taking full 7 to Guard (reducing her Guard to 0).

**Round 2 Stance Decisions:**

- Magnus stays Aggressive (maintaining pressure)
- Elena switches to Defensive (-1 Momentum, wants to protect Lyra)
- Lyra stays Defensive (vulnerable with no Guard)
- Hobgoblin Captain switches to Balanced (free)
- Archers stay Defensive (keeping distance)

The combat continues with these new stance positions affecting turn order and tactical options in Round 2.
