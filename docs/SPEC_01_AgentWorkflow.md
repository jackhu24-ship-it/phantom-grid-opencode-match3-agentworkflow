# SPEC_01 :: OpenCode Match 3 AgentWorkflow Technical Whitepaper
> Full Spec-First Architecture Whitepaper (Rule 65 & v6.1.0 Sovereign Constitution)

## 1. System Overall Topology Diagram (圖一：系統總體架構與拓撲圖)
```mermaid
graph TD
    subgraph IngressLayer ["Ingress & Gateway Layer"]
        CLI["User CLI / Task Ingress"] --> SEC_CHK["Security Nonce & VRAM Pre-check"]
    end
    subgraph CoreBrain ["Level 3 Nexus Master Brain"]
        SEC_CHK --> ORCH["Nexus Master Orchestrator"]
        ORCH --> SM["FSM State Machine (Phase 1-4)"]
        ORCH --> CTX["Isolated Context Manager"]
    end
    subgraph AgentSwarm ["Level 2 Multi-Agent Swarm"]
        CTX --> PLAN["Planner Agent (DAG Decomposition)"]
        PLAN --> EXEC["Executor Agent (Low-latency Dispatch)"]
        EXEC --> REV["Reviewer Agent (Audit & Verification)"]
        REV --> SEC["Security Agent (FTTI & Boundary Guard)"]
    end
    subgraph SafeGuard ["Safety & Physical Layer"]
        SEC --> DAMP["1.35x Geometric Damping Controller"]
        DAMP --> ZDR["2-Pass ZDR (0xAA->0x00) Memory Purger"]
        ZDR --> WORM["WORM Audit Receipt Engine"]
    end
```

## 2. Full Lifecycle Sequence Diagram (圖二：全生命週期時序圖)
```mermaid
sequenceDiagram
    autonumber
    actor Commander as Supreme Commander / Task Dispatcher
    participant Ingress as Ingress Sentinel
    participant Core as Master Orchestrator
    participant Swarm as Multi-Agent Swarm
    participant Safety as ASIL-D Safety Watchdog
    participant Vault as 2-Pass ZDR & WORM Vault

    Commander->>Ingress: Submit Task Spec (E2E Mission)
    Ingress->>Ingress: Verify VRAM (<50GB) & Ingress Nonce
    Ingress->>Core: Forward Sanitized Pipeline Request
    Core->>Swarm: Dispatch DAG Task to Planner / Executor
    Swarm->>Swarm: Execute Pipeline (P99 <= 16.66ms)
    Swarm->>Core: Return Synthesis Artifacts
    Core->>Safety: Evaluate Damping & Dynamic Load
    alt Load > 85% or Overload
        Safety->>Core: Trip 1.35x Damping Scalar
    else Load Nominal
        Safety->>Core: Nominal Scalar 1.0x
    end
    Core->>Vault: Trigger 2-Pass ZDR Physical Purge
    Vault-->>Commander: Issue Immutable WORM Receipt (PASS)
```

## 3. Dynamic Values & Damping State Diagram (圖三：動態數值與阻尼狀態圖)
```mermaid
stateDiagram-v2
    [*] --> STATE_IDLE: System Boots & Hardware Check
    STATE_IDLE --> STATE_DISPATCH: Ingress Verified (VRAM < 50GB)
    STATE_DISPATCH --> STATE_EXECUTION: DAG Graph Instantiated
    state STATE_EXECUTION {
        [*] --> Sub_Planning
        Sub_Planning --> Sub_Executing
        Sub_Executing --> Sub_Auditing
        Sub_Auditing --> [*]
    }
    STATE_EXECUTION --> STATE_DAMPED: High Load / Jitter Detected (Damping = 1.35x)
    STATE_DAMPED --> STATE_EXECUTION: Nominal Stabilization
    STATE_EXECUTION --> STATE_ESTOP: Overload (>85Nm / >50GB) Meltdown
    STATE_EXECUTION --> STATE_ZDR_PURGE: Execution Succeeded
    STATE_ESTOP --> STATE_ZDR_PURGE: Emergency Brake & Zeroize
    STATE_ZDR_PURGE --> [*]: WORM Receipt Signed & Memory Zeroed
```

## 4. Security Boundary & Meltdown Diagram (圖四：安全邊界、顯存熔斷與排版隔離圖)
```mermaid
graph LR
    subgraph NominalZone ["Zone 0: Nominal Operating Zone"]
        N1["VRAM: 0 - 45 GB"]
        N2["Cycle Time: <= 16.66 ms"]
        N3["Damping: 1.0x"]
    end
    subgraph CautionZone ["Zone 1: Dynamic Throttle Zone"]
        C1["VRAM: 45 - 50 GB"]
        C2["Damping Jump: 1.35x Active"]
        C3["Queue Degraded Mode"]
    end
    subgraph HardMeltdownZone ["Zone 2: ASIL-D Meltdown E-STOP"]
        M1["VRAM: >= 50.0 GB (Hard Break)"]
        M2["FTTI: <= 50 ms Immediate Lock"]
        M3["ZDR 2-Pass Bitwise Overwrite"]
    end
    NominalZone --> CautionZone
    CautionZone --> HardMeltdownZone
```

## 5. System Boundary & Defense Matrix (表一：系統資源調配、臨界邊界與防禦矩陣表)

| 關鍵指標 (Key Metric) | 標稱標準 (Nominal) | 警報臨界點 (Warning) | 硬熔斷紅線 (Hard E-STOP) | 防禦阻尼 / 熔斷機制 (Defense SOP) | ASIL 等級 |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **全域顯存佔用 (VRAM)** | <= 32.0 GB | 45.0 GB | >= 50.0 GB | 立即觸發 HARD_MELTDOWN 鎖死 | ASIL-D |
| **端到端管線延遲 (E2E)** | <= 5.0 ms | 16.66 ms (60 FPS) | > 50.0 ms | 自動切換 1.35x 平滑阻尼 | ASIL-B |
| **關節過載扭矩 (Torque)** | <= 45.0 Nm | 70.0 Nm | > 85.0 Nm | 抱閘斷電並寫入黑盒子 | ASIL-D |
| **記憶體殘留清理 (ZDR)** | 0.000000 MB | > 0.0001 MB | 任何弱引用未釋放 | 2-Pass (0xAA -> 0x00) 雙重覆寫 | ASIL-D |
| **WORM 存證唯一性 (Nonce)** | 嚴格單調遞增 | 重複 Nonce 請求 | 雜湊值碰撞衝突 | 重放攻擊即刻攔截拋出 SecurityError | ASIL-D |
