import pytest
from src.execution import ExecutionRouter
from dotenv import load_dotenv

load_dotenv()

def test_submit_intent_to_router():
    router = ExecutionRouter()
    
    # An offline signature just for formatting tests
    signature = "0x" + "0" * 130
    payload = {
        "action": "LIQUIDATE",
        "threshold": 1500,
        "timestamp": 1234567890
    }
    
    tx_hash = router.submit_intent(signature, intent_payload)
    
    assert tx_hash == "0xmock_tx_hash"
    mock_w3.eth.send_raw_transaction.assert_called_with(mock_signed_tx.raw_transaction)
    router.contract.functions.executeIntent.assert_called_once()
