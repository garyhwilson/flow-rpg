# Publication Manifests

Manifests are YAML files that define how to assemble a book from modular source files.

## Basic Structure

```yaml
# Required
title: "Book Title"
output_file: "publications/assembled/book.md"

# Optional
version: "1.0"

# Book content
sections:
  - title: "Section Name"
    content:
      - file: "path/to/file.md"

# Options
options:
  generate_toc: false
  add_page_breaks: false
```

## Content Item Types

### Simple File Include

```yaml
- file: "core_rules/00_introduction.md"
```

### File with Options

```yaml
- file: "core_rules/05_magic.md"
  heading_level_adjust: 1      # Add +1 to all heading levels
  exclude_sections:            # Remove these sections
    - "GM Notes"
    - "Design Commentary"
  rename_to: "The Art of Magic"  # Rename first heading
```

### Section Header

Add a heading without including a file:

```yaml
- section_header: "Part II: Advanced Rules"
```

### Directory Glob

Include multiple files matching a pattern:

```yaml
- files_from_directory: "content_modules/content_types/*.md"
  sort: alphabetical   # or: modified, none
```

## Sections

Sections group related content and add structure:

```yaml
sections:
  - title: "Getting Started"
    intro: "This section covers the basics."
    content:
      - file: "core_rules/00_introduction.md"
      - file: "core_rules/01_basic_mechanics.md"

  - title: "Character Options"
    content:
      - file: "content_modules/00_introduction.md"
      - files_from_directory: "content_modules/content_types/*.md"
```

## Options Reference

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `generate_toc` | boolean | false | Insert table of contents |
| `add_page_breaks` | boolean | false | Add `---` between files |

## File Options Reference

| Option | Type | Description |
|--------|------|-------------|
| `heading_level_adjust` | integer | Add to all heading levels (+1, -1, etc.) |
| `exclude_sections` | list | Section titles to remove |
| `rename_to` | string | New title for first heading |
| `sort` | string | For directory globs: alphabetical, modified, none |

## Example: Multiple Books from Same Source

**Core Rulebook** (everything):
```yaml
title: "Core Rulebook"
sections:
  - title: "Rules"
    content:
      - file: "core_rules/00_introduction.md"
      - file: "core_rules/01_basic_mechanics.md"
  - title: "Options"
    content:
      - files_from_directory: "content_modules/content_types/*.md"
```

**Player's Guide** (excluding GM content):
```yaml
title: "Player's Guide"
sections:
  - title: "Rules"
    content:
      - file: "core_rules/00_introduction.md"
      - file: "core_rules/01_basic_mechanics.md"
        exclude_sections:
          - "GM Notes"
          - "Balance Discussion"
```

**Quick Reference** (just summaries):
```yaml
title: "Quick Reference"
sections:
  - title: "Tables"
    content:
      - file: "content_modules/03_quick_reference.md"
```

## Tips

1. **Start simple** - Begin with just file includes, add options as needed
2. **Test frequently** - Run the assembler after changes
3. **Use meaningful section titles** - They appear in the output
4. **Keep manifests organized** - Comment sections for clarity
