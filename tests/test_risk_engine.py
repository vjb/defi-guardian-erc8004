import pytest
from src.risk_engine import RiskEngine, Action
from dotenv import load_dotenv

load_dotenv()

def test_fetch_prism():
    engine = RiskEngine()
    data = engine.fetch_prism_oracle_data("BTC")
    
    assert "signal" in data
    assert "price" in data
    assert data["price"] > 0.0
    
def test_evaluate_live_data():
    engine = RiskEngine()
    action, data = engine.evaluate("BTC")
    
    assert action in [Action.HOLD, Action.TRIGGER_CIRCUIT_BREAKER]
    assert "signal" in data

def test_evaluate_forced_bearish():
    engine = RiskEngine()
    mock_bearish = {"price": 60000.0, "signal": "bearish", "strength": "strong"}
    
    action, data = engine.evaluate("BTC", mock_data=mock_bearish)
    
    assert action == Action.TRIGGER_CIRCUIT_BREAKER
    assert data["signal"] == "bearish"

def test_missing_api_key_raises_error():
    engine = RiskEngine()
    engine.prism_api_key = None
    with pytest.raises(ValueError, match="PRISM_API_KEY is not configured"):
        engine.fetch_prism_oracle_data("BTC")
