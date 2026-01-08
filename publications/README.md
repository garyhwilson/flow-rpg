# Flow RPG Publication System

This directory contains the infrastructure for assembling publication-ready books from the modular source files in the `drafts/` directory.

## Overview

The publication system uses:
- **YAML manifests** to define book structure
- **Python script** to assemble books automatically
- **Template files** for front matter
- **Modular source files** from drafts/ directory

## Directory Structure

```
publications/
├── manifests/           # YAML files defining book structure
│   ├── core_rulebook.yaml
│   ├── players_guide.yaml
│   ├── gm_guide.yaml
│   ├── grimoire.yaml
│   ├── monster_manual.yaml
│   └── quick_reference.yaml
├── templates/          # Reusable content (title pages, copyright, etc.)
│   ├── title_page.md
│   ├── copyright.md
│   ├── players_guide_title.md
│   ├── gm_guide_title.md
│   ├── grimoire_title.md
│   └── monster_manual_title.md
├── custom_content/     # Book-specific content not in drafts/
│   └── [book_name]/
└── assembled/          # OUTPUT: Generated books (gitignored)
    ├── core_rulebook.md (899 KB)
    ├── players_guide.md (683 KB)
    ├── gm_guide.md (391 KB)
    ├── grimoire.md (169 KB)
    ├── monster_manual.md (109 KB)
    └── quick_reference.md (84 KB)
```

## Quick Start

### 1. Install Dependencies

The assembly script requires Python 3.6+ and PyYAML:

```bash
pip install pyyaml
```

### 2. Assemble a Book

From the project root directory:

```bash
# Core Rulebook (complete game)
python scripts/assemble_book.py publications/manifests/core_rulebook.yaml

# Player's Guide (player-facing content only)
python scripts/assemble_book.py publications/manifests/players_guide.yaml

# Game Master's Guide (GM-facing content only)
python scripts/assemble_book.py publications/manifests/gm_guide.yaml

# Monster Manual (bestiary and NPC compendium)
python scripts/assemble_book.py publications/manifests/monster_manual.yaml

# Grimoire (magic system deep-dive)
python scripts/assemble_book.py publications/manifests/grimoire.yaml

# Quick Reference (printable reference sheet)
python scripts/assemble_book.py publications/manifests/quick_reference.yaml
```

Assembled books are created in: `publications/assembled/`

### 3. Review the Output

Open the assembled markdown file in your preferred editor or convert it to other formats:

```bash
# Open in default markdown viewer
open publications/assembled/core_rulebook.md

# Or convert to PDF using pandoc (if installed)
pandoc publications/assembled/core_rulebook.md -o publications/assembled/core_rulebook.pdf
```

## Manifest Files

Manifests are YAML files that define how books are assembled. They specify:

1. **Metadata** - Title, version, output filename
2. **Sections** - Ordered list of content to include
3. **Options** - Assembly preferences (TOC generation, page breaks, etc.)

### Example Manifest Structure

```yaml
title: "My Book Title"
version: "1.0"
output_file: "publications/assembled/my_book.md"

sections:
  - title: "Part I: Introduction"
    intro: "Optional introductory text..."
    content:
      - file: "drafts/core_rules/01_introduction.md"
      - file: "drafts/core_rules/02_basics.md"
        heading_level_adjust: 1  # Increase heading levels
        exclude_sections:        # Remove these sections
          - "Advanced Topics"

  - title: "Part II: Character Options"
    content:
      - section_header: "Callings"
      - files_from_directory: "drafts/callings/calling_types/*.md"
        sort: alphabetical

options:
  generate_toc: true
  add_page_breaks: false
```

## Manifest Options

### Content Item Types

**Simple file inclusion:**
```yaml
- file: "path/to/file.md"
```

**File with options:**
```yaml
- file: "path/to/file.md"
  heading_level_adjust: 1      # Adjust heading levels (+ or -)
  exclude_sections:            # Remove specific sections
    - "Section Title to Remove"
  rename_to: "New Title"       # Rename first heading
```

**Section header:**
```yaml
- section_header: "My Section Title"
```

**Directory of files:**
```yaml
- files_from_directory: "path/to/dir/*.md"
  sort: alphabetical           # or 'modified', 'none'
```

### Assembly Options

```yaml
options:
  generate_toc: true          # Auto-generate table of contents
  add_page_breaks: false      # Add --- between sections
  fix_internal_links: false   # Update cross-references (future)
  heading_numbering: false    # Auto-number sections (future)
```

## Creating New Books

### 1. Create a Manifest

Create a new YAML file in `publications/manifests/`:

```bash
# Example: Player's Guide
touch publications/manifests/players_guide.yaml
```

### 2. Define the Book Structure

Edit the manifest to specify what content to include:

