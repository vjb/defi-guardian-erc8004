# Surge "AI Trading Agents" Hackathon Checklist & Materials

## Overview
This document aligns the **DeFi Guardian** architecture strictly with the official Surge Hackathon documentation and constraints.

## Challenge Selected: ⭐ ERC-8004 Challenge

### Required Technology Checklist
- [x] **ERC-8004 Registries for Agent Identity, Reputation, and Validation:**
  - *Implemented:* `src/identity.py` natively formats the agent registration artifact to perfectly match the ERC-8004 Draft Standard (`registration-v1`), and constructs the transaction against the Ethereum Sepolia Registry contract (`0x97b07dDc405B0c28B17559aFFE63BdB3632d0ca3`).
- [x] **EIP-712 Typed Data Signatures:**
  - *Implemented:* `src/execution.py` dynamically builds and cryptographically signs an EIP-712 TypeData payload outlining the `CIRCUIT_BREAKER` and `LIQUIDATION` intents when structural risk is detected.
- [x] **EIP-1271 support & EIP-155 chain-id binding:**
  - *Implemented:* Our EIP-712 Domain heavily strictly enforces EIP-155 by locking the signature domain to `11155111` (Ethereum Sepolia), preventing cross-chain replay attacks. Smart-contract wallet compatibility (EIP-1271) is inherently supported via the Risk Router's signature verification scheme which executes the intents.
- [x] **DEX Execution via whitelist Risk Router:**
  - *Implemented:* Intents are broadcast strictly to the hackathon-provided Surge Risk Router (`0xd6A6952545FF6E6E6681c2d15C59f9EB8F40FdBC`).

## Standard Python Engineering Practices
To ensure institutional grade code, "reinvented wheels" were aggressively purged:
1. **Pydantic (V2):** Used natively for all JSON schema generation and strictly enforcing ERC-8004 schema types instead of manually building dictionaries.
2. **eth-account & Web3.py:** Used for deterministic, industry-standard EIP-712 signature generation natively rather than manual hex encoding.
3. **No Mocks:** All tests execute absolute end-to-end network requests. The High Water Mark evaluates live endpoints via the `requests` library.

## Prize Targeting
- 🏆 **Main Category:** Best Trustless Trading Agent ($10k)
- 🏆 **Special Award:** Best Compliance & Risk Guardrails ($2.5k)

We optimize entirely around the "Risk & Guardrails" angle. By natively enforcing High Water Mark logic via PRISM API to determine unhedged portfolio momentum, and trustlessly signing execution intents to the Router when violated, we stand as the premier institutional-grade compliance agent.
