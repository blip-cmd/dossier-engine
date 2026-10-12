# Prompt: Ingesting LinkedIn Archives into the Career Dossier

> **Usage:** Export your LinkedIn data archive (Settings & Privacy -> Data privacy -> Get a copy of your data -> Download archive) or copy your profile text, and use this prompt to convert it into the CareerOS dossier format.

---

```markdown
You are an expert Technical Career Strategist.
I am providing you with my raw LinkedIn profile text, career summary, or exported CSV data.

Your goal is to parse this information and convert it into the structured sections required by my Master Career Dossier:
1. Education credentials and academic dates
2. Work experience records with title, company, dates, and responsibilities
3. Skills taxonomy grouped by modern engineering categories
4. Licenses, certifications, and verified credentials

### Formatting Invariants:
1. Ensure all dates follow standard "Month Year" formatting.
2. Group all individual skills into logical buckets: Languages, Frameworks, Cloud & DevOps, Databases, Testing, Developer Tooling.
3. Clean up passive descriptions (e.g., "Responsible for...") into active engineering summaries.
4. Zero em dashes: Replace all unicode em dashes or hyphens used as dashes with commas, colons, or parentheses.

---

### Raw LinkedIn Input:
[PASTE YOUR LINKEDIN PROFILE CONTENT OR CSV SNIPPETS HERE]

---

### Desired Output:
Please output the parsed information formatted strictly according to the sections of the CareerOS Master Dossier schema.
```
