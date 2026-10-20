# Contributing to DossierEngine

Thank you for your interest in improving DossierEngine. We welcome contributions from developers, researchers, and technical writers.

---

## Code of Conduct and Principles

1. **Simplicity First**: DossierEngine is designed so users gain immediate value within ten minutes. New features, prompts, or scripts should minimize dependencies and complex setup steps.
2. **Strict Privacy by Design**: Never commit personal career data, real phone numbers, addresses, institutional credentials, or sensitive work history into the public codebase.
3. **Typographic Standard**: We follow clean typography. Do not introduce em dashes (neither unicode `—` nor LaTeX triple hyphens) in documentation, scripts, LaTeX templates, or pull request descriptions. Use commas, colons, parentheses, semicolons, or distinct sentences.

---

## Ways to Contribute

- **Ingestion Prompts**: Contribute specialized extraction prompts for unique sources (e.g., GitHub issue discussions, Jira tickets, Obsidian daily notes).
- **LaTeX Themes and Styles**: Refine the standard style sheet (`latex_engine/cvstyle.sty`) to improve ATS parsing compatibility, margins, or modern font options.
- **Workflow Tools**: Improve CLI utilities (`doctor.py`, `add_application.py`, `github_extractor.py`) to work across Windows, macOS, and Linux without third-party dependencies.
- **Documentation**: Clarify setup steps, troubleshoot common TeX distribution problems, and expand the upstream synchronization guide.

---

## Development Workflow

1. Fork the repository on GitHub.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/<your-username>/dossier-engine.git
   cd dossier-engine
   ```
3. Create a descriptive feature branch:
   ```bash
   git checkout -b feat/add-obsidian-prompt
   ```
4. Test your changes locally:
   ```bash
   python tools/doctor.py
   python latex_engine/compile_cvs.py
   ```
5. Commit your changes using Conventional Commits:
   ```bash
   git commit -m "feat(prompts): add Obsidian daily notes extraction prompt"
   ```
6. Push to your fork and submit a Pull Request against the `main` branch.

---

## Commit Message Conventions

We enforce the Conventional Commits specification:
- `feat`: A new user-facing capability or script
- `fix`: A bug fix in templates, scripts, or LaTeX stylesheets
- `docs`: Documentation enhancements, guides, or prompt refinements
- `style`: Changes that do not affect the meaning of code (formatting, whitespace)
- `refactor`: Code refactoring that neither fixes a bug nor adds a feature
- `test`: Adding or updating automated GitHub Actions checks

Thank you for helping empower engineers and professionals worldwide with autonomous career intelligence.
