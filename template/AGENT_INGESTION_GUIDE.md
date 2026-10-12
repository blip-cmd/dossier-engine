# AUTONOMOUS AGENT INGESTION PROTOCOL

> **Directive for Autonomous Coding Agents (Antigravity, Cursor, Windsurf, Claude, Copilot)**
> This document instructs you how to analyze project milestones, commit diffs, or chat transcripts, and update the user's `MASTER_CAREER_DOSSIER.md` cleanly and accurately without asking unnecessary clarifying questions.

---

## 1. Operating Rules for AI Agents

When tasked with ingesting a project or conversation log into `MASTER_CAREER_DOSSIER.md`:

1. **Strictly Grounded in Evidence**: Extract only what the user actually built, architected, debugged, or analyzed. Never invent fictitious metrics, unverified client names, or exaggerated titles.
2. **Standard XYZ Formatting**: Every extracted bullet must follow Google's XYZ formula:
   > *Accomplished [X] as measured by [Y] by doing [Z].*
   Begin every bullet with an active, high-impact past-tense verb (e.g., *Architected, Engineered, Implemented, Streamlined, Reduced, Accelerated, Refactored*).
3. **Typographic Standard**: Strictly maintain zero em dashes across all updates. Never output unicode `—` or LaTeX `---`. Use commas, colons, parentheses, semicolons, or distinct sentences.
4. **Non-Destructive Appending**: Never overwrite, delete, or truncate existing projects, roles, or bullet points in the dossier. Always append new projects under the relevant section.
5. **Atomic Commit Execution**: After updating the dossier, verify git status and commit cleanly with a conventional commit message:
   ```bash
   git add MASTER_CAREER_DOSSIER.md
   git commit -m "docs(dossier): ingest [Project Name] architecture and technical bullets"
   ```

---

## 2. Ingestion Workflow Checklist

```
Step 1: Scan Source Context (Chat log, Git diff, Pull Request, Voice dump)
   │
   ├── Identify: Project Name, Architecture, Tech Stack, Key Challenges Overcome
   └── Quantify: Benchmark numbers, latency gains, test coverage, lines of code, cost reductions
   │
Step 2: Read MASTER_CAREER_DOSSIER.md
   │
   ├── Locate Section 5: Technical Projects Matrix
   └── Locate Section 10: Master Bullet Bank
   │
Step 3: Draft Project Matrix Entry
   │
   ├── Format title, role, stack, repository link, and live deployment
   └── Write a 3-4 sentence architectural synopsis
   │
Step 4: Formulate Tagged Bullets
   │
   ├── Map accomplishments to appropriate tags ([SWE], [DE], [ML], [QA], [LEAD])
   └── Ensure each bullet satisfies Google's XYZ metric formula
   │
Step 5: Write to File and Git Commit
   │
   ├── Append project entry to Section 5
   ├── Append bullets to Section 10 under corresponding tag headings
   └── Run git commit
```

---

## 3. Reference Project Schema

When adding a new entry to **Section 5: Technical Projects Matrix**, follow this exact format:

```markdown
### Project [N]: [Full Project Title]
* **Role / Mandate:** [e.g., Lead Systems Engineer, Full-Stack Developer]
* **Live Deployment:** [URL or N/A]
* **Source Repository:** [github.com/username/project-repo]
* **Core Stack:** [Technology A, Technology B, Database C, Tool D]
* **Architecture Overview:**
  * [Concise technical summary of the system architecture, protocols, and data models]
* **Key Milestones and Outcomes:**
  * [Accomplished [X] as measured by [Y] by doing [Z]]
  * [Accomplished [X] as measured by [Y] by doing [Z]]
```

---

## 4. Reference Calibrated Bullet Formulation

### Poor / Weak Examples (Do Not Produce):
- *Helped build a web app using React and Node.* (Vague, lacks scale, passive)
- *Responsible for writing automated tests.* (Describes duties rather than accomplishments)
- *Used AI to make the app faster.* (Lacks technical specificity and quantification)

### Calibrated / High-Impact Examples (Target Standard):
- *Architected an end-to-end automated testing framework using Playwright and TypeScript, validating 18 routes and 12 business workflows across 5 device viewports.*
- *Built an autonomous 2FA ingestion service using Python and IMAP, reducing authentication latency to under 6 seconds by tracking mailbox message UIDs and solving client-side Altcha challenges.*
- *Optimized Postgres read queries by implementing composite indexing and Redis caching, cutting average p95 API response times from 420ms to 65ms.*
