# Geometric Damping Controller
class DampingController:
    def __init__(self, base_scalar: float = 1.0, high_scalar: float = 1.35):
        self.base_scalar = base_scalar
        self.high_scalar = high_scalar

    def evaluate(self, load_ratio: float, latency_ms: float) -> float:
        if load_ratio > 0.85 or latency_ms > 16.66:
            return self.high_scalar
        return self.base_scalar
