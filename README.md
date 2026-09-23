# RASSP website

Source of **https://rasspitu.github.io/**, the website of the RASSP (RAdar and Sonar Signal Processing)
Research Group, Department of Electronics and Communication Engineering,
Istanbul Technical University.

Every push to `main` rebuilds and publishes the site automatically (GitHub Actions, about 2 minutes).
You can edit files directly on github.com (open the file, click the pencil icon, "Commit changes"),
or clone the repository and work locally.

## Where things are

| What                     | File                                         |
|--------------------------|----------------------------------------------|
| Members                  | `_data/people.yml`, photos in `images/people/` |
| Publications             | `markdown_generator/publications.bib` → `_publications/` |
| News                     | `_data/news.yml`                             |
| Equipment                | `_data/equipment.yml`, photos in `images/equipment/` |
| Research themes          | `_data/research.yml`, figures in `images/research/` |
| Home page text           | `_pages/about.md`                            |
| Contact page             | `_pages/contact.md`                          |
| Sidebar, site title, links | `_config.yml` (`author:` block)            |
| Menu                     | `_data/navigation.yml`                       |
| Colors                   | `_sass/theme/_rassp_light.scss`, `_rassp_dark.scss` |

Each data file starts with a comment that lists its fields.

## Add a person

1. Put a square photo (at least 300×300 px, JPG or PNG) in `images/people/`, e.g. `images/people/ayse-yilmaz.jpg`.
2. Add an entry to `_data/people.yml`:

   ```yaml
   - name: "Ayşe Yılmaz"
     title: "PhD Student"
     role: phd              # pi | faculty | phd | msc | undergrad | alumni
     photo: "ayse-yilmaz.jpg"
     email: "..."
     scholar: "https://scholar.google.com/citations?user=..."
     github: "username"
     orcid: "0000-0000-0000-0000"
     linkedin: "username"
     start_year: 2026
   ```

   Leave out fields you do not need. Use correct Turkish characters. When someone graduates,
   change `role` to `alumni` and put the degree and current position in `title`.

## Add a publication

1. Add the BibTeX entry to `markdown_generator/publications.bib` (Google Scholar: "Cite" → "BibTeX").
   Add `doi` and `url` fields if you have them.
2. Regenerate the pages (needs Python):

   ```
   pip install pybtex
   python markdown_generator/pubsFromBib.py
   ```

3. Commit `publications.bib` and the changed files in `_publications/`.

`@article` entries appear under Journal Articles, `@inproceedings` under Conference Papers,
everything else under Preprints (override with `category = {journal}` in the entry).
Do not edit generated files by hand; they are rewritten on every run. See `markdown_generator/README.md`.

If you cannot run Python, copy `_publications/2000-01-01-placeholder-publication.md`,
rename it `YYYY-MM-DD-short-title.md`, fill in the fields and delete the `placeholder`,
`sitemap` and `published` lines.

## Add a news item

Add an entry at the top of `_data/news.yml`:

```yaml
- date: 2026-10-01
  text: "Our paper on GPR clutter removal was accepted to [Journal Name](https://...)."
```

The three newest items also appear on the home page (`news_on_home` in `_config.yml`).

## Add equipment

Optionally put a photo in `images/equipment/`, then add to `_data/equipment.yml`:

```yaml
- name: "Model name"
  type: "GPR system"
  description: "What it is and what we use it for."
  image: "equipment/model-name.jpg"
  image_alt: "The GPR cart on a test field"
```

## Placeholders

Entries with `placeholder: true` (and text starting with `TODO`) are examples waiting for real data.
They show up in local previews but are **hidden on the live site** (the example publication only
appears with `bundle exec jekyll serve --unpublished`). Replace or delete them;
`grep -rn TODO _data _pages _publications` finds them all.

## Preview locally

With Ruby 3.3 and Bundler installed (Windows: RubyInstaller with DevKit):

```
bundle install
bundle exec jekyll serve
```

then open http://localhost:4000. Alternatively, with Docker: `docker compose up`.
To preview exactly what the live site shows (placeholders hidden), run
`JEKYLL_ENV=production bundle exec jekyll serve` (PowerShell: `$env:JEKYLL_ENV="production"` first).

## Credits

Built with [Jekyll](https://jekyllrb.com) and the [AcademicPages](https://github.com/academicpages/academicpages.github.io)
theme, a fork of Minimal Mistakes (MIT license, see `LICENSE`).
