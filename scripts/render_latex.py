#!/usr/bin/env python3
"""Render a tailored resume to a single-page .tex file.

Reads a JSON content file (the tailored output assembled during the workflow)
and fills templates/resume_template.tex, escaping LaTeX special characters so
the user never has to. Stdlib only.

Usage:
    python scripts/render_latex.py --content out/resume.json --output out/resume.tex
    python scripts/render_latex.py --content out/resume.json --output out/resume.tex \
        --template templates/resume_template.tex

Content JSON shape (all fields optional except name; omit a section to drop it):
{
  "name": "Alex Chen",
  "contact": {
    "phone": "+1 555 123 4567",
    "email": "alex@example.com",
    "linkedin": "https://linkedin.com/in/alexchen",
    "portfolio": "https://alexchen.dev",
    "github": "https://github.com/alexchen"
  },
  "summary": "Senior Sales Engineer with ...",
  "experience": [
    {
      "title": "Senior Sales Engineer",
      "employer": "Meridian Data Systems",
      "dates": "Mar 2021 - Present",
      "location": "Austin, TX",
      "bullets": ["Closed $4.2M ARR ...", "Reduced sales cycle ..."]
    }
  ],
  "skills": {"Sales": ["Salesforce", "HubSpot"], "Technical": ["SQL", "Kubernetes"]},
  "education": [
    {"degree": "B.Sc. Computer Science", "institution": "UT Austin",
     "dates": "2012-2016", "location": "Austin, TX"}
  ],
  "certifications": ["Certified Kubernetes Administrator (CKA), 2022"],
  "awards": ["President's Club - Meridian, 2022 and 2023"],
  "languages": ["English (native)", "Mandarin (conversational)"]
}

"skills" may be a flat list (["SQL", "Salesforce"]) or a dict of category -> list.
"""
import argparse
import json
import sys
from pathlib import Path

MARKER = "%%RESUME_BODY%%"

# Order: escape backslash first, then the rest.
_LATEX_ESCAPES = [
    ("\\", r"\textbackslash{}"),
    ("&", r"\&"),
    ("%", r"\%"),
    ("$", r"\$"),
    ("#", r"\#"),
    ("_", r"\_"),
    ("{", r"\{"),
    ("}", r"\}"),
    ("~", r"\textasciitilde{}"),
    ("^", r"\textasciicircum{}"),
]


def esc(text) -> str:
    """Escape LaTeX special characters in a plain string."""
    if text is None:
        return ""
    s = str(text)
    for char, repl in _LATEX_ESCAPES:
        s = s.replace(char, repl)
    return s


def _display_url(url: str) -> str:
    """Strip scheme and trailing slash for a clean visible link label."""
    d = url.replace("https://", "").replace("http://", "").rstrip("/")
    return d


def build_header(content: dict) -> str:
    name = esc(content.get("name", ""))
    contact = content.get("contact", {}) or {}

    parts = []
    if contact.get("phone"):
        parts.append(esc(contact["phone"]))
    if contact.get("email"):
        email = contact["email"]
        parts.append(f"\\href{{mailto:{email}}}{{\\underline{{{esc(email)}}}}}")
    for key in ("linkedin", "portfolio", "github"):
        url = contact.get(key)
        if url:
            parts.append(f"\\href{{{url}}}{{\\underline{{{esc(_display_url(url))}}}}}")

    sep = " $|$\n    "
    lines = [
        "%----------HEADING----------",
        "\\begin{center}",
        f"    \\textbf{{\\Huge \\scshape {name}}} \\\\ \\vspace{{1pt}}",
        "    \\small " + sep.join(parts),
        "\\end{center}",
    ]
    return "\n".join(lines)


def build_summary(content: dict) -> str:
    summary = content.get("summary")
    if not summary:
        return ""
    return (
        "%----------SUMMARY----------\n"
        "\\section{Summary}\n"
        f"\\small{{{esc(summary)}}}\n\\vspace{{-4pt}}"
    )


