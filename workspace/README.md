# [Your TTRPG System Name]

*A tabletop roleplaying game system.*

## Quick Start

```bash
# Install Python dependencies
pip install -r scripts/requirements.txt

# Assemble a publication
python scripts/assemble_book.py publications/manifests/example_book.yaml

# Validate YAML-Markdown sync
python scripts/validate_yaml_sync.py

# Generate documentation from YAML (optional)
python scripts/generate_docs.py --help
```

## Project Structure

```
├── README.md                   # This file
├── GETTING_STARTED.md          # Detailed workflow guide
├── CLAUDE.md                   # Claude Code instructions
│
├── yaml/                       # YAML source of truth (mechanics)
│   ├── index.yaml             # Master reference
│   └── [system files].yaml    # Your game systems
│
├── core_rules/                 # Core rulebook content (markdown)
├── content_modules/            # Modular content (classes, species, etc.)
│
├── publications/
│   ├── manifests/             # Book assembly definitions
│   ├── templates/             # Reusable content (title pages, etc.)
│   └── assembled/             # Generated output (gitignored)
│
├── templates/
│   ├── generators/            # Jinja2 templates for doc generation
│   └── output/                # Generated output (gitignored)
│
└── scripts/
    ├── assemble_book.py       # Publication assembler
    ├── generate_docs.py       # YAML-to-markdown generator
    └── validate_yaml_sync.py  # Sync validator
```

## Documentation

- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Detailed setup and workflow guide
- **[CLAUDE.md](CLAUDE.md)** - Instructions for Claude Code AI assistant
- **[.claude/instructions.md](.claude/instructions.md)** - Living design document

## Development Workflow

1. **Edit YAML first** for mechanical changes (source of truth)
2. **Update markdown** for narrative content
3. **Run validation** to check sync: `python scripts/validate_yaml_sync.py`
4. **Assemble publications** when ready to review

See [GETTING_STARTED.md](GETTING_STARTED.md) for complete workflow documentation.

## License

[Your license here]
