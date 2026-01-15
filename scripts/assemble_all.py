#!/usr/bin/env python3
"""
Assemble all publication manifests at once.

Usage:
    python scripts/assemble_all.py
"""

import sys
from pathlib import Path

# Add scripts directory to path for import
sys.path.insert(0, str(Path(__file__).parent))

from assemble_book import BookAssembler


def main():
    """Assemble all books from manifests directory."""
    manifests_dir = Path(__file__).parent.parent / "publications" / "manifests"

    if not manifests_dir.exists():
        print(f"Error: Manifests directory not found: {manifests_dir}")
        sys.exit(1)

    manifests = sorted(manifests_dir.glob("*.yaml"))

    if not manifests:
        print("No manifest files found.")
        sys.exit(1)

    print(f"Found {len(manifests)} manifests to assemble:\n")

    success_count = 0
    error_count = 0

    for manifest_path in manifests:
        print(f"Assembling: {manifest_path.name}")
        try:
            assembler = BookAssembler(str(manifest_path))
            assembler.save()
            success_count += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            error_count += 1
        print()

    print("=" * 50)
    print(f"Complete: {success_count} succeeded, {error_count} failed")


if __name__ == "__main__":
    main()
