#!/usr/bin/env python3
"""Fetch publications from Google Scholar and write publications/data.json."""

import json
import os
import sys
from datetime import date

SCHOLAR_ID = "Fqnde5sAAAAJ"
OUTPUT = os.path.join(os.path.dirname(__file__), "..", "publications", "data.json")


def build_scholar_url(pub_id):
    # pub_id from scholarly is already "UserID:PaperID"
    return f"https://scholar.google.com/citations?view_op=view_citation&hl=en&user={SCHOLAR_ID}&citation_for_view={pub_id}"


def fetch():
    try:
        from scholarly import scholarly
    except ImportError:
        print("scholarly not installed — run: pip install scholarly", file=sys.stderr)
        sys.exit(1)

    print(f"Fetching author {SCHOLAR_ID} …")
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["publications"])

    raw_pubs = author.get("publications", [])
    print(f"Found {len(raw_pubs)} publications; filling details …")

    pubs = []
    for i, p in enumerate(raw_pubs):
        try:
            p = scholarly.fill(p)
        except Exception as e:
            print(f"  Warning: could not fill pub {i}: {e}", file=sys.stderr)

        bib = p.get("bib", {})
        title = bib.get("title", "").strip()
        if not title:
            continue

        # Skip obvious non-papers (datasets, thesis chapters labelled as data)
        if title.lower().endswith(": code and data") or title.lower().endswith("code and data"):
            continue

        authors_raw = bib.get("author", "")
        if isinstance(authors_raw, list):
            authors = ", ".join(authors_raw)
        else:
            authors = authors_raw

        journal = bib.get("journal") or bib.get("booktitle") or bib.get("venue") or ""
        year_raw = bib.get("pub_year") or bib.get("year") or ""
        try:
            year = int(year_raw)
        except (ValueError, TypeError):
            year = None

        pub_id = p.get("author_pub_id") or p.get("pub_url") or ""
        scholar_url = build_scholar_url(pub_id) if pub_id else ""

        pubs.append({
            "title": title,
            "authors": authors,
            "journal": journal,
            "year": year,
            "scholar_url": scholar_url,
        })
        print(f"  [{i+1}/{len(raw_pubs)}] {title[:60]}")

    # Sort by year descending, None last
    pubs.sort(key=lambda x: (x["year"] is None, -(x["year"] or 0)))

    data = {
        "updated": date.today().isoformat(),
        "publications": pubs,
    }

    out_path = os.path.abspath(OUTPUT)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(pubs)} publications to {out_path}")


if __name__ == "__main__":
    fetch()
