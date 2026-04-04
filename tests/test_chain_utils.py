import os
import pytest
import time
from eth_account import Account
from dotenv import load_dotenv
from eth_account.messages import encode_typed_data
from src.chain_utils import Web3Manager

load_dotenv()

def test_web3_connection():
    manager = Web3Manager()
    assert manager.w3.is_connected() is True

def test_eip712_signature():
    manager = Web3Manager()
    
    action = "LIQUIDATE"
    threshold = 1500
    timestamp = int(time.time())
    
    signature = manager.sign_trade_intent(action, threshold, timestamp)
    
    assert isinstance(signature, str)
    assert signature.startswith("0x")
    
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
            "verifyingContract": os.getenv("RISK_ROUTER_ADDRESS")
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

def test_hackathon_contracts_are_real():
    manager = Web3Manager()
    
    # Prove the Risk Router is a deployed smart contract
    risk_router = os.getenv("RISK_ROUTER_ADDRESS")
    assert risk_router is not None
    router_code = manager.w3.eth.get_code(risk_router)
    assert len(router_code) > 2, f"RISK_ROUTER_ADDRESS {risk_router} has no deployed bytecode on Sepolia!"
    
    # Prove the Registry is a deployed smart contract
    registry = os.getenv("ERC8004_REGISTRY_ADDRESS")
    assert registry is not None
    registry_code = manager.w3.eth.get_code(registry)
    assert len(registry_code) > 2, f"ERC8004_REGISTRY_ADDRESS {registry} has no deployed bytecode on Sepolia!"


