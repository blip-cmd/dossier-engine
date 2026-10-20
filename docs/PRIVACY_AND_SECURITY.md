# Privacy and Security Guidelines

Your career history contains sensitive information: personal email addresses, phone numbers, compensation history, internal project names, proprietary code metrics, academic transcripts, and references.

DossierEngine is engineered to keep this information strictly under your control.

---

## 1. Public Template vs. Private Fork

GitHub repositories created as a standard fork of a public repository inherit public visibility by default and cannot be easily switched to private under certain organizational setups.

### Recommended Path: Use GitHub's Template Feature

1. Navigate to the official repository at `https://github.com/blip-cmd/dossier-engine`.
2. Click the green **"Use this template"** button and choose **"Create a new repository"**.
3. Choose your own account or organization as the owner.
4. Set Repository visibility to **Private**.
5. Click **Create repository**.

This creates a completely independent, private repository where only you and your authorized collaborators have access.

---

## 2. Local File Protection

DossierEngine comes pre-configured with a `.gitignore` file that prevents your real career files from ever being staged or committed accidentally:

```gitignore
MASTER_CAREER_DOSSIER.md
TRACKER.md
my_dossier*.md
tracker*.md
*.secret.md
latex_engine/output/
*.pdf
```

### Best Practice: Keep Templates Clean
- Maintain `template/MASTER_CAREER_DOSSIER.template.md` as the generalized schema.
- Keep your actual, filled-out career records in `MASTER_CAREER_DOSSIER.md` at the repository root.
- If you ever contribute improvements back to DossierEngine via a pull request, verify that `git status` does not show any of your personal files staged.

---

## 3. Sanitizing Technical Bullets for Public Projects

When extracting achievements from client work or non-disclosure agreements (NDAs):

1. **Focus on Engineering Challenges, Not Proprietary Details**: Mention architectural patterns (e.g., "event-driven microservices", "single-token concurrency management") rather than confidential internal codenames.
2. **Abstract Client Identities**: Replace specific enterprise client names with domain descriptions (e.g., "a leading European logistics provider" or "a national healthcare registry").
3. **Verify Compliance**: Ensure your bullets do not leak internal API credentials, server IP addresses, or internal endpoints.
