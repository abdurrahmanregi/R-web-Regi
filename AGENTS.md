# R-web-Regi — agent notes

Hugo Academic / Wowchemy personal site, built locally with **blogdown** and Hugo **0.100.0**, deployed on Netlify from `main`. Live URL: https://regikusumaatmadja.com/

## Build and preview

- Site: `blogdown::build_site()` from repo root (or `Rscript -e "blogdown::build_site()"`). Output is `public/` (gitignored).
- Preview: `blogdown::serve_site()`.
- Missing Hugo: `blogdown::install_hugo("0.100.0")`.
- Do not commit `public/` or `resources/`. Netlify runs `hugo` on push.

## CV and research statement

Local-only compile. Do not round-trip a PDF from Overleaf or Word.

- Edit `cv/kusumaatmadja_cv.tex` for CV chrome (education, talks lists live in `cv/papers.json`).
- Edit `cv/kusumaatmadja_researchstatement.tex` by hand from current paper abstracts. Do not auto-paste abstracts. Paper order: Internal/External, Entry, Assistance, Mergers.
- `cv/compile.ps1` extracts titles/abstracts from sibling paper `titleInput.tex` files, writes `cv/generated/research_in_progress.tex` and `content/publication/<id>/index.md`, compiles the CV and research statement with `pdflatex`, copies to `static/kusumaatmadja_cv_tinbergen.pdf` and `static/kusumaatmadja_researchstatement.pdf`. Netlify does not see the paper repos; commit the generated publication pages and both PDFs.
- Optional `pdf` in `cv/papers.json` copies that file (never moves it) into `content/publication/<id>/kusumaatmadja_<id>.pdf` and sets `url_pdf`. Only listed papers get a PDF button. Commit those PDFs too.
- Dissertation chapter order is the array order in `cv/papers.json`.
- Paper paths are relative to `cv/` and assume repos sit next to this one under `Work/` (JMP, Entry, Subsidy, Mergers).
- Ignore `cv/build/`. Commit the generated snippet and the PDFs so GitHub/Netlify do not need the paper repos or TeX.

About page links: `/kusumaatmadja_cv_tinbergen.pdf` and `/kusumaatmadja_researchstatement.pdf` in `content/authors/admin/_index.md`.

## Do not

- Force-push `main` unless explicitly asked.
- Commit secrets, `.Rhistory`, or Hugo `public/`.
- Change theme vendored under `themes/` unless the task is a theme update.
