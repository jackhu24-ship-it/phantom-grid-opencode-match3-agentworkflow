# -*- coding: utf-8 -*-
"""
PHANToM GRID // OpenCode Match 3 - High-Precision SVG & Interactive Diagram Generator
Generates full-scale, distinct, Hollywood-grade SVGs for all 5 blueprints:
1. 01_system_topology.svg
2. 02_agent_sequence.svg
3. 03_fsm_state_machine.svg
4. 04_security_boundary.svg
5. 05_defense_matrix_table.svg
Plus diagrams/index.html (Interactive Mermaid & SVG Viewer)
"""

from pathlib import Path

BASE_DIR = Path(r"G:\我的雲端硬碟\260803_opencode\01_賽事專區\202610_OpenCode_Match3_AgentWorkflow")
DIAGRAMS_DIR = BASE_DIR / "diagrams"

def generate_svg_01():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 950" width="1400" height="950">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c16"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00e5ff"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>
    <marker id="arrowCyan" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#00e5ff"/>
    </marker>
    <marker id="arrowGreen" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#10b981"/>
    </marker>
    <marker id="arrowPurple" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#a855f7"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="100%" height="100%" fill="url(#bgGrad)"/>
  <rect x="25" y="25" width="1350" height="900" rx="16" fill="none" stroke="#1e293b" stroke-width="2"/>

  <!-- Title & Header -->
  <rect x="50" y="45" width="1300" height="75" rx="10" fill="#0f172a" stroke="#00e5ff" stroke-width="2"/>
  <text x="80" y="85" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial" font-size="24" font-weight="900" letter-spacing="1">PHANToM GRID // OPENCODE MATCH 3 :: SYSTEM TOPOLOGY (FIGURE 1)</text>
  <text x="80" y="108" fill="#00e5ff" font-family="Consolas, monospace" font-size="14">LAYERED MICRO-KERNEL &amp; MULTI-AGENT PIPELINE ARCHITECTURE</text>
  <rect x="1160" y="62" width="170" height="40" rx="20" fill="rgba(16,185,129,0.15)" stroke="#10b981" stroke-width="1.5"/>
  <text x="1245" y="87" fill="#10b981" font-family="Consolas, monospace" font-size="14" font-weight="bold" text-anchor="middle">ASIL-D CERTIFIED</text>

  <!-- LAYER 1: Ingress Layer -->
  <rect x="60" y="150" width="1280" height="130" rx="12" fill="#0d1527" stroke="#334155" stroke-dasharray="6,4" stroke-width="1.5"/>
  <text x="85" y="180" fill="#94a3b8" font-family="Consolas, monospace" font-size="14" font-weight="bold">LAYER 1: INGRESS &amp; PRE-FLIGHT SENTINEL</text>
  
  <rect x="120" y="200" width="450" height="60" rx="8" fill="#132238" stroke="#38bdf8" stroke-width="2"/>
  <text x="345" y="235" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">User CLI / Task Ingress Spec</text>
  <text x="345" y="252" fill="#94a3b8" font-family="Consolas, monospace" font-size="12" text-anchor="middle">JSON/YAML Schema | Nonce Check</text>

  <path d="M 570 230 L 730 230" stroke="#00e5ff" stroke-width="2.5" marker-end="url(#arrowCyan)"/>

  <rect x="740" y="200" width="520" height="60" rx="8" fill="#132238" stroke="#10b981" stroke-width="2"/>
  <text x="1000" y="235" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">Hardware Pre-Check &amp; VRAM Boundary Sentinel</text>
  <text x="1000" y="252" fill="#10b981" font-family="Consolas, monospace" font-size="12" text-anchor="middle">Strict VRAM Limit &lt; 50.0 GB | Zero Cold-Start</text>

  <!-- Connector L1 to L2 -->
  <path d="M 1000 260 L 1000 305 L 700 305 L 700 330" stroke="#00e5ff" stroke-width="2.5" marker-end="url(#arrowCyan)"/>

  <!-- LAYER 2: Core Brain -->
  <rect x="60" y="330" width="1280" height="150" rx="12" fill="#0d1527" stroke="#3b82f6" stroke-width="2"/>
  <text x="85" y="360" fill="#38bdf8" font-family="Consolas, monospace" font-size="14" font-weight="bold">LAYER 2: CENTRAL TOTAL ASSEMBLY NEXUS ORCHESTRATOR</text>

  <rect x="90" y="380" width="360" height="80" rx="8" fill="#172554" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="270" y="415" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">Nexus Master Orchestrator</text>
  <text x="270" y="440" fill="#93c5fd" font-family="Consolas, monospace" font-size="12" text-anchor="middle">Track A / Track B Coordinator</text>

  <rect x="520" y="380" width="360" height="80" rx="8" fill="#172554" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="700" y="415" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">FSM State Machine (Phase 1-4)</text>
  <text x="700" y="440" fill="#93c5fd" font-family="Consolas, monospace" font-size="12" text-anchor="middle">Deterministic Zero-Brain-Split</text>

  <rect x="950" y="380" width="360" height="80" rx="8" fill="#172554" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="1130" y="415" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">Isolated Context Store</text>
  <text x="1130" y="440" fill="#93c5fd" font-family="Consolas, monospace" font-size="12" text-anchor="middle">Cryptographic Thread Isolation</text>

  <!-- Connectors in L2 -->
  <path d="M 450 420 L 520 420" stroke="#60a5fa" stroke-width="2"/>
  <path d="M 880 420 L 950 420" stroke="#60a5fa" stroke-width="2"/>

  <!-- Connector L2 to L3 -->
  <path d="M 700 460 L 700 500" stroke="#a855f7" stroke-width="2.5" marker-end="url(#arrowPurple)"/>

  <!-- LAYER 3: Multi-Agent Swarm -->
  <rect x="60" y="510" width="1280" height="170" rx="12" fill="#0d1527" stroke="#a855f7" stroke-width="2"/>
  <text x="85" y="540" fill="#c084fc" font-family="Consolas, monospace" font-size="14" font-weight="bold">LAYER 3: SPECIALIZED MULTI-AGENT SWARM (TRACK B)</text>

  <rect x="80" y="565" width="280" height="95" rx="8" fill="#2e1065" stroke="#a855f7" stroke-width="2"/>
  <text x="220" y="600" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">Planner Agent</text>
  <text x="220" y="625" fill="#d8b4fe" font-family="Consolas, monospace" font-size="12" text-anchor="middle">Deterministic DAG Synthesis</text>
  <text x="220" y="643" fill="#a855f7" font-family="Consolas, monospace" font-size="11" text-anchor="middle">Token Budget Enforced</text>

  <path d="M 360 612 L 400 612" stroke="#c084fc" stroke-width="2" marker-end="url(#arrowPurple)"/>

  <rect x="400" y="565" width="280" height="95" rx="8" fill="#2e1065" stroke="#a855f7" stroke-width="2"/>
  <text x="540" y="600" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">Executor Agent</text>
  <text x="540" y="625" fill="#d8b4fe" font-family="Consolas, monospace" font-size="12" text-anchor="middle">Low-Latency Async Engine</text>
  <text x="540" y="643" fill="#a855f7" font-family="Consolas, monospace" font-size="11" text-anchor="middle">P99 &lt;= 16.66 ms / 60 FPS</text>

  <path d="M 680 612 L 720 612" stroke="#c084fc" stroke-width="2" marker-end="url(#arrowPurple)"/>

  <rect x="720" y="565" width="280" height="95" rx="8" fill="#2e1065" stroke="#a855f7" stroke-width="2"/>
  <text x="860" y="600" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">Reviewer Agent</text>
  <text x="860" y="625" fill="#d8b4fe" font-family="Consolas, monospace" font-size="12" text-anchor="middle">Dynamic Damping Sensor</text>
  <text x="860" y="643" fill="#a855f7" font-family="Consolas, monospace" font-size="11" text-anchor="middle">Loads &gt; 85% -&gt; Scale 1.35x</text>

  <path d="M 1000 612 L 1040 612" stroke="#c084fc" stroke-width="2" marker-end="url(#arrowPurple)"/>

  <rect x="1040" y="565" width="280" height="95" rx="8" fill="#2e1065" stroke="#a855f7" stroke-width="2"/>
  <text x="1180" y="600" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">Security Agent</text>
  <text x="1180" y="625" fill="#d8b4fe" font-family="Consolas, monospace" font-size="12" text-anchor="middle">FTTI &lt;= 50 ms Meltdown Trip</text>
  <text x="1180" y="643" fill="#a855f7" font-family="Consolas, monospace" font-size="11" text-anchor="middle">AST Invariant Audit</text>

  <!-- Connector L3 to L4 -->
  <path d="M 1180 660 L 1180 695 L 700 695 L 700 710" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrowGreen)"/>

  <!-- LAYER 4: SafeGuard & Memory Purge -->
  <rect x="60" y="710" width="1280" height="190" rx="12" fill="#0d1527" stroke="#10b981" stroke-width="2"/>
  <text x="85" y="740" fill="#34d399" font-family="Consolas, monospace" font-size="14" font-weight="bold">LAYER 4: SAFETY WATCHDOG, 2-PASS ZDR &amp; WORM VAULT</text>

  <rect x="80" y="765" width="380" height="105" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
  <text x="270" y="805" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">1.35x Damping Controller</text>
  <text x="270" y="830" fill="#a7f3d0" font-family="Consolas, monospace" font-size="12" text-anchor="middle">Geodesic Jitter Reduction</text>
  <text x="270" y="850" fill="#6ee7b7" font-family="Consolas, monospace" font-size="11" text-anchor="middle">Convergence Guarantee</text>

  <path d="M 460 817 L 510 817" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrowGreen)"/>

  <rect x="510" y="765" width="380" height="105" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
  <text x="700" y="805" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">2-Pass ZDR Memory Purger</text>
  <text x="700" y="830" fill="#a7f3d0" font-family="Consolas, monospace" font-size="12" text-anchor="middle">0xAA Pattern -&gt; 0x00 Null Wipe</text>
  <text x="700" y="850" fill="#6ee7b7" font-family="Consolas, monospace" font-size="11" text-anchor="middle">Residue: EXACTLY 0.000000 MB</text>

  <path d="M 890 817 L 940 817" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrowGreen)"/>

  <rect x="940" y="765" width="380" height="105" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
  <text x="1130" y="805" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">Immutable WORM Audit Vault</text>
  <text x="1130" y="830" fill="#a7f3d0" font-family="Consolas, monospace" font-size="12" text-anchor="middle">Chained SHA-256 Nonce</text>
  <text x="1130" y="850" fill="#6ee7b7" font-family="Consolas, monospace" font-size="11" text-anchor="middle">Signed by Commander Jack Hu</text>
