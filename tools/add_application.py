#!/usr/bin/env python3
"""Interactive CLI tool to append applications to TRACKER.md."""

from datetime import date
from pathlib import Path

def main():
    repo_root = Path(__file__).resolve().parent.parent
    tracker_file = repo_root / "TRACKER.md"

    if not tracker_file.exists():
        template_file = repo_root / "template" / "TRACKER.template.md"
        if template_file.exists():
            tracker_file.write_text(template_file.read_text(encoding="utf-8"), encoding="utf-8")
            print(f"[*] Initialized TRACKER.md from template.")
        else:
            print("[!] Error: TRACKER.md and template not found.")
            return

    print("=" * 60)
    print(" CareerOS Application Pipeline Tracker (Add Entry)")
    print("=" * 60)

    role = input("Role / Program Title       : ").strip()
    org = input("Company / Organization     : ").strip()
    loc = input("Location / Remote Mode     : ").strip()
    target_cv = input("Target CV variant (cv_swe) : ").strip() or "cv_swe"
    today_str = date.today().isoformat()
    status = input("Initial Status [APPLY/APPLIED/INTERVIEW] (default: APPLY): ").strip().upper() or "APPLY"
    notes = input("Next Action / Notes        : ").strip()

    content = tracker_file.read_text(encoding="utf-8")
    lines = content.splitlines()

    # Find the table and compute next ID
    max_id = 0
    table_index = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and not line.strip().startswith("| ID") and not line.strip().startswith("|:---"):
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if parts and parts[0].isdigit():
                max_id = max(max_id, int(parts[0]))
            table_index = i

    new_id = f"{max_id + 1:02d}"
    new_row = f"| {new_id} | {role} | {org} | {loc} | `{target_cv}` | {today_str} | `{status}` | {notes} |"

    if table_index != -1:
        lines.insert(table_index + 1, new_row)
        tracker_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"\n[+] Successfully recorded Application #{new_id} in TRACKER.md")
    else:
        print("[!] Could not locate active applications table in TRACKER.md.")

if __name__ == "__main__":
    main()
