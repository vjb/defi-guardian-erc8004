import os
import json
import pytest
from pydantic import ValidationError
from web3 import Web3
from dotenv import load_dotenv
from src.identity import AgentMetadata, AgentIdentityManager

load_dotenv()

def test_generate_metadata():
    # Valid metadata strictly adhering to ERC-8004
    metadata = AgentMetadata(
        name="DeFi Guardian",
        description="Autonomous risk management agent.",
        image="https://example.com/agentimage.png",
        services=[
            {"name": "web", "endpoint": "https://web.agentxyz.com/"},
            {"name": "A2A", "endpoint": "https://agent.example/.well-known/agent-card.json", "version": "0.3.0"}
        ],
        x402Support=False,
        active=True,
        registrations=[
            {"agentId": 22, "agentRegistry": "eip155:11155111:0x97b07dDc405B0c28B17559aFFE63BdB3632d0ca3"}
        ],
        supportedTrust=["reputation", "crypto-economic", "tee-attestation"]
    )
    
    json_str = metadata.model_dump_json()
    parsed = json.loads(json_str)
    
    assert parsed["name"] == "DeFi Guardian"
    assert parsed["type"] == "https://eips.ethereum.org/EIPS/eip-8004#registration-v1"
    assert parsed["registrations"][0]["agentId"] == 22
    assert "tee-attestation" in parsed["supportedTrust"]

    # Invalid metadata should raise ValidationError (missing required schemas like services or registrations)
    with pytest.raises(ValidationError):
        AgentMetadata(
            name="DeFi Guardian",
            description="Autonomous risk management agent.",
            image="not_a_url",
            services=[],  # assuming valid but missing registrations which is required schema type
            x402Support=False,
            active=True
        )

def test_register_agent_tx_build():
    w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_RPC_URL")))
    manager = AgentIdentityManager(w3=w3, account_address="0x1234567890123456789012345678901234567890")
    
    # Executes a live unmocked query to get_transaction_count over the real RPC
    tx = manager.build_registration_tx("ipfs://mock_uri")
    
    assert tx["chainId"] == 11155111
    assert "nonce" in tx
    assert tx["gas"] > 0


