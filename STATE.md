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

## TODO (next phase — apply to live site)

When user approves prototypes, apply changes to live pages:
1. Create `dist/enhancements.css` with design tokens + component classes
2. Update `index.html` — load enhancements.css, btn-accent CTAs
3. Update `research/index.html` — new 3-section alternating layout
4. Update `publications/index.html` — hero, load enhancements.css
5. Update `about/index.html` — hero, slideshow, load enhancements.css
6. Update `404.html` — load enhancements.css
7. (Optional) Google Scholar automation: `scripts/fetch_scholar.py` + GitHub Action

## Social link URLs (verified)
- Scholar: `https://scholar.google.com/citations?user=Fqnde5sAAAAJ`
- ORCID: `https://orcid.org/0000-0002-0258-1107`
- LinkedIn: `https://www.linkedin.com/in/lorenzo-fant`
- ResearchGate: `https://www.researchgate.net/profile/Lorenzo-Fant`
- Twitter: `https://twitter.com/lorenzo_fant`
- Strava: `https://www.strava.com/athletes/58651578`
