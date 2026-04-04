import os
from typing import List, Dict, Optional
from pydantic import BaseModel, HttpUrl, Field, field_validator
from web3 import Web3

class AgentService(BaseModel):
    name: str
    endpoint: str
    version: Optional[str] = None
    skills: Optional[List[str]] = None
    domains: Optional[List[str]] = None

class AgentRegistration(BaseModel):
    agentId: int
    agentRegistry: str

class AgentMetadata(BaseModel):
    type: str = Field(default="https://eips.ethereum.org/EIPS/eip-8004#registration-v1")
    name: str
    description: str
    image: str
    services: List[AgentService]
    x402Support: bool = False
    active: bool = True
    registrations: List[AgentRegistration]
    supportedTrust: Optional[List[str]] = None
    
    @field_validator('type')
    @classmethod
    def validate_type(cls, v: str) -> str:
        if v != "https://eips.ethereum.org/EIPS/eip-8004#registration-v1":
            raise ValueError("Type must match ERC-8004 specification.")
        return v

class AgentIdentityManager:
    """Manages ERC-8004 Metadata validation and contract registration."""
    
    def __init__(self, w3: Optional[Web3] = None, account_address: Optional[str] = None):
        self.registry_address = os.getenv("ERC8004_REGISTRY_ADDRESS", "0x000000000000000000000000000000000000dEaD")
        self.w3 = w3
        self.account_address = account_address
        
        # Minimum ABI for contract calls
        self.abi = [
            {
                "inputs": [{"internalType": "string", "name": "tokenURI", "type": "string"}],
                "name": "registerAgent",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
            }
        ]
        
        if self.w3:
            self.contract = self.w3.eth.contract(
                address=Web3.to_checksum_address(self.registry_address), 
                abi=self.abi
            )

    def build_registration_tx(self, token_uri: str) -> dict:
        """
        Builds the transaction to register the agent on the ERC-8004 registry.
        """
        if not self.w3 or not self.account_address:
            raise ValueError("Web3 connection and account address required to build transaction.")
            
        nonce = self.w3.eth.get_transaction_count(self.account_address)
        
        tx = self.contract.functions.registerAgent(token_uri).build_transaction({
            'chainId': 11155111, # Ethereum Sepolia Testnet
            'gas': 500000,
            'maxFeePerGas': self.w3.to_wei('2', 'gwei'),
            'maxPriorityFeePerGas': self.w3.to_wei('1', 'gwei'),
            'nonce': nonce,
        })
        
        return tx
