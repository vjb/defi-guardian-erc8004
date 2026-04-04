# DeFi Guardian: Official 5-Minute Pitch Script

**Objective:** This script tightly orchestrates your 5 PDF slides alongside your live Terminal demonstration, strictly matching the Lablab.ai hackathon requirements.

---

### [0:00 - 1:00] THE HOOK & ARCHITECTURE (Slides 1-3)

**[VISUAL: Screen share Slide 1: The Institutional Problem]**
**Speaker:** 
"Hello judges, my name is [Your Name], and I built DeFi Guardian.
Current generative trading bots act as volatile black-boxes trying to catch alpha. But institutions don't just need alpha; they need mathematical guarantees against catastrophic loss. We lack enterprise-grade architecture that bridges AI market sentiment directly into trustless, non-custodial portfolio liquidation."

**[VISUAL: Transition to Slide 2: Centralized vs Trustless Risk]**
**Speaker:** 
"DeFi Guardian acts as an absolute institutional backstop. Unlike competitors who rely on centralized API keys that get hacked, our agent operates entirely off-chain."

**[VISUAL: Transition to Slide 3: The Algorithmic Architecture]**
**Speaker:** 
"It continuously ingests real-time data from the PRISM AI Oracle. If structural failure thresholds are hit, the Guardian bypasses exchanges and generates an EIP-712 cryptographically signed payload locally. This intent proves its ERC-8004 Identity on-chain and routes a gasless execution straight through the Surge Risk Router."

---

### [1:00 - 3:45] THE LIVE DEMONSTRATION (Code Execution)

**[VISUAL: Alt-Tab out of the slides into your VSCode/PowerShell Terminal. You should be in the `defi-guardian-erc8004` folder.]**

**Speaker:** 
"Let’s look at the engine in action. I will boot up the Guardian terminal."

**[ACTION: Live type `python guardian_terminal.py` and press Enter]**

**Speaker:** 
*(Speak calmly as the blue lines scroll)* 
"The agent initializes and queries the PRISM Oracle. Instantly, it detects an extreme bearish divergence."

*(Wait for the Red Alert and the Green Hex Box to appear)*
**Speaker:** 
"To protect the $10M vault, the Guardian immediately disconnects from the centralized feed and generates a native EIP-712 Intent Hash using my local hardware wallet key."

*(Wait for the Yellow or Green execution block to print at the bottom)*
**Speaker:** 
"The intent is broadcasted to the Ethereum Sepolia blockchain. As you can see by our native receipt listener, the architecture seamlessly handles the on-chain interaction. The execution is successful relative to the sponsor vault funding status, and the Etherscan trace URL is generated directly in the logs."

---

### [3:45 - 5:00] THE MARKET SCOPE & CLOSE (Slides 4-5)

**[VISUAL: Alt-Tab back to your PDF Presentation, open Slide 4: Market Scope]**

**Speaker:** 
"This is a massive institutional play. The Total Addressable Market for deployed DeFi liquidity is over $50 Billion dollars, with a highly serviceable $5 Billion running in High-Net-Worth autonomous accounts. Our revenue scales horizontally via SaaS licensing and fractional recovery fee routing."

**[VISUAL: Transition to Slide 5: Competitor Analysis & Future]**
**Speaker:** 
"While competitors focus on risky custodial execution, we isolate everything off-chain with gasless cryptographic generation. Moving forward, we intend to integrate this engine natively into ERC-7579 modular smart accounts.

Thank you for your time. The code is public, and the execution trace is verifiable on Sepolia."

**[ACTION: Stop Recording]**
