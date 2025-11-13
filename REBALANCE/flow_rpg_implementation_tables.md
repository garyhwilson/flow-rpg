# Flow RPG Rebalanced - Implementation Tables

## QUICK REFERENCE TABLES

### New Skill Progression
| Tier | Name | Modifier | Milestone Required |
|------|------|----------|-------------------|
| 1 | Untrained | -2 | Starting |
| 2 | Novice | -1 | Starting |
| 3 | Competent | +0 | Starting |
| 4 | Professional | +2 | Minor |
| 5 | Expert | +4 | Minor/Moderate |
| 6 | Master | +6 | Moderate |
| 7 | Legendary | +8 | Major |

### Success Probability Table (2d6 + Modifier vs TN)
| Modifier | TN 6 | TN 8 | TN 10 | TN 12 | TN 14 |
|----------|------|------|-------|-------|-------|
| -2 | 72.2% | 41.7% | 16.7% | 2.8% | 0% |
| -1 | 83.3% | 58.3% | 27.8% | 8.3% | 0% |
| +0 | 91.7% | 72.2% | 41.7% | 16.7% | 2.8% |
| +1 | 97.2% | 83.3% | 58.3% | 27.8% | 8.3% |
| +2 | 100% | 91.7% | 72.2% | 41.7% | 16.7% |
| +3 | 100% | 97.2% | 83.3% | 58.3% | 27.8% |
| +4 | 100% | 100% | 91.7% | 72.2% | 41.7% |
| +5 | 100% | 100% | 97.2% | 83.3% | 58.3% |
| +6 | 100% | 100% | 100% | 91.7% | 72.2% |

### Rebalanced Flow Generation
| Action | Aggressive | Balanced | Defensive |
|--------|------------|----------|-----------|
| Successful Attack | +1 | 0 | 0 |
| Successful Defense | 0 | 0 | +1 |
| Being Attacked | 0 | 0 | +1/round |
| Critical Success | +1 | +1 | +1 |
| Taking Damage | +1 | +1 | +1 |
| Charging (2 zones) | +2 | 0 | N/A |

### Spell Flow Costs (Revised)
| Tier | Spell Level | Old Cost | New Cost | Examples |
|------|-------------|----------|----------|----------|
| 0 | Cantrip | 0 | +1 on success | Spark, Mage Armor |
| 1 | Basic | -1 | 0 | Bolt, Shield, Charm |
| 2 | Advanced | -3 | -1 | Fireball, Heal, Fly |
| 3 | Expert | -6 | -2 | Lightning, Teleport |
| 4 | Master | -10 | -3 | Time Stop, Dominate |

### Damage Scaling by Milestones
| Total Milestones | Damage Bonus | Weapon Die | Special |
|------------------|--------------|------------|---------|
| 0 | +0 | 2d6 | - |
| 2 | +1 | 2d6 | - |
| 4 | +2 | 2d6 | - |
| 5 | +2 | 2d8 | Die upgrade |
| 6 | +3 | 2d8 | - |
| 8 | +4 | 2d8 | - |
| 10 | +5 | 2d8 | Exploding 6s |
| 12 | +6 | 2d10 | Die upgrade |
| 15 | +7 | 2d10 | Exploding 5-6 |

### Armor Rebalanced
| Type | DR | Grace | Flow | Sorcery | Special |
|------|-----|--------|------|---------|---------|
| None | 0 | 0 | +1 when hit | +1 | Extra zone movement |
| Light | 1 | 0 | Normal | 0 | +1 initiative |
| Medium | 2 | -1 | Normal | -1 | +1 Guard/scene |
| Heavy | 4 | -2 | -1 generation | -3 | Immune to knockback |

### Death Saves (2d6 + Will)
| Roll Total | Result |
|------------|---------|
| 6 or less | Lose 1 Vitality |
| 7-8 | Stable this round |
| 9-11 | Stabilize at 0 (unconscious) |
| 12+ | Conscious at 1 Vitality |

---

## GUARD & VITALITY CALCULATIONS

