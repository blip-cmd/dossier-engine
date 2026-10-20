#!/usr/bin/env python3
"""Cross-platform LaTeX Resume Compilation Engine for DossierEngine.

Compiles master_cv.template.tex into target PDF variants (swe, de, ml, rob, full)
and isolates build artifacts in an output directory.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

TARGETS = ["swe", "de", "ml", "rob", "full"]

def find_pdflatex():
    """Locate pdflatex executable in PATH or standard portable directories."""
    cmd = shutil.which("pdflatex")
    if cmd:
        return cmd
    
    # Common Windows portable paths
    possible_paths = [
        Path(r"C:\Users\HP\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"),
        Path(r"C:\Program Files\MiKTeX\miktex\bin\x64\pdflatex.exe"),
        Path(r"C:\miktex\miktex\bin\x64\pdflatex.exe"),
    ]
    for p in possible_paths:
        if p.exists():
            return str(p)
    return None

def compile_target(pdflatex_bin, engine_dir, output_dir, target):
    """Compile a single target profile into a PDF."""
    tex_file = engine_dir / "master_cv.template.tex"
    pdf_output = output_dir / f"cv_{target}.pdf"
    
    print(f"[*] Compiling target profile: [{target}]...")
    
    cmd = [
        pdflatex_bin,
        "-interaction=nonstopmode",
        f"-output-directory={output_dir}",
        f"-jobname=cv_{target}",
        f"\\def\\targetprofile{{{target}}}\\input{{{tex_file.name}}}"
    ]
    
    result = subprocess.run(cmd, cwd=engine_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"[!] Compilation failed for target: {target}")
        print(result.stdout[-800:])
        return False
    
    if pdf_output.exists():
        size_kb = pdf_output.stat().st_size / 1024
        print(f"[+] Successfully generated: {pdf_output.name} ({size_kb:.1f} KB)")
        return True
    return False

def main():
    engine_dir = Path(__file__).resolve().parent
    output_dir = engine_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    pdflatex_bin = find_pdflatex()
    if not pdflatex_bin:
        print("[!] Error: pdflatex not found on PATH. Please install a TeX distribution (MiKTeX, TeX Live, or MacTeX).")
        sys.exit(1)

    print(f"[*] LaTeX Engine: {pdflatex_bin}")
    print(f"[*] Output Directory: {output_dir}")

    targets_to_build = sys.argv[1:] if len(sys.argv) > 1 else TARGETS
    success_count = 0

    for target in targets_to_build:
        if compile_target(pdflatex_bin, engine_dir, output_dir, target):
            success_count += 1

    print(f"\n[+] Compilation finished: {success_count}/{len(targets_to_build)} targets built successfully.")

if __name__ == "__main__":
    main()
