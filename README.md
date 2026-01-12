# butanium.github.io

Personal academic website built with Jekyll and deployed via GitHub Actions.

## Quick Start

### Adding a Redirect

To redirect a path on this site to an external URL:

1. Edit `_data/redirects.yml`:
   ```yaml
   redirects:
     nnterp: https://ndif-team.github.io/nnterp/
     my-project: https://example.com/destination/
   ```

2. Push to `main` or `master` branch

That's it! The redirect pages are generated automatically during build.

### Running Locally

```bash
# Install dependencies
bundle install
pip install pyyaml

# Run build scripts (generates redirects, etc.)
python _build_scripts/run_build_scripts.py

# Start local server
bundle exec jekyll serve
```

Visit `http://localhost:4000` to preview your site.

---

## Build System

This site uses a custom build system that runs Python scripts before Jekyll builds.

### How It Works

1. **GitHub Actions** triggers on push to `main`/`master`
2. **Build scripts** in `_build_scripts/` run in order (defined in `config.yml`)
3. **Jekyll** builds the site
4. **GitHub Pages** deploys the result

### Adding a New Build Script

1. Create your script in `_build_scripts/`:
   ```python
   # _build_scripts/my_script.py
   def main():
       print("Doing something...")
       return 0  # Return 0 for success, non-zero for failure

   if __name__ == '__main__':
       exit(main())
   ```

2. Add it to `_build_scripts/config.yml` in the order you want it to run:
   ```yaml
   scripts:
     - generate_redirects.py
     - my_script.py  # Add your script here
   ```

3. Push your changes

**Important:** All `.py` files in `_build_scripts/` MUST be listed in `config.yml`. The build will fail if any script is missing from the config. This ensures you explicitly decide the execution order.

### Build Scripts Config

`_build_scripts/config.yml` controls which scripts run and in what order:

```yaml
scripts:
  - generate_redirects.py  # Runs first
  - another_script.py      # Runs second
  - final_script.py        # Runs last
```

### Testing Build Scripts Locally

```bash
python _build_scripts/run_build_scripts.py
```

This will:
- Validate all scripts are in the config
- Run each script in order
- Report success/failure

---

## Project Structure

```
.
├── _build_scripts/           # Python scripts that run before Jekyll
│   ├── config.yml            # Script execution order
│   ├── run_build_scripts.py  # Build runner (don't edit)
│   └── generate_redirects.py # Generates redirect pages
├── _data/
│   ├── redirects.yml         # Configure URL redirects here
│   └── ...
├── _layouts/
│   ├── redirect.html         # Redirect page template
│   └── ...
├── _pages/                   # Site pages
├── _redirects/               # Generated redirect pages (don't edit)
├── _config.yml               # Jekyll configuration
├── .github/workflows/
│   └── deploy.yml            # GitHub Actions workflow
└── ...
```

---

## Configuration Reference

### Redirects (`_data/redirects.yml`)

```yaml
redirects:
  # Simple redirect
  old-page: https://new-site.com/page/

  # Nested path
  projects/old-project: https://github.com/user/new-repo

  # External site
  docs: https://docs.example.com/
```

Each entry creates a page at `/<path>/` that redirects to the destination URL.

---

## Original Template

This site was forked from [academicpages](https://github.com/academicpages/academicpages.github.io). See `readme.old.md` for the original documentation.