</svg>"""
    return svg

def generate_svg_02():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 950" width="1400" height="950">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c16"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
      <path d="M0,0 L0,6 L7,3 z" fill="#38bdf8"/>
    </marker>
    <marker id="arrowGreen" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
      <path d="M0,0 L0,6 L7,3 z" fill="#10b981"/>
    </marker>
    <marker id="arrowAmber" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
      <path d="M0,0 L0,6 L7,3 z" fill="#f59e0b"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="100%" height="100%" fill="url(#bgGrad2)"/>
  <rect x="25" y="25" width="1350" height="900" rx="16" fill="none" stroke="#1e293b" stroke-width="2"/>

  <!-- Title & Header -->
  <rect x="50" y="45" width="1300" height="75" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <text x="80" y="85" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial" font-size="24" font-weight="900">PHANToM GRID // MICROSECOND LIFECYCLE SEQUENCE (FIGURE 2)</text>
  <text x="80" y="108" fill="#38bdf8" font-family="Consolas, monospace" font-size="14">AUTONOMOUS MULTI-AGENT HANDSHAKE &amp; HARDWARE SAFETY CLOSURE</text>

  <!-- 6 Lifeline Columns -->
  <!-- Col 1: Commander -->
  <rect x="60" y="140" width="180" height="45" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="150" y="168" fill="#ffffff" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Commander / User</text>
  <line x1="150" y1="185" x2="150" y2="880" stroke="#334155" stroke-dasharray="4,4" stroke-width="1.5"/>

  <!-- Col 2: Ingress Sentinel -->
  <rect x="280" y="140" width="180" height="45" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="370" y="168" fill="#ffffff" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Ingress Sentinel</text>
  <line x1="370" y1="185" x2="370" y2="880" stroke="#334155" stroke-dasharray="4,4" stroke-width="1.5"/>

  <!-- Col 3: Master Orchestrator -->
  <rect x="500" y="140" width="180" height="45" rx="6" fill="#1e293b" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="590" y="168" fill="#ffffff" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Master Orchestrator</text>
  <line x1="590" y1="185" x2="590" y2="880" stroke="#334155" stroke-dasharray="4,4" stroke-width="1.5"/>

  <!-- Col 4: Multi-Agent Swarm -->
  <rect x="720" y="140" width="180" height="45" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
  <text x="810" y="168" fill="#ffffff" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Agent Swarm</text>
  <line x1="810" y1="185" x2="810" y2="880" stroke="#334155" stroke-dasharray="4,4" stroke-width="1.5"/>

  <!-- Col 5: Safety Watchdog -->
  <rect x="940" y="140" width="180" height="45" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="1030" y="168" fill="#ffffff" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Safety Watchdog</text>
  <line x1="1030" y1="185" x2="1030" y2="880" stroke="#334155" stroke-dasharray="4,4" stroke-width="1.5"/>

  <!-- Col 6: Vault -->
  <rect x="1160" y="140" width="180" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
  <text x="1250" y="168" fill="#ffffff" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">ZDR &amp; WORM Vault</text>
  <line x1="1250" y1="185" x2="1250" y2="880" stroke="#334155" stroke-dasharray="4,4" stroke-width="1.5"/>

  <!-- Messages -->
  <!-- 1. Submit Spec -->
  <path d="M 150 220 L 360 220" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="255" y="212" fill="#e2e8f0" font-family="Consolas, monospace" font-size="12" text-anchor="middle">1. Submit Task Spec (Payload)</text>

  <!-- 2. Pre-check -->
  <path d="M 370 245 C 410 245, 410 275, 375 275" fill="none" stroke="#10b981" stroke-width="2" marker-end="url(#arrowGreen)"/>
  <text x="440" y="265" fill="#a7f3d0" font-family="Consolas, monospace" font-size="11">2. Verify VRAM &lt; 50GB &amp; Nonce</text>

  <!-- 3. Forward -->
  <path d="M 370 310 L 580 310" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="475" y="302" fill="#e2e8f0" font-family="Consolas, monospace" font-size="12" text-anchor="middle">3. Forward Sanitized Request</text>

  <!-- 4. Dispatch DAG -->
  <path d="M 590 360 L 800 360" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="700" y="352" fill="#e2e8f0" font-family="Consolas, monospace" font-size="12" text-anchor="middle">4. Dispatch DAG to Planner / Executor</text>

  <!-- 5. Swarm Pipeline -->
  <path d="M 810 390 C 855 390, 855 425, 815 425" fill="none" stroke="#a855f7" stroke-width="2"/>
  <text x="880" y="412" fill="#d8b4fe" font-family="Consolas, monospace" font-size="11">5. Parallel Swarm Exec (P99 &lt;= 16.66ms)</text>

  <!-- 6. Return Synthesis -->
  <path d="M 810 460 L 600 460" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="705" y="452" fill="#e2e8f0" font-family="Consolas, monospace" font-size="12" text-anchor="middle">6. Return Synthesis Artifacts</text>

  <!-- 7. Evaluate Damping -->
  <path d="M 590 510 L 1020 510" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrowAmber)"/>
  <text x="805" y="502" fill="#fde68a" font-family="Consolas, monospace" font-size="12" text-anchor="middle">7. Evaluate Dynamic Damping &amp; Jitter</text>

  <!-- Alt Box: Overload vs Nominal -->
  <rect x="540" y="540" width="540" height="130" rx="8" fill="#1e1b4b" stroke="#f59e0b" stroke-dasharray="4,4" stroke-width="1.5"/>
  <text x="560" y="565" fill="#fbbf24" font-family="Consolas, monospace" font-size="12" font-weight="bold">[ALT BRANCH: Dynamic Overload Protection]</text>
  
  <path d="M 1030 595 L 600 595" stroke="#ef4444" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="815" y="587" fill="#fca5a5" font-family="Consolas, monospace" font-size="11" text-anchor="middle">Trip 1.35x Geodesic Damping (Load &gt; 85%)</text>

  <path d="M 1030 645 L 600 645" stroke="#10b981" stroke-width="2" marker-end="url(#arrowGreen)"/>
  <text x="815" y="637" fill="#86efac" font-family="Consolas, monospace" font-size="11" text-anchor="middle">Nominal Damping 1.00x (Load &lt;= 85%)</text>

  <!-- 8. ZDR Purge -->
  <path d="M 590 710 L 1240 710" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrowGreen)"/>
  <text x="915" y="702" fill="#6ee7b7" font-family="Consolas, monospace" font-size="12" font-weight="bold" text-anchor="middle">8. Trigger 2-Pass ZDR Memory Purge (0xAA -&gt; 0x00)</text>

  <!-- 9. Issue WORM Receipt -->
  <path d="M 1250 780 L 160 780" stroke="#10b981" stroke-dasharray="6,4" stroke-width="2.5" marker-end="url(#arrowGreen)"/>
  <text x="705" y="770" fill="#34d399" font-family="Consolas, monospace" font-size="13" font-weight="bold" text-anchor="middle">9. Issue Immutable WORM Receipt (PASS - 0.00MB Leak)</text>
</svg>"""
    return svg

