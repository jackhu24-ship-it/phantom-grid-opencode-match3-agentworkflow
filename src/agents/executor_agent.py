from .base_agent import BaseAgent
from typing import Dict, Any

class ExecutorAgent(BaseAgent):
    def __init__(self):
        super().__init__('ExecutorAgent')

    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        plan = payload.get('plan', [])
        executed = ['executed_' + str(p) for p in plan]
        return {'executed_steps': executed, 'status': 'EXECUTED'}
