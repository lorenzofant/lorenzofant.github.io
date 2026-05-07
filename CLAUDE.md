# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Personal academic website for Lorenzo Fant (Post-Doc in Theoretical Ecology and Evolution at Instituto Gulbenkian de Ciência). Deployed on GitHub Pages at `https://lorenzofant.github.io`.

## Site structure

Static HTML — no build system. Edit `.html` files directly and push to deploy.

Pages:
- `index.html` — home/landing page with hero image
- `about/index.html` — bio and contacts
- `publications/index.html` — publications and talks
- `research/index.html` — research interests
- `404.html` — error page

Stylesheet: `dist/main.css` (custom CSS + Tachyons-style utilities). Loaded from an absolute URL in subpages (`https://lorenzofant.github.io/dist/main.css`) and a relative URL on the home page (`dist/main.css`).

CV: `misc/CV.pdf`

## Architecture: shared layout (no templating)

There is **no templating engine** — each HTML file duplicates the nav and footer. If you change navigation links or the footer's social icons, you must update all four pages (`index.html`, `about/index.html`, `publications/index.html`, `research/index.html`).

**Two nav elements per page** (both with `id="navt"`):
- `.navbar` — visible on small screens, hidden on large (`dn-l`)
- `.navbar-t` — visible on large screens only (`dn db-l`), has a dropdown toggle via `myFunction()`

The home page hero uses a scroll-based JS listener to fade the header image and change the navbar background color at scroll positions 50px and 360px.

## Design style

- Font: `avenir next, avenir, sans-serif` (set in `dist/main.css` on `body`)
- Background: `#f4f4f4`, text: `#555`
- Minimalistic — avoid decorative elements, grids, borders
- Keep the same nav and footer structure across pages

## STATE of the proj

- write STATE.md to keep track of concrete actions done, everything you should remember after compression or reactivation, todos
- STATE.md is primarily for your use when switching between chats and to keep track of what has been done

## General attitude

- I am a scientist — be precise and concise
- If unsure, find more information rather than guessing
- No argument from authority — I can be wrong too
