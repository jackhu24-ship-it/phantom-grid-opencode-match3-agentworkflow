from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        pass
