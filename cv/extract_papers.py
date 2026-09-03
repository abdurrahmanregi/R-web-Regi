"""Pull titles and abstracts from each paper's titleInput.tex into the CV and Hugo."""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
MANIFEST = ROOT / "papers.json"
OUT_DIR = ROOT / "generated"
OUT_FILE = OUT_DIR / "research_in_progress.tex"
HUGO_PUB_DIR = REPO / "content" / "publication"
GENERATED_MARKER = "generated-by: cv/extract_papers.py"
SITE_URL = "https://regikusumaatmadja.com"


def find_braced_arg(text: str, open_brace: int) -> tuple[str, int]:
    if text[open_brace] != "{":
        raise ValueError("expected '{'")
    depth = 0
    i = open_brace
    while i < len(text):
        ch = text[i]
        if ch == "\\" and i + 1 < len(text) and text[i + 1] in "{}\\":
            i += 2
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[open_brace + 1 : i], i + 1
        i += 1
    raise ValueError("unbalanced braces")


def strip_command(text: str, name: str) -> str:
    pattern = re.compile(r"\\" + name + r"\s*\{")
    while True:
        match = pattern.search(text)
        if not match:
            return text
        _, end = find_braced_arg(text, match.end() - 1)
        text = text[: match.start()] + text[end:]


def strip_line_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        out = []
        i = 0
        while i < len(line):
            if line[i] == "\\" and i + 1 < len(line):
                out.append(line[i : i + 2])
                i += 2
                continue
            if line[i] == "%":
                break
            out.append(line[i])
            i += 1
        lines.append("".join(out))
    return "\n".join(lines)


def collapse_ws(text: str) -> str:
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_title(tex: str) -> str:
    match = re.search(r"\\title\s*\{", tex)
    if match:
        raw, _ = find_braced_arg(tex, match.end() - 1)
        raw = strip_command(raw, "thanks")
        raw = strip_line_comments(raw)
        raw = re.sub(r"\\(?:Large|large|bfseries|textbf)\s*", "", raw)
        raw = re.sub(r"\\\\(?:\[[^\]]*\])?", " ", raw)
        title = collapse_ws(raw).strip(" {}")
        if title:
            return title

    bf = re.search(r"\\bfseries\s*([^}\\]+)", tex)
    small = re.search(r"\{\\small\s+([^}]+)\}", tex)
    if bf:
        main = collapse_ws(bf.group(1))
        if small:
            sub = collapse_ws(strip_line_comments(small.group(1)))
            return f"{main}: {sub}"
        return main

    raise ValueError("could not find a title")


def extract_abstract(tex: str) -> str:
    match = re.search(r"\\begin\{abstract\}(.*)\\end\{abstract\}", tex, re.S)
    if not match:
        raise ValueError("could not find abstract")
    body = strip_line_comments(match.group(1))
    kept = []
    for line in body.splitlines():
        if re.search(r"(?i)\\textbf\{Keywords\}|Keywords:|\\textbf\{JEL|JEL Codes:|JEL:", line):
            continue
        kept.append(line)
    body = "\n".join(kept)
    body = re.sub(r"\\noindent\s*", "", body)
    body = re.sub(r"\\footnotesize\s*", "", body)
    body = re.sub(r"\\enspace\s*", " ", body)
    body = re.sub(r"\\bigskip\s*", "", body)
    body = re.sub(r"\\vspace\*?\{[^}]*\}\s*", "", body)
    body = re.sub(r"\\setlength\{[^}]*\}\{[^}]*\}\s*", "", body)
    body = re.sub(r"\\\\(?:\[[^\]]*\])?", " ", body)
    return collapse_ws(body)


def latex_to_markdown(text: str) -> str:
    text = text.replace(r"\&", "&")
    text = text.replace(r"\%", "%")
    text = text.replace(r"\$", "$")
    text = text.replace(r"\`a", "à")
    text = re.sub(r"\\emph\{([^}]*)\}", r"*\1*", text)
    text = re.sub(r"\\textit\{([^}]*)\}", r"*\1*", text)
    text = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", text)
    text = text.replace("``", '"').replace("''", '"')
    text = text.replace(r"\ ", " ")
    text = re.sub(r"\\hspace\*?\{[^}]*\}", " ", text)
    text = text.replace("---", ", ")
    text = text.replace("--", "-")
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?", "", text)
    text = text.replace("{", "").replace("}", "")
    return collapse_ws(text)


def heading(title: str, job_market: bool, with_authors: str | None, pdf_url: str | None = None) -> str:
    shown = f"{title} (Job Market Paper)" if job_market else title
    bold = f"\\textbf{{{shown}}}"
    if pdf_url:
        head = f"{{\\hypersetup{{urlcolor=blue}}\\href{{{pdf_url}}}{{{bold}}}}}"
    else:
        head = bold
    if with_authors:
        head += f", with {with_authors}."
    return head + "\\\\[0.35em]"


