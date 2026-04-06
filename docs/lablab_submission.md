# Lablab.ai Official Submission Sheet

Use this document to copy-paste exactly what you need into the Lablab.ai hackathon submission portal. 

---

## 1. Basic Information

**Project Title:** 
> DeFi Guardian: Decentralized Institutional Risk Sentry

**Short Description (Max 255 chars):** 
> An autonomous risk-management agent for institutional capital. It ingests PRISM AI market sentiment and executes trustless, EIP-712 bounds and non-custodial risk circuit breakers natively across the Surge Hackathon Vault.

**Long Description (Min 100 words):** 
> **The Problem:** Current generative Web3 trading bots act as highly volatile black-boxes trying to predict alpha. Institutions don't just need alpha; they need strict mathematical guarantees against catastrophic loss. There is currently no enterprise-grade architecture that bridges advanced AI market sentiment directly into trustless, non-custodial portfolio liquidation logic. 
> 
> **The Solution:** DeFi Guardian acts as an absolute institutional backstop. Operating entirely off-chain, the agent continually monitors market conditions via the PRISM AI Oracle. If structural failure triggers are hit, it bypasses centralized exchanges and generates a deterministic EIP-712 cryptographically signed intent. This intent mathematically proves its ERC-8004 identity on-chain and routes a gasless execution through the Surge Risk Router, ensuring smart-contract wallet compatibility (EIP-1271).
> 
> **Target Audience:** Institutional asset managers, decentralized hedge funds, and High-Net-Worth liquidity providers. 
> 
> **Unique Benefits:** Enforced cross-chain replay protection (EIP-155), non-custodial cryptographic security, developer-native Python Rich CLI presentation, and flawless ERC-8004 identity verification locking portfolio security to on-chain execution.

**Technology & Category Tags:**
> Web3, Blockchain, AI Agents, Risk Management, DeFi, Python, ERC-8004, EIP-712, EIP-1271, Smart Contracts

---

## 2. Platform & Repository Links

**Public GitHub Repository:** 
> https://github.com/vjb/defi-guardian-erc8004

**Demo Application URL (Live Etherscan & Terminal Execution Trace):** 
> https://github.com/vjb/defi-guardian-erc8004/blob/main/docs/execution_log.txt

---

## 3. Slide Presentation (For your PDF)

*Lablab tip: Keep slides succinct; limit to 2-3 sentences each. Open Canva or PowerPoint and create 5 simple slides with these titles/texts.*

**Slide 1: Problem Space**
> Generative AI bots chase volatile Alpha. Institutions need verifiable defense against risk. Custodial bots get hacked; we need trustless, cryptographically enforced circuit-breakers.

**Slide 2: Institutional Architecture**
> DeFi Guardian isolates risk metrics by ingesting PRISM AI. Built natively with Pydantic (V2) and a deterministic Python Rich CLI, it operates safely isolated from exchange API keys.

**Slide 3: Trustless Execution Loop**
> Upon detecting threshold failure, the Guardian signs an EIP-712 intent payload locally utilizing offline eth-account generation. The Risk Router smart contract mathematically validates the ERC-8004 Identity on-chain.

**Slide 4: The Market Scope**
> **TAM:** $50B Institutional DeFi Capital deployed in liquidity pools. 
> **SAM:** $5B High Net Worth autonomous allocation accounts.
> **Revenue Stream:** SaaS enterprise licensing fee + fractional percentage of portfolio value protected during drawdown events.

**Slide 5: Competitor Analysis & Future**
> Competitors use custody-based centralized keys (high security risk). Our USP: 100% non-custodial cryptography and natively formatted ERC-8004 specification. Future expansion targets ERC-7579 modular smart account integration.

---

## 4. Video Presentation Structure (Max 5 Mins)

*Use the `docs/video_presentation_script.md` you already have, but structure the physical video exactly like this:*

1. **[0:00 - 1:00] Introduction & Pitch:** Record your face / voiceover reading the Long Description problem/solution. 
2. **[1:00 - 2:00] Slide Deck:** Show the 5 exported PDF slides on your screen and quickly voice over the TAM and Competitor Analysis. 
3. **[2:00 - 4:45] Terminal Demo:** Run `python guardian_terminal.py` live on your screen. Show the PRISM AI logs scrolling and highlight the deterministic creation of the ERC-8004 keys, executing the true cryptographic EIP-712 payload.
4. **[4:45 - 5:00] Closing:** Conclude with the GitHub link.
