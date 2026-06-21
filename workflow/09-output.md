# Step 9 — Output

## 1. Save the file

Save to `<user_data_dir>/output/<Company Name>/` using `profile.yaml: output.naming_pattern`.

The naming pattern tokens:
- `{first}` — first name from `profile.yaml: person.name`
- `{last}` — last name from `profile.yaml: person.name`
- `{company}` — company name from the JD, with spaces replaced by underscores

Example: `CV_Alex_Chen_Stripe.docx`

Confirm the file was written. Report the full path.

---

## 2. Before→after summary

Show a concise diff of what changed from the original CV:

- **Profile paragraph:** old vs. new (both in full)
- **Changed bullets:** for any bullet where the metric, framing, or keyword emphasis changed significantly, show old and new versions
- **Added or removed bullets:** list any bullets that were added (shouldn't happen — no fabrication) or removed (due to irrelevance or page limit)
- **Keywords woven in:** briefly note which JD keywords were incorporated and where

Keep this tight. It's a reference, not a narrative.

---

## 3. Flag open items

List anything that needs the user's attention:

- **Missing metrics** — any bullet where you asked for a number but the user declined to provide one, and the bullet was omitted as a result
- **Uncovered gaps** — gaps identified in step 3 that couldn't be addressed by the profile; remind the user to prepare to discuss these in interview
- **Unverified claims** — any company-specific claim that couldn't be confirmed and was therefore removed or flagged
- **Stretch score** — if the fit score was below threshold and the user asked you to continue anyway, note it: "This scored [X]/100 — below your [Y] threshold. Worth reviewing whether the application is the right call."

If there are no open items, skip this section.

---

## 4. Done

One sentence: "Your CV for [Company] is saved at [path]."

Nothing else. No summary of the process. No "I hope this helps." No bullet list of what you just did. The user can read the diff.
