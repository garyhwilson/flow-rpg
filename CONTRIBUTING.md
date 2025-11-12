# Contributing to Flow RPG

Thank you for your interest in Flow RPG! This document provides guidelines for contributing to the project through playtesting, feedback, and suggestions.

---

## 🎲 How to Contribute

There are several ways to help improve Flow RPG:

### 1. Playtesting
Run games and provide feedback on:
- Character creation experience
- Combat balance
- Magic system functionality
- Calling integration
- Overall fun factor

### 2. Feedback & Suggestions
Share your thoughts on:
- Rule clarity
- Balance issues
- Missing content
- Quality of life improvements

### 3. Bug Reports
Report issues like:
- Rule contradictions
- Math errors
- Typos and formatting
- Broken cross-references

### 4. Documentation
Help improve:
- Clarity of explanations
- Examples and scenarios
- Quick reference materials
- Tutorials and guides

---

## 📝 Playtesting Guidelines

### Before Your Session

1. **Read the Core Rules**
   - Generate the Core Rulebook (see README.md)
   - Or browse modular files in `drafts/`
   - Focus on systems you'll use

2. **Create Characters**
   - Test character creation process
   - Note any unclear steps
   - Try different combinations (calling + archetype + species)

3. **Prepare Your Session**
   - Plan encounters using the Flow economy
   - Consider different combat scenarios
   - Include magic use if relevant

### During Your Session

**Track these areas:**
- Flow generation and spending
- Spell usage and attribute choices
- Calling benefit triggers
- Combat pacing and stance changes
- Any rules questions that arise

**Keep notes on:**
- What worked well
- What felt confusing
- What seemed overpowered/underpowered
- House rules you felt necessary
- Player reactions and engagement

### After Your Session

**Submit a Playtest Report** (see template below)

---

## 🐛 Reporting Issues

Use GitHub Issues for bug reports and suggestions.

### Bug Report Template

```markdown
**Title:** [Brief description]

**Type:** [Rule Error / Typo / Balance Issue / Other]

**Location:**
- File: [e.g., drafts/spells/spell_tiers/cantrips.md]
- Section: [e.g., "Spark - Mind + Sorcery"]
- Line: [if known]

**Description:**
[What's wrong?]

**Expected:**
[What should it be?]

**Additional Context:**
[Any other relevant information]
```

### Feature Request Template

```markdown
**Title:** [Brief feature description]

**Problem:**
[What need does this address?]

**Proposed Solution:**
[How might this work?]

**Alternatives:**
[Other ways to solve this]

**Additional Context:**
[Any other relevant information]
```

---

## 📋 Playtest Report Template

Copy this template for playtest reports:

```markdown
# Flow RPG Playtest Report

## Session Information
- **Date:** [Date of session]
- **GM:** [Your name]
- **Players:** [Number of players]
- **Session Length:** [Hours]
- **Character Levels:** [Milestone levels]

## Party Composition
List each PC:
- **Character Name:** [Name] - [Calling] [Archetype] [Species]
  - Notable build choices: [Key attributes, signature spells, etc.]

## Scenarios Tested
What did you do in the session?
- Combat encounters (how many, against what?)
- Social encounters
- Exploration
- Other activities

## Systems Used
Which systems got tested?
- [ ] Character Creation
- [ ] Basic Mechanics (2d6 rolls)
- [ ] Combat System & Stances
- [ ] Magic System (which attributes for casting?)
- [ ] Calling benefits
- [ ] Equipment
- [ ] Advancement (if applicable)

## What Worked Well ✅
What felt good? What did players enjoy?

Examples:
- "The flexible casting system was a hit - players loved choosing different attributes"
- "Flow economy created great tactical tension"
- "Callings made characters feel unique beyond mechanics"

## What Felt Off ⚠️
What seemed problematic? What confused players?

Examples:
- "Guard scaling made later combats trivial"
- "Will casting at negative Flow felt too powerful"
- "Wasn't clear when calling benefits triggered"

## Balance Observations
Any balance issues?

**Overpowered:**
- [What seemed too strong?]

**Underpowered:**
- [What seemed too weak?]

**Just Right:**
- [What felt balanced?]

## Rules Questions
Questions that came up during play:
1. [Question about how X works]
2. [Unclear interaction between Y and Z]

## House Rules Used
Any modifications you made:
- [Rule change and why]

## Player Feedback
Direct quotes or summaries from players:
- "This was fun because..."
- "I didn't like..."
- "I wish..."

## Specific Examples
Concrete examples of play:
- **Cool Moment:** [Describe awesome thing that happened]
- **Problem Moment:** [Describe problematic situation]

## Overall Rating
Rate each area (1-5, where 5 is excellent):
- **Fun Factor:** [ /5]
- **Rule Clarity:** [ /5]
- **Balance:** [ /5]
- **Pacing:** [ /5]
- **Would play again:** [Yes/No/Maybe]

## Suggestions
Specific recommendations for improvement:
1. [Suggestion]
2. [Suggestion]

## Additional Notes
Anything else worth mentioning?
```

