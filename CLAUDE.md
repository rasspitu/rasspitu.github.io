# CLAUDE.md — RASSP Research Group Website

This file gives Claude Code the standing context for this repository. Read it fully before making changes.

## What we are building

A static research-group website for **RASSP — RAdar and Sonar Signal Processing Research Group**, hosted on GitHub Pages.

- Institution: İstanbul Teknik Üniversitesi (İTÜ / Istanbul Technical University), Istanbul, Türkiye
- Faculty / department within İTÜ: TODO (confirm with the user)
- Group lead (PI, role `pi`): Prof. Dr. Işın Erer
- Researcher (role `faculty`): Dr. Yavuz Emre Kayacan
- Other members: TODO (confirm with the user)
- Write names with correct Turkish characters (Işın, not Isin). On the People page list the PI first, then researchers.
- Do not use the official İTÜ logo or seal unless the user provides the file and confirms permission; link to https://www.itu.edu.tr instead.
- Site language: English (Turkish version optional, see "Open questions")
- GitHub organization: `rasspitu` (https://github.com/rasspitu)
- Site repository: `rasspitu/rasspitu.github.io`
- Public URL: https://rasspitu.github.io/

## Reference site

The structure is modeled on https://mspritu.github.io/ (ITU MSPR group). That site is built with **Jekyll + AcademicPages** (a fork of Minimal Mistakes). We follow the same stack and information architecture, but with our own content, branding and colors. Do not copy any text, images, member data or publications from the reference site.

Reference navigation (reproduce this structure):

| Page         | Purpose                                                       |
|--------------|---------------------------------------------------------------|
| Home         | Logo, one-paragraph mission, research interests, sidebar with location, email, GitHub, Google Scholar |
| Research     | Research themes and projects, each with a short description and optional figure |
| Publications | Journal and conference papers, generated from data files, newest first |
| People       | PI, faculty members, PhD/MSc students, alumni, with photo and links |
| Equipments   | Lab hardware (radar/GPR systems, sonar, compute platforms) |
| Contact      | Address, email, map embed (optional)                          |

We may also add a **News** page (paper acceptances, new members, events) if it stays simple.

## Tech stack and constraints

- Jekyll + AcademicPages theme (MIT license). Keep the "Powered by Jekyll & AcademicPages" credit in the footer; this is a license courtesy.
- Must build on GitHub Pages without custom plugins beyond the GitHub Pages whitelist, OR deploy through a GitHub Actions workflow. Prefer the Actions workflow (`actions/jekyll-build-pages` or a standard Ruby build) so we are not limited by the whitelist.
- Content lives in Markdown and YAML data files so non-developers in the group can edit it. No hard-coded content in layouts.
- Responsive, accessible (alt text on every image, sufficient contrast, keyboard-navigable menu).
- No tracking scripts, no external analytics unless explicitly requested.

## Branding

Logo files (provided by the user, put them in `images/`):
- `rassp_logo.svg`, `rassp_logo.png` — horizontal logo (emblem + wordmark)
- `rassp_icon.svg`, `rassp_icon.png` — square emblem, use for favicon, sidebar avatar and social preview

Color palette (taken from the logo; use as SCSS variables):

| Name        | Hex       | Use                                  |
|-------------|-----------|--------------------------------------|
| Deep navy   | `#0A2540` | Primary text headings, masthead      |
| Radar blue  | `#3FA9F5` | Links, primary accents               |
| Sonar teal  | `#1FC7A6` | Secondary accents, hover, dividers   |
| Steel gray  | `#5B6B7F` | Secondary text, captions             |
| White       | `#FFFFFF` | Background                           |

The logo depicts radar wavefronts above a waterline and sonar wavefronts below it. A subtle wave-shaped divider (like the one under the wordmark) may be reused as a section separator; do not overuse it.

Generate favicons (16, 32, 180, 192, 512 px) from `rassp_icon.png`.

## Research content (initial, editable)

Research interests to list on the home page and expand on the Research page:

- Ground Penetrating Radar (GPR) signal processing and clutter removal
- Deep learning for radar and sonar signals (diffusion models, state-space / Mamba architectures)
- Tensor decomposition methods for radar data (tensor train, tensor ring)
- 3D (C-scan) GPR imaging and subsurface target / threat detection
- Real-time target detection on embedded platforms (e.g. NVIDIA Jetson Orin)
- Ultra-wideband (UWB) radar
- Sonar signal processing and underwater acoustic sensing

Do NOT invent publications, people, grants or equipment. Where real data is not yet provided, create clearly marked placeholder entries (`TODO:` in the text, and `placeholder: true` in front matter) so they are easy to find and replace.

## Data model

- `_data/people.yml` — list of members with fields: `name`, `title`, `role` (pi | faculty | phd | msc | undergrad | alumni), `photo`, `email`, `scholar`, `github`, `orcid`, `linkedin`, `bio`, `start_year`. The People page groups by role.
- `_publications/` — one Markdown file per paper (AcademicPages convention) with `title`, `authors`, `venue`, `date`, `category` (journal | conference | preprint), `paperurl`, `doi`, `bibtex`. Also keep a `publications.bib` or `publications.tsv` and a small script that regenerates the Markdown files from it (AcademicPages ships `markdown_generator/` for this; adapt it).
- `_data/research.yml` or `_research/` collection — themes with `title`, `summary`, `image`, `related_publications`.
- `_data/equipment.yml` — `name`, `type`, `description`, `image`.
- `_posts/` or `_data/news.yml` — news items, only if the News page is added.

## GitHub setup

The organization `rasspitu` already exists. The site repository must be named exactly `rasspitu.github.io` so it is served at the organization root URL.

Setup steps (Claude Code does the CLI parts; web-only steps are reported to the user as a checklist):

1. **CLI prerequisites.** Check `git`, `gh` (GitHub CLI), Ruby + Bundler (or Docker). Run `gh auth status`; if not logged in, ask the user to run `gh auth login` with scopes `repo`, `workflow`, `admin:org`. Never ask for or store tokens in files.
2. **Create the repository** (if it does not exist):
   `gh repo create rasspitu/rasspitu.github.io --public --description "RASSP — RAdar and Sonar Signal Processing Research Group" --homepage "https://rasspitu.github.io"`
   then clone it and work inside it. If it already exists, clone it instead.
3. **Base template.** Copy the AcademicPages template files into the repo (clone `academicpages/academicpages.github.io` into a temp folder and copy the contents without its `.git`), so the repo has its own clean history. Keep the MIT LICENSE file of the template.
4. **Pages source = GitHub Actions.** After the first push of the workflow:
   `gh api -X POST repos/rasspitu/rasspitu.github.io/pages -f build_type=workflow`
   (if it already exists, use `-X PUT` with the same field). Verify with `gh api repos/rasspitu/rasspitu.github.io/pages`.
5. **Workflow permissions.** The deploy workflow must declare `permissions: contents: read, pages: write, id-token: write` and use `actions/configure-pages`, `actions/upload-pages-artifact`, `actions/deploy-pages`. Use a `concurrency: pages` group.
6. **Verify deployment.** Watch the run with `gh run watch`, then confirm https://rasspitu.github.io/ returns 200 (`curl -I`).
7. **Organization profile (optional but recommended).** Create repo `rasspitu/.github` with `profile/README.md`: logo, one-line mission, link to the website, research topics. This shows on the org's GitHub page.
8. **Repository metadata.** Set topics: `gh repo edit rasspitu/rasspitu.github.io --add-topic radar,sonar,signal-processing,gpr,deep-learning,research-group,jekyll`.

Web-only steps to list for the user at the end (the CLI cannot do these):
- Org settings → Profile: upload `images/rassp_icon.png` as the organization avatar; set display name "RASSP Research Group", website https://rasspitu.github.io, location "Istanbul, Türkiye", public email.
- Org settings → Member privileges: confirm members may create public Pages sites (needed only if the repo is created by a member rather than an owner).
- Org → People: invite group members; give the PI and one backup person the Owner role, others Member.
- Repo settings → Branches: optional protection rule on `main` (require pull request) once more people edit the site.
- Optional custom domain later (e.g. a university subdomain): add it under repo Settings → Pages and a `CNAME` file; requires a DNS record from the university IT department.

## Working rules for Claude Code

1. Plan first: before creating files, list the planned directory structure and the files you will change, and wait for confirmation if anything is ambiguous.
2. Remove everything from the template that we do not use (talks, teaching, portfolio, CV, sample posts, sample publications, the template author's personal data). Search the repo for the template author's name, email and URLs and make sure none remain.
3. Keep `_config.yml` clean: site title "RASSP", description, url, repository, author/sidebar block pointing to the group (not a person), social links as TODO placeholders.
4. After each major step, run the local build (`bundle exec jekyll serve` or the Docker setup) and fix all errors and warnings.
5. Verify with a checklist at the end: all nav links resolve, no 404s, images load, favicon shows, mobile menu works, no leftover template content, Lighthouse accessibility score ≥ 90 if tooling is available.
6. Write a short `README.md` explaining how group members add a person, a publication, a news item and a piece of equipment.
7. Commit in small, logically separated commits with clear messages.

## Open questions (ask the user, do not guess)

- Faculty / department at İTÜ to show on the site
- Other members (students, alumni) with titles, photos and links
- Photos, emails, Google Scholar / ORCID links for Prof. Dr. Işın Erer and Dr. Yavuz Emre Kayacan

- Final list of members with photos and links
- Publications list (BibTeX preferred)
- ~~Whether to add a Turkish version of the site~~ → answered: no Turkish version
- ~~Whether a News page is wanted~~ → answered: yes (added, `_data/news.yml`)
- Group email address and physical address for Contact

## Project status (handoff log)

The user works on this project from more than one computer. When they ask
"where did we leave off?" / "nerede kaldık?", answer from this section (in Turkish,
the user's language), then continue. Keep this section up to date at the end of
every work session and commit it.

### Last update: 2026-09-23

**Phases 0–4 of PROMPT.md are done. The site is live at https://rasspitu.github.io/.**

Done:
- Repo `rasspitu/rasspitu.github.io` created (public); GitHub account used: `iturassp` (org admin).
  Commits use the repo-local identity `RASSP <332884513+iturassp@users.noreply.github.com>`.
- AcademicPages template imported (upstream `3d28cd2`) and stripped; RASSP theme in
  `_sass/theme/_rassp_{light,dark}.scss`, custom styles in `_sass/layout/_rassp.scss`.
- Pages: Home, Research, Publications, People, Equipments ("Equipments" label kept on purpose), News, Contact.
- Data: `_data/{people,research,equipment,news}.yml`; publications from
  `markdown_generator/publications.bib` via `markdown_generator/pubsFromBib.py` (needs `pip install pybtex`).
- Entries with `placeholder: true` show locally but are hidden on the live site (`JEKYLL_ENV=production`).
- Deploy: `.github/workflows/pages.yml` (Pages source = GitHub Actions). Every push to `main` deploys.
- Org profile repo `rasspitu/.github` (`profile/README.md`) created; repo topics set.
- Verified: no broken links, alt text everywhere, favicon, mobile menu, dark mode, WCAG AA contrast.
  Lighthouse not run (Node not installed).
- Fixed template issues: theme toggle hidden on desktop (greedy-nav selector, patched in
  `assets/js/main.min.js` and the plugin source), fixed footer covering content, MathJax only
  on pages with `mathjax: true`.

Still open / next steps:
1. Delete the empty repo `rasspitu/rassp` (user approved deleting it). Needs the `delete_repo` scope:
   `gh auth refresh -h github.com -s delete_repo`, then `gh repo delete rasspitu/rassp --yes`,
   or delete it in the browser (Settings → Delete this repository).
2. Real content from the user (see "Open questions" above): faculty/department, members and photos,
   emails / Scholar / ORCID of the two researchers, BibTeX, group email and address.
3. Contact map: not added; suggested OpenStreetMap (no tracking) — waiting for the user's answer.
4. Light/dark theme toggle: kept (follows OS preference by default) — ask whether to keep it.
5. Mission paragraph (`_pages/about.md`) and research summaries (`_data/research.yml`) are drafts
   marked TODO; the group should rewrite them.
6. Web-only steps for the user: org avatar (`images/rassp_icon.png`), org profile fields, invite
   members (PI + one backup as Owner), optional branch protection, optional custom domain.

### Setting up another computer

- This folder syncs via OneDrive, including `.git`. Do not work on both computers at the same
  time; run `git status` and `git pull` before starting.
- Install tools if missing: `winget install --id GitHub.cli -e`, then
  `gh auth login -h github.com -p https -w -s repo,workflow,admin:org` and `gh auth setup-git`;
  `winget install RubyInstallerTeam.RubyWithDevKit.3.3` then `ridk install 3` and `bundle install`
  (installs gems into the Ruby folder, not into OneDrive); `pip install pybtex` for publications.
- Local preview: `bundle exec jekyll serve` → http://localhost:4000.