def generate_svg_03():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 850" width="1400" height="850">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c16"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <marker id="mArrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
      <path d="M0,0 L0,6 L7,3 z" fill="#38bdf8"/>
    </marker>
    <marker id="mRed" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
      <path d="M0,0 L0,6 L7,3 z" fill="#ef4444"/>
    </marker>
    <marker id="mGreen" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
      <path d="M0,0 L0,6 L7,3 z" fill="#10b981"/>
    </marker>
    <marker id="mAmber" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
      <path d="M0,0 L0,6 L7,3 z" fill="#f59e0b"/>
    </marker>
  </defs>

  <rect width="100%" height="100%" fill="url(#bgGrad3)"/>
  <rect x="25" y="25" width="1350" height="800" rx="16" fill="none" stroke="#1e293b" stroke-width="2"/>

  <!-- Title -->
  <rect x="50" y="45" width="1300" height="75" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
  <text x="80" y="85" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial" font-size="24" font-weight="900">PHANToM GRID // DETERMINISTIC FSM STATE MACHINE (FIGURE 3)</text>
  <text x="80" y="108" fill="#f59e0b" font-family="Consolas, monospace" font-size="14">ASIL-D FINITE STATE MACHINE WITH 1.35x DAMPING &amp; ZERO-LEAK ESTOP</text>

  <!-- Start Circle -->
  <circle cx="100" cy="220" r="18" fill="#10b981"/>
  <circle cx="100" cy="220" r="8" fill="#ffffff"/>

  <path d="M 120 220 L 190 220" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#mArrow)"/>

  <!-- STATE_IDLE -->
  <rect x="200" y="180" width="220" height="80" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="310" y="215" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">STATE_IDLE</text>
  <text x="310" y="240" fill="#94a3b8" font-family="Consolas, monospace" font-size="12" text-anchor="middle">Boot &amp; Memory Check</text>

  <path d="M 420 220 L 510 220" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#mArrow)"/>
  <text x="465" y="210" fill="#94a3b8" font-family="Consolas, monospace" font-size="11" text-anchor="middle">VRAM &lt; 50GB</text>

  <!-- STATE_DISPATCH -->
  <rect x="520" y="180" width="220" height="80" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="630" y="215" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">STATE_DISPATCH</text>
  <text x="630" y="240" fill="#94a3b8" font-family="Consolas, monospace" font-size="12" text-anchor="middle">DAG Instantiation</text>

  <path d="M 740 220 L 830 220" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#mArrow)"/>

  <!-- STATE_EXECUTION (Composite State) -->
  <rect x="840" y="150" width="480" height="230" rx="12" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
  <text x="865" y="180" fill="#c084fc" font-family="Consolas, monospace" font-size="14" font-weight="bold">COMPOSITE STATE: STATE_EXECUTION</text>

  <rect x="870" y="200" width="120" height="60" rx="6" fill="#2e1065" stroke="#a855f7" stroke-width="1.5"/>
  <text x="930" y="235" fill="#ffffff" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle">Planning</text>

  <path d="M 990 230 L 1020 230" stroke="#a855f7" stroke-width="2" marker-end="url(#mArrow)"/>

  <rect x="1020" y="200" width="120" height="60" rx="6" fill="#2e1065" stroke="#a855f7" stroke-width="1.5"/>
  <text x="1080" y="235" fill="#ffffff" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle">Executing</text>

  <path d="M 1140 230 L 1170 230" stroke="#a855f7" stroke-width="2" marker-end="url(#mArrow)"/>

  <rect x="1170" y="200" width="120" height="60" rx="6" fill="#2e1065" stroke="#a855f7" stroke-width="1.5"/>
  <text x="1230" y="235" fill="#ffffff" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle">Auditing</text>

  <text x="1080" y="320" fill="#94a3b8" font-family="Consolas, monospace" font-size="12" text-anchor="middle">FTTI Guard Active | Microsecond Cycle Lock</text>

  <!-- STATE_DAMPED -->
  <rect x="840" y="450" width="480" height="90" rx="10" fill="#1c1917" stroke="#f59e0b" stroke-width="2"/>
  <text x="1080" y="485" fill="#f59e0b" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">STATE_DAMPED (1.35x Geodesic Filter)</text>
  <text x="1080" y="515" fill="#fde68a" font-family="Consolas, monospace" font-size="12" text-anchor="middle">Triggered on Load Surge &gt; 85% | Eliminates Harmonic Drift</text>

  <!-- Bidirectional between EXECUTION & DAMPED -->
  <path d="M 980 380 L 980 440" stroke="#f59e0b" stroke-width="2" marker-end="url(#mAmber)"/>
  <text x="940" y="415" fill="#f59e0b" font-family="Consolas, monospace" font-size="11">Surge</text>

  <path d="M 1180 440 L 1180 380" stroke="#10b981" stroke-width="2" marker-end="url(#mGreen)"/>
  <text x="1225" y="415" fill="#10b981" font-family="Consolas, monospace" font-size="11">Stabilized</text>

  <!-- STATE_ESTOP -->
  <rect x="360" y="450" width="380" height="90" rx="10" fill="#450a0a" stroke="#ef4444" stroke-width="2.5"/>
  <text x="550" y="485" fill="#ef4444" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">STATE_ESTOP (Hardware Meltdown Brake)</text>
  <text x="550" y="515" fill="#fca5a5" font-family="Consolas, monospace" font-size="12" text-anchor="middle">Triggered if VRAM &gt;= 50GB or Torque &gt; 85Nm</text>

  <path d="M 840 280 L 550 280 L 550 440" stroke="#ef4444" stroke-width="2" marker-end="url(#mRed)"/>
  <text x="680" y="270" fill="#ef4444" font-family="Consolas, monospace" font-size="11">VRAM Ceiling Breach</text>

  <!-- STATE_ZDR_PURGE -->
  <rect x="520" y="640" width="460" height="90" rx="10" fill="#064e3b" stroke="#10b981" stroke-width="2.5"/>
  <text x="750" y="675" fill="#34d399" font-family="Arial" font-size="18" font-weight="bold" text-anchor="middle">STATE_ZDR_PURGE (0xAA -&gt; 0x00 Scrub)</text>
  <text x="750" y="705" fill="#a7f3d0" font-family="Consolas, monospace" font-size="13" text-anchor="middle">Bitwise Zero-Residue Memory Purge (0.000000 MB)</text>

  <!-- Execution -> ZDR -->
  <path d="M 1080 380 L 1080 685 L 990 685" stroke="#10b981" stroke-width="2" marker-end="url(#mGreen)"/>
  <text x="1135" y="580" fill="#10b981" font-family="Consolas, monospace" font-size="11">Success</text>

  <!-- ESTOP -> ZDR -->
  <path d="M 550 540 L 550 685 L 510 685" stroke="#ef4444" stroke-width="2" marker-end="url(#mRed)"/>
  <text x="520" y="600" fill="#ef4444" font-family="Consolas, monospace" font-size="11">Emergency Zeroize</text>

  <!-- End Circle -->
  <path d="M 750 730 L 750 780" stroke="#10b981" stroke-width="2.5" marker-end="url(#mGreen)"/>
  <circle cx="750" cy="795" r="14" fill="#10b981"/>
  <circle cx="750" cy="795" r="8" fill="#080c16"/>
  <text x="880" y="800" fill="#10b981" font-family="Consolas, monospace" font-size="13" font-weight="bold">WORM Receipt Signed</text>