### Starting Guard Formula
```
Guard = 8 + Higher(Might, Grace) + (Total Milestones × 2)
```

| Might/Grace | Start | 5 Milestones | 10 Milestones | 15 Milestones |
|-------------|-------|--------------|---------------|---------------|
| -2 | 6 | 16 | 26 | 36 |
| -1 | 7 | 17 | 27 | 37 |
| 0 | 8 | 18 | 28 | 38 |
| +1 | 9 | 19 | 29 | 39 |
| +2 | 10 | 20 | 30 | 40 |
| +3 | 11 | 21 | 31 | 41 |
| +4 | 12 | 22 | 32 | 42 |
| +5 | 13 | 23 | 33 | 43 |

### Starting Vitality Formula
```
Vitality = 10 + Will + (Major Milestones × 3)
```

| Will | Start | 1 Major | 2 Major | 3 Major |
|------|-------|---------|---------|---------|
| -2 | 8 | 11 | 14 | 17 |
| -1 | 9 | 12 | 15 | 18 |
| 0 | 10 | 13 | 16 | 19 |
| +1 | 11 | 14 | 17 | 20 |
| +2 | 12 | 15 | 18 | 21 |
| +3 | 13 | 16 | 19 | 22 |
| +4 | 14 | 17 | 20 | 23 |
| +5 | 15 | 18 | 21 | 24 |

---

## STANCE COMPARISON MATRIX

| Aspect | Aggressive | Balanced | Defensive |
|--------|------------|----------|-----------|
| **Turn Order** | First | Second | Last |
| **Damage Mod** | +1 | +0 | -1 |
| **Defense Mod** | -1 | +0 | +2 |
| **Flow/Attack** | +1 | 0 | 0 |
| **Flow/Defense** | 0 | 0 | +1 |
| **Flow/Attacked** | 0 | 0 | +1/round |
| **Flow/Critical** | +1 | +1 | +1 |
| **Movement** | Must approach | Free | Can disengage |
| **Special** | Charge +2 dmg | Free stance switch | Counter on crit defense |

### Optimal Stance Selection Guide
- **Need Flow:** Defensive
- **Need Damage:** Aggressive  
- **Need Flexibility:** Balanced
- **Outnumbered:** Defensive
- **Chasing:** Aggressive
- **Unknown Situation:** Balanced

---

## MILESTONE ADVANCEMENT OPTIONS

### Minor Milestone Menu (Every 1-2 Sessions)
1. **Skill Up:** Advance one skill by one tier (max Expert +4)
2. **New Skill:** Gain new skill at Novice (-1)
3. **Attribute Shuffle:** +1 to one, -1 to another
4. **Combat Edge:** Choose from list below
5. **Skill Edge:** +1 to specific use of a skill
6. **Flow Edge:** +1 maximum Flow capacity

### Combat Edges (Minor Milestone Options)
| Edge | Benefit | Limit |
|------|---------|-------|
| Weapon Focus | +1 damage with weapon type | 1 per weapon |
| Armor Training | Reduce penalty by 1 | 1 per armor type |
| Quick Draw | Switch weapons free | Once |
| Combat Reflexes | +1 to defense rolls | Once |
| Tough | +2 Guard | Twice |
| Hardy | +2 Vitality | Twice |
| Flow Harmony | +1 max Flow | Three times |
| Fast Movement | +1 zone movement | Once |
| Precise Strike | Reroll one damage die | Once |
| Defensive Fighter | +1 Guard in Defensive | Once |

### Moderate Milestone Menu (Every 5-6 Sessions)
1. **Attribute Boost:** +1 to any attribute (max +4 until Major)
2. **Master Skill:** Advance to Master (+6)
3. **Signature Move:** Create personalized technique
4. **Advanced Technique:** Gain high-tier ability
5. **Calling Evolution:** Modify calling benefit

### Major Milestone Menu (Every 12-15 Sessions)
1. **Legendary Skill:** Advance to Legendary (+8)
2. **Attribute Transcendence:** Break +4 cap
3. **Calling Transformation:** Complete calling change
4. **Legendary Technique:** Gain ultimate ability
5. **Mythic Edge:** Gain supernatural capability

