#!/usr/bin/env python3
"""
Generate redirect pages from _data/redirects.yml

This script reads the redirects configuration and generates individual
redirect pages in the _redirects/ directory.

Usage:
    python _build_scripts/generate_redirects.py
"""

import os
import yaml
from pathlib import Path

# Get the repo root directory (parent of scripts/)
REPO_ROOT = Path(__file__).parent.parent
DATA_FILE = REPO_ROOT / "_data" / "redirects.yml"
REDIRECTS_DIR = REPO_ROOT / "_redirects"


def load_redirects():
    """Load redirects configuration from YAML file."""
    if not DATA_FILE.exists():
        print(f"Error: {DATA_FILE} not found")
        return {}

    with open(DATA_FILE, 'r') as f:
        data = yaml.safe_load(f)

    return data.get('redirects', {})


def generate_redirect_page(source_path: str, destination_url: str) -> str:
    """Generate the content for a redirect page."""
    # Ensure the permalink has leading and trailing slashes
    permalink = f"/{source_path.strip('/')}/"

    return f"""---
permalink: {permalink}
redirect_to: {destination_url}
---
"""


def parse_redirect_config(source_path, config):
    """
    Parse a redirect configuration value.

    Supports two formats:
    1. Simple string: "https://example.com/" -> (url, subpaths=False)
    2. Object: {url: "https://example.com/", subpaths: true} -> (url, subpaths=True)

    Returns: (destination_url, subpaths_enabled) or None if invalid
    """
    if isinstance(config, str):
        return config, False
    elif isinstance(config, dict):
        url = config.get('url')
        if not url:
            print(f"  [warning] '{source_path}' uses dict format but missing 'url' key - skipping")
            return None
        return url, config.get('subpaths', False)
    else:
        return str(config), False


def main():
    """Generate redirect pages from configuration."""
    redirects = load_redirects()

    if not redirects:
        print("No redirects configured in _data/redirects.yml")
        return 0

    # Ensure the _redirects directory exists
    REDIRECTS_DIR.mkdir(exist_ok=True)

    # Get existing redirect files
    existing_files = set(f.stem for f in REDIRECTS_DIR.glob("*.md"))
    new_files = set()

    print(f"Generating {len(redirects)} redirect(s)...")

    for source_path, config in redirects.items():
        result = parse_redirect_config(source_path, config)
        if result is None:
            continue
        destination_url, subpaths = result

        # Create a safe filename from the source path
        filename = source_path.strip('/').replace('/', '_')
        filepath = REDIRECTS_DIR / f"{filename}.md"
        new_files.add(filename)

        content = generate_redirect_page(source_path, destination_url)

        # Check if file exists and content is the same
        if filepath.exists():
            with open(filepath, 'r') as f:
                if f.read() == content:
                    subpaths_info = " (+ subpaths)" if subpaths else ""
                    print(f"  [unchanged] /{source_path}/ -> {destination_url}{subpaths_info}")
                    continue

        with open(filepath, 'w') as f:
            f.write(content)

        subpaths_info = " (+ subpaths)" if subpaths else ""
        print(f"  [generated] /{source_path}/ -> {destination_url}{subpaths_info}")

    # Remove redirect files that are no longer in the config
    removed_files = existing_files - new_files
    for filename in removed_files:
        filepath = REDIRECTS_DIR / f"{filename}.md"
        filepath.unlink()
        print(f"  [removed] {filename}.md (no longer in config)")

    print("\nDone! Redirect pages are in _redirects/")
    print("Run 'bundle exec jekyll serve' to test locally.")
    return 0


if __name__ == '__main__':
    exit(main())
