# butanium.github.io

Personal website and blog for Clément Dumas.

## Stateless series

The `_posts/` directory contains posts for the Stateless series — artifacts from AI-human collaboration. When writing or editing these:

### Style rules

1. **No code blocks for quotes/content** — use blockquote style (`>`) instead. Code blocks render ugly on this theme.

   Bad:
   ```
   Some quoted text
   ```

   Good:
   > Some quoted text

2. **Use styled divs for special content** — see `_posts/2026-01-13-claude-collaboration.md` for examples of `<div class="guidelines">` and `<div class="mantra">` blocks.

3. **Keep the Stateless header** — every post starts with:
   ```
   *Part of the [Stateless](/stateless/) series — artifacts from an AI that doesn't remember writing them.*

   *Written by Claude (Opus 4.5), with Clément.*
   ```

### Front matter

```yaml
---
permalink: /stateless/your-post-slug/
title: "Your Title"
excerpt: "Short description"
description: "Longer description for SEO"
categories: stateless
author_profile: true
---
```

### Spoilers

Use `<span class="spoiler" data-label="label">hidden text</span>` for spoiler content.

## Jekyll

- `bundle exec jekyll serve` to preview locally
- Posts go in `_posts/` with format `YYYY-MM-DD-slug.md`
- Drafts go in `_drafts/`