---

## REVISED ARCHETYPE STARTING BUILDS

### Fighter
- **Skills:** Combat (Professional +2), Athletics (Novice -1), Command (Novice -1)
- **Equipment:** Medium armor, martial weapon, shield
- **Special:** +1 Edge at start (Weapon Focus or Tough)

### Ranger
- **Skills:** Combat (Novice -1), Survival (Professional +2), Investigate (Novice -1)
- **Equipment:** Light armor, bow, tracking kit
- **Special:** +1 Edge at start (Fast Movement or Precise Strike)

### Paladin
- **Skills:** Combat (Novice -1), Medicine (Novice -1), Command (Professional +2)
- **Equipment:** Heavy armor, weapon, holy symbol
- **Special:** Can cast divine spells regardless of attributes

### Rogue
- **Skills:** Stealth (Professional +2), Finesse (Professional +2), Deceive (Novice -1)
- **Equipment:** Light armor, daggers, thieves' tools
- **Special:** Two Professional skills at start

### Wizard
- **Skills:** Sorcery (Professional +2), Lore (Professional +2), Investigate (Novice -1)
- **Equipment:** No armor, spellbook, components
- **Special:** Can cast arcane spells regardless of attributes

### Cleric
- **Skills:** Medicine (Professional +2), Sorcery (Novice -1), Empathy (Professional +2)
- **Equipment:** Medium armor, mace, holy symbol
- **Special:** Can cast divine spells regardless of attributes

### Bard
- **Skills:** Perform (Professional +2), Deceive (Novice -1), Sorcery (Novice -1)
- **Equipment:** Light armor, instrument, rapier
- **Special:** Can cast performance spells regardless of attributes

---

## CALLING QUICK TRIGGERS

| Calling | Old Trigger (Rare) | New Trigger (Reliable) |
|---------|-------------------|------------------------|
| **Advocate** | Expose corruption | Any truth revelation |
| **Guardian** | Ally at 0 Vitality | Any ally takes damage |
| **Exemplar** | Complex signature | Any critical success |
| **Seeker** | Act against expectations | Try something new/scene |
| **Scholar** | Bank 2 Flow | Start at +1 Flow |
| **Sentinel** | +1 Guard with Flow | +1 Flow when attacked |
| **Enthusiast** | Gift Flow to ally | Ally gains Flow with you |
| **Champion** | Protect in Aggressive | Attack while allies threatened |
| **Mediator** | Defuse peacefully | Resolve any conflict |

---

## COMBAT TRACKING SHEET

### Flow Tracker
```
Round | Marcus | Silvara | Thorin | Pip | Aldric | Elena | Melody
------|--------|---------|--------|-----|--------|-------|--------
Start |    0   |    0    |   0    |  0  |   +1*  |   0   |   0
  1   |   +1   |    0    |   0    | +1  |   +2   |  +1   |  -1
  2   |   +2   |   +1    |  +1    | +1  |   +3   |   0   |   0
  3   |   +3   |   +2    |  +2    | +2  |   +2   |  +1   |  +1
  4   |   +2   |   +2    |  +3    | +3  |   +3   |  +2   |  +2
End   |   +3   |   +2    |  +3    | +2  |   +4   |  +2   |  +1

* Scholar starts at +1 with new rules
```

### Damage Output Tracking
```
Character | Base | w/Milestones | w/Flow Boost | Critical
----------|------|--------------|--------------|----------
Fighter   | 2d6+3| 2d8+5 (14)   | 2d8+6 (15)   | 4d8+6 (24)
Ranger    | 2d6+2| 2d6+4 (11)   | 2d6+5 (12)   | 4d6+5 (19)
Paladin   | 2d6+1| 2d8+3 (12)   | 2d8+4 (13)   | 4d8+4 (22)
Rogue     | 2d6+0| 2d6+2 (9)    | 3d6+2 (12.5) | 4d6+2 (16)
Wizard    | 1d6+2| 2d6+2 (9)    | 3d6+2 (12.5) | 4d6+2 (16)
Cleric    | 2d6+0| 2d6+2 (9)    | 2d6+3 (10)   | 4d6+3 (17)
Bard      | 2d6+0| 2d6+2 (9)    | 2d6+3 (10)   | 4d6+3 (17)
```