def build_experience(content: dict) -> str:
    roles = content.get("experience") or []
    if not roles:
        return ""
    out = ["%----------EXPERIENCE----------", "\\section{Professional Experience}",
           "  \\resumeSubHeadingListStart"]
    for r in roles:
        out.append(
            "    \\resumeSubheading\n"
            f"      {{{esc(r.get('employer', ''))}}}{{{esc(r.get('location', ''))}}}\n"
            f"      {{{esc(r.get('title', ''))}}}{{{esc(r.get('dates', ''))}}}"
        )
        bullets = r.get("bullets") or []
        if bullets:
            out.append("      \\resumeItemListStart")
            for b in bullets:
                out.append(f"        \\resumeItem{{{esc(b)}}}")
            out.append("      \\resumeItemListEnd")
    out.append("  \\resumeSubHeadingListEnd")
    return "\n".join(out)


def build_skills(content: dict) -> str:
    skills = content.get("skills")
    if not skills:
        return ""
    out = ["%----------SKILLS----------", "\\section{Core Competencies}",
           " \\begin{itemize}[leftmargin=0.15in, label={}]",
           "    \\small{\\item{"]
    if isinstance(skills, dict):
        rows = []
        for category, items in skills.items():
            joined = ", ".join(esc(i) for i in items)
            rows.append(f"     \\textbf{{{esc(category)}}}{{: {joined}}}")
        out.append(" \\\\\n".join(rows))
    else:
        out.append("     " + ", ".join(esc(i) for i in skills))
    out.append("    }}")
    out.append(" \\end{itemize}")
    return "\n".join(out)


def build_education(content: dict) -> str:
    edu = content.get("education") or []
    if not edu:
        return ""
    out = ["%----------EDUCATION----------", "\\section{Education}",
           "  \\resumeSubHeadingListStart"]
    for e in edu:
        out.append(
            "    \\resumeSubheading\n"
            f"      {{{esc(e.get('institution', ''))}}}{{{esc(e.get('location', ''))}}}\n"
            f"      {{{esc(e.get('degree', ''))}}}{{{esc(e.get('dates', ''))}}}"
        )
    out.append("  \\resumeSubHeadingListEnd")
    return "\n".join(out)


def build_simple_list(content: dict, key: str, heading: str) -> str:
    items = content.get(key) or []
    if not items:
        return ""
    out = [f"%----------{key.upper()}----------", f"\\section{{{heading}}}",
           "  \\resumeSubHeadingListStart", "    \\resumeItemListStart"]
    for i in items:
        out.append(f"      \\resumeItem{{{esc(i)}}}")
    out.append("    \\resumeItemListEnd")
    out.append("  \\resumeSubHeadingListEnd")
    return "\n".join(out)


def render(content: dict, template: str) -> str:
    sections = [
        build_header(content),
        build_summary(content),
        build_experience(content),
        build_skills(content),
        build_education(content),
        build_simple_list(content, "certifications", "Certifications"),
        build_simple_list(content, "awards", "Awards"),
        build_simple_list(content, "languages", "Languages"),
    ]
    body = "\n\n".join(s for s in sections if s)
    if MARKER not in template:
        raise ValueError(f"Template is missing the {MARKER} marker.")
    return template.replace(MARKER, body)


def main() -> int:
    ap = argparse.ArgumentParser(description="Render a tailored resume to .tex")
    ap.add_argument("--content", required=True, help="Path to resume content JSON")
    ap.add_argument("--output", required=True, help="Path to write the .tex file")
    ap.add_argument(
        "--template",
        default=str(Path(__file__).resolve().parent.parent / "templates" / "resume_template.tex"),
        help="Path to the .tex template (default: templates/resume_template.tex)",
    )
    args = ap.parse_args()

    content_path = Path(args.content).expanduser().resolve()
    template_path = Path(args.template).expanduser().resolve()
    out_path = Path(args.output).expanduser().resolve()

    if not content_path.exists():
        print(f"Error: content file not found: {content_path}", file=sys.stderr)
        return 1
    if not template_path.exists():
        print(f"Error: template not found: {template_path}", file=sys.stderr)
        return 1

    content = json.loads(content_path.read_text())
    if not content.get("name"):
        print("Error: content JSON must include a 'name' field.", file=sys.stderr)
        return 1

    template = template_path.read_text()
    tex = render(content, template)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(tex)
    print(out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
