# DeFi Guardian: Trustless ERC-8004 Risk Agent

DeFi Guardian is an institutional-grade, trustless DeFi trading agent designed for the Surge "AI Trading Agents" Hackathon. It rigorously enforces human-defined risk boundaries automatically. By tracking high water marks and live pricing via the Strykr PRISM API, it executes non-custodial EIP-712 circuit breakers on Base Sepolia when drawdowns exceed threshold limits.

## Hosted App & Demo
- **Live Institutional Dashboard:** [Streamlit Cloud Placeholder API]
- **Video Presentation:** [YouTube Placeholder URL] 

## Hackathon Judging Criteria Matrix

### 1. Application of Technology
We natively implement the **ERC-8004 Agent Registration** standard, enforcing precise capabilities (`RISK_MANAGEMENT`, `LIQUIDATION`, `CIRCUIT_BREAKER`). Our robust Pydantic-powered schemas guarantee verifiable on-chain metadata. By bridging Web2 real-time data (Strykr PRISM) with Web3 Trustless Execution (EIP-712 Signatures on Base Sepolia), we build an end-to-end decentralized fail-safe.

### 2. Presentation
Our Streamlit dashboard utilizes "Bloomberg Terminal/Vanguard-style" CSS design language to demonstrate the agent's actions in real-time. Judges can use a manual "Force Circuit Breaker Test" button to witness the EIP-712 cryptographic signature generation step-by-step.

### 3. Business Value
Institutions fear unhedged crypto volatility. DeFi Guardian provides professional-grade risk management. It operates completely autonomously and trustlessly, safeguarding millions of TVL while earning liquidator-fee yields during severe market crashes. 

### 4. Originality
Rather than building just another generative trading bot, we focused on risk first. This agent does not guess what to buy—it strictly enforces "Capital Preservation" using EIP-712 intents to act as a permanent, decentralized margin-guardrail that institutions can cryptographically rely upon.

## Target Prize Pools
- 🏆 **Best Risk-Adjusted Return**: Focuses entirely on hedging downside volatility through automated, trustless mitigation techniques.
- 🏆 **Best Compliance & Risk Guardrails**: Complies directly with ERC-8004 standards and operates transparently through cryptographically signed EIP-712 intents.

## Project Structure
- `src/identity.py`: ERC-8004 Metadata generation & Registry implementation.
- `src/risk_engine.py`: Live Strykr PRISM API polling and drawdown calculations.
- `src/execution.py`: Submits perfectly constructed EIP-712 signatures to the Risk Router.
- `app.py`: Institutional real-time dashboard.

## Local Execution
Ensure you have Python 3.10+ installed.
```bash
pip install -r requirements.txt
streamlit run app.py
```

## License
MIT License. See `LICENSE` for details.
