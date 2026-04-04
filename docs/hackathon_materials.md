# Hackathon Materials & Deliverables

## 2-Minute Video Presentation Script

**Slide 1: Intro (0:00 - 0:15)**
"Hi there, we are presenting DeFi Guardian for the Surge 'AI Trading Agents' Hackathon. While others are building bots that guess the market, DeFi Guardian is a trustless ERC-8004 risk agent focused entirely on strict capital preservation."

**Slide 2: ERC-8004 Setup (0:15 - 0:45)**
"Our agent enforces transparency verifiable on-chain. We integrated the ERC-8004 capability standard perfectly, configuring the agent specifically for 'Risk Management, Liquidation, and Circuit Breaker' capabilities. Using Pydantic enforcement, the agent maps directly to the Base Sepolia Registry Contract."

**Slide 3: Live Strykr PRISM API (0:45 - 1:15)**
"Risk is only as good as the data. We integrated true, live polling against the Strykr PRISM target crypto endpoints. Our risk engine constantly maintains a High Water Mark, immediately detecting severe threshold drops in unmanipulable real-time, completely bypassing basic mock values."

**Slide 4: Trustless EIP-712 Execution (1:15 - 1:45)**
"Check out the dashboard's manual override metric. Once a 15% drawdown occurs, the agent refuses to do standard Web2 commands. Instead, it generates a cryptographically enforced EIP-712 Trade Intent. That signature allows our Risk Router on Base Sepolia to execute liquidations transparently and trustlessly."

**Slide 5: Conclusion (1:45 - 2:00)**
"DeFi Guardian represents institutional-grade DeFi safety. Thank you to the Surge Hackathon!"

---

## 5-Slide Presentation Outline

**1. Problem**
- Institutions fear uncapped downside in crypto. Current generative trading bots are dangerous and offer no hard guardrails.
- Relying on Web2 APIs for fail-safes is highly custodial.

**2. Solution & ERC-8004 Identity**
- Our solution is a verifiable Risk Management Agent using strict ERC-8004 metadata.
- Fully transparent identity and execution capabilities registered on Base Sepolia.

**3. Architecture**
- **Data Layer:** Strykr PRISM real-time API.
- **Logic Layer:** Pure Python High Water Mark tracking.
- **Execution Layer:** EIP-712 signed Trade Intents routed to decentralized on-chain contracts.

**4. Business Value**
- Institutional adoption relies strictly on capital preservation. 
- Agents that act as permanent Risk Guards increase total TVL in protocols because whales feel protected against Flash Crashes.

**5. Future Roadmap**
- Expanding the PRISM API multi-asset scanning.
- Deploying dynamic signature throttling techniques on Mainnet.
- Introducing multi-agent consensus before EIP-712 circuit breakers are signed.
