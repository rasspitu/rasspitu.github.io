#!/usr/bin/env python
"""Generate the files in _publications/ from a BibTeX file.

Usage (from the repository root):

    pip install pybtex
    python markdown_generator/pubsFromBib.py                      # uses markdown_generator/publications.bib
    python markdown_generator/pubsFromBib.py path/to/other.bib

Every run first deletes the files this script generated before (they contain
`generated_by: pubsFromBib`) and then writes one Markdown file per BibTeX entry,
so the BibTeX file is the single source of truth. Files you wrote by hand are
never touched.

Category of each entry (see `publication_category` in _config.yml):
  - an explicit `category = {journal|conference|preprint}` field in the entry wins;
  - otherwise @article -> journal, @inproceedings/@conference/@proceedings/@incollection
    -> conference, and anything else (@misc, @unpublished, @techreport, ...) -> preprint.

Adapted from the AcademicPages markdown_generator (MIT license).
"""

import codecs
import json
import re
import sys
import unicodedata
from pathlib import Path

import latexcodec  # noqa: F401  (registers the "ulatex" codec; installed with pybtex)
from pybtex.database import BibliographyData, parse_file

REPO = Path(__file__).resolve().parent.parent
DEFAULT_BIB = REPO / "markdown_generator" / "publications.bib"
OUT_DIR = REPO / "_publications"
MARKER = "generated_by: pubsFromBib"

CATEGORY_BY_TYPE = {
    "article": "journal",
    "inproceedings": "conference",
    "conference": "conference",
    "proceedings": "conference",
    "incollection": "conference",
}
CATEGORIES = {"journal", "conference", "preprint"}

MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], start=1)}

# Turkish letters that NFKD does not reduce to ASCII
ASCII_MAP = str.maketrans({"ı": "i", "İ": "I", "ş": "s", "Ş": "S", "ğ": "g", "Ğ": "G"})


def latex_to_text(value):
    """Decode LaTeX accents (e.g. I{\\c{s}}{\\i}n -> Işın) and drop braces."""
    text = codecs.decode(value, "ulatex")
    text = text.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", text).strip()


def person_name(person):
    parts = person.first_names + person.middle_names + person.prelast_names + person.last_names
    name = " ".join(latex_to_text(p) for p in parts)
    if person.lineage_names:
        name += ", " + " ".join(latex_to_text(p) for p in person.lineage_names)
    return name


def slugify(text, max_len=60):
    text = unicodedata.normalize("NFKD", text.translate(ASCII_MAP))
    text = text.encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:max_len].rstrip("-") or "untitled"


def pub_date(fields):
    year = int(fields["year"])
    month = 1
    raw = fields.get("month", "").strip().lower()
    if raw.isdigit():
        month = int(raw)
    elif raw[:3] in MONTHS:
        month = MONTHS[raw[:3]]
    day = int(fields["day"]) if fields.get("day", "").isdigit() else 1
    return f"{year:04d}-{month:02d}-{day:02d}"


def venue_of(entry):
    f = entry.fields
    for key in ("journal", "booktitle", "howpublished", "publisher", "institution", "school"):
        if f.get(key):
            return latex_to_text(f[key])
    if f.get("eprint"):
        prefix = f.get("archiveprefix", f.get("eprinttype", "arXiv"))
        return f"{prefix}:{f['eprint']}"
    return ""


def category_of(entry):
    explicit = entry.fields.get("category", "").strip().lower()
    if explicit in CATEGORIES:
        return explicit
    return CATEGORY_BY_TYPE.get(entry.type.lower(), "preprint")


def yaml_str(value):
    # A JSON string is a valid YAML double-quoted scalar
    return json.dumps(value, ensure_ascii=False)


def to_markdown(key, entry):
    f = entry.fields
    title = latex_to_text(f["title"])
    date = pub_date(f)
    authors = ", ".join(person_name(p) for p in entry.persons.get("author", []))
    bibtex = BibliographyData({key: entry}).to_string("bibtex").strip()

    lines = [
        "---",
        f"title: {yaml_str(title)}",
        f"authors: {yaml_str(authors)}",
        f"venue: {yaml_str(venue_of(entry))}",
        f"date: {date}",
        f"category: {category_of(entry)}",
    ]
    if f.get("doi"):
        doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", f["doi"].strip())
        lines.append(f"doi: {yaml_str(doi)}")
    if f.get("url"):
        lines.append(f"paperurl: {yaml_str(f['url'].strip())}")
    lines.append("bibtex: |")
    lines += ["  " + line for line in bibtex.splitlines()]
    lines += [MARKER, "---", ""]
    if f.get("abstract"):
        lines += ["**Abstract.** " + latex_to_text(f["abstract"]), ""]

    filename = f"{date}-{slugify(title)}.md"
    return filename, "\n".join(lines)


def main():
    bib_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_BIB
    bib = parse_file(str(bib_path), bib_format="bibtex")
    OUT_DIR.mkdir(exist_ok=True)

    removed = 0
    for old in OUT_DIR.glob("*.md"):
        if MARKER in old.read_text(encoding="utf-8"):
            old.unlink()
            removed += 1

    written, skipped = 0, 0
    for key, entry in bib.entries.items():
        missing = [field for field in ("title", "year") if field not in entry.fields]
        if missing:
            print(f"SKIPPED {key}: missing {', '.join(missing)}")
            skipped += 1
            continue
        filename, content = to_markdown(key, entry)
        with open(OUT_DIR / filename, "w", encoding="utf-8", newline="\n") as out:
            out.write(content)
        print(f"wrote _publications/{filename}")
        written += 1

    print(f"\n{written} written, {skipped} skipped, {removed} old generated files removed.")


if __name__ == "__main__":
    main()
