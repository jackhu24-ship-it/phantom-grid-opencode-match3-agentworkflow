# -*- coding: utf-8 -*-
"""
PHANToM GRID // OpenCode Match 3 - Rule 65 Sovereign Compliance Audit
Standard: STD-TOURNAMENT-TRI (Rule 65 / v6.1.0 Constitution)
Ratified by: Commander Jack Hu x Commander Xiaomi
"""

import sys
import subprocess
from pathlib import Path
from PIL import Image
import pypdf

BASE_DIR = Path(__file__).resolve().parent.parent

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
    slides = BASE_DIR / "docs" / "SLIDES_PRESENTATION.pdf"
    assert slides.exists(), "Deliverable 05: SLIDES_PRESENTATION.pdf missing"
    reader = pypdf.PdfReader(str(slides))
    assert len(reader.pages) == 10, f"Deliverable 05: Expected 10 slides, got {len(reader.pages)}"
    print("[PASS] Deliverable 05: 10-Page Slides PDF Verified")

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

def main():
    print("=" * 80)
    print("PHANToM GRID // OPENCODE MATCH 3 RULE 65 COMPLIANCE AUDIT")
    print("=" * 80)
    check_deliverable_01_project_name()
    check_deliverable_02_elevator_pitch()
    check_deliverable_03_tags()
    check_deliverable_04_cover_image()
    check_deliverable_05_slides()
    check_deliverable_07_repo_assets()
    check_deliverable_08_tests()
    print("-" * 80)
    print("VERDICT: [ 7/7 ACTIVE DELIVERABLES PASSED - RULE 65 COMPLIANT ]")
    print("=" * 80)

if __name__ == "__main__":
    main()
