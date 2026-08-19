#!/usr/bin/env python3
"""Pre-push sanity check: catches the config/content mistakes that break a CI build.

Run from the repo root:  python3 bin/check_site.py
Not a substitute for `docker compose up` — just the cheap checks worth having before a push.
"""

import glob
import os
import pathlib
import re
import sys

import yaml

fail = []


def front_matter(path):
    txt = open(path).read()
    if not txt.startswith("---"):
        fail.append(f"{path}: no YAML front matter")
        return {}
    return yaml.safe_load(txt.split("---")[1]) or {}


for f in glob.glob("_data/*.yml") + ["_config.yml"]:
    try:
        yaml.safe_load(open(f))
    except Exception as e:
        fail.append(f"{f}: {e}")

pages = glob.glob("_pages/*.md") + glob.glob("_news/*.md")
for f in pages:
    try:
        front_matter(f)
    except Exception as e:
        fail.append(f"{f}: {e}")

cfg = yaml.safe_load(open("_config.yml"))
if cfg["url"] != "https://ggalloni.github.io":
    fail.append(f"_config.yml: url is {cfg['url']!r}")
if cfg["baseurl"]:
    fail.append(f"_config.yml: baseurl must be blank for a user site, got {cfg['baseurl']!r}")
if cfg["jekyll_get_json"]:
    fail.append("_config.yml: jekyll_get_json points at a file; the CV feature is off")

# jekyll-scholar needs the author name to match the bib, or nothing gets bolded
if cfg["scholar"]["last_name"] != ["Galloni"]:
    fail.append(f"_config.yml: scholar.last_name is {cfg['scholar']['last_name']!r}")

# a missing woff2 fails silently: headings just fall back to Georgia
local_scss = pathlib.Path("_sass/_local.scss")
if local_scss.exists():
    for font in re.findall(r'url\("(/assets/fonts/[^"]+)"\)', local_scss.read_text()):
        if not os.path.exists(font.lstrip("/")):
            fail.append(f"_sass/_local.scss: missing font {font}")

# The CV renderer dispatches on section NAME. A section it does not recognise falls to a
# generic branch that renders only `label`/`details` or `bullet` entries — anything else
# produces a heading with nothing under it.
CV_TEMPLATED = {
    "Experience", "Volunteer", "Education", "Awards", "Honors and Awards", "Publications",
    "Skills", "Languages", "Interests", "Academic Interests", "Certificates", "Projects",
    "Open Source Projects", "References",
}
cv = yaml.safe_load(open("_data/cv.yml"))["cv"]
for name, entries in (cv.get("sections") or {}).items():
    for i, e in enumerate(entries):
        if any(not isinstance(h, str) for h in (e.get("highlights") or [])):
            fail.append(f"_data/cv.yml: {name}[{i}] has a non-string highlight "
                        f"(an unquoted 'Key: value' parses as a YAML mapping)")
        if name in CV_TEMPLATED:
            continue
        if not (("label" in e and "details" in e) or "bullet" in e):
            fail.append(f"_data/cv.yml: {name}[{i}] would render empty — an unrecognised "
                        f"section needs label+details or bullet, got {sorted(e)}")

if not os.path.exists("cv.tex"):
    fail.append("cv.tex is missing; the deploy workflow compiles it to assets/pdf/cv.pdf")

# al-folio injects page.description into an HTML attribute; markup in it breaks out
# and leaks visible text at the top of the page.
for f in pages:
    desc = str(front_matter(f).get("description") or "")
    if any(c in desc for c in "<>"):
        fail.append(f"{f}: description contains markup, which leaks into the page")

bib = open("_bibliography/papers.bib").read()
if bib.count("{") != bib.count("}"):
    fail.append(f"papers.bib: unbalanced braces ({bib.count('{')} vs {bib.count('}')})")
keys = re.findall(r"@\w+\{([^,]+),", bib)
if len(keys) != len(set(keys)):
    fail.append("papers.bib: duplicate entry keys")

# internal links must resolve to a page that still exists
live = {"/"} | {p for p in (front_matter(f).get("permalink") for f in pages) if p}
for f in pages:
    for href in re.findall(r"\]\((/[^)#]*)\)", open(f).read()):
        if href not in live:
            fail.append(f"{f}: dead internal link {href}")

# referenced local assets must exist (commented-out lines are placeholders, skip them)
for f in pages + glob.glob("_data/*.yml") + ["_config.yml"]:
    for line in open(f):
        if line.lstrip().startswith("#"):
            continue
        for asset in re.findall(r"assets/[\w/.\-]+", line):
            # cv.pdf is fetched by deploy.yml at build time, so it is absent locally
            if asset in ("assets/pdf/cv.pdf",) or "tailwind" in asset:
                continue
            if not os.path.exists(asset):
                fail.append(f"{f}: missing {asset}")

if fail:
    print("FAIL")
    print("\n".join(f"  {x}" for x in fail))
    sys.exit(1)
print(f"OK — {len(keys)} bib entries, {len(live)} pages: {' '.join(sorted(live))}")
