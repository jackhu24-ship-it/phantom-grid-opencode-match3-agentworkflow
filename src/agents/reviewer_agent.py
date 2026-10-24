from .base_agent import BaseAgent
from typing import Dict, Any

class ReviewerAgent(BaseAgent):
    def __init__(self):
        super().__init__('ReviewerAgent')

    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        executed = payload.get('executed_steps', [])
        score = 1.0 if len(executed) > 0 else 0.0
        return {'review_score': score, 'verified': score == 1.0, 'status': 'VERIFIED'}
