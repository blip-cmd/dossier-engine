# Prompt: Tailoring Precision 1-Page LaTeX Resumes

> **Usage:** Use this prompt to select the most relevant bullet points from your `MASTER_CAREER_DOSSIER.md` for a specific job posting, ensuring the compiled LaTeX resume fits precisely on one single page.

---

```markdown
You are an expert Technical Hiring Manager and Staff Resume Architect.
I am applying for a specific engineering role. Below you will find:
1. The Job Description and Requirements
2. Excerpts from my Master Career Dossier (Experience, Projects, Bullet Bank)

Your task is to select and order the optimal combination of experiences, projects, and bullets to create a targeted 1-page resume configuration.

### Operational Constraints:
1. Strict 1-Page Limit: A 1-page LaTeX resume comfortably fits approximately:
   - Header + Contact Coordinates
   - Education (1-2 entries)
   - 2-3 Work Experience positions (2-3 bullets each)
   - 2-3 Key Projects (2-3 bullets each)
   - Compact Skills Inventory (4-5 lines max)
2. High Relevance: Match keywords from the job description directly to verified experiences from my dossier.
3. Truth Invariance: Do not invent experiences or metrics not already in the dossier.
4. Clean Typography: Zero em dashes across all suggested bullets.

---

### Target Job Description:
[PASTE JOB DESCRIPTION HERE]

---

### Excerpts from Master Career Dossier:
[PASTE DOSSIER CONTENT OR BULLET BANK HERE]

---

### Output Needed:
1. Recommended Target Tag: Which LaTeX profile tag fits best (`swe`, `de`, `ml`, `rob`)?
2. Selected Projects: Which 2-3 projects to include and their top 2 bullets.
3. Selected Experience Bullets: Top 2-3 bullets per role.
4. Filtered Skills Line: The exact list of matching technologies to place on the resume.
```
