# ATS rules

These apply to every CV built by this system. They're not user-configurable — they reflect universal ATS parser constraints that override aesthetic preferences.

## Structural rules

**No tables.** ATS parsers frequently can't read table cells. If your source CV uses a table for a two-column layout (common in designed CVs), it will parse as garbled text or nothing. Use plain paragraphs instead.

**No text boxes.** Content inside a Word text box is invisible to most ATS parsers. Any text in a text box — contact info, sidebar skills, callout sections — won't be parsed.

**No images or graphics.** Profile photos, logos, skill bars, icons: all invisible to parsers. Don't use them.

**No headers or footers for content.** Contact details, page numbers in footers, name in headers: frequently skipped by parsers. Put essential contact info in the body of the document.

**Single-column layout only.** Two-column CVs (a popular European and design-influenced format) break most ATS parsers. Everything must be in a single column, top to bottom.

## Bullet format

**Use standard list bullets only.** The docx unpack/repack path preserves whatever list format the source CV uses — if that source uses unicode characters (→, ✓, ▪, ◆), replace them with standard Word list bullets. The LaTeX path uses the template's native `\resumeItem` bullets, which render as standard dots.

**Never use unicode bullet characters directly in text.** Characters like → ✓ ▪ ◆ ▸ render fine visually but parse inconsistently. Use the Word/docx list format instead.

## Section names

Use these exact header strings — they match the ATS keyword library most systems are tuned to:

- `Professional Experience` (not "Work History," "Career History," "Experience")
- `Education`
- `Core Competencies` or `Skills` (not "Capabilities," "Expertise Areas")
- `Languages` (not "Language Skills")
- `Awards` or `Achievements`

Custom section names ("Where I've Had Impact," "What I Bring") are risky. The parser may not classify them correctly.

## Typography

**Standard fonts only.** Arial, Calibri, Times New Roman, Garamond. Unusual or decorative fonts may not render when the ATS converts to plain text.

**No colored text for body content.** Section headers may use a dark color; body text should be black. Colored text sometimes drops out in plain-text conversion.

**Minimum 10pt font.** Below 10pt some parsers miss content.

**Write hyperlink URLs as visible text.** If you include a LinkedIn URL, show the actual URL — don't hide it behind a label like "LinkedIn Profile." Some parsers strip hyperlinks and keep only the visible text.

## File format

Submit as `.docx`. PDF is widely accepted but DOCX gives the parser direct access to structured XML — more reliable. Never submit `.pages`, `.odt`, or image-based PDFs (scanned documents).
