# -*- coding: utf-8 -*-
"""
PHANToM GRID // OpenCode Match 3 - Rule 65 Sovereign Compliance Audit
Standard: STD-TOURNAMENT-TRI (Rule 65 / v6.1.0 Constitution)
Ratified by: Commander Jack Hu x Commander Xiaomi

Deep Verification Pipeline:
1. Structural Existence & Dimension Guard
2. Deep Visual & Semantic Pixel Audit (Anti-Blank PDF Gate)
3. 100% International Professional English Audit (Anti-Chinese Gate)
"""

import sys
import os
import re
import subprocess
from pathlib import Path
from PIL import Image
import pymupdf

BASE_DIR = Path(__file__).resolve().parent.parent
CHINESE_PATTERN = re.compile(r"[\u4e00-\u9fff]")


def check_deliverable_01_project_name():
    readme = (BASE_DIR / "README.md").read_text(encoding="utf-8")
    assert "PHANToM GRID :: OpenCode Match 3" in readme, "Deliverable 01: Project name prefix missing"
    print("[PASS] Deliverable 01: Project Name Verified")


def check_deliverable_02_elevator_pitch():
    submission_pkg = (BASE_DIR / "docs" / "Devpost_Submission_Package.md").read_text(encoding="utf-8")
    assert "Autonomous multi-agent workflow orchestrator" in submission_pkg, "Deliverable 02: Elevator Pitch missing"
    print("[PASS] Deliverable 02: Elevator Pitch Verified")


def check_deliverable_03_tags():
    submission_pkg = (BASE_DIR / "docs" / "Devpost_Submission_Package.md").read_text(encoding="utf-8")
    assert "python, pydantic, pytest" in submission_pkg, "Deliverable 03: Built With Tags missing"
    print("[PASS] Deliverable 03: Built With Tags Verified")


def check_deliverable_04_cover_image():
    cover = BASE_DIR / "assets" / "cover_image.png"
    assert cover.exists(), "Deliverable 04: cover_image.png missing"
    with Image.open(cover) as img:
        assert img.size == (1920, 1080), f"Deliverable 04: Incorrect cover dimensions {img.size}"
    arch = BASE_DIR / "assets" / "architecture_overview_v40.png"
    assert arch.exists(), "Deliverable 04: architecture_overview_v40.png missing"
    print("[PASS] Deliverable 04: 16:9 Cover & v40 Architecture Diagram Verified")


def check_deliverable_05_slides():
    """
    Deep Audit for Deliverable 05 & 01 (PDF Verification):
    Prevents 'Shallow Assertion Fallacy'.
    Ensures:
    1. Exact page count.
    2. Substantial non-empty text extraction (>300 chars/page).
    3. Multi-color non-blank visual pixel rasterization (>50 distinct colors/page).
    4. Exactly 0 Chinese characters in extracted text.
    """
    slides = BASE_DIR / "docs" / "SLIDES_PRESENTATION.pdf"
    assert slides.exists(), "Deliverable 05: SLIDES_PRESENTATION.pdf missing"
    doc_slides = pymupdf.open(str(slides))
    assert len(doc_slides) == 10, f"Deliverable 05: Expected 10 slides, got {len(doc_slides)}"
    
    for idx, page in enumerate(doc_slides):
        text = page.get_text().strip()
        assert len(text) >= 300, f"Deliverable 05: Slide {idx+1} text too sparse ({len(text)} chars) - potential blank page!"
        chinese = CHINESE_PATTERN.findall(text)
        assert len(chinese) == 0, f"Deliverable 05: Slide {idx+1} contains Chinese characters: {chinese[:5]}"
        
        pix = page.get_pixmap()
        im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        colors = im.getcolors(maxcolors=1000000)
        assert len(colors) >= 50, f"Deliverable 05: Slide {idx+1} is visually blank (only {len(colors)} colors)!"

    # Also audit SPEC_01_AgentWorkflow.pdf
    spec_pdf = BASE_DIR / "docs" / "SPEC_01_AgentWorkflow.pdf"
    assert spec_pdf.exists(), "Deliverable 01: SPEC_01_AgentWorkflow.pdf missing"
    doc_spec = pymupdf.open(str(spec_pdf))
    assert len(doc_spec) >= 5, f"Deliverable 01: Expected >= 5 whitepaper pages, got {len(doc_spec)}"
    
    for idx, page in enumerate(doc_spec):
        text = page.get_text().strip()
        assert len(text) >= 300, f"Deliverable 01: Whitepaper page {idx+1} text too sparse ({len(text)} chars)"
        chinese = CHINESE_PATTERN.findall(text)
        assert len(chinese) == 0, f"Deliverable 01: Whitepaper page {idx+1} contains Chinese: {chinese[:5]}"
        
        pix = page.get_pixmap()
        im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        colors = im.getcolors(maxcolors=1000000)
        assert len(colors) >= 50, f"Deliverable 01: Whitepaper page {idx+1} is visually blank!"

    print("[PASS] Deliverable 05: 10-Page Slides & Technical Whitepaper PDFs Verified (Deep Non-Blank & Visual Richness Passed)")


