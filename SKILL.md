# cv-tailor

Triggered when the user pastes a job description, or says something like "tailor my CV," "apply for this role," or "help me with this JD."

---

## On trigger

### 1. Check for profile.yaml

Look for `profile.yaml` in the user's data directory. The default location is `../my-cv-tailor-data/profile.yaml` relative to this repo. If the user has configured a different location, use that.

- **Not found:** Run `setup/SETUP_GUIDE.md`. Do nothing else until setup is complete.
- **Found:** Continue to step 2.

### 2. Check for a JD

If no job description has been provided yet, ask: "Paste the job description and I'll get started." Do nothing else. Wait.

### 3. Detect environment mode

Read `profile.yaml: environment.mode`:

- **`agent`**: Claude Code or Cowork. Agent-spawning, bash execution, and file writes are available.
- **`inline`**: claude.ai or any environment without tool execution. Reviewer runs inline; docx build outputs edit instructions instead of executing them.
- **`auto`** (default): Detect from available tools. If bash execution and file writes are available → agent mode. Otherwise → inline mode.

### 4. Run the workflow

Load and execute each file in order. Substitute `profile.yaml` values throughout.

1. `workflow/01-fit-scoring.md`
2. `workflow/02-jd-keyword-extraction.md`
3. `workflow/03-gap-analysis.md`
4. `workflow/04-bullet-rewrite.md`
5. `workflow/05-profile-rewrite.md`
6. `workflow/06-build-docx.md`
7. `workflow/07-reviewer.md`
8. `workflow/08-self-audit.md`
9. `workflow/09-output.md`

---

## Critical constraint

Do not read the user's source CV file (docx or PDF) before workflow step 6. All writing steps (02–05) use structured data from `profile.yaml` only.

This keeps context usage low and prevents re-deriving facts from unstructured text when structured data already exists. The source file is only opened at step 6 when it's time to build the output document.

---

## How to add this to your Claude Code project

In your project's `CLAUDE.md` (or create one at the repo root), add:

```
When the user pastes a job description or asks to tailor their CV, load and follow SKILL.md from the cv-tailor repo.
```

Or reference it directly in a new session by opening `SKILL.md` and saying "follow these instructions."
