import os
import json
import pytest
from pydantic import ValidationError
from web3 import Web3
from dotenv import load_dotenv
from src.identity import AgentMetadata, AgentIdentityManager

load_dotenv()

def test_generate_metadata():
    # Valid metadata
    metadata = AgentMetadata(
        name="DeFi Guardian",
        description="Autonomous risk management agent.",
        image="https://example.com/avatar.png",
        external_url="https://example.com",
        agent_wallet="0x1234567890123456789012345678901234567890",
        capabilities=["RISK_MANAGEMENT", "LIQUIDATION", "CIRCUIT_BREAKER"],
        endpoints={
            "api": "https://api.example.com",
            "mcp": "https://mcp.example.com"
        }
    )
    
    json_str = metadata.model_dump_json()
    parsed = json.loads(json_str)
    
    assert parsed["name"] == "DeFi Guardian"
    assert "RISK_MANAGEMENT" in parsed["capabilities"]

    # Invalid metadata should raise ValidationError
    with pytest.raises(ValidationError):
        AgentMetadata(
            name="DeFi Guardian",
            description="Autonomous risk management agent.",
            image="not_a_url",
            external_url="https://example.com",
            agent_wallet="not_a_hex",
            capabilities=["RISK_MANAGEMENT"],
            endpoints={"api": "https://api.example.com"}
        )

def test_register_agent_tx_build():
    w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_RPC_URL")))
    manager = AgentIdentityManager(w3=w3, account_address="0x1234567890123456789012345678901234567890")
    
    # Executes a live unmocked query to get_transaction_count over the real RPC
    tx = manager.build_registration_tx("ipfs://mock_uri")
    
    assert tx["chainId"] == 11155111
    assert "nonce" in tx
    assert tx["gas"] > 0


