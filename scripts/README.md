# Scripts

This directory contains scripts used for maintaining the website.

## update_last_modified.py

This script is run automatically by the pre-commit framework whenever `_pages/about.md` is modified and committed. It updates the `_data/last_updated.yml` file with the current date.

### Setup

1. Install pre-commit: `pip install pre-commit`
2. Install the hooks: `pre-commit install`

The pre-commit configuration is in `.pre-commit-config.yaml` at the root of the repository.

### How it works

- When `_pages/about.md` is staged for commit, the pre-commit hook runs
- The script updates `_data/last_updated.yml` with the current date in DD/MM/YYYY format
- The updated YAML file is automatically staged and included in the commit
- The about page displays this date using `{{ site.data.last_updated.date }}`

This ensures the "Last updated" date is always accurate and automatically maintained. 