---

## ENEMY SCALING GUIDELINES

### Enemy HP by Character Level
| Milestones | Minion | Standard | Elite | Boss |
|------------|--------|----------|-------|------|
| 0-2 | 8 | 15 | 25 | 40 |
| 3-5 | 12 | 20 | 35 | 55 |
| 6-8 | 16 | 28 | 45 | 75 |
| 9-11 | 22 | 38 | 60 | 95 |
| 12-14 | 30 | 50 | 80 | 120 |
| 15+ | 40 | 65 | 100 | 150 |

### Enemy Damage by Character Level
| Milestones | Minion | Standard | Elite | Boss |
|------------|--------|----------|-------|------|
| 0-2 | 1d6 | 2d6 | 2d6+2 | 3d6 |
| 3-5 | 1d6+1 | 2d6+1 | 2d6+3 | 3d6+2 |
| 6-8 | 1d6+2 | 2d6+2 | 3d6+2 | 3d6+4 |
| 9-11 | 2d6 | 2d6+3 | 3d6+4 | 4d6+3 |
| 12-14 | 2d6+1 | 3d6+2 | 3d6+5 | 4d6+5 |
| 15+ | 2d6+2 | 3d6+3 | 4d6+4 | 5d6+4 |

---

## ENCOUNTER BALANCE CALCULATOR

### Threat Rating Formula
```
Threat = (Enemy HP / Party Average Damage) + (Enemy Damage × Hit Rate / Party Average Guard)

Balanced Encounter: Threat = 3-5
Easy Encounter: Threat = 1-2
Hard Encounter: Threat = 6-8
Deadly Encounter: Threat = 9+
```

### Quick Encounter Builder
| Party Size | Easy | Standard | Hard | Deadly |
|------------|------|----------|------|--------|
| 3 PCs | 2 Minions | 1 Standard | 1 Elite | 1 Boss |
| 4 PCs | 3 Minions | 2 Standards | 1 Elite + 1 Minion | 1 Boss + 1 Standard |
| 5 PCs | 4 Minions | 2 Standards + 1 Minion | 2 Elites | 1 Boss + 2 Standards |
| 6 PCs | 5 Minions | 3 Standards | 2 Elites + 1 Standard | 1 Boss + 1 Elite |
| 7 PCs | 6 Minions | 4 Standards | 3 Elites | 2 Bosses |

---

## PLAYTESTING CHECKLIST

### Session 1-2 Validation
- [ ] All archetypes can use their core features
- [ ] Combat lasts 3-5 rounds
- [ ] Flow generation balanced across party
- [ ] Spellcasters viable in combat
- [ ] Death saves feel fair but tense

### Session 3-5 Validation  
- [ ] Minor milestones provide meaningful choices
- [ ] Damage scaling keeps pace with enemy HP
- [ ] All stances see use
- [ ] Calling benefits trigger regularly
- [ ] No character feels useless

### Session 6+ Validation
- [ ] Moderate milestone feels significant
- [ ] Characters haven't hit advancement ceiling
- [ ] Combat remains tactical not just numerical
- [ ] Flow economy still balanced
- [ ] High-level play maintains interest

---

## CONVERSION NOTES

### For Existing Characters
1. Add Novice tier between Untrained and Competent
2. Reduce all Competent skills to Novice (-1)
3. Recalculate Guard with new formula
4. Grant Edge equal to milestones/3
5. Adjust spell costs to new scale
6. Remove armor casting restrictions for appropriate archetypes

### For Existing Encounters
1. Reduce enemy HP by 20%
2. Increase enemy damage by 1 per 5 character milestones
3. Add Flow generation for taking damage
4. Rebalance boss HP to 3× standard enemy
5. Add minion category for swarm encounters

This implementation guide provides all the tables and references needed to run the rebalanced system immediately.