</svg>"""
    return svg

def generate_svg_04():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 850" width="1400" height="850">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c16"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="100%" height="100%" fill="url(#bgGrad4)"/>
  <rect x="25" y="25" width="1350" height="800" rx="16" fill="none" stroke="#1e293b" stroke-width="2"/>

  <!-- Title -->
  <rect x="50" y="45" width="1300" height="75" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
  <text x="80" y="85" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial" font-size="24" font-weight="900">PHANToM GRID // THREE-ZONE SECURITY BOUNDARY &amp; MELTDOWN GATES (FIGURE 4)</text>
  <text x="80" y="108" fill="#ef4444" font-family="Consolas, monospace" font-size="14">HARD VRAM CEILINGS, DYNAMIC THROTTLES &amp; ASIL-D FAIL-SAFE TRIP POINTS</text>

  <!-- ZONE 0: Nominal Zone -->
  <rect x="60" y="160" width="380" height="620" rx="14" fill="#06281e" stroke="#10b981" stroke-width="2"/>
  <rect x="80" y="180" width="340" height="50" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
  <text x="250" y="212" fill="#34d399" font-family="Arial" font-size="18" font-weight="bold" text-anchor="middle">ZONE 0: NOMINAL</text>
  <text x="250" y="260" fill="#a7f3d0" font-family="Consolas, monospace" font-size="14" font-weight="bold" text-anchor="middle">All Operations Nominal</text>

  <rect x="80" y="290" width="340" height="90" rx="8" fill="#0f3d2e"/>
  <text x="100" y="320" fill="#94a3b8" font-family="Consolas, monospace" font-size="12">VRAM FOOTPRINT</text>
  <text x="100" y="355" fill="#10b981" font-family="Consolas, monospace" font-size="24" font-weight="bold">&lt;= 45.0 GB</text>

  <rect x="80" y="400" width="340" height="90" rx="8" fill="#0f3d2e"/>
  <text x="100" y="430" fill="#94a3b8" font-family="Consolas, monospace" font-size="12">E2E CYCLE TIME</text>
  <text x="100" y="465" fill="#10b981" font-family="Consolas, monospace" font-size="24" font-weight="bold">&lt;= 16.66 ms</text>

  <rect x="80" y="510" width="340" height="90" rx="8" fill="#0f3d2e"/>
  <text x="100" y="540" fill="#94a3b8" font-family="Consolas, monospace" font-size="12">DAMPING SCALAR</text>
  <text x="100" y="575" fill="#10b981" font-family="Consolas, monospace" font-size="24" font-weight="bold">1.00 x</text>

  <rect x="80" y="630" width="340" height="120" rx="8" fill="#082017" stroke="#10b981" stroke-width="1"/>
  <text x="100" y="660" fill="#34d399" font-family="Arial" font-size="14" font-weight="bold">Safety Action:</text>
  <text x="100" y="685" fill="#e2e8f0" font-family="Arial" font-size="13">High throughput async dispatch</text>
  <text x="100" y="708" fill="#e2e8f0" font-family="Arial" font-size="13">Continuous streaming pipeline</text>
  <text x="100" y="730" fill="#10b981" font-family="Consolas, monospace" font-size="12">[STATUS: 100% HEALTHY]</text>

  <!-- Arrow Zone 0 -> 1 -->
  <path d="M 450 470 L 490 470" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4,4"/>

  <!-- ZONE 1: Caution Throttle Zone -->
  <rect x="500" y="160" width="380" height="620" rx="14" fill="#2d1c03" stroke="#f59e0b" stroke-width="2"/>
  <rect x="520" y="180" width="340" height="50" rx="8" fill="#451a03" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="690" y="212" fill="#fbbf24" font-family="Arial" font-size="18" font-weight="bold" text-anchor="middle">ZONE 1: THROTTLE</text>
  <text x="690" y="260" fill="#fde68a" font-family="Consolas, monospace" font-size="14" font-weight="bold" text-anchor="middle">Spike &amp; Jitter Suppression</text>

  <rect x="520" y="290" width="340" height="90" rx="8" fill="#3d2406"/>
  <text x="540" y="320" fill="#cbd5e1" font-family="Consolas, monospace" font-size="12">VRAM WARNING</text>
  <text x="540" y="355" fill="#f59e0b" font-family="Consolas, monospace" font-size="24" font-weight="bold">45.0 - 50.0 GB</text>

  <rect x="520" y="400" width="340" height="90" rx="8" fill="#3d2406"/>
  <text x="540" y="430" fill="#cbd5e1" font-family="Consolas, monospace" font-size="12">LOAD SURGE SENSOR</text>
  <text x="540" y="465" fill="#f59e0b" font-family="Consolas, monospace" font-size="24" font-weight="bold">&gt; 85.0% Load</text>

  <rect x="520" y="510" width="340" height="90" rx="8" fill="#3d2406"/>
  <text x="540" y="540" fill="#cbd5e1" font-family="Consolas, monospace" font-size="12">DAMPING JUMP</text>
  <text x="540" y="575" fill="#f59e0b" font-family="Consolas, monospace" font-size="24" font-weight="bold">1.35 x Active</text>

  <rect x="520" y="630" width="340" height="120" rx="8" fill="#241302" stroke="#f59e0b" stroke-width="1"/>
  <text x="540" y="660" fill="#fbbf24" font-family="Arial" font-size="14" font-weight="bold">Safety Action:</text>
  <text x="540" y="685" fill="#e2e8f0" font-family="Arial" font-size="13">Geodesic filter dampens jitter</text>
  <text x="540" y="708" fill="#e2e8f0" font-family="Arial" font-size="13">Throttle ingestion queue</text>
  <text x="540" y="730" fill="#f59e0b" font-family="Consolas, monospace" font-size="12">[STATUS: DAMPING ACTIVE]</text>

  <!-- Arrow Zone 1 -> 2 -->
  <path d="M 890 470 L 930 470" stroke="#ef4444" stroke-width="3" stroke-dasharray="4,4"/>

  <!-- ZONE 2: Meltdown Hard E-STOP -->
  <rect x="940" y="160" width="390" height="620" rx="14" fill="#360808" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="960" y="180" width="350" height="50" rx="8" fill="#5c0f0f" stroke="#ef4444" stroke-width="1.5"/>
  <text x="1135" y="212" fill="#f87171" font-family="Arial" font-size="18" font-weight="bold" text-anchor="middle">ZONE 2: ASIL-D E-STOP</text>
  <text x="1135" y="260" fill="#fca5a5" font-family="Consolas, monospace" font-size="14" font-weight="bold" text-anchor="middle">Emergency Physical Trip</text>

  <rect x="960" y="290" width="350" height="90" rx="8" fill="#4a0d0d"/>
  <text x="980" y="320" fill="#cbd5e1" font-family="Consolas, monospace" font-size="12">HARD VRAM LIMIT</text>
  <text x="980" y="355" fill="#ef4444" font-family="Consolas, monospace" font-size="24" font-weight="bold">&gt;= 50.0 GB</text>

  <rect x="960" y="400" width="350" height="90" rx="8" fill="#4a0d0d"/>
  <text x="980" y="430" fill="#cbd5e1" font-family="Consolas, monospace" font-size="12">FAULT RESPONSE (FTTI)</text>
  <text x="980" y="465" fill="#ef4444" font-family="Consolas, monospace" font-size="24" font-weight="bold">&lt;= 50 ms</text>

  <rect x="960" y="510" width="350" height="90" rx="8" fill="#4a0d0d"/>
  <text x="980" y="540" fill="#cbd5e1" font-family="Consolas, monospace" font-size="12">BITWISE MEMORY PURGE</text>
  <text x="980" y="575" fill="#ef4444" font-family="Consolas, monospace" font-size="24" font-weight="bold">2-Pass (0xAA-&gt;0x00)</text>

  <rect x="960" y="630" width="350" height="120" rx="8" fill="#2b0505" stroke="#ef4444" stroke-width="1"/>
  <text x="980" y="660" fill="#f87171" font-family="Arial" font-size="14" font-weight="bold">Safety Action:</text>
  <text x="980" y="685" fill="#e2e8f0" font-family="Arial" font-size="13">Immediate hardware shutdown</text>
  <text x="980" y="708" fill="#e2e8f0" font-family="Arial" font-size="13">Zero memory residue scrub</text>
  <text x="980" y="730" fill="#ef4444" font-family="Consolas, monospace" font-size="12">[STATUS: EMERGENCY SAFE]</text>
</svg>"""
    return svg

