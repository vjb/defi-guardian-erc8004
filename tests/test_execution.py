import os
import pytest
from unittest.mock import MagicMock
from src.execution import ExecutionRouter

def test_submit_intent_to_router(mocker):
    # Setup env
    mocker.patch.dict(os.environ, {
        "RISK_ROUTER_ADDRESS": "0x1234567890123456789012345678901234567890",
        "PRIVATE_KEY": "0x" + "1" * 64,
        "WEB3_RPC_URL": "https://test.rpc"
    })
    
    router = ExecutionRouter()
    
    # Mock Web3 connection
    mock_w3 = MagicMock()
    mock_w3.eth.get_transaction_count.return_value = 10
    mock_w3.eth.max_priority_fee = 1000000000
    mock_w3.eth.send_raw_transaction.return_value = b'mock_tx_hash'
    mock_w3.to_hex.return_value = "0xmock_tx_hash"
    
    # Needs to simulate account signing
    mock_signed_tx = MagicMock()
    mock_signed_tx.raw_transaction = b'signed_raw_tx'
    mock_w3.eth.account.sign_transaction.return_value = mock_signed_tx
    
    router.w3 = mock_w3
    
    # Mock contract and function
    mock_contract = MagicMock()
    mock_func = MagicMock()
    mock_func.build_transaction.return_value = {
        'chainId': 84532,
        'gas': 300000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
        'nonce': 10
    }
    mock_contract.functions.executeIntent.return_value = mock_func
    router.contract = mock_contract
    
    signature = "0x" + "a" * 130
    intent_payload = {
        "action": "LIQUIDATE",
        "threshold": 1500,
        "timestamp": 1234567890
    }
    
    tx_hash = router.submit_intent(signature, intent_payload)
    
    assert tx_hash == "0xmock_tx_hash"
    mock_w3.eth.send_raw_transaction.assert_called_with(mock_signed_tx.raw_transaction)
    router.contract.functions.executeIntent.assert_called_once()
