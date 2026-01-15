#!/usr/bin/env python3
"""
Autumn Phoenix RPG Documentation Generator

Generates markdown documentation from YAML source files using Jinja2 templates.
Enables rapid iteration on game mechanics while maintaining narrative context.

Usage:
    python generate_docs.py --all              # Generate all documentation
    python generate_docs.py --validate         # Validate YAML consistency

    # Character Creation
    python generate_docs.py --callings         # Generate calling docs
    python generate_docs.py --species          # Generate species docs
    python generate_docs.py --archetypes       # Generate archetype docs

    # Equipment
    python generate_docs.py --armor            # Generate armor docs
    python generate_docs.py --weapons          # Generate weapon docs
    python generate_docs.py --shields          # Generate shield docs
    python generate_docs.py --gear-kits        # Generate gear kits
    python generate_docs.py --consumables      # Generate consumables
    python generate_docs.py --magic-items      # Generate magic items
    python generate_docs.py --equipment-bonding      # Generate equipment bonding
    python generate_docs.py --signature-equipment    # Generate signature equipment
    python generate_docs.py --equipment-quality      # Generate equipment quality
    python generate_docs.py --tools-utilities        # Generate tools & utilities

    # Magic
    python generate_docs.py --spells           # Generate spell docs
    python generate_docs.py --spell-combinations     # Generate spell combos
    python generate_docs.py --ritual-magic           # Generate ritual magic
    python generate_docs.py --metamagic              # Generate metamagic
    python generate_docs.py --magic-crafting         # Generate magic crafting

    # Progression
    python generate_docs.py --edges            # Generate edges
    python generate_docs.py --milestones       # Generate milestones
    python generate_docs.py --signature-moves        # Generate signature moves
    python generate_docs.py --advanced-techniques    # Generate advanced techniques
    python generate_docs.py --legendary-techniques   # Generate legendary techniques

    # Combat
    python generate_docs.py --stances          # Generate stances
    python generate_docs.py --techniques       # Generate techniques
    python generate_docs.py --signature-combat       # Generate signature combat
    python generate_docs.py --environmental-combat   # Generate environmental combat
    python generate_docs.py --social-combat          # Generate social combat

    # Core Rules
    python generate_docs.py --skill-list             # Generate skill list
    python generate_docs.py --target-numbers         # Generate target numbers
    python generate_docs.py --advantage-disadvantage # Generate advantage/disadvantage

    # GM Tools
    python generate_docs.py --npc-generator    # Generate NPC generator
    python generate_docs.py --enemy-templates  # Generate enemy templates
    python generate_docs.py --encounters       # Generate encounters
    python generate_docs.py --npc-templates    # Generate NPC templates
    python generate_docs.py --random-tables          # Generate random tables
    python generate_docs.py --campaign-tracker       # Generate campaign tracker
"""

import argparse
import sys
from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from typing import Dict, Any, List

# Path configuration
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
YAML_DIR = PROJECT_ROOT / 'yaml'
TEMPLATE_DIR = PROJECT_ROOT / 'templates'
OUTPUT_DIR = TEMPLATE_DIR / 'output'

