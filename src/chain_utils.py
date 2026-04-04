import os
import time
from web3 import Web3
from eth_account import Account
from eth_account.messages import encode_typed_data

class Web3Manager:
    """Manages Web3 connections and EIP-712 typed data signatures."""

    def __init__(self):
        rpc_url = os.getenv("WEB3_RPC_URL")
        private_key = os.getenv("PRIVATE_KEY")
        self.risk_router = os.getenv("RISK_ROUTER_ADDRESS", "0x000000000000000000000000000000000000dEaD")
        
        if not rpc_url or not private_key:
            raise ValueError("WEB3_RPC_URL or PRIVATE_KEY not found in environment.")

        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.account = Account.from_key(private_key)

    def sign_trade_intent(self, action: str, threshold: int, timestamp: int = None) -> str:
        """
        Generates an EIP-712 structured signature for a TradeIntent.
        """
        if timestamp is None:
            timestamp = int(time.time())

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
                "chainId": 84532, # Base Sepolia
                "verifyingContract": self.risk_router
            },
            "message": {
                "action": action,
                "threshold": threshold,
                "timestamp": timestamp
            }
        }

        encoded_message = encode_typed_data(full_message=typed_data)
        signed_message = Account.sign_message(encoded_message, private_key=self.account.key)
        
        return "0x" + signed_message.signature.hex()
