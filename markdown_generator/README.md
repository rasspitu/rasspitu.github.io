# Publication generator

`pubsFromBib.py` turns `publications.bib` into one Markdown file per paper in `_publications/`,
which the Publications page lists by category, newest first.

```
pip install pybtex
python markdown_generator/pubsFromBib.py
```

- Run it from the repository root after every change to `publications.bib`, then commit
  both the `.bib` file and the regenerated `_publications/` files.
- Files it generated earlier (marked `generated_by: pubsFromBib`) are deleted and rewritten,
  so edit the BibTeX, not the generated files. Hand-written files are left alone.
- Category: `@article` → Journal Articles, `@inproceedings` / `@conference` → Conference Papers,
  anything else → Preprints. Add `category = {journal}` (or `conference`, `preprint`) to an
  entry to override.
- Entries without `title` or `year` are skipped with a message.
