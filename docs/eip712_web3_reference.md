# Web3.py EIP-712 Signature Reference

When signing Trade Intents for the Surge Hackathon Risk Router, you MUST use the `eth_account` library's `encode_typed_data` method. Do not use outdated or JavaScript-based workarounds.

Reference implementation for Python:

```python
from eth_account import Account
from eth_account.messages import encode_typed_data

# 1. Define the EIP-712 Domain and Message Dict
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
        "verifyingContract": "0xYourRiskRouterAddressHere"
    },
    "message": {
        "action": "LIQUIDATE",
        "threshold": 1500,
        "timestamp": 1710000000
    }
}

# 2. Encode and Sign
encoded_message = encode_typed_data(full_message=typed_data)
signed_message = Account.sign_message(encoded_message, private_key=PRIVATE_KEY)

# signed_message.signature.hex() is what gets sent to the smart contract
```
