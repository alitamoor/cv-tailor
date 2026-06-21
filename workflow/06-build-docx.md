# Step 6 — Build docx

This step branches based on source CV format and environment mode.

---

## Agent mode + docx source — unpack → edit XML → repack

**Condition:** `environment.mode == "agent"` AND `source_cv.format == "docx"` AND the file at `source_cv.path` is readable.

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

## Agent mode + PDF source — JS rebuild fallback

**Condition:** `environment.mode == "agent"` AND `source_cv.format == "pdf"` (or docx is structurally unparseable).

Tell the user: "Your source CV is a PDF, so I can't preserve your exact formatting. I'll build a clean ATS-safe docx using a standard template — Arial, US Letter, standard section structure."

Write and execute a Node.js script using the `docx` npm package. The output must meet these specs:

- **Font:** Arial or Calibri, 11pt body, 12pt section headers
- **Page size:** US Letter (8.5" × 11"), 1" margins on all sides
- **Section headers:** bold, 12pt, title case per `rules/ats-rules.md` conventions
- **Bullets:** use `LevelFormat.BULLET` — never unicode bullet characters in text nodes
- **No tables, text boxes, or images**
- **Hyperlinks:** LinkedIn URL and email as proper `ExternalHyperlink` elements, URL visible as text
- **Section order:** Profile | Professional Experience | Education | Languages (if present) | Awards (if present)
- **Max pages:** per `profile.yaml: output.max_pages`

The fallback must still produce a professional, clean document. It's not an afterthought — it's the only output PDF users get.

---

## Inline mode — edit instructions

**Condition:** `environment.mode == "inline"` (or code execution is unavailable).

You can't execute code here, so instead:

**If source is docx:**
Produce a clear, section-by-section edit list the user can apply manually in Word or Google Docs:

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

**If source is PDF (inline mode):**
Produce the full CV as clean plain text, structured for manual copy-paste into a Word template. Lay it out in the correct section order per `rules/ats-rules.md`. Note that the user will need to apply their own formatting.

In both cases: tell the user what you've done and why ("I can't build the file directly in this environment, so here are the exact changes to make").
