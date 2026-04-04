# 🛡️ DeFi Guardian: The ERC-8004 Institutional Risk Sentry

<p align="center">
  <b>Built for the Surge "AI Trading Agents" Hackathon</b><br>
  <i>Trustless Risk Management and EIP-712 Intent Execution</i>
</p>

---

## 📖 Project Overview
Current generative trading bots act as volatile black-boxes trying to predict alpha. But institutions don't just need alpha; they need **mathematical guarantees against catastrophic loss.**

**DeFi Guardian** entirely bypasses centralized risk management strategies by acting as an autonomous terminal agent deeply integrated with the official **ERC-8004 Trustless Agents Specification**. Powered by the Strykr PRISM AI Signals API, the Guardian actively monitors live market thresholds and cryptographically executes non-custodial `EIP-712` circuit breakers to the Ethereum Sepolia Risk Router the exact moment structural failure is detected.

No Twitter spam. No unpredictable PnL battles. Just pure, institutional-grade mathematical defense mechanisms.

> 🏆 **View our Complete Hackathon Judging Rubric & Verification Map:** [`docs/surge_hackathon_rubric.md`](docs/surge_hackathon_rubric.md)

---

## 🎥 Pitch & Presentation
Our codebase is designed to run flawlessly during demonstrations by utilizing an incredibly clean Python `Rich` terminal UI. 

Please refer to [`docs/video_presentation_script.md`](docs/video_presentation_script.md) for the exact script, pacing, and visual prompts needed to record the perfect 2-minute hackathon pitch.

---

## ⚡ Core Features
1. **Strict ERC-8004 Registration Schemas:** Uses Pydantic V2 to mathematically lock the agent payload precisely to the `"registration-v1"` specification over `eip155:11155111`.
2. **True Native AI Signals:** Natively polls the Strykr PRISM sponsor endpoint (`/signals/{symbol}`) to extract verified institutional market consensus matrices.
3. **Trustless Intent Execution:** Upon receiving a `bearish` signal, the agent skips centralized exchanges. It dynamically encodes EIP-155 safe EIP-712 domains and signs a cryptographically verifiable payload locally, ready for broadcast to the Surge Risk Router.

---

## 🚀 Getting Started

### 1. Requirements
- Python 3.10+
- The `rich` CLI and standard libraries.
```bash
pip install -r requirements.txt
```

### 2. Configure Environment (`.env`)
You must configure the standard keys in `.env`. Mocks have been disabled to ensure hackathon authenticity.

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

## 🛠️ Testing Validations
Verified 100% against native Ethereum capabilities (Zero mocking):
```bash
pytest tests/ -v
```
