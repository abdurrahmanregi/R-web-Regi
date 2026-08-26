# R-web-Regi

Personal site for [Regi Kusumaatmadja](https://regikusumaatmadja.com/), built with [Hugo](https://gohugo.io/) Academic / Wowchemy via [blogdown](https://bookdown.org/yihui/blogdown/). Production deploys on Netlify from `main`.

## Local site build

Hugo **0.100.0** is pinned in `.Rprofile` and `netlify.toml`. From the repo root, in R:

```r
blogdown::build_site()
```

Or from PowerShell:

```powershell
Rscript -e "blogdown::build_site()"
```

That writes HTML into `public/` (gitignored). Preview with:

```r
blogdown::serve_site()
```

If Hugo is missing, install the pinned version once:

```r
blogdown::install_hugo("0.100.0")
```

Pushing `main` to GitHub is enough for Netlify (`hugo`, publish `public`). You do not need to commit `public/`.

## Curriculum vitae

The CV is edited and compiled in this repo. Do not copy-paste a PDF from Overleaf.

| Role | Path |
|---|---|
| Source | `cv/kusumaatmadja_cv.tex` |
| Paper list (order, coauthors, talks) | `cv/papers.json` |
| Compile | `cv/compile.ps1` |
| Site PDF | `static/kusumaatmadja_cv_tinbergen.pdf` |

```powershell
powershell -ExecutionPolicy Bypass -File cv\compile.ps1
```

The script (1) pulls titles and abstracts from sibling paper repos listed in `cv/papers.json`, (2) writes `cv/generated/research_in_progress.tex`, (3) runs `pdflatex`, (4) copies the PDF to `static/` so Hugo serves it at `/kusumaatmadja_cv_tinbergen.pdf`.

Paper folders are expected next to this repo under `OneDrive/Work/` (for example `../VU-Internal-External-RD/titleInput.tex`). Presentation lists stay in `cv/papers.json`. LaTeX aux files go in `cv/build/` and are gitignored.

Needs a local TeX install (MiKTeX) and Python 3 for the extractor.

## Content

- Homepage widgets: `content/home/`
- About / bio: `content/authors/admin/_index.md`
- Posts: `content/post/`
- Static files (CV PDF, research statement): `static/`
