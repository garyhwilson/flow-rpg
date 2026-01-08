# Templates Directory

This directory contains Jinja2 templates for generating markdown documentation from YAML data.

## Structure

```
templates/
├── generators/          # Jinja2 templates for doc generation
│   └── example.jinja   # Example template
└── output/             # Generated markdown (gitignored)
    └── .gitkeep
```

## How It Works

1. **YAML** defines your game mechanics (source of truth)
2. **Jinja2 templates** transform YAML into markdown
3. **generate_docs.py** runs the transformation
4. **Output** is written to `templates/output/`

## When to Use This

Use the generation system when:

- You want mechanical content auto-generated from YAML
- You need consistent formatting across many similar items
- You're iterating rapidly on game mechanics

Write markdown directly when:

- Content is primarily narrative
- Each item needs unique formatting
- You're doing one-off documentation

## Template Syntax

Jinja2 templates use `{{ }}` for variables and `{% %}` for logic:

```jinja
# {{ title }}

{% for item in items %}
## {{ item.name }}

{{ item.description }}

{% endfor %}
```

## Creating a New Template

1. Create `templates/generators/your_template.jinja`
2. Add a generator method to `scripts/generate_docs.py`:

```python
def generate_your_content(self):
    template = self.env.get_template('your_template.jinja')
    data = self.yaml_data.get('your_content', {})
    output = template.render(content=data)
    self._write_output('your_content.md', output)
```

3. Add command line argument:

```python
parser.add_argument('--your-content', action='store_true',
                    help='Generate your content documentation')
```

4. Run: `python scripts/generate_docs.py --your-content`

## Example Workflow

```bash
# Edit YAML data
vim yaml/equipment.yaml

# Regenerate equipment documentation
python scripts/generate_docs.py --equipment

# Review output
cat templates/output/equipment.md
```

## Tips

- Keep templates readable - complex logic should be in Python
- Use template inheritance for common layouts
- Test with small datasets first
- Include comments in templates for maintainability
