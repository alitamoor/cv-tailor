# cv-tailor

Paste a job description. Get a tailored, ATS-safe, fabrication-free CV in your own formatting.

cv-tailor is a Claude skill — a set of instruction files that guide Claude through a structured tailoring workflow. It scores fit, extracts keywords, rewrites bullets with the right metrics and JD language, rebuilds your docx file preserving your formatting, and runs a reviewer pass before finishing. Works in Claude Code (full workflow with agent reviewer and file output) and claude.ai (inline reviewer, edit instructions instead of file output).

---

## What it does

1. **Fits scoring** — scores the JD against your profile on 4 dimensions before writing anything. Stops and asks if the score is below your threshold.
2. **Keyword extraction** — pulls the top 15–20 ATS keywords from the JD, categorised by type.
3. **Gap analysis** — maps JD requirements to your profile. Surfaces real gaps honestly; never covers them with invented experience.
4. **Bullet rewrite** — rewrites bullets per JD using STAR structure and active verbs. Stops and asks if any bullet is missing a metric. Never invents numbers.
5. **Profile paragraph** — ~80 words, opens with the JD title, includes your biggest relevant metric and 1–2 differentiators chosen for this specific role.
6. **Docx build** — edits your source docx XML in place (preserving fonts, spacing, layout) or rebuilds from a clean ATS-safe template if you only have a PDF.
7. **Reviewer pass** — spawns a fresh reviewer (agent mode) or runs a self-critique (inline mode) to catch generic language, unverified company claims, and AI writing tics before the file is saved.
8. **Self-audit** — scans against banned word lists, checks every bullet for a number, verifies omit-from-profile flags, checks ATS structure, and runs a Voice DNA litmus test.
9. **Output** — saves the file, shows a before/after diff, flags any open items.

---

## Prerequisites

- **Claude Code** or **claude.ai** (claude.ai covers inline mode; Claude Code covers the full workflow)
- **Python 3.9+** — for the docx unpack/repack scripts (`scripts/unpack.py`, `scripts/pack.py`)
- **Node.js 18+** and the `docx` npm package — only needed for the JS-fallback path (PDF source CVs in agent mode)

No API keys. No external services. Everything runs in your Claude session.

---

## Quickstart

**1. Clone the repo**
```bash
git clone https://github.com/alitamoor/cv-tailor.git
cd cv-tailor
```

**2. Create your data directory** (outside the repo — this keeps your personal data out of git)
```bash
mkdir -p ../my-cv-tailor-data/source ../my-cv-tailor-data/output
```

Copy your current CV (`.docx` preferred, `.pdf` works) into `../my-cv-tailor-data/source/`.

**3. Run setup**

Open a Claude Code session in the `cv-tailor` directory, or start a claude.ai conversation and share the `SKILL.md` file. Then say:

> "Run cv-tailor setup"

Claude will ask you a series of questions about your background, tone, and differentiators, then write your `profile.yaml` to the data directory.

**4. Tailor a CV**

Paste any job description into the conversation:

> "Here's a JD — tailor my CV for it: [paste JD]"

Claude runs the full workflow and saves the output to `../my-cv-tailor-data/output/<Company>/`.

---

## Using with Claude Code

Add this to your project's `CLAUDE.md`:

```
When the user pastes a job description or asks to tailor their CV,
load and follow SKILL.md from the cv-tailor directory.
```

Or open a session with `cv-tailor/` as your working directory — Claude Code will pick up `SKILL.md` automatically if you reference it.

---

## Privacy

Your CV and `profile.yaml` never leave your machine or your own Claude conversation. Nothing in this repo collects, stores, or transmits personal data. The `.gitignore` explicitly excludes your data directory, source CV, and output files so they can't be accidentally committed.

The repo contains only instruction files and scripts. No personal data, employer names, or metrics from any user are ever part of the codebase.

---

## Environments

| Feature | Claude Code / Cowork | claude.ai |
|---|---|---|
| Fit scoring | Yes | Yes |
| Keyword extraction | Yes | Yes |
| Bullet + profile rewrite | Yes | Yes |
| Docx build (unpack/repack) | Yes — file written directly | No — edit instructions provided |
| Docx build (JS fallback) | Yes — script executed | No — plain text output |
| Reviewer | Spawns general-purpose agent | Self-critique, inline |
| File saved to disk | Yes | No (user applies changes manually) |

---

## Data directory layout

```
my-cv-tailor-data/         ← lives outside the repo, never committed
├── profile.yaml           ← written by interactive setup
├── source/
│   └── CV_YourName.docx   ← your source CV
└── output/
    └── CompanyName/
        └── CV_You_Company.docx
```

---

## Contributing

PRs to `rules/` and `workflow/` are welcome — improvements to the rubric, new ATS rules, better reviewer prompts.

`profile.yaml` is always personal and never committed. Don't add example profiles with real employer names or metrics.

---

## License

MIT. See `LICENSE`.
