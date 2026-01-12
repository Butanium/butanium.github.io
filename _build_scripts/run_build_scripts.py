#!/usr/bin/env python3
"""
Build Script Runner

This script runs all Python build scripts in the order specified in config.yml.
It validates that ALL .py files in _build_scripts/ are listed in the config,
ensuring developers explicitly decide the execution order for each script.

Usage:
    python _build_scripts/run_build_scripts.py

Exit codes:
    0 - All scripts ran successfully
    1 - Validation failed (unlisted scripts found)
    2 - A script failed during execution
"""

import subprocess
import sys
import yaml
from pathlib import Path

# Get the directory containing this script
SCRIPTS_DIR = Path(__file__).parent
CONFIG_FILE = SCRIPTS_DIR / "config.yml"
REPO_ROOT = SCRIPTS_DIR.parent


def load_config():
    """Load the build scripts configuration."""
    if not CONFIG_FILE.exists():
        print(f"ERROR: {CONFIG_FILE} not found!")
        print("Create a config.yml file listing all build scripts.")
        sys.exit(1)

    with open(CONFIG_FILE, 'r') as f:
        config = yaml.safe_load(f)

    return config.get('scripts', [])


def get_all_python_scripts():
    """Get all .py files in the build scripts directory, excluding this runner."""
    scripts = set()
    for py_file in SCRIPTS_DIR.glob("*.py"):
        # Exclude the runner script itself
        if py_file.name != "run_build_scripts.py":
            scripts.add(py_file.name)
    return scripts


def validate_config(configured_scripts, actual_scripts):
    """
    Validate that all Python scripts are listed in the config.

    Returns True if valid, False otherwise.
    """
    configured_set = set(configured_scripts)

    # Check for scripts in folder but not in config
    unlisted = actual_scripts - configured_set
    if unlisted:
        print("=" * 60)
        print("BUILD FAILED: Unlisted scripts found!")
        print("=" * 60)
        print()
        print("The following scripts exist in _build_scripts/ but are NOT")
        print("listed in config.yml:")
        print()
        for script in sorted(unlisted):
            print(f"  - {script}")
        print()
        print("Please add them to _build_scripts/config.yml in the order")
        print("you want them to run, or delete them if not needed.")
        print()
        print("This check ensures you explicitly decide the execution order")
        print("for each build script.")
        print("=" * 60)
        return False

    # Check for scripts in config but not in folder (warning only)
    missing = configured_set - actual_scripts
    if missing:
        print("WARNING: The following scripts are in config.yml but don't exist:")
        for script in sorted(missing):
            print(f"  - {script}")
        print()

    return True


def run_script(script_name):
    """Run a single build script."""
    script_path = SCRIPTS_DIR / script_name

    if not script_path.exists():
        print(f"  SKIP: {script_name} (file not found)")
        return True

    print(f"  Running: {script_name}")
    print("-" * 40)

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(REPO_ROOT)
    )

    print("-" * 40)

    if result.returncode != 0:
        print(f"  FAILED: {script_name} (exit code {result.returncode})")
        return False

    print(f"  OK: {script_name}")
    return True


def main():
    """Main entry point."""
    print("=" * 60)
    print("Build Scripts Runner")
    print("=" * 60)
    print()

    # Load configuration
    configured_scripts = load_config()
    actual_scripts = get_all_python_scripts()

    print(f"Scripts in config: {len(configured_scripts)}")
    print(f"Scripts in folder: {len(actual_scripts)}")
    print()

    # Validate all scripts are configured
    if not validate_config(configured_scripts, actual_scripts):
        return 1

    if not configured_scripts:
        print("No scripts configured. Nothing to do.")
        return 0

    print(f"Running {len(configured_scripts)} script(s) in order...")
    print()

    # Run scripts in order
    for script_name in configured_scripts:
        if not run_script(script_name):
            print()
            print("BUILD FAILED: Script execution failed.")
            return 2
        print()

    print("=" * 60)
    print("All build scripts completed successfully!")
    print("=" * 60)
    return 0


if __name__ == '__main__':
    sys.exit(main())
