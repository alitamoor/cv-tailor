# Example session transcript

*A short illustrative walkthrough using the fictional profile from `example-profile.yaml`.
This shows what a typical session looks like — not a complete transcript, just the key moments.*

---

## Starting the session

**User:** Here's a job description — can you tailor my CV for it?

*[pastes JD for a Senior Sales Engineer role at a B2B data infrastructure company, Cloudform Inc.]*

**Claude:** Loading your profile and scoring fit...

---

## Step 1 — Fit scoring

**Claude:** Fit score: **74/100**

- Skills match (40%): 78 — strong overlap on data infrastructure, Kubernetes, enterprise SaaS. One gap: no Snowflake experience listed, which the JD treats as preferred.
- Experience match (30%): 82 — senior SE background with comparable deal sizes and cycle lengths. Apex Analytics' early-stage context fits Cloudform's Series C growth phase.
- Culture fit (15%): 71 — JD emphasises "founder mentality" and "you'll own the technical sales process." That matches your framing notes exactly.
- Career alignment (15%): 65 — natural step up; the JD mentions "help build out our SE team" which aligns with your Apex experience.

Proceeding with tailoring.

---

## Step 4 — Bullet rewrite (mid-process)

**Claude:** The bullet about your NovaTech onboarding work doesn't have a metric. What number could we attach? For example: how many customers onboarded, time to first value, reduction in onboarding time?

**User:** We cut onboarding time by 40% after I rebuilt the integration guide.

**Claude:** Got it. Bullet becomes: "Rebuilt integration documentation for 3 flagship API connectors, cutting customer onboarding time 40% and reducing support tickets 38% in the same quarter."

---

## Step 5 — Profile paragraph

**Claude:** Draft profile for Cloudform:

> Senior Sales Engineer with 8 years closing data infrastructure deals for enterprise buyers — including $4.2M ARR in FY2023 as sole SE on accounts averaging $800K deal size. Built Apex Analytics' pre-sales function from scratch, achieving a 90% POC win rate across 47 evaluations. Kubernetes-certified and comfortable at the infrastructure level, not just the API layer. Looking to bring that foundation to a team building out enterprise SE at scale.

---

## Step 7 — Reviewer feedback (inline mode)

**Claude (switching perspective):** Three things I'd fix:

Part A:
1. "comfortable at the infrastructure level" is vague. Replace with: "can demo at the kernel and container-orchestration level, not just the API surface" — more specific and more credible to a DevOps buyer.
2. "Looking to bring that foundation" — passive and generic. Replace with: "Here to do the same at Cloudform."

Part B:
- The Apex Analytics POC win rate (90% / 47 evaluations) is the strongest single differentiator for this JD, which mentions "technical evaluation to close" as a core responsibility. It's in the profile but could open the paragraph — consider leading with it.

---

## Step 9 — Output

**Claude:** CV saved to `my-cv-tailor-data/output/Cloudform/CV_Alex_Chen_Cloudform.docx`

Before→after summary:
- Profile paragraph: rewritten (see above)
- Meridian bullets: 4 kept, 1 de-emphasised (internal tooling bullet), "leverage" replaced in 2 bullets
- Apex bullets: 3 kept, POC win rate moved to first position
- NovaTech bullets: 2 kept, onboarding metric added

Open items:
- Snowflake: no experience in profile. Worth acknowledging if it comes up in interview.
