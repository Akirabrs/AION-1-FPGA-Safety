# ╔════════════════════════════════════════════════════════════════════════════╗
# 📅 TIMELINE: 25/12/2025 | 11:20 AM (GMT-3)
# 🛡️ PROJECT: AION (Artificial Intelligence Operating Network)
# 📂 MODULE: aion-signal-intelligence
# 🛠️ FILE: aion_signal_filter.py
# ╚════════════════════════════════════════════════════════════════════════════╝

import numpy as np

class AionAdaptiveFilter:
    """Filtro de inteligência de sinal para limpeza de ruído de plasma."""
    
    def __init__(self, alpha: float = 0.1):
        self.alpha = alpha
        self.ema = None

    def apply(self, signal_chunk: np.ndarray) -> np.ndarray:
        """Aplica Média Móvel Exponencial para suavizar transientes clássicos."""
        if self.ema is None:
            self.ema = np.mean(signal_chunk)
            
        filtered_signal = []
        for x in signal_chunk:
            self.ema = self.alpha * x + (1 - self.alpha) * self.ema
            filtered_signal.append(self.ema)
            
        return np.array(filtered_signal)

# Exemplo de Integração AION -> AEGIS
if __name__ == "__main__":
    raw_data = np.random.normal(0, 1, 100)
    filter_unit = AionAdaptiveFilter(alpha=0.2)
    clean_data = filter_unit.apply(raw_data)
    print(f"✅ AION: Sinal processado. Redução de ruído instrumental concluída.")
