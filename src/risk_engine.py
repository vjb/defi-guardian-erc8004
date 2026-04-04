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

    def fetch_prism_oracle_data(self, symbol: str) -> float:
        """
        Queries the Strykr PRISM API for live token pricing.
        Requires the PRISM_API_KEY to be set in the environment.
        """
        if not self.prism_api_key:
            raise ValueError("PRISM_API_KEY is not configured in the environment.")
            
        url = f"https://api.prismapi.ai/crypto/price/{symbol}"
        headers = {
            "X-API-Key": self.prism_api_key
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            return float(data.get("price_usd", 0.0))
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"PRISM Oracle evaluation failed: {e}")

    def evaluate(self, symbol: str, current_price: Optional[float] = None) -> Action:
        """
        Evaluates the symbol using live PRISM data or a mock price. Updates the High Water Mark and calculates drawdown.
        """
        if current_price is None:
            current_price = self.fetch_prism_oracle_data(symbol)
        
        if current_price <= 0:
            return Action.HOLD
            
        highest_price = self.high_water_marks.get(symbol, 0.0)
        
        if current_price > highest_price:
            self.high_water_marks[symbol] = current_price
            return Action.HOLD
            
        drop_percentage = (highest_price - current_price) / highest_price
        
        if drop_percentage > self.threshold_percentage:
            return Action.TRIGGER_CIRCUIT_BREAKER
            
        return Action.HOLD
