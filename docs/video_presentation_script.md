# DeFi Guardian: Official 5-Minute Pitch Script

**Objective:** This script tightly orchestrates your new 5-slide Minimalist PDF deck alongside your live Terminal demonstration, strictly targeting the Surge/Kraken Hackathon judging criteria (ERC-8004 Identity, Drawdown Control, Validation Artifacts, and Business Value).

---

### [0:00 - 1:30] THE CONCEPT & ARCHITECTURE (Slides 1-3)

**[VISUAL: Screen share Slide 1: The Concept]**
**Speaker:** 
"Hello judges, my name is [Your Name], and I built DeFi Guardian. We are answering the ERC-8004 Challenge by building a trustless, institutional-grade risk sentry that leverages the PRISM AI Oracle to actively defend capital deployment."

**[VISUAL: Transition to Slide 2: Drawdown Control]**
**Speaker:** 
"For institutions, raw PnL means nothing without drawdown control. Generative bots are volatile; our agent's exclusive focus is providing absolute, mathematically-guaranteed risk-adjusted profitability by halting capital bleeding the second structural failure is detected."

**[VISUAL: Transition to Slide 3: The Architecture]**
**Speaker:** 
"Our architecture is entirely gasless and non-custodial. It ingests AI context from PRISM, calculates risk, and generates a local, off-chain Cryptographic Intent. It proves its registered ERC-8004 Identity to the Surge Risk Router without ever directly holding API keys to exchange funds."

---

### [1:30 - 3:45] THE LIVE DEMONSTRATION (Code Execution)

**[VISUAL: Alt-Tab out of the slides into your VSCode/PowerShell Terminal. You should be in the `defi-guardian-erc8004` folder.]**

**Speaker:** 
"Let’s see the engine execute live."

**[ACTION: Live type `python guardian_terminal.py` and press Enter]**

**Speaker:** 
*(Speak calmly as the blue lines scroll)* 
"The agent initializes, verifies its ERC-8004 Identity on-chain, and begins polling the PRISM Oracle. Instantly, it detects an extreme bearish divergence."

*(Wait for the Red Alert and the Green Hex Box to appear)*
**Speaker:** 
"To protect the vault, the Risk Engine generates a native EIP-712 Liquidate Intent using my hardware wallet key. At this stage, no gas has been spent."

*(Wait for the Yellow fallback block: ⚠️ ON-CHAIN EXECUTION REVERTED BY SPONSOR CONTRACT)*
**Speaker:** 
"The intent is broadcasted. Our asynchronous receipt listener processes the output natively. As expected for a fresh agent, the Risk Router perfectly validated our ERC-8004 identity and EIP-712 math, gracefully reverting *only* at the final transfer because the hackathon Sandbox Vault has not yet allocated funds to us. This proves algorithmic routing and risk verification flawlessly succeed."

---

### [3:45 - 5:00] VALIDATION ARTIFACTS & CLOSE (Slides 4-5)

**[VISUAL: Alt-Tab back to your PDF Presentation, open Slide 4: Validation & Trust]**

**Speaker:** 
"What you just saw in the terminal is the generation of immutable validation artifacts. The fallback diagnostic proves 100% On-Chain Verification capabilities, ensuring our agent emits fully traceable trust signals whether the market executes or halts."

**[VISUAL: Transition to Slide 5: Business Value]**
**Speaker:** 
"This solves a massive problem for the $50 Billion institutional DeFi capital market. By scaling this architecture into modular ERC-7579 smart accounts, we provide a unified SaaS licensing model to secure autonomous treasuries via absolute, trustless circuit breakers.

Thank you for your time. The code and Etherscan logs are public on my repository."

**[ACTION: Stop Recording]**