def generate_svg_05():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 850" width="1400" height="850">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c16"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="100%" height="100%" fill="url(#bgGrad5)"/>
  <rect x="25" y="25" width="1350" height="800" rx="16" fill="none" stroke="#1e293b" stroke-width="2"/>

  <!-- Title -->
  <rect x="50" y="45" width="1300" height="75" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
  <text x="80" y="85" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial" font-size="24" font-weight="900">PHANToM GRID // SYSTEM DEFENSE MATRIX &amp; RESOURCE CONTRACT (TABLE 1)</text>
  <text x="80" y="108" fill="#10b981" font-family="Consolas, monospace" font-size="14">EXACT MACHINE-READABLE INVARIANTS, THRESHOLDS &amp; ASIL-D ENFORCEMENT</text>

  <!-- Table Container -->
  <rect x="50" y="145" width="1300" height="650" rx="12" fill="#0b1324" stroke="#1e293b" stroke-width="2"/>

  <!-- Table Header -->
  <rect x="50" y="145" width="1300" height="60" rx="12" fill="#1e293b"/>
  <text x="80" y="182" fill="#38bdf8" font-family="Arial" font-size="15" font-weight="bold">SYSTEM METRIC / PARAMETER</text>
  <text x="420" y="182" fill="#10b981" font-family="Arial" font-size="15" font-weight="bold">NOMINAL SAFE ZONE</text>
  <text x="680" y="182" fill="#f59e0b" font-family="Arial" font-size="15" font-weight="bold">WARNING THRESHOLD</text>
  <text x="940" y="182" fill="#ef4444" font-family="Arial" font-size="15" font-weight="bold">ASIL-D HARD MELTDOWN</text>
  <text x="1190" y="182" fill="#a855f7" font-family="Arial" font-size="15" font-weight="bold">ENFORCEMENT</text>

  <!-- Divider lines -->
  <line x1="50" y1="205" x2="1350" y2="205" stroke="#334155" stroke-width="2"/>

  <!-- Row 1: Global VRAM -->
  <rect x="50" y="210" width="1300" height="85" fill="#0f172a"/>
  <text x="80" y="245" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold">1. Global VRAM Overhead</text>
  <text x="80" y="270" fill="#94a3b8" font-family="Consolas, monospace" font-size="12">GPU/Host Shared Memory Allocation</text>
  <text x="420" y="258" fill="#34d399" font-family="Consolas, monospace" font-size="15" font-weight="bold">&lt;= 32.0 GB</text>
  <text x="680" y="258" fill="#fbbf24" font-family="Consolas, monospace" font-size="15" font-weight="bold">45.0 GB</text>
  <text x="940" y="258" fill="#f87171" font-family="Consolas, monospace" font-size="15" font-weight="bold">&gt;= 50.0 GB (Hard E-STOP)</text>
  <text x="1190" y="258" fill="#c084fc" font-family="Arial" font-size="13">Hardware Watchdog</text>
  <line x1="50" y1="295" x2="1350" y2="295" stroke="#1e293b" stroke-width="1"/>

  <!-- Row 2: Latency -->
  <rect x="50" y="300" width="1300" height="85" fill="#09101f"/>
  <text x="80" y="335" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold">2. E2E Cycle Latency</text>
  <text x="80" y="360" fill="#94a3b8" font-family="Consolas, monospace" font-size="12">60 FPS Real-Time Control Loop</text>
  <text x="420" y="348" fill="#34d399" font-family="Consolas, monospace" font-size="15" font-weight="bold">&lt;= 16.66 ms</text>
  <text x="680" y="348" fill="#fbbf24" font-family="Consolas, monospace" font-size="15" font-weight="bold">&gt; 25.0 ms</text>
  <text x="940" y="348" fill="#f87171" font-family="Consolas, monospace" font-size="15" font-weight="bold">&gt; 50.0 ms (FTTI Breach)</text>
  <text x="1190" y="348" fill="#c084fc" font-family="Arial" font-size="13">Async Kernel Dispatch</text>
  <line x1="50" y1="385" x2="1350" y2="385" stroke="#1e293b" stroke-width="1"/>

  <!-- Row 3: Damping -->
  <rect x="50" y="390" width="1300" height="85" fill="#0f172a"/>
  <text x="80" y="425" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold">3. Geodesic Damping Factor</text>
  <text x="80" y="450" fill="#94a3b8" font-family="Consolas, monospace" font-size="12">Harmonic Stabilization against Spikes</text>
  <text x="420" y="438" fill="#34d399" font-family="Consolas, monospace" font-size="15" font-weight="bold">1.00 x (Nominal)</text>
  <text x="680" y="438" fill="#fbbf24" font-family="Consolas, monospace" font-size="15" font-weight="bold">Surge Detected</text>
  <text x="940" y="438" fill="#f87171" font-family="Consolas, monospace" font-size="15" font-weight="bold">1.35 x Geodesic Jump</text>
  <text x="1190" y="438" fill="#c084fc" font-family="Arial" font-size="13">Non-linear Limiter</text>
  <line x1="50" y1="475" x2="1350" y2="475" stroke="#1e293b" stroke-width="1"/>

  <!-- Row 4: Joint Torque -->
  <rect x="50" y="480" width="1300" height="85" fill="#09101f"/>
  <text x="80" y="515" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold">4. Physical Joint Torque</text>
  <text x="80" y="540" fill="#94a3b8" font-family="Consolas, monospace" font-size="12">Embodied Actuator Safety Ceiling</text>
  <text x="420" y="528" fill="#34d399" font-family="Consolas, monospace" font-size="15" font-weight="bold">&lt;= 60.0 Nm</text>
  <text x="680" y="528" fill="#fbbf24" font-family="Consolas, monospace" font-size="15" font-weight="bold">75.0 Nm</text>
  <text x="940" y="528" fill="#f87171" font-family="Consolas, monospace" font-size="15" font-weight="bold">&gt;= 85.0 Nm (E-STOP)</text>
  <text x="1190" y="528" fill="#c084fc" font-family="Arial" font-size="13">Magnetic Brake</text>
  <line x1="50" y1="565" x2="1350" y2="565" stroke="#1e293b" stroke-width="1"/>

  <!-- Row 5: Memory Residue -->
  <rect x="50" y="570" width="1300" height="85" fill="#0f172a"/>
  <text x="80" y="605" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold">5. Memory Residue (ZDR)</text>
  <text x="80" y="630" fill="#94a3b8" font-family="Consolas, monospace" font-size="12">Zero-Data-Residue Cryptographic Wipe</text>
  <text x="420" y="618" fill="#34d399" font-family="Consolas, monospace" font-size="15" font-weight="bold">0.000000 MB</text>
  <text x="680" y="618" fill="#fbbf24" font-family="Consolas, monospace" font-size="15" font-weight="bold">Leak Flagged</text>
  <text x="940" y="618" fill="#f87171" font-family="Consolas, monospace" font-size="15" font-weight="bold">&gt; 0.00 MB Disallowed</text>
  <text x="1190" y="618" fill="#c084fc" font-family="Arial" font-size="13">2-Pass Bitwise Wipe</text>
  <line x1="50" y1="655" x2="1350" y2="655" stroke="#1e293b" stroke-width="1"/>

  <!-- Row 6: Audit Traceability -->
  <rect x="50" y="660" width="1300" height="85" fill="#09101f"/>
  <text x="80" y="695" fill="#ffffff" font-family="Arial" font-size="16" font-weight="bold">6. Audit Traceability</text>
  <text x="80" y="720" fill="#94a3b8" font-family="Consolas, monospace" font-size="12">Immutable WORM Receipt Verification</text>
  <text x="420" y="708" fill="#34d399" font-family="Consolas, monospace" font-size="15" font-weight="bold">Immutable Nonce</text>
  <text x="680" y="708" fill="#fbbf24" font-family="Consolas, monospace" font-size="15" font-weight="bold">SHA-256 Chained</text>
  <text x="940" y="708" fill="#f87171" font-family="Consolas, monospace" font-size="15" font-weight="bold">Tamper Violation</text>
  <text x="1190" y="708" fill="#c084fc" font-family="Arial" font-size="13">Git Commit + WORM</text>
