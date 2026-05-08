# STATE.md — website modernization tracker

## Completed (prototype phase)

All four inner-page prototypes are done as standalone HTML files with inline CSS:

| File | Status | Notes |
|------|--------|-------|
| `prototype-v2.html` | ✅ Complete | Home page, hero scroll JS, sage-green design system |
| `prototype-v2-research.html` | ✅ Complete | 3-section alternating image layout, new content |
| `prototype-v2-publications.html` | ✅ Complete | Hero image, per-icon hover colors |
| `prototype-v2-about.html` | ✅ Complete | 4-image slideshow, correct social URLs, hero image |

### Research page sections (last edit)
1. **Marine plankton and ecosystem metabolism** (image left) — covers NatComm 2024 + PNAS submitted (both with Ghedini)
2. **Structure and stability of microbial communities** (image right) — Macocco+Grilli preprint + Mazzarisi+Droghetti preprint
3. **Stochasticity, dispersal, and the evolution of individual strategies** (image left) — PhysRevE 2023 + Hidalgo in-prep

### Key design decisions
- CSS custom properties: `--accent:#4a7c59`, `--bg:#f4f4f4`, `--nav-h:52px`, `--footer-h:56px`, `--max-w:900px`
- Nav inner padding: `0 max(1rem, calc((100% - var(--max-w)) / 2))` to align with 900px hero
- Icon hover: per-icon fill colors via `.icon-link.CLASS:hover svg path { fill: COLOR !important; }`
- ORCID SVG: no embedded `<style>` tag; CSS handles `path.st0` (circle) and `path.st1` (white letters)
- ResearchGate SVG: `style="fill-rule:evenodd;clip-rule:evenodd"` on `<svg>` element required

## Stylesheet refactor (done)

Created `dist/site.css` with all shared CSS (design tokens, reset, nav, hero, footer, icon hover states, responsive breakpoints). Each page now loads it via `<link rel="stylesheet" href="/dist/site.css">` and keeps only page-specific styles in a small inline `<style>` block. `404.html` was also rewritten to use the new design system (dropped old Tachyons-based markup). `dist/main.css` and `dist/enhancements.css` are no longer loaded by any page.

## Social link URLs (verified)
- Scholar: `https://scholar.google.com/citations?user=Fqnde5sAAAAJ`
- ORCID: `https://orcid.org/0000-0002-0258-1107`
- LinkedIn: `https://www.linkedin.com/in/lorenzo-fant`
- ResearchGate: `https://www.researchgate.net/profile/Lorenzo-Fant`
- Twitter: `https://twitter.com/lorenzo_fant`
- Strava: `https://www.strava.com/athletes/58651578`
