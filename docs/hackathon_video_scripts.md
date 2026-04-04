# Hackathon Presentation Video Scripts

Since you are submitting to two different hackathon tracks (Auth0 and Surge/Kraken) with the same overarching codebase, you should record **two separate videos** tailored entirely to what each judging panel cares about. 

Here are the step-by-step video outlines and voiceover scripts for both 3-minute video submissions.

---

## 🛡️ Auth0 Hackathon Script: "Zero-Trust M2M Agent"
**Goal:** Prove to the Auth0 judges that you mastered the Token Vault, Client Credentials flow, and M2M backend security for autonomous agents.
**Estimated Time:** ~2 Minutes

### Screen 1: The Code Architecture (0:00 - 0:45)
*(Have `src/security.py` and `app.py` open in your IDE)*
**Voiceover:** 
"Hi, I'm presenting the DeFi Guardian—an autonomous risk agent. Most Web3 AI agents hardcode plaintext API keys in their environment variables, creating a massive single point of failure. To achieve true Zero-Trust architecture, this agent uses Auth0's Machine-to-Machine flow. In our `security.py` file, you can see that before the agent is allowed to execute any trades or fetch PRISM data, it negotiates via the Client Credentials flow to retrieve a tightly scoped JWT. The token exists purely ephemerally in memory."

### Screen 2: The UI Authentication (0:45 - 1:15)
*(Open the Streamlit App. Keep it in the "PENDING M2M VERIFICATION" state)*
**Voiceover:** 
"Here in our Institutional Dashboard, if a market crash occurs but the backend isn't authorized by Auth0, the circuit breaker intent strictly fails. The LLM or execution engine is locked out. Watch what happens when we verify the environment."
*(Click 'Authenticate Client'. Show the green SUCCESS UI with the JWT token snippet)*
"We've successfully requested our Vault token. The agent now has a cryptographic handshake with the backend and data layers, without requiring sticky user consent flows."

### Screen 3: The Execution (1:15 - 1:50)
*(Click 'Trigger Market Crash (-25%)' and show the Ledger)*
**Voiceover:** 
"Now when a portfolio drawdown is detected, the agent uses its Auth0 token to securely poll the live pricing oracle. Once verified, it executes an autonomous hedging protocol, signing the Web3 intent entirely automatically. Auth0 made securing this headless agent pipeline incredibly frictionless."

---

## 🌊 Surge / Kraken Hackathon Script: "Agentic Economic Viability"
**Goal:** Prove to Surge judges you understand EIP-712, ERC-8004 identities, Base Sepolia margins, and the PRISM API for risk evaluation. 
**Estimated Time:** ~2.5 Minutes

### Screen 1: The Context & PRISM Data (0:00 - 1:00)
*(Show the Streamlit App running. Briefly show `src/risk_engine.py`)*
**Voiceover:** 
"Welcome to DeFi Guardian. High-frequency AI agents operating on Ethereum L1 burn through their portfolio margins purely in execution gas. To solve this, our agent is built for Base Sepolia, relying on off-chain EIP-712 intent signatures that are routed to a centralized Risk Engine. 
Our agent begins by querying the Strykr PRISM API to fetch live oracle treasury data. If a drawdown crosses the 15% threshold, our algorithmic circuit breaker triggers."

### Screen 2: The Flash Loan Simulation (1:00 - 1:45)
*(Click 'Trigger Market Crash (-25%)' in the Streamlit UI)*
**Voiceover:** 
"Let's simulate a massive delta variance. The agent immediately identifies the critical state. Notice the Economic Viability matrix that just generated. By utilizing Base Sepolia, the gas cost of this agentic pipeline is just completely offset by the Flash Loan Arbitrage Yield. We extract $1,250 in liquidator fees, saving $15,000 in capital, at the cost of a fraction of a cent."

### Screen 3: Web3 Standards + MCP (1:45 - 2:30)
*(Show `src/execution.py` and `src/mcp_server.py`)*
**Voiceover:** 
"Beneath the hood, this isn't just a generic script. Our execution engine strictly validates against the ERC-8004 Agent Identity schema using Python Pydantic models. We sign fully compliant EIP-712 structured data packets. Furthermore, we've wrapped the entire execution logic inside the official Anthropics Model Context Protocol (MCP) `FastMCP` server, meaning any reasoning engine like Claude 3.5 can natively adopt this Guardian to guard protocol margins."
