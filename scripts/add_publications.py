#!/usr/bin/env python3
"""
Add publications to the academicpages site from a BibTeX file.

Parses a .bib file (exported from Zotero or similar) and writes one
Markdown page per entry into _publications/, in the same format used
across the rest of the site (title, venue, authors, keywords, citation,
optional header image).

Usage:
    python3 scripts/add_publications.py path/to/entries.bib
    python3 scripts/add_publications.py path/to/entries.bib --force
    python3 scripts/add_publications.py path/to/entries.bib --images path/to/image/folder

By default, entries whose target Markdown file already exists in
_publications/ are skipped, so re-running this on a growing .bib file
(e.g. your whole Zotero export) will only create files for new entries
and will not overwrite anything you've hand-edited. Pass --force to
regenerate existing files too.

Images: if a bib entry has a `note` field that looks like an image
filename (e.g. "note = {my-figure.jpg}"), the script looks for that
file first under --images (if given) and then under images/publications/
in this repo. If found, it's copied into images/publications/ (if not
already there) and a header/teaser block is added to the generated page.
If not found, the entry is still created, just without an image.
"""

import argparse
import html
import os
import re
import shutil
import sys

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB_DIR = os.path.join(SITE_ROOT, "_publications")
IMG_DST_DIR = os.path.join(SITE_ROOT, "images", "publications")

IMG_EXT_RE = re.compile(r"\.(jpe?g|png|gif|webp)$", re.IGNORECASE)
ENTRY_START_RE = re.compile(r"^@(\w+)\{([^,]+),", re.MULTILINE)
FIELD_RE = re.compile(
    r'(\w+)\s*=\s*(\{(?:[^{}]|\{[^{}]*\})*\}|"[^"]*")\s*,?'
)


def parse_bib(text):
    starts = [m.start() for m in ENTRY_START_RE.finditer(text)]
    starts.append(len(text))
    entries = []
    for i in range(len(starts) - 1):
        chunk = text[starts[i] : starts[i + 1]]
        m = re.match(r"^@(\w+)\{([^,]+),", chunk)
        if not m:
            continue
        etype = m.group(1).lower()
        citekey = m.group(2).strip()
        body = chunk[m.end() :]
        fields = {}
        for fm in FIELD_RE.finditer(body):
            key = fm.group(1).lower()
            val = fm.group(2).strip()
            if val.startswith("{") and val.endswith("}"):
                val = val[1:-1]
            elif val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            val = val.replace("{", "").replace("}", "").strip()
            fields[key] = val
        entries.append((etype, citekey, fields))
    return entries


