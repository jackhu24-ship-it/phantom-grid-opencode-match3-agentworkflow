# 100% Pure ASCII Closure Test (§3.4.24, §3.4.28)
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.core.orchestrator import MasterOrchestrator

class TestWorkflowClosure(unittest.TestCase):
    def setUp(self):
        self.orch = MasterOrchestrator()

    def test_01_nominal_e2e_cycle(self):
        payload = {'task': 'test_nominal', 'vram_usage_gb': 12.0, 'joint_torque_nm': 30.0, 'load_ratio': 0.4}
        res = self.orch.run_pipeline(payload)
        self.assertEqual(res.get('status'), 'PASS')
        self.assertLess(res.get('latency_ms', 999.0), 16.66)
        print('[TEST 1 PASS] Nominal E2E Cycle passed.')

    def test_02_vram_meltdown_trip(self):
        payload = {'task': 'test_vram_overflow', 'vram_usage_gb': 52.5, 'joint_torque_nm': 30.0}
        res = self.orch.run_pipeline(payload)
        self.assertEqual(res.get('status'), 'ESTOP_TRIP')
        self.assertTrue(res.get('estop', False))
        print('[TEST 2 PASS] 50GB Global VRAM Meltdown Trip passed.')

    def test_03_joint_overload_damping(self):
        payload = {'task': 'test_load_damping', 'vram_usage_gb': 20.0, 'joint_torque_nm': 30.0, 'load_ratio': 0.95}
        res = self.orch.run_pipeline(payload)
        damp = res.get('damping_scalar', res.get('damping', 1.0))
        self.assertEqual(damp, 1.35)
        print('[TEST 3 PASS] 1.35x Damping Jump passed.')

    def test_04_zdr_and_worm_receipt(self):
        payload = {'task': 'test_zdr', 'vram_usage_gb': 15.0, 'joint_torque_nm': 20.0}
        res = self.orch.run_pipeline(payload)
        zdr = res.get('zdr_verified', False)
        worm = res.get('worm_receipt_id', res.get('worm_receipt', ''))
        self.assertTrue(zdr)
        self.assertTrue(worm.startswith('WORM-'))
        print('[TEST 4 PASS] 2-Pass ZDR Purge and WORM Receipt passed.')

if __name__ == '__main__':
    unittest.main()
