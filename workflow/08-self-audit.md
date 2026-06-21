# Step 8 — Self-audit

Run each check in order. Fix issues before moving on. Do not pass a failing check and continue.

---

## 1. Banned words (rules/anti-ai.md §3)

Scan every word and phrase in the CV. If any banned term appears — from §3A through §3F — replace it.

§3F (negative parallelisms) is the most dangerous and the easiest to miss. Read every sentence that contains a negation word ("not," "never," "no," "without," "rather than"). If it negates one framing and asserts another, rewrite.

One instance fails the check. Find it, fix it, then re-scan.

---

## 2. Bullet structure (rules/anti-ai-cv-addendum.md)

**Every bullet has ≥ 1 number.**

If any bullet lacks a number:
- **Stop. Do not output the CV.**
- Go back to the user: "The bullet about [X] still doesn't have a number. I can't include it without one — what metric can we attach?"
- Wait for a real figure before continuing.

**No "we"** in any bullet.

**Bullets are verb-led fragments** — not full sentences with subject pronouns. If a bullet starts with "I" or includes "we," it's wrong.

---

## 3. omit_from_profile enforcement

Scan all CV text against the list of education entries where `omit_from_profile: true`.

Confirm that:
- The degree name does not appear in the profile paragraph.
- The institution does not appear in the profile paragraph.
- No implied reference to the omitted entry appears anywhere in the profile text.

It should still appear correctly in the Education section — only the profile paragraph is checked here.

---

## 4. ATS plain-text parse test

Read the CV content as if all formatting were stripped. Confirm that all key information survives:
- Job titles and employers
- Dates (in a consistent format throughout)
- Metrics and numbers
- Section headers (as the expected strings from `rules/ats-rules.md`)

If any critical information would only be readable due to formatting (e.g., a text box, a table cell, colored-only differentiation), it fails. Fix the structure, not the formatting.

---

## 5. Page count check

Estimate page count based on word count and standard CV density. If over `profile.yaml: output.max_pages`:

- Trim bullets by relevance to this JD (least relevant bullets go first).
- Never reduce font size, margin, or line spacing to fit. Trim content.
- If trimming would remove an `always_keep_metrics` entry: flag it to the user instead. Don't auto-remove protected metrics.

---

## 6. Hyperlink check

Any LinkedIn URL or email address in the CV must be a proper hyperlink (a `<w:hyperlink>` element in the docx XML, or a functional link in the JS-built output), not bare plain text.

Also confirm the URL is visible as text (not hidden behind a label like "click here") — per `rules/ats-rules.md`.

---

## 7. Date format consistency

All dates in the CV must use the same format (e.g., "Jan 2020 – Mar 2023" throughout, or "2020–2023" throughout). Mixed formats fail.

---

## 8. Voice DNA litmus test (final pass)

Read the complete CV — profile paragraph and all bullets — as if hearing it for the first time.

Ask: "Does this sound like something the user would actually say, or does it sound like an AI trying very hard?"

If you can feel the AI through rhythm, vocabulary, or a sentence that's too clean — revise until the answer is genuinely "yes, this sounds human."

This test has no checklist. It's judgment. Apply it.

---

After all checks pass: proceed to step 9.
