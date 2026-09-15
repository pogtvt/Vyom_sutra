import math

class VyomSutraCore:
    PI = math.pi
    PHI = 1.618033988749895

    @staticmethod
    def calculate_token_phase(token: str) -> float:
        if not token:
            return 0.0
        ascii_sum = sum(ord(c) * (VyomSutraCore.PHI ** (i % 5)) for i, c in enumerate(token))
        return (ascii_sum / 100.0) % (2.0 * VyomSutraCore.PI)

    @staticmethod
    def compute_resonance(ctx_phase: float, token_phase: float) -> tuple:
        delta = abs(ctx_phase - token_phase)
        c_munu = math.sin(delta) * 50.0
        if c_munu >= 48.0:
            return 0.01, c_munu
        resonance = math.exp(-1.2 * (delta ** 2))
        return max(0.05, resonance), c_munu

THEMES = {
    "cyber": {
        "CYAN": "\033[96m", "GREEN": "\033[92m", "YELLOW": "\033[93m",
        "GRAY": "\033[90m", "MAGENTA": "\033[95m", "RED": "\033[91m",
        "BOLD": "\033[1m", "RESET": "\033[0m"
    },
    "matrix": {
        "CYAN": "\033[32m", "GREEN": "\033[92m", "YELLOW": "\033[32m",
        "GRAY": "\033[90m", "MAGENTA": "\033[32m", "RED": "\033[31m",
        "BOLD": "\033[1m", "RESET": "\033[0m"
    },
    "neon": {
        "CYAN": "\033[94m", "GREEN": "\033[96m", "YELLOW": "\033[93m",
        "GRAY": "\033[37m", "MAGENTA": "\033[91m", "RED": "\033[95m",
        "BOLD": "\033[1m", "RESET": "\033[0m"
    }
}