def esc_dq(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def esc_sq(s):
    return s.replace("'", "''")


def html_escape_amp(s):
    return s.replace("&", "&amp;")


def parse_date(d):
    d = (d or "1900").strip()
    parts = d.split("-")
    if len(parts) == 1:
        return f"{parts[0]}-01-01", parts[0]
    elif len(parts) == 2:
        return f"{parts[0]}-{parts[1]}-01", parts[0]
    return d, parts[0]


def authors_list(raw):
    parts = [p.strip() for p in re.split(r"\s+and\s+", raw)]
    names = []
    for p in parts:
        if "," in p:
            last, first = [x.strip() for x in p.split(",", 1)]
            names.append(f"{first} {last}")
        else:
            names.append(p)
    return names


def format_author_str(authors):
    if not authors:
        return "Simon Ostermann"
    if len(authors) == 1:
        return authors[0]
    if len(authors) == 2:
        return f"{authors[0]} and {authors[1]}"
    return ", ".join(authors[:-1]) + ", and " + authors[-1]


def venue_for(etype, fields):
    if etype == "thesis":
        return fields.get("institution", ""), "theses"
    return fields.get("booktitle", fields.get("journal", "")), "conferences"


def find_image(note, extra_dirs):
    if not note or not IMG_EXT_RE.search(note):
        return None
    search_dirs = list(extra_dirs) + [IMG_DST_DIR]
    for d in search_dirs:
        candidate = os.path.join(d, note)
        if os.path.isfile(candidate):
            return candidate
    return None


def build_entry(etype, citekey, fields, image_dirs):
    title_raw = fields["title"]
    date_str, year = parse_date(fields.get("date", fields.get("year")))
    venue_raw, category = venue_for(etype, fields)
    authors = authors_list(fields["author"]) if "author" in fields else []
    url = fields.get("url", "")
    note = fields.get("note", "")
    abstract = fields.get("abstract", "")
    keywords_raw = fields.get("keywords", "")

    slug = citekey.replace("_", "-")
    filename = f"{date_str}-{slug}.md"
    permalink = f"/publication/{date_str}-{slug}"

    author_str = format_author_str(authors)
    citation_plain = f'{author_str}. ({year}). "{title_raw}." {venue_raw}.'

    lines = ["---"]
    lines.append(f'title: "{esc_dq(title_raw)}"')
    lines.append("collection: publications")
    lines.append(f"category: {category}")
    lines.append(f"permalink: {permalink}")
    lines.append(f"date: {date_str}")
    lines.append(f"venue: '{esc_sq(venue_raw)}'")
    lines.append(f"authors: '{esc_sq(author_str)}'")
    if keywords_raw:
        lines.append(f"keywords: '{esc_sq(keywords_raw)}'")
    if url:
        lines.append(f"paperurl: '{esc_sq(url)}'")
    lines.append(f"citation: '{esc_sq(html_escape_amp(citation_plain))}'")

    image_src = find_image(note, image_dirs)
    teaser_name = os.path.basename(image_src) if image_src else None
    if teaser_name:
        lines.append("header:")
        lines.append(f"  teaser: publications/{teaser_name}")
        lines.append(f"  image: /images/publications/{teaser_name}")

    lines.append("---")
    lines.append("")
    if abstract:
        lines.append(abstract)
        lines.append("")
    if url:
        lines.append(f'[Access paper here]({url}){{:target="_blank"}}')
    else:
        q = html.escape(title_raw.replace(" ", "+"))
        lines.append(
            f"Use [Google Scholar](https://scholar.google.com/scholar?q={q})"
            '{:target="_blank"} for full citation'
        )
    lines.append("")

    return filename, "\n".join(lines), image_src


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bib_file", help="Path to a .bib file with one or more entries")
    ap.add_argument(
        "--images",
        action="append",
        default=[],
        help="Extra folder(s) to look for images referenced in a bib entry's `note` field "
        "(can be given multiple times). images/publications/ is always checked too.",
    )
    ap.add_argument(
        "--force",
        action="store_true",
        help="Overwrite Markdown files that already exist (default: skip them)",
    )
    args = ap.parse_args()

    if not os.path.isfile(args.bib_file):
        print(f"error: no such file: {args.bib_file}", file=sys.stderr)
        sys.exit(1)

    text = open(args.bib_file, encoding="utf-8").read()
    entries = parse_bib(text)
    if not entries:
        print("No BibTeX entries found in that file.")
        return

    os.makedirs(PUB_DIR, exist_ok=True)
    os.makedirs(IMG_DST_DIR, exist_ok=True)

    created, skipped, errors = [], [], []

    for etype, citekey, fields in entries:
        try:
            filename, content, image_src = build_entry(etype, citekey, fields, args.images)
        except KeyError as e:
            errors.append((citekey, f"missing required field {e}"))
            continue

        outpath = os.path.join(PUB_DIR, filename)
        if os.path.exists(outpath) and not args.force:
            skipped.append(filename)
            continue

        with open(outpath, "w", encoding="utf-8") as f:
            f.write(content)

        if image_src:
            dst = os.path.join(IMG_DST_DIR, os.path.basename(image_src))
            if not os.path.exists(dst):
                shutil.copyfile(image_src, dst)

        created.append(filename)

    print(f"Created/updated: {len(created)}")
    for f in created:
        print(f"  + {f}")
    if skipped:
        print(f"\nSkipped (already exist, use --force to overwrite): {len(skipped)}")
        for f in skipped:
            print(f"  = {f}")
    if errors:
        print(f"\nErrors: {len(errors)}")
        for citekey, msg in errors:
            print(f"  ! {citekey}: {msg}")


if __name__ == "__main__":
    main()
