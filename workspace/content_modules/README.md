# Content Modules

This directory demonstrates the **modular content pattern** used for major game systems like character classes, species, spells, equipment categories, and more.

## The 4-File Pattern

Each content category should have these four introductory files:

```
content_category/
├── 00_introduction.md       # What this content is about
├── 01_gm_guidelines.md      # How GMs should use this content
├── 02_system_integration.md # How this connects to other systems
├── 03_quick_reference.md    # Tables and summaries
└── content_types/           # Individual items
    ├── item_a.md
    ├── item_b.md
    └── item_c.md
```

## Why This Pattern?

1. **Consistent navigation** - Players and GMs always know where to find things
2. **Flexible publication** - Include what you need per book
3. **GM support** - Every system has dedicated guidance
4. **Separation of concerns** - Overview vs. individual content

## Creating New Content Modules

To add a new content category (e.g., "classes", "species", "spells"):

1. Create a new directory: `classes/`
2. Copy the four intro files from this template
3. Create `classes/class_types/` for individual class files
4. Update file content to match your new category
5. Add to publication manifests as needed

## Example: Character Classes

```
classes/
├── 00_introduction.md       # "What are classes?"
├── 01_gm_guidelines.md      # "Helping players choose classes"
├── 02_system_integration.md # "How classes work with species and skills"
├── 03_quick_reference.md    # Class comparison table
└── class_types/
    ├── warrior.md           # Full warrior class details
    ├── mage.md              # Full mage class details
    └── rogue.md             # Full rogue class details
```

## Publication Integration

In your manifest, you can include:

```yaml
sections:
  - title: "Character Classes"
    content:
      - file: "classes/00_introduction.md"
      - files_from_directory: "classes/class_types/*.md"
        sort: alphabetical
```

Or for a GM-only guide:

```yaml
sections:
  - title: "Running Classes at Your Table"
    content:
      - file: "classes/01_gm_guidelines.md"
      - file: "classes/02_system_integration.md"
```
