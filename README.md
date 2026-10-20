# DossierEngine

**Stop writing resumes from memory under deadline pressure. Let AI mine your everyday engineering work.**

DossierEngine is a private, local-first system that turns git diffs, terminal logs, and messy coding chat transcripts into an audit-proof technical dossier, then compiles precision one-page LaTeX resumes on demand.

---

## The Reality of Technical Job Hunting

* **Engineering Amnesia**: You solved a concurrency deadlock in Redis four months ago. When applying for jobs tonight, all you remember is "worked on backend." The architectural decisions, latency numbers, and hard-fought trade-offs have vanished from your memory.
* **LLM Hallucination Trap**: Asking an AI to "write my resume" produces generic corporate fluff (*"Spearheaded synergy across cross-functional stakeholders to drive 40% growth"*) that technical interviewers immediately see through and question during interviews.
* **Resume Sprawl Hell**: You have fourteen versions of `resume_swe_final_v3.docx`. When a recruiter calls three weeks later, you have no idea which bullet points they are looking at.
* **Formatting Friction**: Trying to force a resume to stay on exactly one page in Word or Google Docs causes layout shifts. Adjusting one line pushes contact information onto an awkward second page.

---

## How This System Solves It

DossierEngine introduces an engineering workflow for your career history:

1. **Three-Minute Voice Brain Dumps (`Win + H` / Dictation)**
   When you finish a tough feature or close a major pull request, turn on speech-to-text and talk freely for three minutes about what you built, what broke, how you debugged it, and what numbers changed. The system turns that raw brain dump into calibrated bullet points.

2. **The Dossier Pattern (Separating Truth from Layout)**
   Your career history is maintained in an unconstrained master vault ([`MASTER_CAREER_DOSSIER.md`](template/MASTER_CAREER_DOSSIER.template.md)). You never delete an achievement or dilute technical details to fit a page limit. Page constraints exist only on compiled outputs.

3. **Grounded Google XYZ Formulation**
   Included mining prompts enforce Google's XYZ formula:
   > *Accomplished [X] as measured by [Y] by doing [Z].*
   The prompts extract only verifiable technical accomplishments and explicitly prohibit exaggerated claims.

4. **Single-Source, Multi-Target LaTeX Engine**
   Maintain one single LaTeX file that conditionally compiles into distinct, ATS-safe, one-page PDFs based on build flags:
   - `python latex_engine/compile_cvs.py swe` (Software Engineering / Systems)
   - `python latex_engine/compile_cvs.py de` (Data Platform / Distributed Pipelines)
   - `python latex_engine/compile_cvs.py ml` (Machine Learning / Applied AI)
   - `python latex_engine/compile_cvs.py rob` (Robotics / Hardware Systems)
   - `python latex_engine/compile_cvs.py full` (Comprehensive multi-page academic CV)

5. **Autonomous AI Agent Protocol**
   Feed [`template/AGENT_INGESTION_GUIDE.md`](template/AGENT_INGESTION_GUIDE.md) to coding assistants like Cursor, Windsurf, Claude, or Antigravity. The agent reads your pull request diffs, structures the project matrix entry, updates your bullet bank, and commits the changes cleanly without altering your existing records.

6. **Privacy-First Architecture**
   Your real dossier and application history are gitignored by default. Using GitHub's **"Use this template"** feature ensures your private records remain inside your private repository while still allowing you to pull upstream system updates.

---

## ⚡ Quickstart: Zero to Value in 5 Minutes

### Step 1: Create Your Private Repository
1. Click the green **"Use this template"** button at the top of this repository.
2. Select **"Create a new repository"**.
3. Set visibility to **Private** to keep your records confidential.
4. Clone to your machine:
   ```bash
   git clone https://github.com/<your-username>/dossier-engine.git
   cd dossier-engine
   ```

### Step 2: Initialize Your Working Files
```bash
cp template/MASTER_CAREER_DOSSIER.template.md MASTER_CAREER_DOSSIER.md
cp template/TRACKER.template.md TRACKER.md
```

### Step 3: Run the Speech-to-Text Shortcut
> [!TIP]
> **Pro-Tip: Use Speech-to-Text for Fast Brain Dumps**
> - **Windows**: Press `Win + H` to activate Windows Voice Typing.
> - **macOS**: Press `Fn` twice (or `Cmd + Space` if configured) to launch Dictation.
>
> Open any text scratchpad, press the shortcut, and describe what you built, what broke, how you debugged it, and what numbers changed. Do not worry about grammar or resume formatting.

Copy that raw text alongside [`prompts/extract_from_transcripts.md`](prompts/extract_from_transcripts.md) into any AI assistant. It will output structured, audit-proof project entries ready for your dossier.

---

## 🏗️ Repository Architecture

```
dossier-engine/
├── MASTER_CAREER_DOSSIER.md       # Private single source of truth (gitignored)
├── TRACKER.md                    # Active application pipeline (gitignored)
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

## 📄 Compiling Targeted LaTeX Resumes

Verify your local environment dependencies:
```bash
python tools/doctor.py
```

Compile all target 1-page PDF resumes into `latex_engine/output/`:
```bash
python latex_engine/compile_cvs.py
```

Or compile a single target role:
```bash
python latex_engine/compile_cvs.py swe
```

---

## 🔄 Pulling Future Upstream Improvements

Keep your private repository up to date with core template releases without overwriting your personal data:

```bash
git remote add upstream https://github.com/blip-cmd/dossier-engine.git
git fetch upstream
git merge upstream/main --allow-unrelated-histories -m "chore: sync updates from upstream"
```

For complete conflict resolution instructions, see [`docs/UPSTREAM_SYNC_GUIDE.md`](docs/UPSTREAM_SYNC_GUIDE.md).

---

## 📜 License

Distributed under the [MIT License](LICENSE).
