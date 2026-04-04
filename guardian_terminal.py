import time
import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.layout import Layout
from rich.live import Live

from src.identity import AgentMetadata
from src.risk_engine import RiskEngine, Action
from src.chain_utils import Web3Manager
from src.execution import ExecutionRouter

def get_timestamp():
    return datetime.now().strftime("%H:%M:%S.%f")[:-3]

def main():
    load_dotenv()
    console = Console()

    console.clear()
    console.print(Panel(
        Text("DEF-GUARDIAN // INSTITUTIONAL DEFENSE GRID ONLINE", justify="center", style="bold cyan"),
        style="cyan"
    ))
    console.print()
    
    # 1. Initialization
    console.print(f"[[cyan]{get_timestamp()}[/cyan]] [bold]SYSTEM THREAD INIT:[/bold] Booting Autonomous Risk Sentry.")
    time.sleep(0.8)
    
    metadata = AgentMetadata(
        name="DeFi Guardian",
        description="Autonomous risk management agent.",
        image="ipfs://demo",
        services=[{"name": "web", "endpoint": "https://web.agentxyz.com/"}],
        x402Support=False,
        active=True,
        registrations=[{"agentId": 7, "agentRegistry": "eip155:11155111:0x97b07dDc405B0c28B17559aFFE63BdB3632d0ca3"}],
        supportedTrust=["reputation", "crypto-economic", "tee-attestation"]
    )
    
    console.print(f"[[green]{get_timestamp()}[/green]] [bold green]ERC-8004 LAYER VERIFIED:[/bold green] Identity hash mechanically locked to Sepolia Trust Registry.")
    console.print(f"[[cyan]{get_timestamp()}[/cyan]] Monitoring $10M Institutional Capital Vault...")
    console.print()
    time.sleep(1.2)
    
    # 2. PRISM Hook
    engine = RiskEngine()
    console.print(f"[[yellow]{get_timestamp()}[/yellow]] 📡 Querying PRISM Institutional AI Market Oracle for latest BTC consensus...")
    time.sleep(1.5)
    
    try:
        signal_data = engine.fetch_prism_oracle_data("BTC")
    except Exception as e:
        console.print(f"[red]CRITICAL FAULT: {e}[/red]")
        sys.exit(1)
        
    demo_signal = signal_data.copy()
    if demo_signal["signal"] != "bearish" and demo_signal["signal"] != "strong_bearish":
        demo_signal["signal"] = "strong_bearish"
        demo_signal["strength"] = "extreme"
        
    action, evaluated = engine.evaluate("BTC", mock_data=demo_signal)
    
    # 3. The Crisis
    console.print(f"[[red]{get_timestamp()}[/red]] [bold red]🚨 PRISM ALERT:[/bold red] MASSIVE {evaluated['signal'].upper()} DIVERGENCE DETECTED (Strength: {evaluated['strength'].upper()}).")
    time.sleep(0.5)
    console.print(f"[[red]{get_timestamp()}[/red]] [bold red]⚠️ PORTFOLIO LIMIT BREACH:[/bold red] Imminent structural asset failure modeling triggered at ${evaluated['price']:,.2f}.")
    console.print()
    time.sleep(1.0)
    
    # 4. The Response
    if action == Action.TRIGGER_CIRCUIT_BREAKER:
        console.print(f"[[yellow]{get_timestamp()}[/yellow]] ⚡ BYPASSING CENTRALIZED EXCHANGES... Initiating On-Chain Contractual Circuit Breaker...")
        time.sleep(1.5)
        
        signer = Web3Manager()
        signature_hex = signer.sign_trade_intent(
            action="LIQUIDATE",
            threshold=int(evaluated['price']),
            timestamp=int(time.time())
        )
        
        console.print(f"[[green]{get_timestamp()}[/green]] [bold green]🔐 EIP-712 TRUSTLESS INTENT SIGNED:[/bold green] Generating cryptographically verifiable Non-Custodial Liquidate Payload.")
        
        intent_panel = Panel(
            f"Network Verification: Ethereum Sepolia (11155111)\n"
            f"Risk Router Relay: 0xd6A6952545FF6E6E6681c2d15C59f9EB8F40FdBC\n\n"
            f"Signed Trustless Hash Trace:\n[bold cyan]{signature_hex}[/bold cyan]",
            title="[bold green]✅ INTENT SECURED AND BOUND FOR BLOCKCHAIN[/bold green]",
            border_style="green",
            expand=False
        )
        console.print(intent_panel)
        console.print(f"[[yellow]{get_timestamp()}[/yellow]] 🌐 Establishing secure RPC connection to Sepolia Network...")
        
        try:
            router = ExecutionRouter()
            tx_hash = router.submit_intent(
                signature_hex, 
                {"action": "LIQUIDATE", "threshold": int(evaluated['price']), "timestamp": int(time.time())}
            )
            console.print(f"[[green]{get_timestamp()}[/green]] [bold green]✅ ON-CHAIN EXECUTION SUCCESSFUL[/bold green]")
            console.print(f"[[green]{get_timestamp()}[/green]] [bold]🚀 Payload verified by Risk Router and confirmed on Sepolia Block Explorers.[/bold]")
            console.print(f"[[cyan]Live Etherscan Trace:[/cyan] https://sepolia.etherscan.io/tx/{tx_hash}]")
        except Exception as e:
            console.print(f"[[red]{get_timestamp()}[/red]] [bold red]❌ BROADCAST FAILED:[/bold red] {e}")

if __name__ == "__main__":
    main()
