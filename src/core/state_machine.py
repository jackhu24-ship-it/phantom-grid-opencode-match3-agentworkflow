from enum import Enum

class SystemState(Enum):
    IDLE = 'IDLE'
    DISPATCH = 'DISPATCH'
    EXECUTION = 'EXECUTION'
    ESTOP = 'ESTOP'
    ZDR_PURGE = 'ZDR_PURGE'

class StateMachine:
    def __init__(self):
        self.current_state = SystemState.IDLE

    def transition_to(self, new_state: SystemState):
        self.current_state = new_state
        return self.current_state
