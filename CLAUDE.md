# chuma.world

Personal website for Chuma Okoro — portfolio, articles, projects, videos, resume, and career coaching CTA.

## Stack
- Jekyll 4.3.4 + minima 2.5.2 theme
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
- Color in use: `#014397` (blue) for CTA buttons

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