</svg>"""
    return svg

def generate_interactive_html():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>PHANToM GRID // OpenCode Match 3 - Architecture Blueprint Viewer</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #080c16;
      color: #f1f5f9;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      padding: 30px;
    }
    .header {
      background: #0f172a;
      border: 1px solid #1e293b;
      border-left: 6px solid #00e5ff;
      border-radius: 10px;
      padding: 25px 35px;
      margin-bottom: 30px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .header h1 {
      font-size: 26px;
      font-weight: 900;
      letter-spacing: 1px;
      color: #ffffff;
    }
    .header p {
      color: #94a3b8;
      font-size: 14px;
      margin-top: 6px;
      font-family: Consolas, monospace;
    }
    .badge {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid #10b981;
      color: #10b981;
      padding: 8px 18px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: bold;
      letter-spacing: 1px;
    }
    .tabs {
      display: flex;
      gap: 12px;
      margin-bottom: 25px;
      flex-wrap: wrap;
    }
    .tab-btn {
      background: #1e293b;
      color: #94a3b8;
      border: 1px solid #334155;
      padding: 12px 24px;
      border-radius: 8px;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .tab-btn:hover {
      background: #334155;
      color: #ffffff;
    }
    .tab-btn.active {
      background: #00e5ff;
      color: #080c16;
      border-color: #00e5ff;
      box-shadow: 0 0 15px rgba(0, 229, 255, 0.4);
    }
    .content-card {
      background: #0d1527;
      border: 1px solid #1e293b;
      border-radius: 12px;
      padding: 30px;
      min-height: 700px;
    }
    .pane {
      display: none;
    }
    .pane.active {
      display: block;
    }
    .pane-title {
      font-size: 20px;
      font-weight: 800;
      color: #38bdf8;
      margin-bottom: 15px;
    }
    .pane-desc {
      font-size: 14px;
      color: #94a3b8;
      margin-bottom: 25px;
      line-height: 1.6;
    }
    .svg-viewer {
      background: #080c16;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 20px;
      text-align: center;
      margin-bottom: 25px;
    }
    .svg-viewer img {
      max-width: 100%;
      height: auto;
      border-radius: 6px;
    }
    .mermaid-box {
      background: #080c16;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 25px;
      margin-top: 20px;
      overflow-x: auto;
    }
  </style>
</head>
<body>

  <div class="header">
    <div>
      <h1>PHANToM GRID // BLUEPRINT &amp; ARCHITECTURE SUITE</h1>
      <p>OpenCode 2026 Match 3 :: Autonomous Multi-Agent Workflow Nexus</p>
    </div>
    <div class="badge">RULE 65 TRINITY VERIFIED</div>
  </div>

  <div class="tabs">
    <button class="tab-btn active" onclick="showTab(0)">01. System Topology</button>
    <button class="tab-btn" onclick="showTab(1)">02. Agent Sequence</button>
    <button class="tab-btn" onclick="showTab(2)">03. FSM State Machine</button>
    <button class="tab-btn" onclick="showTab(3)">04. Security Boundary</button>
    <button class="tab-btn" onclick="showTab(4)">05. Defense Matrix Table</button>
  </div>

  <div class="content-card">
    <!-- PANE 1 -->
    <div class="pane active" id="pane-0">
      <div class="pane-title">FIGURE 1: FOUR-LAYER SYSTEM TOPOLOGY</div>
      <div class="pane-desc">Layer 1 Ingress Sentinel &rarr; Layer 2 Central Nexus Brain &rarr; Layer 3 Multi-Agent Swarm (Track B) &rarr; Layer 4 Safety Watchdog, 2-Pass ZDR &amp; WORM Vault.</div>
      <div class="svg-viewer">
        <img src="01_system_topology.svg" alt="01 System Topology">
      </div>
    </div>

    <!-- PANE 2 -->
    <div class="pane" id="pane-1">
      <div class="pane-title">FIGURE 2: MICROSECOND LIFECYCLE SEQUENCE</div>
      <div class="pane-desc">Microsecond lifecycle interaction across 6 lifelines: Commander &rarr; Ingress &rarr; Core &rarr; Swarm &rarr; Safety Watchdog &rarr; 2-Pass ZDR &amp; WORM Vault.</div>
      <div class="svg-viewer">
        <img src="02_agent_sequence.svg" alt="02 Agent Sequence">
      </div>
    </div>

    <!-- PANE 3 -->
    <div class="pane" id="pane-2">
      <div class="pane-title">FIGURE 3: DETERMINISTIC FSM STATE MACHINE</div>
      <div class="pane-desc">Automotive-grade ASIL-D state machine with composite planning/execution states, 1.35x geodesic damping jumps, and fail-safe zero-data-residue ESTOP wipes.</div>
      <div class="svg-viewer">
        <img src="03_fsm_state_machine.svg" alt="03 FSM State Machine">
      </div>
    </div>

    <!-- PANE 4 -->
    <div class="pane" id="pane-3">
      <div class="pane-title">FIGURE 4: THREE-ZONE SECURITY BOUNDARY &amp; MELTDOWN GATES</div>
      <div class="pane-desc">Zone 0 (Nominal &lt;= 45GB) &rarr; Zone 1 (Throttle 45-50GB, 1.35x Damping) &rarr; Zone 2 (Hard Meltdown &gt;= 50GB, FTTI &lt;= 50ms, 2-Pass ZDR Purge).</div>
      <div class="svg-viewer">
        <img src="04_security_boundary.svg" alt="04 Security Boundary">
      </div>
    </div>

    <!-- PANE 5 -->
    <div class="pane" id="pane-4">
      <div class="pane-title">TABLE 1: SYSTEM DEFENSE MATRIX &amp; RESOURCE CONTRACT</div>
      <div class="pane-desc">Machine-readable SLA and safety contract defining VRAM limits, latency budgets, joint torque cutoffs, 2-pass ZDR zero-residue purges, and immutable WORM audit receipts.</div>
      <div class="svg-viewer">
        <img src="05_defense_matrix_table.svg" alt="05 Defense Matrix Table">
      </div>
    </div>
  </div>

  <script>
    function showTab(idx) {
      document.querySelectorAll('.tab-btn').forEach((btn, i) => {
        btn.classList.toggle('active', i === idx);
      });
      document.querySelectorAll('.pane').forEach((pane, i) => {
        pane.classList.toggle('active', i === idx);
      });
    }
  </script>
</body>
</html>"""
    return html

