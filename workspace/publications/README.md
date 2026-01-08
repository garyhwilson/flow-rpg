# Publication System

This directory contains everything needed to assemble modular markdown files into publication-ready books.

## Overview

```
publications/
├── manifests/           # YAML files defining book structure
│   ├── README.md       # Manifest format documentation
│   └── example_book.yaml
├── templates/           # Reusable content (title pages, etc.)
│   ├── title_page.md
│   └── copyright.md
└── assembled/           # Generated output (gitignored)
    └── .gitkeep
```

## Quick Start

```bash
# Assemble a book from its manifest
python scripts/assemble_book.py publications/manifests/example_book.yaml

# Output appears in publications/assembled/
```

## How It Works

1. **Create a manifest** (YAML) defining your book's structure
2. **Reference source files** from core_rules/, content_modules/, etc.
3. **Run the assembler** to combine everything into one markdown file
4. **Convert to final format** (PDF, HTML, etc.) using your preferred tool

## Creating Different Books

From the same source files, you can create multiple publications:

| Book | Contents | Audience |
|------|----------|----------|
| Core Rulebook | Everything | All readers |
| Player's Guide | Player-focused sections only | Players |
| GM Guide | GM-focused sections only | Game Masters |
| Quick Reference | Tables and summaries | At-table reference |

Each book gets its own manifest that includes the relevant source files.

## Tips

- **Don't duplicate content** - Reference the same source files in multiple manifests
- **Use exclude_sections** - Remove GM content from player books
- **Use heading_level_adjust** - Ensure consistent heading hierarchy across files
- **Use rename_to** - Give sections contextual names per book

See [manifests/README.md](manifests/README.md) for the complete manifest format reference.
