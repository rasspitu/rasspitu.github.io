Build the RASSP research group website described in CLAUDE.md. Read CLAUDE.md completely before doing anything.

Goal: a GitHub Pages site with the same structure and look-and-feel as https://mspritu.github.io/ (Jekyll + AcademicPages), but with our own branding, colors and content. Do not copy any text, images or data from that site.

Work in these phases and stop for my confirmation at the end of phase 0 (if anything is blocked) and at the end of phase 1:

**Phase 0 — GitHub setup**
- Our GitHub organization is `rasspitu`. The site repo must be `rasspitu/rasspitu.github.io`, served at https://rasspitu.github.io/.
- Follow the "GitHub setup" section of CLAUDE.md: check tools and `gh auth status`, create (or clone) the repo, and work inside it. If authentication is missing, tell me the exact command to run and wait.

**Phase 1 — Plan**
- Inspect the current repo (it may be empty or a fresh AcademicPages fork).
- Propose the directory structure, the list of pages, the data files and the deployment method (GitHub Actions preferred).
- List every question from the "Open questions" section of CLAUDE.md that you need answered, plus any new ones.

**Phase 2 — Scaffold**
- Set up AcademicPages (clone/fork if the repo is empty), strip all unused template content and the template author's personal data.
- Configure `_config.yml`, navigation (Home, Research, Publications, People, Equipments, Contact; News only if I confirm).
- Add the logo files from `images/`, generate favicons, apply the color palette through SCSS variables.

**Phase 3 — Content structure**
- Create the data files and layouts from the "Data model" section.
- Fill research themes from CLAUDE.md. Use clearly marked TODO placeholders for people, publications and equipment; never invent real-looking entries.
- Adapt the publication generator so I can drop in a BibTeX file and regenerate the Publications page.

**Phase 4 — Deploy and verify**
- Add the GitHub Actions workflow for Pages, push, set the Pages source to GitHub Actions via `gh api`, watch the run and confirm https://rasspitu.github.io/ is live.
- Create the organization profile repo `rasspitu/.github` with `profile/README.md` and set repo topics.
- Build locally, fix all errors and warnings, then run through the verification checklist in CLAUDE.md and report the result.
- Write README.md with editing instructions for group members.
- Finish with a checklist of the web-only steps from CLAUDE.md (org avatar, profile fields, inviting members, roles) that I must do in the browser.

Keep commits small and descriptive. When something is ambiguous, ask instead of guessing.
