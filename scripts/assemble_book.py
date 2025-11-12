#!/usr/bin/env python3
"""
Flow RPG Book Assembly Script

Assembles publication-ready markdown documents from modular source files
based on YAML manifest definitions.

Usage:
    python assemble_book.py <manifest_file>
    python assemble_book.py publications/manifests/core_rulebook.yaml
"""

import yaml
import sys
import re
from pathlib import Path
from typing import List, Dict, Any, Optional


class BookAssembler:
    """Assembles markdown books from manifests."""

    def __init__(self, manifest_path: str, base_dir: Optional[Path] = None):
        """
        Initialize the assembler.

        Args:
            manifest_path: Path to the YAML manifest file
            base_dir: Base directory for resolving relative paths (default: parent of manifest)
        """
        self.manifest_path = Path(manifest_path)
        self.base_dir = base_dir or self.manifest_path.parent.parent.parent

        with open(self.manifest_path, 'r', encoding='utf-8') as f:
            self.manifest = yaml.safe_load(f)

        self.output = []
        self.toc_entries = []

    def assemble(self) -> str:
        """
        Assemble the book according to the manifest.

        Returns:
            The assembled markdown content as a string
        """
        # Add title and metadata
        self._add_title()

        # Process all sections
        for section in self.manifest.get('sections', []):
            self._process_section(section)

        # Generate TOC if requested
        if self.manifest.get('options', {}).get('generate_toc', False):
            self._insert_toc()

        return '\n'.join(self.output)

    def _add_title(self):
        """Add book title and metadata."""
        title = self.manifest.get('title', 'Untitled')
        version = self.manifest.get('version', '')

        self.output.append(f"# {title}")
        if version:
            self.output.append(f"\n*Version {version}*")
        self.output.append("\n---\n")

    def _process_section(self, section: Dict[str, Any], level: int = 1):
        """
        Process a section from the manifest.

        Args:
            section: Section definition from manifest
            level: Current heading level
        """
        # Add section title if present
        if 'title' in section:
            heading = '#' * level + ' ' + section['title']
            self.output.append(f"\n{heading}\n")
            self.toc_entries.append((level, section['title']))

        # Add intro text if present
        if 'intro' in section:
            self.output.append(f"\n{section['intro']}\n")

        # Process content
        content = section.get('content', [])
        for item in content:
            self._process_content_item(item, level + 1)

    def _process_content_item(self, item: Any, level: int):
        """
        Process a single content item.

        Args:
            item: Content item (can be string, dict, or path)
            level: Current heading level
        """
        # Handle different item types
        if isinstance(item, str):
            # Simple file path
            self._include_file(item)

        elif isinstance(item, dict):
            if 'file' in item:
                # File with options
                self._include_file(
                    item['file'],
                    heading_adjust=item.get('heading_level_adjust', 0),
                    exclude_sections=item.get('exclude_sections', []),
                    rename_to=item.get('rename_to')
                )

            elif 'section_header' in item:
                # Standalone section header
                heading = '#' * level + ' ' + item['section_header']
                self.output.append(f"\n{heading}\n")
                self.toc_entries.append((level, item['section_header']))

            elif 'files_from_directory' in item:
                # Multiple files from directory
                self._include_directory(
                    item['files_from_directory'],
                    sort=item.get('sort', 'alphabetical')
                )

    def _include_file(
        self,
        file_path: str,
        heading_adjust: int = 0,
        exclude_sections: List[str] = None,
        rename_to: Optional[str] = None
    ):
        """
        Include a markdown file in the output.

        Args:
            file_path: Path to the file (relative to base_dir)
            heading_adjust: Number of levels to adjust headings (+ increases, - decreases)
            exclude_sections: List of section titles to exclude
            rename_to: Optional new title for the file's main heading
        """
        full_path = self.base_dir / file_path

        if not full_path.exists():
            self.output.append(f"\n**ERROR: File not found: {file_path}**\n")
            return

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Process the content
        if exclude_sections:
            content = self._exclude_sections(content, exclude_sections)

        if heading_adjust != 0:
            content = self._adjust_headings(content, heading_adjust)

        if rename_to:
            content = self._rename_first_heading(content, rename_to)

        # Add page break if requested
        if self.manifest.get('options', {}).get('add_page_breaks', False):
            self.output.append("\n---\n")

        self.output.append(content)
        self.output.append("\n")

    def _include_directory(self, pattern: str, sort: str = 'alphabetical'):
        """
        Include all matching files from a directory.

        Args:
            pattern: Glob pattern (e.g., "drafts/callings/calling_types/*.md")
            sort: How to sort files ('alphabetical', 'modified', 'none')
        """
        # Resolve glob pattern
        files = list(self.base_dir.glob(pattern))

        # Sort files
        if sort == 'alphabetical':
            files.sort(key=lambda p: p.name)
        elif sort == 'modified':
            files.sort(key=lambda p: p.stat().st_mtime)

        # Include each file
        for file_path in files:
            relative_path = file_path.relative_to(self.base_dir)
            self._include_file(str(relative_path))

    def _adjust_headings(self, content: str, adjustment: int) -> str:
        """
        Adjust heading levels in markdown content.

        Args:
            content: Markdown content
            adjustment: Number of levels to adjust (+ or -)

        Returns:
            Content with adjusted headings
        """
        def replace_heading(match):
            hashes = match.group(1)
            title = match.group(2)
            new_level = len(hashes) + adjustment
            new_level = max(1, min(6, new_level))  # Clamp between 1-6
            return '#' * new_level + ' ' + title

        return re.sub(r'^(#{1,6})\s+(.+)$', replace_heading, content, flags=re.MULTILINE)

    def _exclude_sections(self, content: str, sections_to_exclude: List[str]) -> str:
        """
        Remove specified sections from content.

        Args:
            content: Markdown content
            sections_to_exclude: List of section titles to remove

        Returns:
            Content with sections removed
        """
        # This is a simple implementation - could be more sophisticated
        for section_title in sections_to_exclude:
            # Pattern to match section and everything until next same-level heading
            pattern = rf'^#+\s+{re.escape(section_title)}.*?(?=^#+\s|\Z)'
            content = re.sub(pattern, '', content, flags=re.MULTILINE | re.DOTALL)

        return content

    def _rename_first_heading(self, content: str, new_title: str) -> str:
        """
        Rename the first heading in the content.

        Args:
            content: Markdown content
            new_title: New title for first heading

        Returns:
            Content with renamed first heading
        """
        def replace_first(match):
            hashes = match.group(1)
            return hashes + ' ' + new_title

        return re.sub(r'^(#{1,6})\s+.+$', replace_first, content, count=1, flags=re.MULTILINE)

    def _insert_toc(self):
        """Insert a table of contents at the beginning."""
        if not self.toc_entries:
            return

        toc = ["\n## Table of Contents\n"]

        for level, title in self.toc_entries:
            indent = '  ' * (level - 1)
            # Create anchor link (simplified - may need more robust implementation)
            anchor = title.lower().replace(' ', '-').replace(':', '')
            toc.append(f"{indent}- [{title}](#{anchor})")

        toc.append("\n---\n")

        # Insert TOC after title (find first --- separator)
        try:
            separator_index = self.output.index("---\n")
            self.output = self.output[:separator_index + 1] + toc + self.output[separator_index + 1:]
        except ValueError:
            # No separator found, add at beginning
            self.output = toc + self.output

    def save(self, output_path: Optional[str] = None):
        """
        Save the assembled book to a file.

        Args:
            output_path: Path to save to (default: from manifest)
        """
        if output_path is None:
            output_path = self.manifest.get('output_file', 'output.md')

        # Resolve output path relative to base_dir
        full_output_path = self.base_dir / output_path

        # Create parent directories if needed
        full_output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the content
        content = self.assemble()
        with open(full_output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✓ Assembled book saved to: {full_output_path}")
        print(f"  Total size: {len(content):,} characters")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python assemble_book.py <manifest_file>")
        print("\nExample:")
        print("  python assemble_book.py publications/manifests/core_rulebook.yaml")
        sys.exit(1)

    manifest_path = sys.argv[1]

    try:
        assembler = BookAssembler(manifest_path)
        assembler.save()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing manifest: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
