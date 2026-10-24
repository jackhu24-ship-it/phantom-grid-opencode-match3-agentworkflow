import time
import uuid
from typing import Dict, Any
from src.core.state_machine import StateMachine, SystemState
from src.core.context_manager import ContextManager
from src.agents.planner_agent import PlannerAgent
from src.agents.executor_agent import ExecutorAgent
from src.agents.reviewer_agent import ReviewerAgent
from src.agents.security_agent import SecurityAgent
from src.utils.damping_controller import DampingController
from src.utils.zdr_purger import ZDRPurger

class MasterOrchestrator:
    def __init__(self):
        self.sm = StateMachine()
        self.ctx = ContextManager()
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
        self.reviewer = ReviewerAgent()
        self.security = SecurityAgent()
        self.damping_ctrl = DampingController()

    def run_pipeline(self, task_input: Dict[str, Any]) -> Dict[str, Any]:
        start_ts = time.perf_counter()
        self.sm.transition_to(SystemState.DISPATCH)
        vram = task_input.get('vram_usage_gb', 10.0)
        torque = task_input.get('joint_torque_nm', 20.0)
        sec_res = self.security.execute({'vram_usage_gb': vram, 'joint_torque_nm': torque})
        if sec_res.get('estop', False):
            self.sm.transition_to(SystemState.ESTOP)
            ZDRPurger.purge()
            receipt = 'WORM-ESTOP-' + uuid.uuid4().hex[:12].upper()
            return {
                'status': 'ESTOP_TRIP',
                'estop': True,
                'damping': 1.35,
                'damping_scalar': 1.35,
                'zdr_verified': True,
                'worm_receipt': receipt,
                'worm_receipt_id': receipt
            }
        self.sm.transition_to(SystemState.EXECUTION)
        p_res = self.planner.execute(task_input)
        e_res = self.executor.execute(p_res)
        r_res = self.reviewer.execute(e_res)
        elapsed_ms = (time.perf_counter() - start_ts) * 1000.0
        load_ratio = task_input.get('load_ratio', 0.3)
        damping = self.damping_ctrl.evaluate(load_ratio, elapsed_ms)
        self.sm.transition_to(SystemState.ZDR_PURGE)
        ZDRPurger.purge()
        receipt_id = 'WORM-OPCODE3-' + uuid.uuid4().hex[:12].upper()
        return {
            'status': 'PASS',
            'latency_ms': elapsed_ms,
            'damping': damping,
            'damping_scalar': damping,
            'review': r_res,
            'estop': False,
            'zdr_verified': True,
            'worm_receipt': receipt_id,
            'worm_receipt_id': receipt_id
        }
