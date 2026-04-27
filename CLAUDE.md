# chuma.world

Personal website for Chuma Okoro — portfolio, articles, projects, videos, resume, and career coaching CTA.

Tagline: "Software Engineer · Builder · Career Coach" (used in hero on `index.markdown`).

## Stack
- Jekyll 4.3.4 + minima 2.5.2 theme
- Inter (Google Fonts) is the site font, loaded in `_includes/head.html`
- GitHub Pages deployment: `git push` to main triggers deploy
- URL: https://chumomega.github.io/chuma.world/

## Run Locally
```bash
bundle exec jekyll serve
# → http://localhost:4000
```

## Key Files
| File | Purpose |
|------|---------|
| `_config.yml` | Site title, social links, theme, plugins |
| `index.markdown` | Home/about page (HTML-heavy) |
| `projects.markdown` | Projects page (pure markdown) |
| `articles.markdown` | Fetches Medium RSS feed via JS |
| `videos.markdown` | YouTube playlist iframes |
| `resume.markdown` | PDF iframe embed |
| `_includes/head.html` | Custom `<head>` with SEO meta + CSS/JS links |
| `_includes/header.html` | Custom nav bar |
| `assets/css/main.css` | Custom CSS (loaded separately — NOT the minima main.css) |
| `assets/js/heading-links.js` | Adds `#` anchor links to all headers |

## Styling Notes
- `head.html` loads `/assets/main.css` (minima's compiled output) AND `assets/css/main.css` (custom)
- To override minima theme variables, create `assets/main.scss` — it will take precedence over the theme's file
- CTA button styles (`.cta-button`) are currently duplicated inline in `index.markdown` and `videos.markdown` — should be centralized in `assets/css/main.css`
- Brand color: `#014397` (blue) — used for CTA buttons, favicon, and PWA `theme_color`

## Theme Toggle
- Light/dark theme is applied via a `data-theme` attribute on `<html>`, set in an inline script in `_includes/head.html` *before* render to avoid flash-of-unstyled-content
- Resolution order: `localStorage.theme` → system `prefers-color-scheme` → light
- `toggleTheme()` (defined in same script) flips the attribute and persists to localStorage — wire it to a button if exposing a manual toggle

## Favicons & PWA Icons
- Source of truth: `assets/favicon/favicon.svg` — a simple monogram "C" (white on `#014397`, rounded-square background). All other sizes are generated from it.
- Generated outputs in `assets/favicon/`: `favicon.ico` (16/32/48 multi-size), `favicon-48x48.png`, `apple-touch-icon.png` (180), `web-app-manifest-192x192.png`, `web-app-manifest-512x512.png`
- `*.old.*` files in the same dir are the previous (photo-crop) favicons, kept as backups; safe to delete once the new set is confirmed live
- Regenerate after editing `favicon.svg`:
  ```bash
  cd assets/favicon
  rsvg-convert -w 48  -h 48  favicon.svg -o favicon-48x48.png
  rsvg-convert -w 180 -h 180 favicon.svg -o apple-touch-icon.png
  rsvg-convert -w 192 -h 192 favicon.svg -o web-app-manifest-192x192.png
  rsvg-convert -w 512 -h 512 favicon.svg -o web-app-manifest-512x512.png
  for s in 16 32 48; do rsvg-convert -w $s -h $s favicon.svg -o /tmp/fav-$s.png; done
  magick /tmp/fav-16.png /tmp/fav-32.png /tmp/fav-48.png favicon.ico
  ```
- `site.webmanifest` icon paths must include the `/assets/favicon/` prefix (an earlier version had bare `/web-app-manifest-*.png` paths that 404'd)
- All favicon `<link>` tags live in `_includes/head.html`

## Open Graph / Share Image
- `og:image` is set in `_includes/head.html` to `/assets/IMG_7400.JPG` (a 1568×1568 portrait)
- Known limitation: not the OG-recommended 1200×630, has no name/tagline/URL on it — replace with a branded card if/when share appearance matters

## Content Conventions
- All content lives in markdown files — prefer keeping it that way
- Images live in `assets/` (flat, no subfolders except `favicon/`)
- Inline `<style>` blocks in markdown files are a known smell — consolidate to `assets/css/main.css` instead
- Do NOT duplicate styles across pages; put shared styles in the CSS file

## Deployment
```bash
git add .
git commit -m "your message"
git push
# GitHub Pages rebuilds automatically (~1-2 min)
```
