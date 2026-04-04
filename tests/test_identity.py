import os
import json
import pytest
from pydantic import ValidationError
from src.identity import AgentMetadata, AgentIdentityManager

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
            image="not_a_url",  # Should be a valid URL
            external_url="https://example.com",
            agent_wallet="not_a_hex", # Invalid wallet
            capabilities=["RISK_MANAGEMENT"],
            endpoints={"api": "https://api.example.com"}
        )

def test_register_agent_tx_build(mocker):
    # Setup environment 
    mocker.patch.dict(os.environ, {
        "ERC8004_REGISTRY_ADDRESS": "0xRegistryAddress",
        "PRIVATE_KEY": "0x" + "1" * 64
    })
    
    manager = AgentIdentityManager()
    manager.account_address = "0x1234567890123456789012345678901234567890"
    
    # Mock Web3
    mock_w3 = mocker.MagicMock()
    mock_w3.eth.get_transaction_count.return_value = 5
    mock_w3.eth.max_priority_fee = 1000000000
    mock_w3.eth.gas_price = 2000000000
    manager.w3 = mock_w3
    
    # Mock contract
    mock_contract = mocker.MagicMock()
    mock_function = mocker.MagicMock()
    mock_function.build_transaction.return_value = {
        "chainId": 84532,
        "nonce": 5,
        "to": "0xRegistryAddress",
        "value": 0,
        "gas": 200000,
        "maxFeePerGas": 3000000000,
        "maxPriorityFeePerGas": 1000000000,
        "data": "0xMockData"
    }
    mock_contract.functions.registerAgent.return_value = mock_function
    manager.contract = mock_contract
    
    tx = manager.build_registration_tx("ipfs://mock_uri")
    
    assert tx["chainId"] == 84532
    assert tx["nonce"] == 5
    manager.contract.functions.registerAgent.assert_called_with("ipfs://mock_uri")
    mock_function.build_transaction.assert_called_once()

