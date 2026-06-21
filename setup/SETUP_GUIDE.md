# Setup guide

*Instructions for Claude to run when a user starts without a `profile.yaml`.
Run this as a conversation — ask questions naturally, don't read a form aloud.
Complete all steps before writing the profile.yaml.*

---

## Step A — Orient the user

Explain in 2–3 sentences what's about to happen:

- You're going to ask a few questions about their background and working style.
- Then they'll upload their current CV.
- After that, they can paste any job description and you'll tailor the CV for it automatically.

Keep it short. Don't list every feature. Get to the questions.

---

## Step B — Source CV

Ask the user to share their current CV. They can upload a file or paste the text.

- `.docx` is preferred — it enables direct formatting preservation (unpack/edit/repack).
- `.pdf` works, but the CV will be rebuilt from a clean template since PDFs can't be edited in place.

When they upload:
- Confirm the format and note it for `source_cv.format`.
- Ask where they'd like to save it (default: `my-cv-tailor-data/source/`).
- Note the filename for `source_cv.path`.

---

## Step C — Experience, one employer at a time

Ask about each role. Don't interrogate — ask one natural question and follow up based on what they say.

For each role, you need:
- Job title
- Employer name
- Start and end dates (or "present")
- Location (or "remote")
- The 1–3 metrics that must never be dropped or altered — ask: "What's the number you're most proud of from that role?"
- Maximum bullets to use for this role (suggest 4 for their most recent role, 2–3 for earlier ones)
- Any special framing note — ask: "Anything you'd want me to know about how to position that role? For example, if you wore multiple hats, or if the title undersells what you actually did."

After each role: "Any other roles you want me to know about?" Keep going until they say no.

Work in reverse chronological order (most recent first). That's also the order they'll appear in the CV.

---

## Step D — Education

For each degree or certification:
- Full degree name and institution
- Dates

Then ask explicitly: "Is there anything in your education you'd rather address in conversation than have on the page?" — some people have advanced degrees they prefer not to feature (overqualification concerns, relevance questions, etc.). If yes, set `omit_from_profile: true` for that entry and ask if they'd like to note a reason for their own reference.

---

## Step E — Languages

Ask: "Any languages other than English?" List them with proficiency level.

---

## Step F — Awards or notable recognition

Ask: "Any awards, President's Club memberships, or formal recognition worth including?" If yes, get the exact wording they want — Claude will list them verbatim.

---

## Step G — Tone

Ask these questions, one at a time. Keep it conversational.

1. "How would you describe the way you work — are you more of a builder, a strategist, a closer, a connector? Whatever comes naturally."

2. "Is there a gap between how you're usually perceived and how you'd want to come across?" (This is where you gather the `behavioral_tone.notes` — the framing they actually want.)

3. "Do you have a DISC or DI profile, or any personality/leadership assessment results?" If yes, get the scores. If not, that's fine — skip it.

4. "Are there any specific phrases you hate seeing on CVs? Things like 'passionate about' or 'results-driven'?" Add those to `behavioral_tone.never_say`.

---

## Step H — Anti-AI rules

Tell them:

"There's a default set of banned words and AI writing patterns included with this tool — things like 'leverage,' 'synergy,' and 'innovative' that are dead giveaways of machine-written text. Is there anything specific beyond that list that you want avoided?"

Don't make them review the full list. Just capture any additions for `behavioral_tone.never_say`. They can edit `rules/anti-ai.md` directly later if they want to go deeper.

---

## Step I — Differentiators

Ask: "What are 3–5 things that set you apart from other people in your field — things you'd want a recruiter to remember 30 seconds after putting your CV down?"

For each one, ask: "When do you think that one matters most — what kind of role or company is that most relevant for?" This becomes the `weight_hint` that helps Claude pick the right 1–2 per JD.

---

## Step J — Write and confirm profile.yaml

Once you have all the information:

1. Write the `profile.yaml` file using the schema in `setup/profile.schema.yaml`.
2. Show the user a plain-English summary (not raw YAML) of what you've captured. Example:
   > "I've got 3 roles: Senior SE at Meridian (2021–present), SE at Apex Analytics (2018–2021), and TS Engineer at NovaTech (2016–2018). Source CV is the docx you uploaded. Your top metric to always keep: $4.2M ARR in FY2023. Anti-AI rules: defaults plus 'passionate about' and 'results-driven' banned. Does that look right?"
3. Ask: "Anything I missed or got wrong?" Make corrections if needed.
4. Save the file to `my-cv-tailor-data/profile.yaml` (or wherever the user specifies).

---

## Step K — Hand off

Tell the user setup is done. One sentence: "You're all set — paste any job description and I'll tailor the CV for it."

Don't re-explain the whole workflow. They'll see it when they paste a JD.