def public_pdf_url(paper: dict) -> str | None:
    if not paper.get("pdf"):
        return None
    return f"{SITE_URL}/publication/{paper['id']}/{pdf_dest_name(paper['id'])}"


def render(papers: list[dict]) -> str:
    blocks = ["% Auto-generated by extract_papers.py. Edit papers.json or the paper titleInput.tex files.", "\\section*{Research in Progress}"]
    for i, paper in enumerate(papers):
        src = Path(paper["source"])
        if not src.is_file():
            raise FileNotFoundError(f"paper source not found: {src}")
        tex = strip_line_comments(src.read_text(encoding="utf-8"))
        title = extract_title(tex)
        abstract = extract_abstract(tex)
        if not abstract:
            raise ValueError(f"empty abstract in {src}")
        block = [
            heading(title, bool(paper.get("job_market_paper")), paper.get("with"), public_pdf_url(paper)),
            abstract + "\\par",
        ]
        presentation = paper.get("presentation")
        if presentation:
            block.append("\\vspace*{0.05in}")
            block.append(f"\\textit{{Presentation}}: {presentation}\\par")
        blocks.append("\n".join(block))
        if i != len(papers) - 1:
            blocks.append("\\vspace*{0.12in}")
    return "\n".join(blocks) + "\n"


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def yaml_block(text: str, indent: int = 2) -> str:
    pad = " " * indent
    return "|\n" + "\n".join(pad + line if line else pad for line in text.splitlines())


def pdf_dest_name(paper_id: str) -> str:
    return f"kusumaatmadja_{paper_id.replace('-', '_')}.pdf"


def copy_paper_pdf(paper: dict) -> str | None:
    rel = paper.get("pdf")
    if not rel:
        return None
    src = Path(rel)
    if not src.is_absolute():
        src = (ROOT / src).resolve()
    if not src.is_file():
        raise FileNotFoundError(f"paper PDF not found: {src}")
    name = pdf_dest_name(paper["id"])
    dest_dir = HUGO_PUB_DIR / paper["id"]
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / name
    shutil.copy2(src, dest)
    return name


def write_hugo_page(paper_id: str, title: str, abstract: str, authors: list[str], date: str, publication_types: list[str], publication: str, doi: str = "", url_pdf: str = "") -> Path:
    folder = HUGO_PUB_DIR / paper_id
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "index.md"
    lines = [
        "---",
        f"# {GENERATED_MARKER}",
        f"title: {yaml_quote(title)}",
        "authors:",
    ]
    for author in authors:
        lines.append(f"- {yaml_quote(author)}")
    lines.extend(
        [
            f"date: {date}",
            f"publishDate: {date}",
            "publication_types:",
        ]
    )
    for pub_type in publication_types:
        lines.append(f'- "{pub_type}"')
    lines.append(f"publication: {yaml_quote(publication)}")
    if doi:
        lines.append(f"doi: {yaml_quote(doi)}")
    if url_pdf:
        lines.append(f"url_pdf: {yaml_quote(url_pdf)}")
    lines.append("abstract: " + yaml_block(abstract))
    lines.extend(
        [
            "featured: false",
            "---",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_hugo_publications(spec: dict) -> list[str]:
    written = []
    for paper in spec["papers"]:
        src = Path(paper["source"])
        tex = strip_line_comments(src.read_text(encoding="utf-8"))
        title = latex_to_markdown(extract_title(tex))
        abstract = latex_to_markdown(extract_abstract(tex))
        pdf_name = copy_paper_pdf(paper)
        url_pdf = f"/publication/{paper['id']}/{pdf_name}" if pdf_name else ""
        path = write_hugo_page(
            paper["id"],
            title,
            abstract,
            paper.get("authors") or ["admin"],
            paper["date"],
            paper.get("publication_types") or ["3"],
            paper.get("publication") or "Working paper",
            url_pdf=url_pdf,
        )
        written.append(f"{path.name}: {title}")
        if pdf_name:
            written.append(f"  pdf {pdf_name}")
    for paper in spec.get("published") or []:
        path = write_hugo_page(
            paper["id"],
            paper["title"],
            paper["abstract"],
            paper.get("authors") or ["admin"],
            paper["date"],
            paper.get("publication_types") or ["2"],
            paper["publication"],
            paper.get("doi") or "",
        )
        written.append(f"{path.name}: {paper['title']}")
    return written


def main() -> int:
    spec = json.loads(MANIFEST.read_text(encoding="utf-8"))
    papers = spec["papers"]
    for paper in papers:
        paper["source"] = str((ROOT / paper["source"]).resolve())
    tex = render(papers)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(tex, encoding="utf-8")
    print(f"Wrote {OUT_FILE}")
    for paper in papers:
        src = Path(paper["source"])
        title = extract_title(strip_line_comments(src.read_text(encoding="utf-8")))
        print(f"  - {title}")
    for line in write_hugo_publications(spec):
        print(f"  hugo {line}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"extract_papers.py: {exc}", file=sys.stderr)
        raise SystemExit(1)
