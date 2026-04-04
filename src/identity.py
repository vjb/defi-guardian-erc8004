import os
from typing import List, Dict, Optional
from pydantic import BaseModel, HttpUrl, Field, field_validator
from web3 import Web3

class AgentEndpoints(BaseModel):
    api: HttpUrl
    mcp: Optional[HttpUrl] = None

class AgentMetadata(BaseModel):
    name: str
    description: str
    image: HttpUrl
    external_url: HttpUrl
    agent_wallet: str = Field(..., pattern=r"^0x[a-fA-F0-9]{40}$")
    capabilities: List[str] = Field(default=["RISK_MANAGEMENT", "LIQUIDATION", "CIRCUIT_BREAKER"])
    endpoints: AgentEndpoints

    @field_validator('capabilities')
    @classmethod
    def check_capabilities(cls, v: List[str]) -> List[str]:
        required = ["RISK_MANAGEMENT", "LIQUIDATION", "CIRCUIT_BREAKER"]
        if not all(cap in v for cap in required):
            raise ValueError(f"Capabilities must include all of {required}")
        return v

class AgentIdentityManager:
    """Manages ERC-8004 Metadata validation and contract registration."""
    
    def __init__(self, w3: Optional[Web3] = None, account_address: Optional[str] = None):
        self.registry_address = os.getenv("ERC8004_REGISTRY_ADDRESS", "0x000000000000000000000000000000000000dEaD")
        self.w3 = w3
        self.account_address = account_address
        
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
            'chainId': 84532, # Base Sepolia
            'gas': 500000,
            'maxFeePerGas': self.w3.to_wei('2', 'gwei'),
            'maxPriorityFeePerGas': self.w3.to_wei('1', 'gwei'),
            'nonce': nonce,
        })
        
        return tx