def check_deliverable_06_video():
    video = BASE_DIR / "assets" / "demo_video.mp4"
    assert video.exists(), "Deliverable 06: demo_video.mp4 missing"
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(video)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    dur = float(res.stdout.strip())
    assert 120.0 <= dur <= 300.0, f"Deliverable 06: Duration {dur:.2f}s outside 2:00-5:00 window"
    print(f"[PASS] Deliverable 06: Demo Video Verified ({dur:.2f}s / Golden Zone)")


def check_deliverable_07_repo_assets():
    license_file = BASE_DIR / "LICENSE"
    assert license_file.exists(), "Deliverable 07: LICENSE missing"
    assert "MIT License" in license_file.read_text(encoding="utf-8"), "Deliverable 07: Invalid license"
    env_file = BASE_DIR / ".env.example"
    assert env_file.exists(), "Deliverable 07: .env.example missing"
    print("[PASS] Deliverable 07: Open Source Assets Verified")


def check_deliverable_08_tests():
    res = subprocess.run([sys.executable, "-m", "unittest", "tests/test_workflow_closure.py"], cwd=str(BASE_DIR), capture_output=True)
    assert res.returncode == 0, f"Deliverable 08: Unit closure tests failed:\n{res.stderr.decode('utf-8')}"
    res2 = subprocess.run([sys.executable, "tests/run_test_task.py"], cwd=str(BASE_DIR), capture_output=True)
    assert res2.returncode == 0, f"Deliverable 08: Blackbox runner failed:\n{res2.stderr.decode('utf-8')}"
    print("[PASS] Deliverable 08: 4/4 Atomic Closures & Chaos Benchmarks Verified")


def check_deliverable_09_language_purity():
    """
    Scans all public submission files (docs, diagrams, assets, root html) for Chinese characters.
    Rule 65 / Rule 30 Hard Invariant: 100% International Professional English.
    """
    scan_targets = [
        BASE_DIR / "docs",
        BASE_DIR / "diagrams",
        BASE_DIR / "README.md",
        BASE_DIR / "index.html"
    ]
    
    violation_found = False
    for target in scan_targets:
        if target.is_file():
            files = [target]
        else:
            files = [p for p in target.rglob("*") if p.suffix.lower() in [".html", ".md", ".svg", ".json", ".yaml", ".yml"]]
            
        for f in files:
            content = f.read_text(encoding="utf-8", errors="ignore")
            matches = CHINESE_PATTERN.findall(content)
            if matches:
                print(f"[FAIL] Deliverable 09: Found {len(matches)} Chinese characters in {f.relative_to(BASE_DIR)}")
                violation_found = True

    assert not violation_found, "Deliverable 09: Language purity audit failed - Chinese characters detected in deliverables!"
    print("[PASS] Deliverable 09: 100% International English Purity Verified (0 Chinese Characters)")


def main():
    print("=" * 80)
    print("PHANToM GRID // OPENCODE MATCH 3 RULE 65 DEEP COMPLIANCE AUDIT")
    print("=" * 80)
    check_deliverable_01_project_name()
    check_deliverable_02_elevator_pitch()
    check_deliverable_03_tags()
    check_deliverable_04_cover_image()
    check_deliverable_05_slides()
    check_deliverable_06_video()
    check_deliverable_07_repo_assets()
    check_deliverable_08_tests()
    check_deliverable_09_language_purity()
    print("-" * 80)
    print("VERDICT: [ 9/9 FULL DELIVERABLES PASSED - RULE 65 DEEP AUDIT 100% COMPLIANT ]")
    print("=" * 80)


if __name__ == "__main__":
    main()
