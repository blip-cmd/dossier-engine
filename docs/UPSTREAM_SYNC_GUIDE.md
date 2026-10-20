# Upstream Synchronization Guide

When you create your private career repository from the DossierEngine template, your repository begins as an independent copy. As new features, compilation scripts, LaTeX styling improvements, and AI ingestion prompts are released upstream, you can easily pull them in.

This guide explains how to synchronize your private repository with upstream releases without overwriting your personal data.

---

## 1. Configure the Upstream Remote

In your local cloned repository, check your existing remotes:

```bash
git remote -v
```

If `upstream` is not listed, add the official DossierEngine repository as your upstream remote:

```bash
git remote add upstream https://github.com/blip-cmd/dossier-engine.git
```

Verify that the remote was added successfully:

```bash
git remote -v
# origin    https://github.com/<your-username>/dossier-engine.git (fetch)
# origin    https://github.com/<your-username>/dossier-engine.git (push)
# upstream  https://github.com/blip-cmd/dossier-engine.git (fetch)
# upstream  https://github.com/blip-cmd/dossier-engine.git (push)
```

---

## 2. Fetch and Merge Upstream Changes

Whenever you want to update your system tooling:

```bash
# Fetch the latest branches and tags from upstream
git fetch upstream

# Ensure you are on your default branch
git checkout main

# Merge upstream changes into your branch
git merge upstream/main --allow-unrelated-histories -m "chore: sync updates from upstream dossier-engine"
```

The `--allow-unrelated-histories` flag is required because repositories created via GitHub's "Use this template" feature start with a separate initial commit history.

---

## 3. Resolving Merge Conflicts

Because your private personal records (`MASTER_CAREER_DOSSIER.md`, `TRACKER.md`) are gitignored and separate from the template files (`template/*.template.md`), merge conflicts are rare.

If a conflict arises in a shared script or configuration file:
1. Open the conflicted file in your editor.
2. Review the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
3. Accept the upstream enhancements while preserving any custom changes you made to local tooling.
4. Stage the resolved files and finish the merge:
   ```bash
   git add <resolved-file>
   git commit -m "chore: resolve upstream merge conflict"
   git push origin main
   ```
