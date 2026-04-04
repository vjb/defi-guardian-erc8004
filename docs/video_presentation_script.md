# Surge Hackathon Video Presentation Script: DeFi Guardian

**Target Duration:** 2.0 - 2.5 Minutes
**Objective:** Clearly articulate how DeFi Guardian solves institutional crypto risk by strictly enforcing ERC-8004 capabilities and EIP-712 trustless architecture to bypass centralized execution.

---

## 🎬 Section 1: The Hook & The Problem (0:00 - 0:30)

**[Screen Direction: Camera on Speaker, then transition to a clean, dramatic UI title card reading: *"DeFi Guardian: Trustless Institutional Shield"*]**

**Speaker:**
"Everyone is building generative trading agents right now—bots trying to predict alpha and guess market trends. But institutions don’t just want alpha; they want guarantees against catastrophic loss. Current trading bots operate black-boxes, lacking verifiable guardrails and transparency. If we want millions of dollars in TVL governed by agents, we need trustless protection."

**[Screen Direction: Show a quick architecture diagram or simply split-screen pointing to a traditional Web2 Bot vs an ERC-8004 Agent]**

**Speaker:**
"Welcome to DeFi Guardian. Instead of guessing what to buy, we built the ultimate defense mechanism for the Surge AI Trading Agents Hackathon. We natively implemented the **ERC-8004 Trustless Agents Specification** to create an autonomous risk-sentry designed exclusively for verifiable on-chain capital preservation."

---

## 💻 Section 2: The UI & The Technology Stack (0:30 - 1:15)

**[Screen Direction: Screen-share the Streamlit Institutional Dashboard. Slowly scroll down to show the active connection to Ethereum Sepolia and the 'Circuit Breaker' parameters]**

**Speaker:**
"Here is the institutional dashboard. Under the hood, the Guardian completely replaces centralized Auth0 workflows with native Web3 specifications. We enforce the ERC-8004 Agent Registration schema strictly—registering the agent mathematically on the Ethereum Sepolia registry and explicitly locking its capabilities exclusively to `RISK_MANAGEMENT`, `LIQUIDATION`, and `CIRCUIT_BREAKER`."

**[Screen Direction: Click the 'Poll Live PRISM API' button so the live price updates on screen]**

**Speaker:**
"To calculate risk, our engine tracks 'High Water Mark' drawdowns in real-time. We directly query the Strykr PRISM API to pull live asset prices. It dynamically tracks the highest watermark a portfolio achieves, and calculates structural downside risk perfectly."

---

## 🚀 Section 3: The 'Aha!' Moment / Trustless Execution (1:15 - 1:55)

**[Screen Direction: Smoothly hover over and click the 'Force Circuit Breaker Test (-25% Drop)' button. Make sure the screen is focused perfectly on the 'EXECUTION LEDGER' panel as it turns yellow, then flashes Green with the EIP-712 payload]**

**Speaker:**
"This is where DeFi Guardian shines. Watch what happens when a 25% critical drawdown is breached. The agent does *not* execute a web2 custodial market order. "

"Instead it instantly kicks in the trustless execution sequence. It takes the intent, encodes it to meet EIP-155 Chain-ID bindings to prevent replay attacks, and locally generates a cryptographic **EIP-712 Signed TypeData signature**. That non-custodial signature is sent directly to the Surge Risk Router."

**[Screen Direction: Highlight the text showing the raw hexadecimal signature block on the screen so the judges see the technical depth]**

"Institutions don't have to trust the server. The smart-contract Risk Router mathematically verifies the EIP-712 signature against our agent's ERC-8004 registered identity before processing the liquidation."

---

## 🏆 Section 4: Wrap-Up & Business Value (1:55 - 2:15)

**[Screen Direction: Camera returns to Speaker. Final logo overlay with text: 'Winner: Best Compliance & Risk Guardrails']**

**Speaker:**
"This is the future of the agentic economy. A world where safety boundaries are mathematically guaranteed. By bridging real-time Web2 pricing data with strict Web3 Trustless Execution intents, DeFi Guardian acts as the permanent, decentralized margin-guardrail that institutions can cryptographically rely upon. Thank you to Surge and the judges!"

---

### 🎥 Production Tips:
- **No Pauses:** Keep the energy high and the technical jargon punchy. 
- **Screen Clarity:** Enlarge the text on your IDE and Streamlit dashboard so the judges can actually read the EIP-712 text output when evaluating on mobile devices.
- **Lighting:** Record in a well-lit space. Use a simple, institutional-looking background to match the "institutional-grade" narrative of the pitch.
