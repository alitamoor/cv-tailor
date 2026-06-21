# Step 6 — Build the document

This step branches on `profile.yaml: output.format` (`docx` or `latex`) and `environment.mode`.

Pick the path:

| output.format | source | mode | Path |
|---|---|---|---|
| `docx` | docx available | agent | **A — unpack/repack** (preserves formatting) |
| `docx` | PDF only | agent | **B — no docx source** (offer LaTeX or ask for a docx) |
| `latex` | any | agent | **C — LaTeX render** |
| any | — | inline | **D — inline output** |

---

## Path A — Agent mode, docx output, docx source: unpack → edit XML → repack

**Condition:** `environment.mode == "agent"` AND `output.format == "docx"` AND `source_cv.format == "docx"` AND the file at `source_cv.path` is readable.

This path preserves your exact formatting — fonts, spacing, margins, line heights — by editing the document XML in place rather than rebuilding from scratch.

### Steps

1. Unpack the source docx:
   ```
   python scripts/unpack.py <source_cv_path> /tmp/cv_unpacked
   ```

2. Open `/tmp/cv_unpacked/word/document.xml`.

3. Locate the relevant text nodes. Search by content strings from the original CV (employer names, section headers, key phrases). The XML structure will be paragraphs (`<w:p>`) containing runs (`<w:r>`) containing text (`<w:t>`).

4. Replace bullet text, one bullet at a time, with the rewritten text from step 4. Replace the profile paragraph text with the rewrite from step 5.

5. **Preserve all XML attributes exactly.** Only change `<w:t>` content — nothing else. Don't touch `<w:rPr>` (font, bold, size, color), `<w:pPr>` (paragraph style, indent, spacing), or any relationship IDs.

6. **Merge split runs before editing.** A single word or phrase may be split across multiple `<w:r>` elements due to tracked changes, spellcheck marks, or formatting mid-word. Merge all runs within a paragraph that share the same `<w:rPr>` before replacing text — otherwise you'll produce garbled output.

7. Repack the edited directory:
   ```
   python scripts/pack.py /tmp/cv_unpacked <output_path>
   ```
   where `output_path` follows `profile.yaml: output.naming_pattern` and resolves to the user's `output/<Company Name>/` directory.

8. Confirm the file was created. Report the full output path.

---

## Path B — Agent mode, docx output, but no usable docx source

**Condition:** `output.format == "docx"` AND `source_cv.format == "pdf"` (or the docx is structurally unparseable).

You can't preserve docx formatting from a PDF — there's no XML to edit. Don't rebuild a generic docx from scratch; it loses the whole point of the docx path. Instead, tell the user:

> "Your source CV is a PDF, so I can't preserve its exact docx formatting. Two options: (1) I build a clean, single-page PDF via LaTeX (you compile it in Overleaf in one click), or (2) you upload your CV as a .docx and I preserve your existing formatting. Which do you want?"

- If they pick LaTeX → switch to **Path C**.
- If they'll provide a docx → wait for it, then use **Path A**.

---

## Path C — Agent mode, LaTeX output

**Condition:** `environment.mode == "agent"` AND `output.format == "latex"` (or the user chose LaTeX in Path B).

LaTeX builds from the tailored content directly — it doesn't read the source CV at all. The result is a clean, single-page, ATS-safe PDF the user compiles in Overleaf or locally.

### Steps

1. Assemble the tailored content into a JSON file. Use the rewritten bullets (step 4), the profile paragraph (step 5), and the static facts from `profile.yaml` (name, contact, education, languages, awards, certifications). Shape:

   ```json
   {
     "name": "...",
     "contact": {"phone": "", "email": "", "linkedin": "", "portfolio": "", "github": ""},
     "summary": "<profile paragraph from step 5>",
     "experience": [
       {"title": "", "employer": "", "dates": "", "location": "",
        "bullets": ["<tailored bullet>", "..."]}
     ],
     "skills": {"Category": ["..."]},
     "education": [{"degree": "", "institution": "", "dates": "", "location": ""}],
     "certifications": ["..."],
     "awards": ["..."],
     "languages": ["..."]
   }
   ```

   - `skills` can be a flat list or a category→list dict.
   - Respect `omit_from_profile`: an omitted education entry still goes in `education` (it belongs in the Education section), but its degree/institution must not appear in `summary`.
   - Drop any section by omitting its key (e.g., no awards → leave out `awards`).

   Write the JSON to `/tmp/resume_content.json`.

2. Render the `.tex`:
   ```
   python scripts/render_latex.py --content /tmp/resume_content.json --output <output_path>
   ```
   where `output_path` follows `profile.yaml: output.naming_pattern` (with a `.tex` extension) in the user's `output/<Company Name>/` directory.

   The script escapes LaTeX special characters (`$ & % # _ { } ~ ^`) automatically — don't pre-escape them in the JSON.

3. Compile to PDF if a LaTeX distribution is available:
   ```
   pdflatex -interaction=nonstopmode -output-directory <output_dir> <output_path>
   ```
   - If `pdflatex` is installed, run it twice (LaTeX needs a second pass for layout) and report the PDF path.
   - If `pdflatex` is not installed, tell the user: "The .tex is ready at [path]. To get a PDF: upload it to [Overleaf](https://www.overleaf.com), set the compiler to pdfLaTeX, and click Recompile. Or install MiKTeX/TeX Live to compile locally."

4. Confirm the file(s) created. Report the full path(s).

---

## Path D — Inline mode (claude.ai or no code execution)

**Condition:** `environment.mode == "inline"` (or code execution is unavailable).

You can't run scripts here, so deliver the content for the user to apply or compile themselves.

**If `output.format == "docx"` and source is docx:**
Produce a clear, section-by-section edit list the user applies manually in Word or Google Docs:

```
PROFILE PARAGRAPH
Replace with:
[new profile text]

PROFESSIONAL EXPERIENCE — [Employer Name] ([Dates])
Bullet 1: Replace with:
[new bullet]
Bullet 2: Replace with:
[new bullet]
...
```

**If `output.format == "latex"` (or source is PDF):**
Output the complete `.tex` file as a code block. Build it from the same content as Path C — apply the LaTeX template structure from `templates/resume_template.tex` and escape special characters by hand (`$`→`\$`, `&`→`\&`, `%`→`\%`, `#`→`\#`, `_`→`\_`). Then tell the user:

> "Here's your resume as LaTeX. Copy it into a new [Overleaf](https://www.overleaf.com) project (set compiler to pdfLaTeX) and click Recompile to get your PDF."

In every inline case: tell the user what you've done and why ("I can't build the file directly in this environment, so here's the content to apply").
