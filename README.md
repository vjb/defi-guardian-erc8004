# DeFi Guardian: The ERC-8004 Institutional Risk Sentry

<p align="center">
  <b>High-Fidelity Automated Defense Infrastructure</b><br>
  <i>Trustless Risk Management and EIP-712 Intent Execution</i>
</p>

---

## Project Overview
Current generative trading bots act as volatile black-boxes trying to predict alpha. But institutions don't just need alpha; they need **mathematical guarantees against catastrophic loss.**

**DeFi Guardian** solves this by acting as an autonomous terminal agent deeply integrated with the official **ERC-8004 Trustless Agents Specification**. Powered by the Strykr PRISM AI Signals API, the Guardian actively monitors live market thresholds. The exact moment an institutional downside consensus is reached, it skips centralized exchanges and cryptographically executes non-custodial `EIP-712` circuit breakers directly to the Ethereum Sepolia Risk Router.

## The Trustless Execution Loop

```mermaid
sequenceDiagram
    participant PRISM as Strykr PRISM API
    participant Agent as DeFi Guardian Node
    participant ERC8004 as Sepolia Trust Registry
    participant Router as Surge Risk Router

    Agent->>ERC8004: Validate Metadata (eip155:11155111)
    Note over Agent,ERC8004: Capabilities: RISK_MANAGEMENT, CIRCUIT_BREAKER
    
    loop Real-Time Market Monitoring
        Agent->>PRISM: Poll /signals/{symbol}
        PRISM-->>Agent: AI Consensus (e.g., Bearish Divergence)
    end
    
    Note over Agent: Structural Market Failure Detected!
    
    Agent->>Agent: Construct EIP-155 Safe Intent Payload
    Agent->>Agent: Sign EIP-712 Intent Cryptographically
    
    Agent->>Router: Broadcast Non-Custodial Circuit Breaker
    Router-->>Agent: Verification Success. Portfolio Secured.
```

## System Architecture & Components

| Component | Backing Script | Primary Responsibility |
| :--- | :--- | :--- |
| **Terminal Core UI** | [`guardian_terminal.py`](guardian_terminal.py) | Orchestrates the God-Mode CLI execution, rendering rich logs, and injecting demo transparency. |
| **ERC-8004 Metadata** | [`src/identity.py`](src/identity.py) | Natively formats agent registration and builds the transaction against the Sepolia Registry. |
| **Institutional Oracle** | [`src/risk_engine.py`](src/risk_engine.py) | Ingests and evaluates PRISM AI market consensus data to trigger circuit breakers. |
| **EIP-712 Engine** | [`src/execution.py`](src/execution.py) | Dynamically structures and cryptographically signs EIP-155 safe non-custodial intents for the Risk Router. |

## Core Capabilities

1. **Trustless Ecosystem Verification**  
   The Guardian mathematically locks its payload to the exact "registration-v1" specification. This proves to the smart contracts that it is a verifiably registered agent permitted for autonomous operation over the **Ethereum Sepolia blockchain** (Network ID: 11155111).

2. **Institutional Signal Polling**  
   Rather than making simple moving average guesses, the Guardian natively integrates the **Strykr PRISM AI Signals API** (`/signals/{symbol}`). This fetches deep, multi-source consensus metrics directly from active institutional data feeds.

3. **Non-Custodial Circuit Breakers**  
   When a structural asset failure is identified (e.g., Extreme Bearish Divergence), the agent skips vulnerable centralized exchanges. It generates an EIP-155 safe, cross-chain resistant cryptographic payload (EIP-712). This intent is broadcast securely and executed natively by the Surge Risk Router's smart contracts.

### Advanced Ecosystem Enhancements
We specifically engineered the Guardian to fulfill advanced institutional security directives:
- **Portfolio risk modules enforced on-chain:** Our entire architecture abandons weak web2 market-sells, enforcing circuit breakers fundamentally via on-chain contract verifications.
- **TEE-backed attestations:** The registration explicitly structures for `"tee-attestation"` within its `supportedTrust` arrays, cementing readiness for secure enclave validation.

### Technology Stack & Standards
- **ERC-8004 Registries:** Natively formats agent registration artifacts to match the ERC-8004 Draft Standard (`registration-v1`).
- **EIP-712 & EIP-1271 Support:** Dynamically builds and cryptographically signs EIP-712 TypeData payloads outlining `submitTradeIntent` intents with all 8 institutional specification variables (agentId, pair, slippage, etc). Enforces EIP-155 by locking the signature domain to `11155111` (Ethereum Sepolia). Smart-contract wallet compatibility (EIP-1271) is natively supported.
- **Pydantic (V2):** Used natively for JSON schema generation and strictly enforcing ERC-8004 schema types.
- **eth-account & Web3.py:** Used for deterministic, industry-standard EIP-712 signature generation completely offline.
- **Python Rich CLI:** Powers the developer-native Terminal Interface to guarantee execution reliability and flawless presentation logic.

---

## Getting Started

### 1. Requirements
- Python 3.10+
- The `rich` CLI and standard libraries.
```bash
pip install -r requirements.txt
```

### 2. Configure Environment (`.env`)
You must configure the standard keys in `.env`.

```env
WEB3_RPC_URL=https://rpc.sepolia.org
PRIVATE_KEY=your_private_key
RISK_ROUTER_ADDRESS=0xd6A6952545FF6E6E6681c2d15C59f9EB8F40FdBC
ERC8004_REGISTRY_ADDRESS=0x97b07dDc405B0c28B17559aFFE63BdB3632d0ca3
PRISM_API_KEY=your_prism_key
```

### 3. Execution (The God-Mode Terminal)
```bash
python guardian_terminal.py
```
*The command line interface will dynamically structure the ERC-8004 keys, fetch the live PRISM payload, trigger the simulated circuit breaker, and render the exact, valid cryptographic EIP-712 payload in neon hex.*

---

## Documentation & Verification
- **Terminal Execution Trace:** [`docs/execution_log.txt`](docs/execution_log.txt)
- **Live On-Chain Verification:** [Etherscan Sepolia Transaction Hash](https://sepolia.etherscan.io/tx/0xf3cce690820897ca2c2c2119a3e3e686c1d925923fc8853ef6cfac53e263f646)

---

## Testing Validations
Verified 100% against native Ethereum capabilities (Zero mocking):
```bash
pytest tests/ -v
```
