# ERC-8004: Trustless Agent Identity Metadata Standard

When generating the Agent Registration JSON for the ERC-8004 Identity Registry, the AI Agent must conform to this standard JSON schema.

{
  "name": "String - The name of the agent (e.g., 'DeFi Guardian')",
  "description": "String - What the agent does",
  "image": "String (URL) - Link to agent avatar",
  "external_url": "String (URL) - Link to agent dashboard/code",
  "agent_wallet": "String (Hex Address) - The EVM address the agent uses to sign intents",
  "capabilities": [
    "Array of Strings - e.g., 'RISK_MANAGEMENT', 'LIQUIDATION', 'PORTFOLIO_MONITORING'"
  ],
  "endpoints": {
    "api": "String (URL) - Where the agent receives requests",
    "mcp": "String (URL) - Optional MCP server endpoint"
  }
}

The Python `AgentIdentityManager` must use Pydantic to strictly enforce this schema before pinning it to IPFS or submitting the URI to the `registerAgent` smart contract function.
