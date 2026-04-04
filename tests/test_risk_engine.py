import pytest
from src.risk_engine import RiskEngine, Action
from dotenv import load_dotenv

load_dotenv()

def test_evaluate_safe_portfolio():
    engine = RiskEngine()
    engine.evaluate("BTC", current_price=100000)
    action = engine.evaluate("BTC", current_price=98000)
    assert action == Action.HOLD
    
def test_evaluate_critical_portfolio():
    engine = RiskEngine()
    engine.evaluate("BTC", current_price=100000)
    action = engine.evaluate("BTC", current_price=75000)
    assert action == Action.TRIGGER_CIRCUIT_BREAKER
    
def test_fetch_prism_oracle_success():
    engine = RiskEngine()
    # Perform a live unmocked network request using .env API keys
    price = engine.fetch_prism_oracle_data("BTC")
    assert isinstance(price, float)
    assert price > 0

def test_missing_api_key_raises_error():
    engine = RiskEngine()
    engine.prism_api_key = None
    with pytest.raises(ValueError, match="PRISM_API_KEY is not configured"):
        engine.fetch_prism_oracle_data("BTC")

