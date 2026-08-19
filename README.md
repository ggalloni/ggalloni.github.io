# ggalloni.github.io

Personal academic site, built on [al-folio](https://github.com/alshedivat/al-folio).
Live at <https://ggalloni.github.io>.

## Editing

| What | Where |
| --- | --- |
| Landing page | `_pages/about.md` |
| Research | `_pages/research.md` |
| Publications | `_bibliography/papers.bib` — the page is generated from it |
| Software | `_pages/software.md` (prose) + `_data/repositories.yml` (repo cards) |
| Teaching | `_pages/teaching.md` |
| News items on the landing page | `_news/*.md` |
| Links and IDs | `_data/socials.yml` |
| CV | `_data/cv.yml` (the `/cv/` page) **and** `cv.tex` (the PDF) |

Publications come from `_bibliography/papers.bib`, which is a copy of
`all_publications.bib` in the [autoCV](https://github.com/ggalloni/autoCV) repo with
al-folio's extra fields added (`abbr`, `arxiv`, `code`, `selected`). To add a paper, paste
the INSPIRE-HEP BibTeX entry and optionally add those fields; `selected = {true}` puts it on
the landing page.

The CV exists twice, on purpose, and **both copies must be updated together**:

- `_data/cv.yml` drives the HTML `/cv/` page.
- `cv.tex` is the PDF (classic academic style: EB Garamond, letter-spaced small-caps
  headings). The deploy workflow compiles it with pdflatex to `assets/pdf/cv.pdf`, which is
  what the download icon on `/cv/` points at. The PDF itself is not committed.

To check a PDF change locally:

```bash
pdflatex cv.tex
```

Page `description:` front matter must be **plain text** — al-folio injects it into an HTML
attribute, so any markup breaks out and leaks visible characters at the top of the page.
`bin/check_site.py` guards against this.

## Local theme overrides

Three files diverge from stock al-folio. Everything else is gem-owned, so upstream merges
stay cheap.

| File | Why |
| --- | --- |
| `assets/css/main.scss` | Copy of the gem's, with `@use "local"` appended |
| `_sass/_local.scss` | All site-specific CSS: palette, fonts, sidebar and mobile fixes |
| `assets/fonts/EBGaramond-*.woff2` | Self-hosted, subset from texlive's OTFs (~25 KB each) |

The palette is set as CSS custom-property overrides in `_local.scss`, **not** as a local
`_sass/_variables.scss`. The theme's `_themes.scss` resolves `@use "variables"` to its own
sibling inside the gem, so a local copy of that file is never reached.

Colours are the two poles of a CMB temperature map: cold blue `#1f4e8c` for links and
navigation, warm `#c8461e` for current state only. `_data/venues.yml` puts refereed journals
on the cold end and preprints on the warm one, so the publication badges read on the same
axis.

To regenerate the font subsets after a texlive update:

```bash
python3 -m fontTools.subset /usr/share/texlive/texmf-dist/fonts/opentype/public/ebgaramond/EBGaramond-Regular.otf --unicodes="U+0000-00FF,U+2000-206F,U+2212" --layout-features="kern,liga,calt,onum,pnum" --flavor=woff2 --output-file=assets/fonts/EBGaramond-Regular.woff2
```

## Deploying

Pushing to `master` triggers `.github/workflows/deploy.yml`, which builds the site and
pushes `_site` to the `gh-pages` branch. GitHub Pages must be set to serve from
`gh-pages` / root.

## Local preview

Needs Docker (no Ruby on the host):

```bash
docker compose up
```

Then open <http://localhost:8080>.

## Upstream updates

```bash
git remote add upstream https://github.com/alshedivat/al-folio.git
git fetch upstream && git merge upstream/master
```