class FlowRPGGenerator:
    """Main generator class for Autumn Phoenix RPG documentation."""

    def __init__(self):
        """Initialize the generator with Jinja2 environment."""
        self.yaml_data = {}
        self.env = Environment(
            loader=FileSystemLoader(TEMPLATE_DIR / 'generators'),
            autoescape=select_autoescape(),
            trim_blocks=True,
            lstrip_blocks=True
        )

        # Ensure output directory exists
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    def load_yaml(self, filename: str) -> Dict[str, Any]:
        """Load a YAML file and return parsed data."""
        yaml_path = YAML_DIR / filename
        if not yaml_path.exists():
            print(f"⚠️  Warning: {filename} not found at {yaml_path}")
            return {}

        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        print(f"✓ Loaded {filename}")
        return data

    def load_all_yaml(self):
        """Load all YAML files."""
        yaml_files = [
            'core_rules.yaml',
            'character.yaml',
            'combat.yaml',
            'magic.yaml',
            'advancement.yaml',
            'equipment.yaml',
            'gm_tools.yaml',
            'examples.yaml',
            'index.yaml'
        ]

        for filename in yaml_files:
            key = filename.replace('.yaml', '')
            self.yaml_data[key] = self.load_yaml(filename)

    def validate_yaml(self) -> bool:
        """Validate YAML data for consistency."""
        print("\n🔍 Validating YAML data...")
        errors = []
        warnings = []

        # Check if character.yaml exists and has callings
        if 'character' in self.yaml_data:
            char_data = self.yaml_data['character']

            # Validate callings exist
            if 'callings' in char_data:
                callings = char_data['callings']
                expected_count = 9
                actual_count = len(callings)

                if actual_count != expected_count:
                    warnings.append(
                        f"Expected {expected_count} callings, found {actual_count}"
                    )

                # Validate each calling has required fields
                for calling_name, calling_data in callings.items():
                    if 'momentum_benefit' not in calling_data:
                        errors.append(
                            f"Calling '{calling_name}' missing momentum_benefit"
                        )
                    elif not isinstance(calling_data['momentum_benefit'], dict):
                        errors.append(
                            f"Calling '{calling_name}' momentum_benefit must be a dict"
                        )
                    else:
                        benefit = calling_data['momentum_benefit']
                        required_fields = ['name', 'trigger', 'effect']
                        for field in required_fields:
                            if field not in benefit:
                                errors.append(
                                    f"Calling '{calling_name}' momentum_benefit missing '{field}'"
                                )

        # Check equipment armor data
        if 'equipment' in self.yaml_data:
            equip_data = self.yaml_data['equipment']
            if 'armor' in equip_data and 'types' in equip_data['armor']:
                armor = equip_data['armor']['types']
                expected_types = ['no_armor', 'light_armor', 'medium_armor', 'heavy_armor']

                for armor_type in expected_types:
                    if armor_type not in armor:
                        errors.append(f"Missing armor type: {armor_type}")
                    elif armor_type != 'no_armor':
                        # Validate required fields
                        armor_data = armor[armor_type]
                        required = ['damage_reduction', 'cost']
                        for field in required:
                            if field not in armor_data:
                                errors.append(
                                    f"Armor '{armor_type}' missing '{field}'"
                                )

        # Print results
        if errors:
            print("\n❌ Validation Errors:")
            for error in errors:
                print(f"   • {error}")

        if warnings:
            print("\n⚠️  Validation Warnings:")
            for warning in warnings:
                print(f"   • {warning}")

        if not errors and not warnings:
            print("✓ All validations passed!")
            return True
        elif not errors:
            print("✓ Validation passed with warnings")
            return True
        else:
            print("\n❌ Validation failed")
            return False

    def generate_callings(self):
        """Generate calling documentation from YAML."""
        print("\n📝 Generating calling documentation...")

        if 'character' not in self.yaml_data:
            print("⚠️  No character data loaded")
            return

        callings = self.yaml_data['character'].get('callings', {})
        if not callings:
            print("⚠️  No calling data found")
            return

        # Load template
        try:
            template = self.env.get_template('callings.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            print("   Skipping calling generation (template will be created in Phase 3)")
            return

        # Generate markdown
        output = template.render(callings=callings)

        # Write to file
        output_path = OUTPUT_DIR / 'calling_mechanics.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated calling documentation: {output_path}")
        print(f"  ({len(callings)} callings processed)")

    def generate_armor(self):
        """Generate armor documentation from YAML."""
        print("\n📝 Generating armor documentation...")

        if 'equipment' not in self.yaml_data:
            print("⚠️  No equipment data loaded")
            return

        armor_data = self.yaml_data['equipment'].get('armor', {})
        armor_types = armor_data.get('types', {})
        if not armor_types:
            print("⚠️  No armor data found")
            return

        # Load template
        try:
            template = self.env.get_template('armor.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            print("   Skipping armor generation (template will be created in Phase 3)")
            return

        # Generate markdown
        output = template.render(armor_types=armor_types)

        # Write to file
        output_path = OUTPUT_DIR / 'armor_mechanics.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated armor documentation: {output_path}")
        print(f"  ({len(armor_types)} armor types processed)")

    def generate_spells(self):
        """Generate spell documentation from YAML."""
        print("\n📝 Generating spell documentation...")

        if 'magic' not in self.yaml_data:
            print("⚠️  No magic data loaded")
            return

        spell_tiers = self.yaml_data['magic'].get('spell_tiers', {})
        if not spell_tiers:
            print("⚠️  No spell tier data found")
            return

        # Load template
        try:
            template = self.env.get_template('spells.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            print("   Skipping spell generation (template will be created in Phase 3)")
            return

        # Generate markdown
        output = template.render(spell_tiers=spell_tiers)

        # Write to file
        output_path = OUTPUT_DIR / 'spell_mechanics.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated spell documentation: {output_path}")
        print(f"  ({len(spell_tiers)} spell tiers processed)")

    def generate_species(self):
        """Generate species documentation from YAML."""
        print("\n📝 Generating species documentation...")

        if 'character' not in self.yaml_data:
            print("⚠️  No character data loaded")
            return

        species_data = self.yaml_data['character'].get('species', {})
        if not species_data:
            print("⚠️  No species data found")
            return

        # Filter out non-species entries (like design_note)
        filtered_species = {
            key: value for key, value in species_data.items()
            if isinstance(value, dict) and 'name' in value
        }

        if not filtered_species:
            print("⚠️  No valid species data found")
            return

        # Load template
        try:
            template = self.env.get_template('species.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            print("   Skipping species generation (template will be created in Phase 5)")
            return

        # Generate markdown
        output = template.render(species_data=filtered_species)

        # Write to file
        output_path = OUTPUT_DIR / 'species_mechanics.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated species documentation: {output_path}")
        print(f"  ({len(filtered_species)} species processed)")

    def generate_archetypes(self):
        """Generate archetype documentation from YAML."""
        print("\n📝 Generating archetype documentation...")

        if 'character' not in self.yaml_data:
            print("⚠️  No character data loaded")
            return

        archetypes = self.yaml_data['character'].get('archetypes', {})
        if not archetypes:
            print("⚠️  No archetype data found")
            return

        # Filter out non-archetype entries (like design_note)
        filtered_archetypes = {
            key: value for key, value in archetypes.items()
            if isinstance(value, dict) and 'name' in value
        }

        if not filtered_archetypes:
            print("⚠️  No valid archetype data found")
            return

        # Load template
        try:
            template = self.env.get_template('archetypes.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            print("   Skipping archetype generation (template will be created in Phase 5)")
            return

        # Generate markdown
        output = template.render(archetypes=filtered_archetypes)

        # Write to file
        output_path = OUTPUT_DIR / 'archetype_mechanics.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated archetype documentation: {output_path}")
        print(f"  ({len(filtered_archetypes)} archetypes processed)")

    def generate_weapons(self):
        """Generate weapon documentation from YAML."""
        print("\n📝 Generating weapon documentation...")

        if 'equipment' not in self.yaml_data:
            print("⚠️  No equipment data loaded")
            return

        weapons = self.yaml_data['equipment'].get('weapons', {})
        if not weapons:
            print("⚠️  No weapon data found")
            return

        # Load template
        try:
            template = self.env.get_template('weapons.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            print("   Skipping weapon generation (template will be created in Phase 5)")
            return

        # Generate markdown
        output = template.render(weapons=weapons)

        # Write to file
        output_path = OUTPUT_DIR / 'weapon_mechanics.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated weapon documentation: {output_path}")
        weapon_count = sum(len(cat.get('examples', {})) for cat in weapons.get('categories', {}).values())
        print(f"  ({weapon_count} weapons in {len(weapons.get('categories', {}))} categories)")

    def generate_edges(self):
        """Generate edges documentation from YAML."""
        print("\n📝 Generating edges documentation...")

        if 'advancement' not in self.yaml_data:
            print("⚠️  No advancement data loaded")
            return

        edges_data = self.yaml_data['advancement'].get('edges_system', {})
        advancement_data = self.yaml_data['advancement']

        if not edges_data:
            print("⚠️  No edges data found")
            return

        try:
            template = self.env.get_template('edges.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(edges_data=edges_data, advancement_data=advancement_data)
        output_path = OUTPUT_DIR / 'edges_mechanics.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated edges documentation: {output_path}")

    def generate_milestones(self):
        """Generate advancement documentation from YAML."""
        print("\n📝 Generating advancement documentation...")

        if 'advancement' not in self.yaml_data:
            print("⚠️  No advancement data loaded")
            return

        advancement_data = self.yaml_data['advancement']

        try:
            template = self.env.get_template('milestones.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(advancement_data=advancement_data)
        output_path = OUTPUT_DIR / 'advancement_mechanics.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated advancement documentation: {output_path}")

    def generate_stances(self):
        """Generate stances documentation from YAML."""
        print("\n📝 Generating stances documentation...")

        if 'combat' not in self.yaml_data:
            print("⚠️  No combat data loaded")
            return

        stances = self.yaml_data['combat'].get('stances', {})

        if not stances:
            print("⚠️  No stances data found")
            return

        try:
            template = self.env.get_template('stances.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(stances=stances)
        output_path = OUTPUT_DIR / 'stances_mechanics.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated stances documentation: {output_path}")
        print(f"  ({len(stances)} stances processed)")

    def generate_techniques(self):
        """Generate combat techniques documentation from YAML."""
        print("\n📝 Generating combat techniques documentation...")

        if 'combat' not in self.yaml_data:
            print("⚠️  No combat data loaded")
            return

        techniques = self.yaml_data['combat'].get('combat_techniques', {})

        if not techniques:
            print("⚠️  No techniques data found")
            return

        try:
            template = self.env.get_template('techniques.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(techniques=techniques)
        output_path = OUTPUT_DIR / 'techniques_mechanics.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated techniques documentation: {output_path}")

    def generate_shields(self):
        """Generate shields documentation from YAML."""
        print("\n📝 Generating shields documentation...")

        if 'equipment' not in self.yaml_data:
            print("⚠️  No equipment data loaded")
            return

        armor_data = self.yaml_data['equipment'].get('armor', {})
        shields = armor_data.get('shields', {})

        if not shields:
            print("⚠️  No shields data found")
            return

        try:
            template = self.env.get_template('shields.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(shields=shields)
        output_path = OUTPUT_DIR / 'shields_mechanics.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated shields documentation: {output_path}")
        print(f"  ({len(shields)} shield types processed)")

    def generate_gear_kits(self):
        """Generate adventuring gear kits documentation from YAML."""
        print("\n📝 Generating gear kits documentation...")

        if 'equipment' not in self.yaml_data:
            print("⚠️  No equipment data loaded")
            return

        gear_data = self.yaml_data['equipment'].get('adventuring_gear', {})
        kits = gear_data.get('kits', {})

        if not kits:
            print("⚠️  No gear kits data found")
            return

        try:
            template = self.env.get_template('gear_kits.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(kits=kits)
        output_path = OUTPUT_DIR / 'gear_kits_mechanics.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated gear kits documentation: {output_path}")
        print(f"  ({len(kits)} kits processed)")

    def generate_consumables(self):
        """Generate consumables documentation from YAML."""
        print("\n📝 Generating consumables documentation...")

        if 'equipment' not in self.yaml_data:
            print("⚠️  No equipment data loaded")
            return

        gear_data = self.yaml_data['equipment'].get('adventuring_gear', {})
        consumables = gear_data.get('consumables', {})

        if not consumables:
            print("⚠️  No consumables data found")
            return

        try:
            template = self.env.get_template('consumables.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(consumables=consumables)
        output_path = OUTPUT_DIR / 'consumables_mechanics.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated consumables documentation: {output_path}")
        print(f"  ({len(consumables)} consumable types processed)")

    def generate_magic_items(self):
        """Generate magic items documentation from YAML."""
        print("\n📝 Generating magic items documentation...")

        if 'equipment' not in self.yaml_data:
            print("⚠️  No equipment data loaded")
            return

        magic_items = self.yaml_data['equipment'].get('magic_items', {})

        if not magic_items:
            print("⚠️  No magic items data found")
            return

        try:
            template = self.env.get_template('magic_items.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(
            rarity_tiers=magic_items.get('rarity_tiers', {}),
            enhancement_bonuses=magic_items.get('enhancement_bonuses', {}),
            weapon_properties=magic_items.get('weapon_properties', {}),
            armor_properties=magic_items.get('armor_properties', {})
        )
        output_path = OUTPUT_DIR / 'magic_items_mechanics.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated magic items documentation: {output_path}")

    def generate_npc_generator(self):
        """Generate NPC generator documentation from YAML."""
        print("\n📝 Generating NPC generator documentation...")

        if 'gm_tools' not in self.yaml_data:
            print("⚠️  No GM tools data loaded")
            return

        npc_data = self.yaml_data['gm_tools'].get('npc_generation', {})

        if not npc_data:
            print("⚠️  No NPC generation data found")
            return

        try:
            template = self.env.get_template('npc_generator.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(npc_data=npc_data)
        output_path = OUTPUT_DIR / 'npc_generator.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated NPC generator documentation: {output_path}")

    def generate_enemy_templates(self):
        """Generate enemy templates documentation from YAML."""
        print("\n📝 Generating enemy templates documentation...")

        if 'gm_tools' not in self.yaml_data:
            print("⚠️  No GM tools data loaded")
            return

        scene_data = self.yaml_data['gm_tools'].get('scene_design', {})
        enemy_templates = scene_data.get('enemy_templates', {})

        if not enemy_templates:
            print("⚠️  No enemy templates data found")
            return

        try:
            template = self.env.get_template('enemy_templates.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(enemy_templates=enemy_templates)
        output_path = OUTPUT_DIR / 'enemy_templates.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated enemy templates documentation: {output_path}")
        print(f"  ({len(enemy_templates)} template types processed)")

    def generate_encounters(self):
        """Generate encounters documentation from YAML."""
        print("\n📝 Generating encounters documentation...")

        if 'gm_tools' not in self.yaml_data:
            print("⚠️  No GM tools data loaded")
            return

        scene_data = self.yaml_data['gm_tools'].get('scene_design', {})
        opposition_types = scene_data.get('opposition_types', {})

        if not opposition_types:
            print("⚠️  No opposition types data found")
            return

        try:
            template = self.env.get_template('encounters.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(encounter_composition=opposition_types)
        output_path = OUTPUT_DIR / 'encounters.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated encounters documentation: {output_path}")

    def generate_npc_templates(self):
        """Generate NPC templates reference documentation."""
        print("\n📝 Generating NPC templates reference documentation...")

        try:
            template = self.env.get_template('npc_templates.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render()
        output_path = OUTPUT_DIR / 'npc_templates_reference.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated NPC templates reference documentation: {output_path}")

    def generate_signature_moves(self):
        """Generate signature moves documentation from YAML."""
        print("\n📝 Generating signature moves documentation...")

        if 'advancement' not in self.yaml_data:
            print("⚠️  No advancement data loaded")
            return

        advancement_data = self.yaml_data['advancement']
        # Signature moves are now part of the advance menu options
        signature_moves = advancement_data.get('advance_menu', {}).get('options', {}).get('signature_move', {})

        try:
            template = self.env.get_template('signature_moves.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(signature_moves=signature_moves, advancement_data=advancement_data)
        output_path = OUTPUT_DIR / 'signature_moves.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated signature moves documentation: {output_path}")

    def generate_advanced_techniques(self):
        """Generate advanced techniques documentation from YAML."""
        print("\n📝 Generating advanced techniques documentation...")

        if 'advancement' not in self.yaml_data:
            print("⚠️  No advancement data loaded")
            return

        advancement_data = self.yaml_data['advancement']

        try:
            template = self.env.get_template('advanced_techniques.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(advancement_data=advancement_data)
        output_path = OUTPUT_DIR / 'advanced_techniques.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated advanced techniques documentation: {output_path}")

    def generate_legendary_techniques(self):
        """Generate legendary techniques documentation from YAML."""
        print("\n📝 Generating legendary techniques documentation...")

        if 'advancement' not in self.yaml_data:
            print("⚠️  No advancement data loaded")
            return

        advancement_data = self.yaml_data['advancement']

        try:
            template = self.env.get_template('legendary_techniques.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(advancement_data=advancement_data)
        output_path = OUTPUT_DIR / 'legendary_techniques.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated legendary techniques documentation: {output_path}")

    def generate_signature_combat(self):
        """Generate signature combat reference documentation."""
        print("\n📝 Generating signature combat reference documentation...")

        try:
            template = self.env.get_template('signature_combat.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render()
        output_path = OUTPUT_DIR / 'signature_combat_reference.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated signature combat reference documentation: {output_path}")

    def generate_environmental_combat(self):
        """Generate environmental combat documentation from YAML."""
        print("\n📝 Generating environmental combat documentation...")

        if 'combat' not in self.yaml_data:
            print("⚠️  No combat data loaded")
            return

        combat_data = self.yaml_data['combat']
        environmental_data = combat_data.get('environmental_hazards', {})

        try:
            template = self.env.get_template('environmental_combat.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(environmental_data=environmental_data, combat_data=combat_data)
        output_path = OUTPUT_DIR / 'environmental_combat.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated environmental combat documentation: {output_path}")

    def generate_equipment_bonding(self):
        """Generate equipment bonding documentation from YAML."""
        print("\n📝 Generating equipment bonding documentation...")

        if 'equipment' not in self.yaml_data:
            print("⚠️  No equipment data loaded")
            return

        equipment_data = self.yaml_data['equipment']
        bonding_data = equipment_data.get('equipment_bonding', {})

        try:
            template = self.env.get_template('equipment_bonding.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(bonding_data=bonding_data, equipment_data=equipment_data)
        output_path = OUTPUT_DIR / 'equipment_bonding.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated equipment bonding documentation: {output_path}")

    def generate_signature_equipment(self):
        """Generate signature equipment documentation from YAML."""
        print("\n📝 Generating signature equipment documentation...")

        if 'equipment' not in self.yaml_data:
            print("⚠️  No equipment data loaded")
            return

        equipment_data = self.yaml_data['equipment']
        signature_data = equipment_data.get('signature_items', {})

        try:
            template = self.env.get_template('signature_equipment.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(signature_data=signature_data, equipment_data=equipment_data)
        output_path = OUTPUT_DIR / 'signature_equipment.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated signature equipment documentation: {output_path}")

    def generate_equipment_quality(self):
        """Generate equipment quality documentation from YAML."""
        print("\n📝 Generating equipment quality documentation...")

        if 'equipment' not in self.yaml_data:
            print("⚠️  No equipment data loaded")
            return

        equipment_data = self.yaml_data['equipment']
        quality_data = equipment_data.get('quality_tiers', {})

        try:
            template = self.env.get_template('equipment_quality.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(quality_data=quality_data, equipment_data=equipment_data)
        output_path = OUTPUT_DIR / 'equipment_quality.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated equipment quality documentation: {output_path}")

    def generate_tools_utilities(self):
        """Generate tools and utilities documentation from YAML."""
        print("\n📝 Generating tools and utilities documentation...")

        if 'equipment' not in self.yaml_data:
            print("⚠️  No equipment data loaded")
            return

        gear_data = self.yaml_data['equipment'].get('adventuring_gear', {})
        tools_data = gear_data.get('tools', {})

        try:
            template = self.env.get_template('tools_utilities.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(tools_data=tools_data, gear_data=gear_data)
        output_path = OUTPUT_DIR / 'tools_utilities.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated tools and utilities documentation: {output_path}")

    def generate_random_tables(self):
        """Generate random tables documentation from YAML."""
        print("\n📝 Generating random tables documentation...")

        if 'gm_tools' not in self.yaml_data:
            print("⚠️  No GM tools data loaded")
            return

        gm_data = self.yaml_data['gm_tools']
        random_data = gm_data.get('random_generation', {})

        try:
            template = self.env.get_template('random_tables.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(random_data=random_data, gm_data=gm_data)
        output_path = OUTPUT_DIR / 'random_tables.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated random tables documentation: {output_path}")

    def generate_target_numbers(self):
        """Generate target numbers documentation from YAML."""
        print("\n📝 Generating target numbers documentation...")

        if 'core_rules' not in self.yaml_data:
            print("⚠️  No core rules data loaded")
            return

        core_data = self.yaml_data['core_rules']
        target_data = core_data.get('target_numbers', {})

        try:
            template = self.env.get_template('target_numbers.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(target_data=target_data, core_data=core_data)
        output_path = OUTPUT_DIR / 'target_numbers.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated target numbers documentation: {output_path}")

    def generate_advantage_disadvantage(self):
        """Generate advantage/disadvantage documentation from YAML."""
        print("\n📝 Generating advantage/disadvantage documentation...")

        if 'core_rules' not in self.yaml_data:
            print("⚠️  No core rules data loaded")
            return

        core_data = self.yaml_data['core_rules']
        modifier_data = core_data.get('modifiers', {})

        try:
            template = self.env.get_template('advantage_disadvantage.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(modifier_data=modifier_data, core_data=core_data)
        output_path = OUTPUT_DIR / 'advantage_disadvantage.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated advantage/disadvantage documentation: {output_path}")

    def generate_spell_combinations(self):
        """Generate spell combinations documentation from YAML."""
        print("\n📝 Generating spell combinations documentation...")

        if 'magic' not in self.yaml_data:
            print("⚠️  No magic data loaded")
            return

        magic_data = self.yaml_data['magic']
        combo_data = magic_data.get('tactical_casting', {})

        try:
            template = self.env.get_template('spell_combinations.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(combo_data=combo_data, magic_data=magic_data)
        output_path = OUTPUT_DIR / 'spell_combinations.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated spell combinations documentation: {output_path}")

    def generate_ritual_magic(self):
        """Generate ritual magic documentation from YAML."""
        print("\n📝 Generating ritual magic documentation...")

        if 'magic' not in self.yaml_data:
            print("⚠️  No magic data loaded")
            return

        magic_data = self.yaml_data['magic']
        ritual_data = magic_data.get('ritual_casting', {})

        try:
            template = self.env.get_template('ritual_magic.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(ritual_data=ritual_data, magic_data=magic_data)
        output_path = OUTPUT_DIR / 'ritual_magic.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated ritual magic documentation: {output_path}")

    def generate_metamagic(self):
        """Generate metamagic documentation from YAML."""
        print("\n📝 Generating metamagic documentation...")

        if 'magic' not in self.yaml_data:
            print("⚠️  No magic data loaded")
            return

        magic_data = self.yaml_data['magic']
        metamagic_data = magic_data.get('metamagic_options', {})

        try:
            template = self.env.get_template('metamagic.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(metamagic_data=metamagic_data, magic_data=magic_data)
        output_path = OUTPUT_DIR / 'metamagic.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated metamagic documentation: {output_path}")

    def generate_social_combat(self):
        """Generate social combat documentation from YAML."""
        print("\n📝 Generating social combat documentation...")

        if 'combat' not in self.yaml_data:
            print("⚠️  No combat data loaded")
            return

        combat_data = self.yaml_data['combat']
        social_data = combat_data.get('social_combat', {})

        try:
            template = self.env.get_template('social_combat.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(social_data=social_data, combat_data=combat_data)
        output_path = OUTPUT_DIR / 'social_combat.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated social combat documentation: {output_path}")

    def generate_campaign_tracker(self):
        """Generate campaign tracker documentation from YAML."""
        print("\n📝 Generating campaign tracker documentation...")

        if 'gm_tools' not in self.yaml_data:
            print("⚠️  No GM tools data loaded")
            return

        gm_data = self.yaml_data['gm_tools']
        tracker_data = gm_data.get('campaign_tracking', {})

        try:
            template = self.env.get_template('campaign_tracker.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(tracker_data=tracker_data, gm_data=gm_data)
        output_path = OUTPUT_DIR / 'campaign_tracker.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated campaign tracker documentation: {output_path}")

    def generate_skill_list(self):
        """Generate skill list documentation from YAML."""
        print("\n📝 Generating skill list documentation...")

        if 'core_rules' not in self.yaml_data:
            print("⚠️  No core rules data loaded")
            return

        core_data = self.yaml_data['core_rules']
        skills_data = core_data.get('skills', {})

        try:
            template = self.env.get_template('skill_list.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(skills_data=skills_data, core_data=core_data)
        output_path = OUTPUT_DIR / 'skill_list.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated skill list documentation: {output_path}")

    def generate_magic_crafting(self):
        """Generate magic item crafting documentation from YAML."""
        print("\n📝 Generating magic item crafting documentation...")

        if 'magic' not in self.yaml_data:
            print("⚠️  No magic data loaded")
            return

        magic_data = self.yaml_data['magic']
        crafting_data = magic_data.get('item_crafting', {})

        try:
            template = self.env.get_template('magic_crafting.jinja')
        except Exception as e:
            print(f"⚠️  Template not found: {e}")
            return

        output = template.render(crafting_data=crafting_data, magic_data=magic_data)
        output_path = OUTPUT_DIR / 'magic_crafting.md'
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"✓ Generated magic item crafting documentation: {output_path}")

    def generate_all(self):
        """Generate all documentation."""
        print("\n🚀 Generating all documentation...")
        # Character Creation
        self.generate_callings()
        self.generate_species()
        self.generate_archetypes()
        # Equipment
        self.generate_armor()
        self.generate_weapons()
        self.generate_shields()
        self.generate_gear_kits()
        self.generate_consumables()
        self.generate_magic_items()
        self.generate_equipment_bonding()
        self.generate_signature_equipment()
        self.generate_equipment_quality()
        self.generate_tools_utilities()
        # Magic
        self.generate_spells()
        self.generate_spell_combinations()
        self.generate_ritual_magic()
        self.generate_metamagic()
        self.generate_magic_crafting()
        # Progression
        self.generate_edges()
        self.generate_milestones()
        self.generate_signature_moves()
        self.generate_advanced_techniques()
        self.generate_legendary_techniques()
        # Combat
        self.generate_stances()
        self.generate_techniques()
        self.generate_signature_combat()
        self.generate_environmental_combat()
        self.generate_social_combat()
        # Core Rules
        self.generate_skill_list()
        self.generate_target_numbers()
        self.generate_advantage_disadvantage()
        # GM Tools
        self.generate_npc_generator()
        self.generate_enemy_templates()
        self.generate_encounters()
        self.generate_npc_templates()
        self.generate_random_tables()
        self.generate_campaign_tracker()
        print("\n✅ All documentation generated!")


def main():
    """Main entry point for the generator."""
    parser = argparse.ArgumentParser(
        description='Generate Autumn Phoenix RPG documentation from YAML sources'
    )
    parser.add_argument(
        '--all', action='store_true',
        help='Generate all documentation'
    )
    parser.add_argument(
        '--callings', action='store_true',
        help='Generate calling documentation'
    )
    parser.add_argument(
        '--species', action='store_true',
        help='Generate species documentation'
    )
    parser.add_argument(
        '--archetypes', action='store_true',
        help='Generate archetype documentation'
    )
    parser.add_argument(
        '--armor', action='store_true',
        help='Generate armor documentation'
    )
    parser.add_argument(
        '--weapons', action='store_true',
        help='Generate weapon documentation'
    )
    parser.add_argument(
        '--spells', action='store_true',
        help='Generate spell documentation'
    )
    parser.add_argument(
        '--shields', action='store_true',
        help='Generate shield documentation'
    )
    parser.add_argument(
        '--gear-kits', action='store_true',
        help='Generate gear kits documentation'
    )
    parser.add_argument(
        '--consumables', action='store_true',
        help='Generate consumables documentation'
    )
    parser.add_argument(
        '--magic-items', action='store_true',
        help='Generate magic items documentation'
    )
    parser.add_argument(
        '--edges', action='store_true',
        help='Generate edges documentation'
    )
    parser.add_argument(
        '--milestones', action='store_true',
        help='Generate milestones documentation'
    )
    parser.add_argument(
        '--stances', action='store_true',
        help='Generate stances documentation'
    )
    parser.add_argument(
        '--techniques', action='store_true',
        help='Generate combat techniques documentation'
    )
    parser.add_argument(
        '--npc-generator', action='store_true',
        help='Generate NPC generator documentation'
    )
    parser.add_argument(
        '--enemy-templates', action='store_true',
        help='Generate enemy templates documentation'
    )
    parser.add_argument(
        '--encounters', action='store_true',
        help='Generate encounters documentation'
    )
    parser.add_argument(
        '--npc-templates', action='store_true',
        help='Generate NPC templates reference documentation'
    )
    parser.add_argument(
        '--signature-moves', action='store_true',
        help='Generate signature moves documentation'
    )
    parser.add_argument(
        '--advanced-techniques', action='store_true',
        help='Generate advanced techniques documentation'
    )
    parser.add_argument(
        '--legendary-techniques', action='store_true',
        help='Generate legendary techniques documentation'
    )
    parser.add_argument(
        '--signature-combat', action='store_true',
        help='Generate signature combat reference'
    )
    parser.add_argument(
        '--environmental-combat', action='store_true',
        help='Generate environmental combat documentation'
    )
    parser.add_argument(
        '--equipment-bonding', action='store_true',
        help='Generate equipment bonding documentation'
    )
    parser.add_argument(
        '--signature-equipment', action='store_true',
        help='Generate signature equipment documentation'
    )
    parser.add_argument(
        '--equipment-quality', action='store_true',
        help='Generate equipment quality documentation'
    )
    parser.add_argument(
        '--tools-utilities', action='store_true',
        help='Generate tools and utilities documentation'
    )
    parser.add_argument(
        '--random-tables', action='store_true',
        help='Generate random tables documentation'
    )
    parser.add_argument(
        '--target-numbers', action='store_true',
        help='Generate target numbers documentation'
    )
    parser.add_argument(
        '--advantage-disadvantage', action='store_true',
        help='Generate advantage/disadvantage documentation'
    )
    parser.add_argument(
        '--spell-combinations', action='store_true',
        help='Generate spell combinations documentation'
    )
    parser.add_argument(
        '--ritual-magic', action='store_true',
        help='Generate ritual magic documentation'
    )
    parser.add_argument(
        '--metamagic', action='store_true',
        help='Generate metamagic documentation'
    )
    parser.add_argument(
        '--social-combat', action='store_true',
        help='Generate social combat documentation'
    )
    parser.add_argument(
        '--campaign-tracker', action='store_true',
        help='Generate campaign tracker documentation'
    )
    parser.add_argument(
        '--skill-list', action='store_true',
        help='Generate skill list documentation'
    )
    parser.add_argument(
        '--magic-crafting', action='store_true',
        help='Generate magic item crafting documentation'
    )
    parser.add_argument(
        '--validate', action='store_true',
        help='Validate YAML consistency'
    )

    args = parser.parse_args()

    # Show help if no arguments
    if not any(vars(args).values()):
        parser.print_help()
        return

    # Initialize generator
    print("🎲 Autumn Phoenix RPG Documentation Generator")
    print("=" * 50)
    generator = FlowRPGGenerator()

    # Load YAML data
    print("\n📂 Loading YAML files...")
    generator.load_all_yaml()

    # Run validation if requested
    if args.validate or args.all:
        if not generator.validate_yaml():
            print("\n⚠️  Continuing despite validation errors...")

    # Generate documentation
    if args.all:
        generator.generate_all()
    else:
        if args.callings:
            generator.generate_callings()
        if args.species:
            generator.generate_species()
        if args.archetypes:
            generator.generate_archetypes()
        if args.armor:
            generator.generate_armor()
        if args.weapons:
            generator.generate_weapons()
        if args.shields:
            generator.generate_shields()
        if getattr(args, 'gear_kits', False):
            generator.generate_gear_kits()
        if args.consumables:
            generator.generate_consumables()
        if getattr(args, 'magic_items', False):
            generator.generate_magic_items()
        if args.spells:
            generator.generate_spells()
        if args.edges:
            generator.generate_edges()
        if args.milestones:
            generator.generate_milestones()
        if args.stances:
            generator.generate_stances()
        if args.techniques:
            generator.generate_techniques()
        if getattr(args, 'npc_generator', False):
            generator.generate_npc_generator()
        if getattr(args, 'enemy_templates', False):
            generator.generate_enemy_templates()
        if args.encounters:
            generator.generate_encounters()
        if getattr(args, 'npc_templates', False):
            generator.generate_npc_templates()
        if getattr(args, 'signature_moves', False):
            generator.generate_signature_moves()
        if getattr(args, 'advanced_techniques', False):
            generator.generate_advanced_techniques()
        if getattr(args, 'legendary_techniques', False):
            generator.generate_legendary_techniques()
        if getattr(args, 'signature_combat', False):
            generator.generate_signature_combat()
        if getattr(args, 'environmental_combat', False):
            generator.generate_environmental_combat()
        if getattr(args, 'equipment_bonding', False):
            generator.generate_equipment_bonding()
        if getattr(args, 'signature_equipment', False):
            generator.generate_signature_equipment()
        if getattr(args, 'equipment_quality', False):
            generator.generate_equipment_quality()
        if getattr(args, 'tools_utilities', False):
            generator.generate_tools_utilities()
        if getattr(args, 'random_tables', False):
            generator.generate_random_tables()
        if getattr(args, 'target_numbers', False):
            generator.generate_target_numbers()
        if getattr(args, 'advantage_disadvantage', False):
            generator.generate_advantage_disadvantage()
        if getattr(args, 'spell_combinations', False):
            generator.generate_spell_combinations()
        if getattr(args, 'ritual_magic', False):
            generator.generate_ritual_magic()
        if args.metamagic:
            generator.generate_metamagic()
        if getattr(args, 'social_combat', False):
            generator.generate_social_combat()
        if getattr(args, 'campaign_tracker', False):
            generator.generate_campaign_tracker()
        if getattr(args, 'skill_list', False):
            generator.generate_skill_list()
        if getattr(args, 'magic_crafting', False):
            generator.generate_magic_crafting()

    print("\n" + "=" * 50)
    print("✨ Generation complete!")


if __name__ == '__main__':
    main()
