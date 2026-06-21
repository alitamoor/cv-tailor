# Step 5 — Profile paragraph rewrite

Load `rules/anti-ai.md` (primary reference — the profile is prose, not bullets, so all voice rules apply directly).
Load `profile.yaml: behavioral_tone` and `profile.yaml: differentiators`.

Check `profile.yaml: education[*].omit_from_profile` before writing. Any entry flagged `true` must not appear anywhere in the profile paragraph — not the degree name, not the institution, not an implied reference.

## What to write

**Target length:** ~80 words. Hard cap: 100 words. If you're at 110, cut — don't tighten the font.

**Open with the JD's job title** (or a close variant). This anchors the paragraph for ATS parsing and immediately tells the reader what the candidate is applying as.

**Include 2–3 JD keywords** from step 2, where they're accurate and natural. If they don't fit naturally, don't force them. A keyword crammed into an awkward sentence hurts more than it helps.

**Include the single most impressive relevant metric.** Choose the number that is both (a) impressive and (b) directly relevant to *this* JD. If the biggest number in the profile is irrelevant to this role, pick the most relevant one instead.

**Apply `behavioral_tone.notes`.** If the user has tone guidance ("lead with commercial impact first," "startup-founding framing"), honor it. This is more important than any generic "strong profile" formula.

**Pick 1–2 differentiators** from `profile.yaml: differentiators` that best match this JD's `weight_hint`. Never list all of them — that's what the full CV is for. Pick the ones that are most distinctive for *this* role.

## Apply rules/anti-ai.md in full

The profile paragraph is prose. All of these apply:
- Contractions
- Direct voice (no passive)
- Varied rhythm (no metronome pacing)
- No banned words (§3A through §3F)
- No negative parallelisms (§3F) — especially dangerous in profile paragraphs
- No puffery or significance inflation (§4A)
- No rule of three (§4B)

The profile paragraph is the most-read sentence on the CV. It also shows AI fingerprints most clearly when written carelessly. Apply the litmus test: does this sound like the user, or like AI writing a profile for a person?

Proceed to step 6.