def main():
    DIAGRAMS_DIR.mkdir(parents=True, exist_ok=True)
    
    print("[*] Generating 01_system_topology.svg...")
    (DIAGRAMS_DIR / "01_system_topology.svg").write_text(generate_svg_01(), encoding="utf-8")

    print("[*] Generating 02_agent_sequence.svg...")
    (DIAGRAMS_DIR / "02_agent_sequence.svg").write_text(generate_svg_02(), encoding="utf-8")

    print("[*] Generating 03_fsm_state_machine.svg...")
    (DIAGRAMS_DIR / "03_fsm_state_machine.svg").write_text(generate_svg_03(), encoding="utf-8")

    print("[*] Generating 04_security_boundary.svg...")
    (DIAGRAMS_DIR / "04_security_boundary.svg").write_text(generate_svg_04(), encoding="utf-8")

    print("[*] Generating 05_defense_matrix_table.svg...")
    (DIAGRAMS_DIR / "05_defense_matrix_table.svg").write_text(generate_svg_05(), encoding="utf-8")

    print("[*] Generating diagrams/index.html (Interactive Blueprint Viewer)...")
    (DIAGRAMS_DIR / "index.html").write_text(generate_interactive_html(), encoding="utf-8")

    print("[SUCCESS] All 5 Distinct Diagrams & Interactive Dashboard successfully generated in diagrams/!")

if __name__ == "__main__":
    main()
