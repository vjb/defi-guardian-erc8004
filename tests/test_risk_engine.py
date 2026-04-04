import pytest
from src.risk_engine import RiskEngine, Action

def test_evaluate_safe_portfolio(mocker):
    engine = RiskEngine()
    
    # establish HWM
    engine.evaluate("BTC", current_price=100000)
    
    # 2% drop
    action = engine.evaluate("BTC", current_price=98000)
    assert action == Action.HOLD
    
def test_evaluate_critical_portfolio(mocker):
    engine = RiskEngine()
    
    # establish HWM
    engine.evaluate("BTC", current_price=100000)
    
    # 25% drop
    action = engine.evaluate("BTC", current_price=75000)
    assert action == Action.TRIGGER_CIRCUIT_BREAKER
    
def test_fetch_prism_oracle_success(mocker):
    engine = RiskEngine()
    mocker.patch.dict("os.environ", {"PRISM_API_KEY": "mock_prism_key"})
    
    # Because __init__ pulls PRISM_API_KEY at instantiated time, 
    # we should re-instantiate or explicitly set it for the test if it wasn't there
    engine.prism_api_key = "mock_prism_key"
    
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"price": 75000.0}
    mocker.patch("requests.get", return_value=mock_response)
    
    price = engine.fetch_prism_oracle_data("BTC")
    assert price == 75000.0
    
    import requests
    requests.get.assert_called_once_with(
        "https://api.prismapi.ai/crypto/BTC/price",
        headers={"X-API-Key": "mock_prism_key"}
    )
    
def test_fetch_prism_oracle_failure(mocker):
    engine = RiskEngine()
    engine.prism_api_key = "mock_prism_key"
    
    mock_response = mocker.MagicMock()
    mock_response.status_code = 403
    import requests
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("403 Forbidden")
    mocker.patch("requests.get", return_value=mock_response)
    
    with pytest.raises(RuntimeError):
        engine.fetch_prism_oracle_data("BTC")

def test_missing_api_key_raises_error():
    engine = RiskEngine()
    engine.prism_api_key = None
    with pytest.raises(ValueError, match="PRISM_API_KEY is not configured"):
        engine.fetch_prism_oracle_data("BTC")
