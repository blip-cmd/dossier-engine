# CareerOS: Autonomous Career Intelligence and Resume System

CareerOS is an open-source operating system for your professional life. It turns unorganized work logs, coding chats, and project histories into an audit-proof Career Dossier, and compiles precision-targeted, one-page LaTeX resumes on demand.

Instead of writing resumes manually under deadline stress, you let autonomous AI agents mine your everyday technical achievements, organize your impact metrics, and compile tailored resumes in seconds.

---

## ⚡ The 5-Minute Quickstart

You do not need to spend hours configuring systems before getting value. Follow these three steps:

### 1. Create Your Private Repository
To keep your personal career records completely confidential:
1. Click the green **"Use this template"** button at the top of this GitHub repository.
2. Select **"Create a new repository"**.
3. Choose **Private** for repository visibility.
4. Clone your new private repository to your local computer:
   ```bash
   git clone https://github.com/<your-username>/career-os.git
   cd career-os
   ```

### 2. Copy the Starter Templates
Duplicate the included templates to create your working files:
```bash
cp template/MASTER_CAREER_DOSSIER.template.md MASTER_CAREER_DOSSIER.md
cp template/TRACKER.template.md TRACKER.md
```

### 3. Do a 3-Minute Voice Brain-Dump
> [!TIP]
> **Pro-Tip: Use Speech-to-Text for Effortless Brain Dumps**
> 
> Typing down everything you built is exhausting. Instead, turn on your operating system's built-in speech-to-text engine and talk freely about your work for three minutes:
> - **Windows**: Press `Win + H` to activate Windows Voice Typing.
> - **macOS**: Press `Fn` twice (or `Cmd + Space` if configured) to launch Dictation.
>
> Open any text scratchpad, press the shortcut, and describe what you built, what broke, how you debugged it, and what numbers changed. Do not worry about grammar or resume buzzwords.

Once you have your raw brain dump or chat transcript, pass it along with [`prompts/extract_from_transcripts.md`](prompts/extract_from_transcripts.md) to any AI assistant (ChatGPT, Claude, Cursor, Antigravity, or Windsurf). The AI will structure your raw thoughts into high-impact, Google XYZ-formula bullet points and update your `MASTER_CAREER_DOSSIER.md`.

---

## 🏗️ System Architecture

```
career-os/
├── MASTER_CAREER_DOSSIER.md       # Your private single source of career truth (gitignored)
├── TRACKER.md                    # Active job and fellowship application pipeline (gitignored)
├── template/
│   ├── MASTER_CAREER_DOSSIER.template.md  # Comprehensive dossier schema
│   ├── TRACKER.template.md                # Application tracking lifecycle table
│   └── AGENT_INGESTION_GUIDE.md           # Instructions for autonomous AI coding agents
├── prompts/
│   ├── extract_from_transcripts.md        # Convert raw chat logs into XYZ bullets
│   ├── extract_from_linkedin.md           # Ingest LinkedIn data dumps into the dossier
│   ├── tailor_1_page_cv.md                # Generate role-targeted LaTeX resume variants
│   └── sop_narrative_builder.md           # Craft graduate school and fellowship statements
├── latex_engine/
│   ├── cvstyle.sty                        # ATS-safe, clean typographic stylesheet
│   ├── master_cv.template.tex             # Conditional multi-target LaTeX resume template
│   └── compile_cvs.py                     # Cross-platform build script generating PDF targets
├── tools/
│   ├── doctor.py                          # Environment health check (pdflatex, Python, Git)
│   ├── add_application.py                 # Fast CLI helper to append jobs to TRACKER.md
│   └── github_extractor.py                # Fetch public GitHub repository metrics
└── docs/
    ├── PRIVACY_AND_SECURITY.md            # Guidelines on protecting personal career records
    └── UPSTREAM_SYNC_GUIDE.md             # How to pull core template updates cleanly
```

---

## 🤖 Autonomous AI Agent Workflow

CareerOS is built from the ground up for modern AI coding tools (such as Cursor, Windsurf, Antigravity, and GitHub Copilot CLI).

When you finish a major coding feature or milestone in any project:
1. Provide the agent with [`template/AGENT_INGESTION_GUIDE.md`](template/AGENT_INGESTION_GUIDE.md).
2. Point the agent to your project conversation log, commit diffs, or code files.
3. The agent reads the guide, extracts technical accomplishments, formats them according to the Google XYZ standard (Accomplished [X] as measured by [Y] by doing [Z]), and appends them to your `MASTER_CAREER_DOSSIER.md`.

---

## 📄 Multi-Target LaTeX Resume Engine

CareerOS lets you maintain **one single master LaTeX source** that compiles into multiple specialized one-page resumes based on build flags:

- `swe`: Software Engineering
- `de`: Data Engineering and Backend Systems
- `ml`: Machine Learning and Data Science
- `rob`: Robotics and Hardware Systems
- `full`: Complete multi-page comprehensive master CV

### Compiling Resumes

Check that your environment has Python and a TeX distribution (such as MiKTeX, TeX Live, or MacTeX):

```bash
# Run system diagnostic
python tools/doctor.py

# Compile all targeted one-page PDFs
python latex_engine/compile_cvs.py
```

All compiled PDFs are saved into `latex_engine/output/` without cluttering your root workspace.

---

## 🔒 Privacy and Security Guarantee

Your personal career history, contact details, grades, and application records belong to you alone.

1. **Local Files are Gitignored**: The root `.gitignore` file automatically excludes your live `MASTER_CAREER_DOSSIER.md`, `TRACKER.md`, and private PDF builds from ever being pushed to public remotes.
2. **Private Template Usage**: When you generate your repository using **"Use this template"**, make sure you mark your personal repository as **Private**.
3. **Audit Before Sharing**: For complete details on keeping your data secure, consult [`docs/PRIVACY_AND_SECURITY.md`](docs/PRIVACY_AND_SECURITY.md).

---

## 🔄 Syncing with Upstream Improvements

As new features, LaTeX styling updates, and ingestion prompts are added to the official `career-os` repository, you can pull them into your private repository without overwriting your personal dossier:

```bash
# Add upstream remote once
git remote add upstream https://github.com/blip-cmd/career-os.git

# Pull template enhancements
git fetch upstream
git merge upstream/main --allow-unrelated-histories
```

Step-by-step conflict resolution instructions are documented in [`docs/UPSTREAM_SYNC_GUIDE.md`](docs/UPSTREAM_SYNC_GUIDE.md).

---

## 🤝 Contributing

We welcome community contributions, additional prompt recipes, and styling improvements. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

---

## 📜 License

CareerOS is open source under the [MIT License](LICENSE).
