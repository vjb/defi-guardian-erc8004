import os
import pytest
from unittest.mock import MagicMock
from eth_account import Account
from src.chain_utils import Web3Manager

def test_web3_connection(mocker):
    # Setup mock env vars
    mocker.patch.dict(os.environ, {
        "WEB3_RPC_URL": "https://test.rpc",
        "PRIVATE_KEY": "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        "RISK_ROUTER_ADDRESS": "0x1234567890123456789012345678901234567890"
    })
    
    # Mock Web3 connection
    mock_w3 = MagicMock()
    mock_w3.is_connected.return_value = True
    mocker.patch("src.chain_utils.Web3", return_value=mock_w3)

    manager = Web3Manager()
    assert manager.w3.is_connected() == True

@pytest.fixture
def mock_env(mocker):
    # Valid 32-byte private key for testing
    pk = "0x" + "1" * 64
    mocker.patch.dict(os.environ, {
        "WEB3_RPC_URL": "https://test.rpc",
        "PRIVATE_KEY": pk,
        "RISK_ROUTER_ADDRESS": "0x000000000000000000000000000000000000dEaD"
    })
    
    mock_w3 = MagicMock()
    mock_w3.is_connected.return_value = True
    mocker.patch("src.chain_utils.Web3", return_value=mock_w3)
    return pk

def test_eip712_signature(mock_env):
    manager = Web3Manager()
    
    action = "LIQUIDATE"
    threshold = 1500
    
    # We will mock timestamp to be deterministic if needed, or we just extract the signature and recover it.
    import time
    timestamp = int(time.time())
    
    # Actually let's just test that sign_trade_intent returns a string of the correct length and recover matches
    signature = manager.sign_trade_intent(action, threshold, timestamp)
    
    assert isinstance(signature, str)
    assert signature.startswith("0x")
    
    # Recover the address to verify signature
    from eth_account.messages import encode_typed_data
    
    typed_data = {
        "types": {
            "EIP712Domain": [
                {"name": "name", "type": "string"},
                {"name": "version", "type": "string"},
                {"name": "chainId", "type": "uint256"},
                {"name": "verifyingContract", "type": "address"}
            ],
            "TradeIntent": [
                {"name": "action", "type": "string"},
                {"name": "threshold", "type": "uint256"},
                {"name": "timestamp", "type": "uint256"}
            ]
        },
        "primaryType": "TradeIntent",
        "domain": {
            "name": "DeFiGuardian",
            "version": "1",
            "chainId": 11155111,
            "verifyingContract": "0x000000000000000000000000000000000000dEaD"
        },
        "message": {
            "action": action,
            "threshold": threshold,
            "timestamp": timestamp
        }
    }
    
    encoded_message = encode_typed_data(full_message=typed_data)
    recovered_address = Account.recover_message(encoded_message, signature=signature)
    
    assert recovered_address.lower() == manager.account.address.lower()
