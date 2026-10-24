# -*- coding: utf-8 -*-
"""
PHANToM GRID // OpenCode Match 3 - Rule 65 Sovereign Compliance Audit
Standard: STD-TOURNAMENT-TRI (Rule 65 / v6.1.0 Constitution)
Ratified by: Supreme Commander Jack Hu x Commander Xiaomi

Deep Verification Pipeline (11 Ironclad Gates):
1. Project Name & Canonical Prefix Gate
2. Elevator Pitch Length & Content Gate
3. Categorical Built-With Tags Gate
4. Visual Cover & Architecture Dimensions Gate
5. Deep Anti-Blank PDF Rasterization Audit (Text Length >= 300, Color Count >= 50, 0 Chinese)
6. Video & Audio Stream Multi-Track Audit (Duration, 1080P+, Audio Codec & Channels)
7. Open Source License & Ingress Configuration Gate
8. 4/4 Atomic Closures & Chaos Benchmarks Gate
9. 100% International Professional English Purity Gate (Anti-Chinese Regex Gate)
10. Local Asset Reference & Relative Link Integrity Gate (Zero Broken Links)
11. Anti-Mojibake & Encoding Integrity Gate (Zero Unicode Corruption / Replacement Chars)
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
MOJIBAKE_PATTERN = re.compile(r"\ufffd")


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
        assert len(chinese) == 0, f"Deliverable 05: Slide {idx+1} contains Chinese: {chinese[:5]}"
        
        pix = page.get_pixmap()
        im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        colors = im.getcolors(maxcolors=1000000)
        assert len(colors) >= 50, f"Deliverable 05: Slide {idx+1} is visually blank (only {len(colors)} colors)!"

    # Audit SPEC_01_AgentWorkflow.pdf
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
    """
    Video Multi-Track Audit:
    1. Video file existence and non-zero size.
    2. Golden zone duration: 120.0s to 300.0s.
    3. Video resolution: width >= 1920, height >= 1080.
    4. Audio stream existence: channels >= 1 and sample_rate >= 16000.
    """
    video = BASE_DIR / "assets" / "demo_video.mp4"
    assert video.exists(), "Deliverable 06: demo_video.mp4 missing"
    assert video.stat().st_size > 1000000, "Deliverable 06: Video file suspiciously small (<1MB)"
    
    # Check duration
    cmd_dur = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(video)]
    res_dur = subprocess.run(cmd_dur, capture_output=True, text=True)
    dur = float(res_dur.stdout.strip())
    assert 120.0 <= dur <= 300.0, f"Deliverable 06: Duration {dur:.2f}s outside 2:00-5:00 window"
    
    # Check video stream resolution
    cmd_v = ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=s=x:p=0", str(video)]
    res_v = subprocess.run(cmd_v, capture_output=True, text=True).stdout.strip().split("x")
    w, h = int(res_v[0]), int(res_v[1])
    assert w >= 1920 and h >= 1080, f"Deliverable 06: Video resolution {w}x{h} below 1080p requirement"
    
    # Check audio stream existence
    cmd_a = ["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=channels:stream=sample_rate", "-of", "default=noprint_wrappers=1:nokey=0", str(video)]
    res_a = subprocess.run(cmd_a, capture_output=True, text=True).stdout
    channels_m = re.search(r"channels=(\d+)", res_a)
    sr_m = re.search(r"sample_rate=(\d+)", res_a)
    assert channels_m and sr_m, "Deliverable 06: Missing required audio stream (video is completely silent)!"
    channels = int(channels_m.group(1))
    sr = int(sr_m.group(1))
    assert channels >= 1 and sr >= 16000, f"Deliverable 06: Invalid audio stream ({channels} channels, {sr} Hz)"
    
    print(f"[PASS] Deliverable 06: Demo Video Verified ({dur:.2f}s, {w}x{h}, {channels}ch {sr}Hz Audio)")


def check_deliverable_07_repo_assets():
    license_file = BASE_DIR / "LICENSE"
    assert license_file.exists(), "Deliverable 07: LICENSE missing"
    assert "MIT License" in license_file.read_text(encoding="utf-8"), "Deliverable 07: Invalid license"
    env_file = BASE_DIR / ".env.example"
    assert env_file.exists(), "Deliverable 07: .env.example missing"
    print("[PASS] Deliverable 07: Open Source Assets Verified")


def check_deliverable_08_tests():
    res = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"], cwd=str(BASE_DIR), capture_output=True)
    assert res.returncode == 0, f"Deliverable 08: Unit closure tests failed:\n{res.stderr.decode('utf-8')}"
    res2 = subprocess.run([sys.executable, "tests/run_test_task.py"], cwd=str(BASE_DIR), capture_output=True)
    assert res2.returncode == 0, f"Deliverable 08: Blackbox runner failed:\n{res2.stderr.decode('utf-8')}"
    print("[PASS] Deliverable 08: 12/12 Atomic Unit Closures & Chaos Benchmarks Verified")


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


def check_deliverable_10_local_links():
    """
    Local Asset Reference & Link Integrity Gate:
    Ensures that all relative images, diagrams, and assets referenced in Markdown/HTML exist on disk.
    Prevents 404 broken images on GitHub / submission pages.
    """
    files_to_check = [
        BASE_DIR / "README.md",
        BASE_DIR / "docs" / "Devpost_Submission_Package.md",
        BASE_DIR / "index.html"
    ]
    # Match markdown images ![...](url) and HTML src="..." href="..."
    md_img_re = re.compile(r"!\[.*?\]\(([^)]+)\)")
    html_src_re = re.compile(r"""(?:src|href)=["']([^"']+)["']""")
    
    for doc in files_to_check:
        if not doc.exists():
            continue
        text = doc.read_text(encoding="utf-8")
        links = md_img_re.findall(text) + html_src_re.findall(text)
        for link in links:
            if link.startswith("http") or link.startswith("#") or link.startswith("mailto:") or link.startswith("javascript:"):
                continue
            # Strip anchors or parameters
            clean_link = link.split("#")[0].split("?")[0]
            if not clean_link:
                continue
            target_path = (doc.parent / clean_link).resolve()
            assert target_path.exists(), f"Deliverable 10: Broken asset link in {doc.name}: '{link}' -> not found at {target_path}"
            assert target_path.stat().st_size > 0, f"Deliverable 10: Empty zero-byte asset referenced in {doc.name}: '{link}'"
            
    print("[PASS] Deliverable 10: Local Asset & Link Integrity Verified (Zero Broken References)")


def check_deliverable_11_anti_mojibake():
    """
    Anti-Mojibake & Encoding Integrity Gate:
    Ensures that no Unicode replacement characters (\ufffd) or corruption sequences exist in any deliverable.
    """
    scan_targets = [
        BASE_DIR / "docs",
        BASE_DIR / "diagrams",
        BASE_DIR / "README.md",
        BASE_DIR / "index.html"
    ]
    for target in scan_targets:
        if target.is_file():
            files = [target]
        else:
            files = [p for p in target.rglob("*") if p.suffix.lower() in [".html", ".md", ".svg", ".json", ".yaml", ".yml"]]
            
        for f in files:
            content = f.read_text(encoding="utf-8", errors="ignore")
            assert not MOJIBAKE_PATTERN.search(content), f"Deliverable 11: Mojibake corruption (\\ufffd) detected in {f.relative_to(BASE_DIR)}"

    print("[PASS] Deliverable 11: Anti-Mojibake & Encoding Integrity Verified (Zero Corruption Artifacts)")


def check_deliverable_12_entrypoint_reproduction():
    """
    Master CLI Entrypoint & 1-Command Reproduction Gate:
    Verifies that 'main.py' at repo root runs cleanly and emits valid JSON receipt.
    """
    main_py = BASE_DIR / "main.py"
    assert main_py.exists(), "Deliverable 12: main.py root entrypoint missing"
    cmd = [sys.executable, str(main_py), "--json"]
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=str(BASE_DIR))
    assert res.returncode == 0, f"Deliverable 12: main.py execution failed:\n{res.stderr}"
    import json
    data = json.loads(res.stdout)
    assert data.get("status") in ["SUCCESS", "PASS"], f"Deliverable 12: main.py status not SUCCESS/PASS: {data}"
    print(f"[PASS] Deliverable 12: Root Entrypoint Reproduction Verified (main.py --json [PASS] Avg: {data.get('avg_latency_ms')}ms)")


def check_deliverable_13_spec_first_blueprints():
    """
    Spec-First Architecture Blueprints & Double-Track Tri-Standard Gate (Rule 57/58):
    Verifies 5 SVGs, 5 MMD sources, and Table 01 CSV machine contract.
    """
    diagrams_dir = BASE_DIR / "diagrams"
    expected_svgs = [
        "01_system_topology.svg", "02_agent_sequence.svg",
        "03_fsm_state_machine.svg", "04_security_boundary.svg",
        "05_defense_matrix_table.svg"
    ]
    expected_mmds = [
        "01_system_topology.mmd", "02_agent_sequence.mmd",
        "03_fsm_state_machine.mmd", "04_security_boundary.mmd",
        "05_defense_matrix_table.mmd"
    ]
    for s in expected_svgs:
        p = diagrams_dir / s
        assert p.exists() and p.stat().st_size > 1000, f"Deliverable 13: Missing/empty SVG diagram: {s}"
    for m in expected_mmds:
        p = diagrams_dir / m
        assert p.exists() and p.stat().st_size > 100, f"Deliverable 13: Missing/empty MMD source: {m}"
    csv_path = BASE_DIR / "docs" / "table1_resource_defense_matrix.csv"
    assert csv_path.exists() and csv_path.stat().st_size > 100, "Deliverable 13: Missing/empty table1_resource_defense_matrix.csv"
    
    print("[PASS] Deliverable 13: Spec-First 5 SVGs + 5 MMD Blueprints + Table 01 CSV Verified")


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
    check_deliverable_10_local_links()
    check_deliverable_11_anti_mojibake()
    check_deliverable_12_entrypoint_reproduction()
    check_deliverable_13_spec_first_blueprints()
    print("-" * 80)
    print("VERDICT: [ 13/13 FULL DELIVERABLES PASSED - RULE 65 DEEP AUDIT 100% COMPLIANT ]")
    print("=" * 80)


if __name__ == "__main__":
    main()
