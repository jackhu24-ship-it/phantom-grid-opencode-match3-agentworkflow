# -*- coding: utf-8 -*-
"""
PHANToM GRID // OpenCode Match 3 - Comprehensive Unit & Closure Test Suite
Standards: ISO 26262 ASIL-D | Rule 65 Sovereign Constitution v6.1.0
Zero Strawman Assertions | 100% Deep Real-World Semantic Verification
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.core.orchestrator import MasterOrchestrator
from src.core.state_machine import StateMachine, SystemState
from src.core.context_manager import ContextManager
from src.agents.planner_agent import PlannerAgent
from src.agents.executor_agent import ExecutorAgent
from src.agents.reviewer_agent import ReviewerAgent
from src.agents.security_agent import SecurityAgent
from src.utils.damping_controller import DampingController
from src.utils.zdr_purger import ZDRPurger


class TestWorkflowClosure(unittest.TestCase):
    def setUp(self):
        self.orch = MasterOrchestrator()

    def test_01_nominal_e2e_cycle(self):
        """Verifies end-to-end nominal dispatch within 16.66ms 60 FPS budget."""
        payload = {"task": "test_nominal", "vram_usage_gb": 12.0, "joint_torque_nm": 30.0, "load_ratio": 0.4}
        res = self.orch.run_pipeline(payload)
        self.assertEqual(res.get("status"), "PASS")
        self.assertFalse(res.get("estop"))
        self.assertLess(res.get("latency_ms", 999.0), 16.66)
        self.assertTrue(res.get("zdr_verified"))
        self.assertTrue(res.get("worm_receipt_id", "").startswith("WORM-OPCODE3-"))

    def test_02_vram_meltdown_boundary(self):
        """Verifies VRAM >= 50.0 GB threshold strictly triggers HARD_MELTDOWN ESTOP."""
        # Just below boundary (49.9 GB) -> Nominal
        res_sub = self.orch.run_pipeline({"task": "sub_bound", "vram_usage_gb": 49.9, "joint_torque_nm": 30.0})
        self.assertEqual(res_sub.get("status"), "PASS")
        self.assertFalse(res_sub.get("estop"))

        # Exact boundary (50.0 GB) -> ESTOP
        res_exact = self.orch.run_pipeline({"task": "exact_bound", "vram_usage_gb": 50.0, "joint_torque_nm": 30.0})
        self.assertEqual(res_exact.get("status"), "ESTOP_TRIP")
        self.assertTrue(res_exact.get("estop"))

        # Above boundary (55.0 GB) -> ESTOP
        res_above = self.orch.run_pipeline({"task": "above_bound", "vram_usage_gb": 55.0, "joint_torque_nm": 30.0})
        self.assertEqual(res_above.get("status"), "ESTOP_TRIP")
        self.assertTrue(res_above.get("estop"))

    def test_03_torque_meltdown_boundary(self):
        """Verifies Actuator Torque > 85.0 Nm strictly trips ESTOP relay decouple."""
        # At boundary (85.0 Nm) -> Nominal
        res_safe = self.orch.run_pipeline({"task": "torque_safe", "vram_usage_gb": 20.0, "joint_torque_nm": 85.0})
        self.assertEqual(res_safe.get("status"), "PASS")

        # Exceeds boundary (85.1 Nm) -> ESTOP
        res_trip = self.orch.run_pipeline({"task": "torque_trip", "vram_usage_gb": 20.0, "joint_torque_nm": 85.1})
        self.assertEqual(res_trip.get("status"), "ESTOP_TRIP")
        self.assertTrue(res_trip.get("estop"))

    def test_04_load_damping_jump(self):
        """Verifies system load ratio > 0.85 activates 1.35x geometric rigidity damping."""
        ctrl = DampingController()
        # Normal load
        self.assertEqual(ctrl.evaluate(load_ratio=0.85, latency_ms=5.0), 1.0)
        # Heavy load
        self.assertEqual(ctrl.evaluate(load_ratio=0.86, latency_ms=5.0), 1.35)

        # Pipeline integration
        res = self.orch.run_pipeline({"task": "load_damping", "vram_usage_gb": 20.0, "joint_torque_nm": 30.0, "load_ratio": 0.90})
        self.assertEqual(res.get("damping_scalar"), 1.35)

    def test_05_latency_damping_jump(self):
        """Verifies latency > 16.66ms activates 1.35x damping to prevent frame drops."""
        ctrl = DampingController()
        self.assertEqual(ctrl.evaluate(load_ratio=0.5, latency_ms=16.66), 1.0)
        self.assertEqual(ctrl.evaluate(load_ratio=0.5, latency_ms=16.67), 1.35)

    def test_06_zdr_bitwise_physical_zeroization(self):
        """
        Anti-Fake ZDR Test:
        Populates real memory buffer with sensitive bytes, invokes ZDR purger,
        and verifies bitwise zeroization (all bytes == 0x00).
        """
        secret_payload = bytearray(b"CLASSIFIED_TOP_SECRET_ORCHESTRATOR_MISSION_PAYLOAD_XYZ_987654321")
        self.assertNotEqual(secret_payload[0], 0x00)
        self.assertGreater(len(secret_payload), 0)

        # Purge buffer
        purged = ZDRPurger.purge(secret_payload)
        self.assertTrue(purged)
        # Verify 100% bitwise zeroization
        self.assertTrue(all(byte == 0x00 for byte in secret_payload), "Memory buffer contains non-zero remnant data!")
        self.assertEqual(set(secret_payload), {0x00})

    def test_07_worm_receipt_uniqueness(self):
        """Verifies every task invocation generates an immutable, unique WORM receipt ID."""
        receipts = set()
        for i in range(25):
            res = self.orch.run_pipeline({"task": f"worm_check_{i}", "vram_usage_gb": 10.0, "joint_torque_nm": 20.0})
            rid = res.get("worm_receipt_id")
            self.assertIsNotNone(rid)
            self.assertNotIn(rid, receipts, f"Duplicate WORM receipt collision detected: {rid}")
            receipts.add(rid)
        self.assertEqual(len(receipts), 25)

    def test_08_planner_agent_dag_decomposition(self):
        """Verifies PlannerAgent decomposes high-level goals into sequential DAG steps."""
        planner = PlannerAgent()
        out = planner.execute({"task": "deploy_swarm"})
        self.assertEqual(out.get("status"), "PLANNED")
        plan = out.get("plan", [])
        self.assertEqual(len(plan), 3)
        self.assertTrue(all("deploy_swarm" in step for step in plan))

    def test_09_executor_agent_dispatch(self):
        """Verifies ExecutorAgent executes every planned step atomically."""
        executor = ExecutorAgent()
        plan = ["step_alpha", "step_beta", "step_gamma"]
        out = executor.execute({"plan": plan})
        self.assertEqual(out.get("status"), "EXECUTED")
        executed = out.get("executed_steps", [])
        self.assertEqual(executed, ["executed_step_alpha", "executed_step_beta", "executed_step_gamma"])

    def test_10_reviewer_agent_verification(self):
        """Verifies ReviewerAgent correctly scores valid vs invalid execution traces."""
        reviewer = ReviewerAgent()
        # Valid trace
        valid_out = reviewer.execute({"executed_steps": ["step_1", "step_2"]})
        self.assertEqual(valid_out.get("review_score"), 1.0)
        self.assertTrue(valid_out.get("verified"))

        # Empty/Failed trace
        empty_out = reviewer.execute({"executed_steps": []})
        self.assertEqual(empty_out.get("review_score"), 0.0)
        self.assertFalse(empty_out.get("verified"))

    def test_11_state_machine_deterministic_transitions(self):
        """Verifies Finite State Machine transitions cleanly without orphaned states."""
        sm = StateMachine()
        self.assertEqual(sm.current_state, SystemState.IDLE)
        sm.transition_to(SystemState.DISPATCH)
        self.assertEqual(sm.current_state, SystemState.DISPATCH)
        sm.transition_to(SystemState.EXECUTION)
        self.assertEqual(sm.current_state, SystemState.EXECUTION)
        sm.transition_to(SystemState.ZDR_PURGE)
        self.assertEqual(sm.current_state, SystemState.ZDR_PURGE)
        sm.transition_to(SystemState.ESTOP)
        self.assertEqual(sm.current_state, SystemState.ESTOP)

    def test_12_context_manager_isolation_and_purge(self):
        """Verifies ContextManager sets, gets, and purges state variables cleanly."""
        ctx = ContextManager()
        ctx.set("agent_id", "Reviewer_01")
        ctx.set("vram_quota", 32.0)
        self.assertEqual(ctx.get("agent_id"), "Reviewer_01")
        self.assertEqual(ctx.get("vram_quota"), 32.0)
        ctx.clear()
        self.assertIsNone(ctx.get("agent_id"))
        self.assertIsNone(ctx.get("vram_quota"))


if __name__ == "__main__":
    unittest.main()
