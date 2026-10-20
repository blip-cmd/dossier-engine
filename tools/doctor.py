#!/usr/bin/env python3
"""DossierEngine Environment Diagnostic Script.

Checks for essential dependencies: Python, pdflatex, and Git.
"""

import shutil
import subprocess
import sys

def check_command(name, cmd_args, help_url):
    """Check if a command is available on PATH and report its version."""
    bin_path = shutil.which(cmd_args[0])
    if not bin_path:
        print(f"[-] {name:<12}: NOT FOUND on PATH")
        print(f"    -> Installation Guide: {help_url}")
        return False
    
    try:
        res = subprocess.run(cmd_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        first_line = res.stdout.strip().splitlines()[0] if res.stdout.strip() else "Detected"
        print(f"[+] {name:<12}: FOUND ({first_line})")
        return True
    except Exception as e:
        print(f"[+] {name:<12}: FOUND ({bin_path}), but check failed: {e}")
        return True

def main():
    print("=" * 60)
    print(" DossierEngine System Diagnostic (Doctor)")
    print("=" * 60)
    
    python_ok = sys.version_info >= (3, 8)
    print(f"[{'+' if python_ok else '-'}] Python      : {sys.version.split()[0]} ({'OK' if python_ok else 'Requires Python 3.8+'})")

    git_ok = check_command("Git", ["git", "--version"], "https://git-scm.com/downloads")
    latex_ok = check_command("pdflatex", ["pdflatex", "--version"], "https://miktex.org/download or https://tug.org/texlive/")

    print("-" * 60)
    if python_ok and git_ok and latex_ok:
        print("[+] All core requirements satisfied. Your DossierEngine environment is ready.")
    else:
        print("[!] Some components are missing. Review the instructions above to complete setup.")
    print("=" * 60)

if __name__ == "__main__":
    main()
