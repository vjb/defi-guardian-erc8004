import os
from typing import Dict
from web3 import Web3
from eth_account import Account

class ExecutionRouter:
    """Submits EIP-712 signed Trade Intents to the on-chain Risk Router."""
    
    def __init__(self):
        rpc_url = os.getenv("WEB3_RPC_URL")
        private_key = os.getenv("PRIVATE_KEY")
        self.router_address = os.getenv("RISK_ROUTER_ADDRESS", "0x000000000000000000000000000000000000dEaD")
        
        if not rpc_url or not private_key:
            raise ValueError("WEB3_RPC_URL or PRIVATE_KEY not found in environment.")
            
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.account = Account.from_key(private_key)
        
        # Standard ABI for executing the intent
        self.abi = [
            {
                "inputs": [
                    {
                        "components": [
                            {"internalType": "uint256", "name": "agentId", "type": "uint256"},
                            {"internalType": "address", "name": "agentWallet", "type": "address"},
                            {"internalType": "string", "name": "pair", "type": "string"},
                            {"internalType": "string", "name": "action", "type": "string"},
                            {"internalType": "uint256", "name": "amountUsdScaled", "type": "uint256"},
                            {"internalType": "uint256", "name": "maxSlippageBps", "type": "uint256"},
                            {"internalType": "uint256", "name": "nonce", "type": "uint256"},
                            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
                        ],
                        "internalType": "struct RiskRouter.TradeIntent",
                        "name": "intent",
                        "type": "tuple"
                    },
                    {"internalType": "bytes", "name": "signature", "type": "bytes"}
                ],
                "name": "submitTradeIntent",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "inputs": [{"internalType": "uint256", "name": "agentId", "type": "uint256"}],
                "name": "getIntentNonce",
                "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                "stateMutability": "view",
                "type": "function"
            }
        ]
        
        self.contract = self.w3.eth.contract(
            address=Web3.to_checksum_address(self.router_address),
            abi=self.abi
        )
        
    def get_intent_nonce(self, agent_id: int) -> int:
        return self.contract.functions.getIntentNonce(agent_id).call()

    def submit_intent(self, signature: str, intent_payload: Dict) -> str:
        """
        Submits the intent to the smart contract.
        Returns the transaction hash.
        """
        # Convert hex signature to bytes
        sig_bytes = Web3.to_bytes(hexstr=signature)
        
        intent_tuple = (
            intent_payload["agentId"],
            intent_payload["agentWallet"],
            intent_payload["pair"],
            intent_payload["action"],
            intent_payload["amountUsdScaled"],
            intent_payload["maxSlippageBps"],
            intent_payload["nonce"],
            intent_payload["deadline"]
        )
        
        nonce = self.w3.eth.get_transaction_count(self.account.address)
        
        # Build the transaction
        tx = self.contract.functions.submitTradeIntent(intent_tuple, sig_bytes).build_transaction({
            'chainId': 11155111, # Ethereum Sepolia Testnet
            'gas': 500000,
            'maxFeePerGas': self.w3.to_wei('2', 'gwei'),
            'maxPriorityFeePerGas': self.w3.to_wei('1', 'gwei'),
            'nonce': nonce,
        })
        
        # Sign the transaction
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=self.account.key)
        
        # Broadcast
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        tx_hex = self.w3.to_hex(tx_hash)
        
        # Wait for on-chain block mining to determine absolute success/revert status
        try:
            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
            status = receipt.status
        except Exception:
            status = 2 # 2 implies timeout/unknown
            
        return {
            "tx_hash": tx_hex,
            "status": status
        }