```yaml
title: "Flow RPG Player's Guide"
version: "1.0"
output_file: "publications/assembled/players_guide.md"

sections:
  - title: "Front Matter"
    content:
      - file: "publications/templates/title_page.md"

  - title: "Character Creation"
    content:
      - file: "drafts/callings/00_introduction.md"
      # ... etc
```

### 3. Assemble and Review

```bash
python scripts/assemble_book.py publications/manifests/players_guide.yaml
```

## Available Publications

All publications are ready to assemble:

### 1. Core Rulebook (`core_rulebook.yaml`) - 899 KB
**Complete game with everything**
- All core rules
- All character options (callings, archetypes, species)
- Complete magic system
- Monsters & NPCs (complete bestiary)
- Equipment and advancement
- Both player and GM content
- **Audience:** Everyone

### 2. Player's Guide (`players_guide.yaml`) - 683 KB
**Player-focused content only**
- Character creation
- Combat and magic systems
- Equipment
- Advancement
- Quick references
- **Excludes:** GM guidelines, balance discussions, monsters
- **Audience:** Players

### 3. Game Master's Guide (`gm_guide.yaml`) - 391 KB
**GM-focused content only**
- Running all systems
- Complete monster & NPC compendium
- Encounter design
- Flow economy management
- Campaign frameworks
- Balance considerations
- **Audience:** Game Masters

### 4. Monster Manual (`monster_manual.yaml`) - 109 KB
**Bestiary and NPC compendium**
- Named adversaries with motivations and tactics
- Comprehensive NPC templates
- Encounter building guidelines
- Tactical notes for running creatures
- Quick reference tables
- **Audience:** Game Masters

### 5. The Grimoire (`grimoire.yaml`) - 169 KB
**Magic system deep-dive**
- Complete spell system
- All four casting approaches
- Magical traditions
- Tactical spellcasting
- Character examples
- **Audience:** Players and GMs who want magic mastery

### 6. Quick Reference (`quick_reference.yaml`) - 84 KB
**Printable at-table reference**
- All quick reference sections
- Core mechanics summaries
- Combat tables
- Spell lists
- Equipment tables
- **Audience:** At-table lookup during play

## Customization

### Adding Custom Content

For book-specific content not in drafts/:

1. Create directory: `publications/custom_content/[book_name]/`
2. Add markdown files
3. Reference in manifest: `file: "publications/custom_content/[book_name]/intro.md"`

### Modifying Templates

Edit files in `publications/templates/`:
- `title_page.md` - Book title and credits
- `copyright.md` - Copyright and license information

Add new templates as needed.

## Advanced Usage

### Script Options

The assembly script supports various operations:

```python
from scripts.assemble_book import BookAssembler

# Create assembler
assembler = BookAssembler('publications/manifests/core_rulebook.yaml')

# Assemble and get content
content = assembler.assemble()

# Save to file
assembler.save()

# Or save to custom location
assembler.save('custom/output/path.md')
```

### Processing Pipeline

The script performs these operations:

1. **Parse manifest** - Read YAML configuration
2. **Collect files** - Gather all referenced markdown files
3. **Process content**:
   - Adjust heading levels
   - Remove excluded sections
   - Rename headings
4. **Generate TOC** - Create table of contents
5. **Assemble** - Concatenate in specified order
6. **Output** - Write to assembled/ directory

## Workflow

### Development Workflow

1. **Edit modular sources** in `drafts/` directory
2. **Test changes** locally
3. **Regenerate book** when ready to review full document
4. **Iterate** on individual modules
5. **Reassemble** as needed

### Publication Workflow

1. **Finalize content** in drafts/
2. **Update manifest** if structure changed
3. **Assemble book** using script
4. **Review output** for consistency
5. **Convert to PDF** or other formats
6. **Publish** final version

## Troubleshooting

### Common Issues

**"File not found" errors:**
- Check file paths are relative to project root
- Verify files exist in drafts/ directory
- Ensure no typos in manifest

**Heading levels wrong:**
- Use `heading_level_adjust` to fix
- Check source files use proper markdown headings

**Missing sections:**
- Verify all required files are in manifest
- Check `exclude_sections` isn't removing needed content

**Script won't run:**
- Verify Python 3.6+ installed: `python --version`
- Install PyYAML: `pip install pyyaml`
- Make script executable: `chmod +x scripts/assemble_book.py`

## Future Enhancements

Potential additions to the system:

- [ ] Automatic internal link fixing
- [ ] Section numbering
- [ ] Multiple output formats (PDF, HTML, EPUB)
- [ ] Index generation
- [ ] Glossary compilation
- [ ] Cross-reference validation
- [ ] Spell checker integration
- [ ] Automated TOC styling
- [ ] Template variables/substitution

## Support

For questions or issues:
- Check manifest syntax carefully
- Review script output for error messages
- Test with simple manifest first
- Consult example manifests in this directory

---

*This publication system enables efficient management of large TTRPG projects by maintaining modular source files while generating cohesive publication-ready documents.*
