from .base_agent import BaseAgent
from typing import Dict, Any

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__('PlannerAgent')

    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        task = payload.get('task', 'default_task')
        steps = ['step_1_plan_' + str(task), 'step_2_exec_' + str(task), 'step_3_review_' + str(task)]
        return {'plan': steps, 'status': 'PLANNED'}
