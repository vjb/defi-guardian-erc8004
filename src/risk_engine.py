import os
import requests
from enum import Enum
from typing import Dict, Optional

class Action(Enum):
    HOLD = "HOLD"
    TRIGGER_CIRCUIT_BREAKER = "TRIGGER_CIRCUIT_BREAKER"

class RiskEngine:
    """Evaluates portfolio risk and decides if protective actions are necessary based on live PRISM API data."""
    
    def __init__(self):
        self.threshold_percentage = 0.15 # 15% drop threshold
        self.prism_api_key = os.getenv("PRISM_API_KEY")
        self.high_water_marks: Dict[str, float] = {}

    def fetch_prism_oracle_data(self, symbol: str) -> dict:
        """
        Queries the Strykr PRISM API for live AI Signals.
        Requires the PRISM_API_KEY to be set in the environment.
        """
        if not self.prism_api_key:
            raise ValueError("PRISM_API_KEY is not configured in the environment.")
            
        url = f"https://api.prismapi.ai/signals/{symbol}"
        headers = {
            "X-API-Key": self.prism_api_key
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            # PRISM Signals schema returns {"object": "list", "data": [...]}
            signals = data.get("data", [])
            if not signals:
                return {"signal": "unknown", "price": 0.0}
                
            first_signal = signals[0]
            return {
                "signal": first_signal.get("overall_signal", "neutral").lower(),
                "strength": first_signal.get("strength", "none"),
                "price": float(first_signal.get("current_price", 0.0))
            }
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"PRISM Oracle evaluation failed: {e}")

    def evaluate(self, symbol: str, mock_data: Optional[dict] = None) -> (Action, dict):
        """
        Evaluates the symbol using live PRISM AI signals. 
        Returns an Action (HOLD or TRIGGER_CIRCUIT_BREAKER) and the signal context.
        """
        signal_data = mock_data if mock_data else self.fetch_prism_oracle_data(symbol)
        
        if signal_data["signal"] == "bearish" or signal_data["signal"] == "strong_bearish":
            return Action.TRIGGER_CIRCUIT_BREAKER, signal_data
            
        return Action.HOLD, signal_data
