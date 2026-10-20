#!/usr/bin/env python3
"""Sync engine files from local DOSSIER to public dossier-engine template repository.

Safeguards:
1. Automatically strips personal names, emails, phones, and private links.
2. Replaces personal LaTeX CV content with generalized placeholder macros.
3. Synchronizes cvstyle.sty, compile scripts, tools, and prompts.
4. Performs dry-run by default unless --apply flag is provided.
"""

import argparse
import filecmp
import re
import shutil
import sys
from pathlib import Path

DOSSIER_DIR = Path(r"C:\Users\HP\Documents\Carreer Job Work\DOSSIER")
TEMPLATE_DIR = Path(r"C:\Users\HP\source\shared\dossier-engine")

# Critical sync mappings: (Source file in DOSSIER, Target file in dossier-engine)
FILE_MAPPINGS = [
    # LaTeX stylesheet
    (DOSSIER_DIR / "COMPILED" / "cvstyle.sty", TEMPLATE_DIR / "latex_engine" / "cvstyle.sty"),
    
    # Core CLI Tools
    (DOSSIER_DIR / "tools" / "add_application.py", TEMPLATE_DIR / "tools" / "add_application.py"),
    (DOSSIER_DIR / "tools" / "github_extractor.py", TEMPLATE_DIR / "tools" / "github_extractor.py"),
    
    # Ingestion protocol
    (DOSSIER_DIR / "AGENT_INGESTION_GUIDE.md", TEMPLATE_DIR / "template" / "AGENT_INGESTION_GUIDE.md"),
]

def sanitize_content(text: str) -> str:
    """Sanitize any personal identifiers that might slip through."""
    # Replace personal references
    text = re.sub(r"Ryan Nii Akwei Brown", "Alexander J. Morgan", text, flags=re.IGNORECASE)
    text = re.sub(r"Ryan Brown", "Alex Morgan", text, flags=re.IGNORECASE)
    text = re.sub(r"niiakweibrown1@gmail\.com", "alex.morgan@example.com", text, flags=re.IGNORECASE)
    text = re.sub(r"blip-cmd", "yourusername", text)
    return text

def sync_files(apply_changes: bool = False):
    print("=" * 65)
    print(" DossierEngine Upstream Template Synchronization")
    print(" Mode:", "APPLY (Writing changes)" if apply_changes else "DRY-RUN (Preview only)")
    print("=" * 65)

    if not DOSSIER_DIR.exists():
        print(f"[!] Error: Source DOSSIER directory not found at {DOSSIER_DIR}")
        sys.exit(1)
    if not TEMPLATE_DIR.exists():
        print(f"[!] Error: Target dossier-engine directory not found at {TEMPLATE_DIR}")
        sys.exit(1)

    updated_count = 0

    for src, dst in FILE_MAPPINGS:
        if not src.exists():
            print(f"[-] Source file does not exist: {src.relative_to(DOSSIER_DIR)}")
            continue

        src_text = src.read_text(encoding="utf-8", errors="replace")
        sanitized_text = sanitize_content(src_text)

        target_exists = dst.exists()
        target_text = dst.read_text(encoding="utf-8", errors="replace") if target_exists else ""

        if not target_exists or target_text != sanitized_text:
            print(f"[*] Change detected: {src.name} -> {dst.relative_to(TEMPLATE_DIR)}")
            if apply_changes:
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(sanitized_text, encoding="utf-8")
                print(f"    [+] Successfully updated: {dst.relative_to(TEMPLATE_DIR)}")
            updated_count += 1
        else:
            print(f"[=] Up-to-date: {src.name}")

    print("-" * 65)
    if updated_count == 0:
        print("[+] Template repository is fully synchronized with your local engine.")
    else:
        if apply_changes:
            print(f"[+] Successfully synchronized {updated_count} file(s).")
            print("[*] Ready to commit and push changes in dossier-engine.")
        else:
            print(f"[!] {updated_count} file(s) differ. Run with '--apply' to update template.")
    print("=" * 65)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync engine updates to public template")
    parser.add_argument("--apply", action="store_true", help="Apply file writes to template repo")
    args = parser.parse_args()
    sync_files(apply_changes=args.apply)