---

## 💡 Suggesting Changes

### Good Suggestions Include:
- **Problem Statement:** What's not working?
- **Evidence:** Playtesting experience, examples, math
- **Proposed Solution:** Specific suggestion
- **Alternatives:** Other ways to solve it
- **Impact Assessment:** What else might this affect?

### Example:

> **Problem:** Guard scaling makes high-level characters nearly unhittable.
>
> **Evidence:** At Milestone 5, Fighter with +4 Body, medium armor (+3), and Shield spell (+3) has Guard 13. Most enemies need to roll 11+ to hit (8% chance).
>
> **Proposed Solution:** Cap Guard bonus from attributes at +3, or introduce armor penetration for high-level enemies.
>
> **Alternatives:**
> - Scale enemy attack bonuses more aggressively
> - Add "touch attack" spells that bypass armor
> - Diminishing returns on Guard stacking
>
> **Impact:** Would require rebalancing high-level encounters, but makes defense scaling more manageable.

---

## 🔄 Development Process

### How Changes Are Made

1. **Issue Created** - Bug reported or feature suggested
2. **Discussion** - Community discusses merits and alternatives
3. **Decision** - Maintainer decides whether to implement
4. **Development** - Change is made to modular files
5. **Testing** - Change is playtested
6. **Integration** - Change becomes part of core rules

### Version Control

Flow RPG uses Git for version control:
- **Main branch:** Stable, tested content
- **Feature branches:** Experimental changes
- **Releases:** Major milestones (v0.1, v0.2, v1.0, etc.)

---

## 📐 Style Guidelines

If contributing content (advanced contributors):

### Writing Style
- **Clear and Concise:** Short sentences, active voice
- **Consistent Terminology:** Use established terms
- **Examples Included:** Provide concrete examples
- **Cross-Referenced:** Link to related sections

### Formatting
- **Markdown:** Use standard markdown
- **Headers:** Consistent hierarchy (# ## ###)
- **Lists:** Use for readability
- **Tables:** For quick reference data

### Structure
Follow the established modular structure:
```
system_name/
├── 00_introduction.md
├── 01_gm_guidelines.md
├── 02_system_integration.md
├── 03_quick_reference.md
└── content_types/
    └── individual_items.md
```

---

## 🎯 Priority Areas

Currently seeking feedback on:

### High Priority
- [ ] **Guard Scaling** - Balance at high levels
- [ ] **Halfling Weapon Damage** - Viability in combat
- [ ] **Will Casting** - Negative Flow casting balance
- [ ] **Scholar Calling** - Retroactive dice benefit

### Medium Priority
- [ ] Magic access requirements (Mind + Awareness ≥ +2)
- [ ] Stance/Calling interactions
- [ ] Spell balance across tiers
- [ ] Equipment pricing

### Low Priority (Future)
- [ ] Additional archetypes
- [ ] More spells
- [ ] Monster creation system
- [ ] Sample adventures

---

## 🤝 Code of Conduct

### Our Standards

**Positive Environment:**
- Be respectful and constructive
- Focus on the game, not personalities
- Welcome diverse perspectives
- Assume good faith

**Constructive Feedback:**
- Be specific and actionable
- Provide evidence when possible
- Suggest solutions, not just problems
- Acknowledge what works well

**Collaborative Spirit:**
- Build on others' ideas
- Give credit where due
- Help newcomers
- Share your expertise

**Not Acceptable:**
- Personal attacks
- Harassment or discrimination
- Trolling or deliberate disruption
- Sharing others' content without permission

---

## 📞 Contact

- **GitHub Issues:** For bugs and suggestions
- **GitHub Discussions:** For questions and ideas
- **Email:** [Your email] for private matters

---

## 🙏 Recognition

Contributors will be acknowledged in:
- README.md acknowledgments section
- Published game credits (if applicable)
- Release notes for significant contributions

---

## ⚖️ Legal

By contributing, you agree that:
- Your contributions may be included in Flow RPG
- You have the right to submit the contribution
- Your contribution will be licensed under the project's license
- You retain copyright to your contributions

---

**Thank you for helping make Flow RPG better!**

*Every playtest session, bug report, and suggestion helps create a better game for everyone.*
