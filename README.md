# Autumn Phoenix RPG

**A narrative-driven tabletop roleplaying game where your momentum shapes reality**

Autumn Phoenix RPG is a complete TTRPG system built around an elegant, unified resource economy. Every action—from swinging a sword to casting a spell to pursuing your character's calling—feeds into a dynamic Momentum system that creates dramatic pacing and meaningful tactical choices.

---

## 🎯 Core Concepts

### Flexible Casting System

The same spell adapts to your approach. Cast Fireball with:

- **Mind** for precision (exclude allies from the blast)
- **Awareness** for maximum damage
- **Will** for reliability (even at negative Momentum)
- **Presence** for terror (survivors flee)

### Momentum Economy

One unified resource powers everything:

- Magic spells cost Momentum
- Combat actions generate Momentum
- Stances modify Momentum dynamics
- Callings provide Momentum benefits

### Callings System

Your character's motivation drives mechanical benefits. Are you an Explorer seeking new horizons? A Protector shielding the weak? Your calling shapes how you play.

### Dynamic Combat

Three stances create tactical depth:

- **Aggressive:** High risk, high reward, generate Momentum
- **Defensive:** Build resources, improve defenses
- **Balanced:** Versatile and adaptable

---

## 📊 Current Status

**Version:** 1.0 Draft (In Development)

### Complete Systems ✓

- ✅ Core Rules (modularized)
- ✅ Callings (9 callings fully documented)
- ✅ Archetypes (6 core archetypes)
- ✅ Species (4 core species)
- ✅ Equipment (complete equipment system)
- ✅ Spells (all 4 tiers: cantrips, standard, advanced, master)
- ✅ Publication System (automated book assembly)

### In Development

- Monster/NPC creation system
- Sample adventures
- Additional archetypes and species
- Expanded spell list

---

## 📁 Project Structure

```
momentum-rpg/
├── drafts/                    # Modular source files
│   ├── core_rules/           # Core mechanics (9 files)
│   ├── callings/             # Character motivation system
│   ├── archetypes/           # Character classes (6 archetypes)
│   ├── species/              # Character heritage (4 species)
│   ├── equipment/            # Gear and magical items
│   └── spells/               # Magic system (4 spell tiers)
├── publications/             # Book assembly system
│   ├── manifests/            # YAML book definitions
│   ├── templates/            # Reusable content
│   └── assembled/            # Generated books (gitignored)
└── scripts/                  # Automation tools
    └── assemble_book.py      # Book assembly script
```

---

## 🚀 Quick Start

### For Readers/Playtesters

**Option 1: Read Modular Files**
Browse the `drafts/` directory to explore individual systems:

- `core_rules/` - Start here for basic mechanics
- `callings/` - Understand character motivation
- `archetypes/` - See character classes
- `spells/` - Explore the flexible magic system

**Option 2: Generate Complete Book**

```bash
# Requires Python 3.6+ and PyYAML
pip install pyyaml
python scripts/assemble_book.py publications/manifests/core_rulebook.yaml
# Read: publications/assembled/core_rulebook.md
```

### For Contributors

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Providing feedback
- Playtesting
- Reporting issues
- Suggesting improvements

---

## 🎲 Design Philosophy

### 1. Elegance over Complexity

- Simple, unified resolution system (2d6 + attribute + skill)
- One resource (Momentum) unifies all subsystems
- Minimal bookkeeping, maximum decision space

### 2. Narrative-First with Tactical Depth

- Story drives mechanics, not vice versa
- Tactical options for those who want them
- Every rule supports the fiction

### 3. Momentum as Universal Resource

- Single resource unifying combat, magic, and narrative
- Dynamic economy creating dramatic pacing
- Intuitive resource mirroring character momentum

### 4. Player Agency

- Meaningful choices in character building
- Choose how to cast each spell (Mind/Awareness/Will/Presence)
- Tactical decisions in combat (stance selection)
- Narrative permissions granting special capabilities

---

## 📖 Key Features

### Revolutionary Magic System

Unlike traditional RPGs where each caster type has unique spells, Autumn Phoenix RPG lets you cast the same spells different ways:

- Wizards use Mind for precision and control
- Sorcerers use Awareness for raw power
- Clerics use Will for reliability
- Bards use Presence for social impact

**Same spell, different story, different tactics.**

### Callings Drive Story

Your calling isn't just flavor—it provides concrete mechanical benefits:

- **Explorer** generates Momentum when discovering new things
- **Scholar** can retroactively add knowledge dice
- **Protector** gains benefits when defending others
- **Avenger** gets bonuses against specific foes
- And 6 more unique callings...

### Integrated Systems

Everything connects to Momentum:

- Cast spells: Spend Momentum
- Attack in Aggressive stance: Generate Momentum
- Defend in Defensive stance: Build Momentum
- Pursue your calling: Get Momentum benefits

---

## 🛠️ Publication System

Autumn Phoenix RPG uses a modular development approach with automated book assembly:

1. **Develop in Modules** - Edit focused, manageable files
2. **Define Book Structure** - YAML manifests specify what goes where
3. **Assemble Automatically** - Python script generates complete books
4. **Iterate Efficiently** - Change modules, regenerate books instantly

See `publications/README.md` for details.

**Current Publications:**

- Core Rulebook (complete manifest ready)

**Planned Publications:**

- Player's Guide
- Game Master's Guide
- Grimoire: Advanced Magic
- Additional supplements

---

## 📋 Status & Roadmap

### Milestone 1: Core Systems ✓ COMPLETE

- [x] Basic mechanics
- [x] Character creation
- [x] Combat system
- [x] Magic system
- [x] All core archetypes, species, callings
- [x] Equipment system
- [x] Complete spell list (4 tiers)

### Milestone 2: Publication Ready (In Progress)

- [x] Publication assembly system
- [x] Core Rulebook manifest
- [ ] Playtest and balance
- [ ] Professional editing
- [ ] Layout and formatting

### Milestone 3: Expansion Content

- [ ] Additional archetypes (Monk, Druid, Warlock)
- [ ] Additional species variants
- [ ] Expanded spell list
- [ ] Monster/NPC creation system
- [ ] Sample adventures

### Milestone 4: Community & Release

- [ ] Public playtesting
- [ ] Community feedback integration
- [ ] Final polish
- [ ] Publication

---

## 🤝 Contributing

We welcome feedback, playtesting reports, and suggestions! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

**Currently Seeking:**

- Playtest feedback on balance
- Character build examples
- Session reports
- Typo/clarity improvements

---

## 📄 License

[Choose your license - see LICENSE.md for options]

This is currently a development draft. Final licensing will be determined before publication.

---

## 📞 Contact

- **Issues:** Use GitHub Issues for bug reports and suggestions
- **Discussions:** Use GitHub Discussions for questions and ideas
- **Email:** [Your email here]

---

## 🙏 Acknowledgments

Thanks to all playtesters and contributors who have helped shape Autumn Phoenix RPG.

[Add specific acknowledgments as appropriate]

---

## ⭐ Key Design Innovations

1. **Attribute-Flexible Spellcasting** - Same spell, four different approaches
2. **Unified Momentum Economy** - One resource for everything
3. **Calling-Driven Mechanics** - Motivation provides tangible benefits
4. **Stance-Based Combat** - Dynamic tactical choices
5. **Modular Development** - Efficient creation and maintenance

---

_Momentum RPG: Where your character's momentum becomes reality._
