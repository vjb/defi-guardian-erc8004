import time
import os
import streamlit as st
from src.risk_engine import RiskEngine, Action
from src.chain_utils import Web3Manager
from src.execution import ExecutionRouter

st.set_page_config(page_title="Institutional Risk Management Dashboard", layout="wide")

# Inject rigorous, Vanguard/Schwab-style corporate CSS
st.markdown("""
    <style>
    /* Institutional Layout */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1600px;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        background-color: #f8f9fa;
        color: #333333;
    }
    
    .corporate-panel {
        background-color: white;
        border: 1px solid #d2d6dc;
        padding: 24px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05); margin-bottom: 24px;
    }
    
    .panel-header {
        font-size: 14px;
        font-weight: 700;
        text-transform: uppercase;
        color: #004b87; /* Corporate Navy */
        border-bottom: 2px solid #004b87;
        margin-bottom: 16px;
        padding-bottom: 8px;
    }

    .data-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 13px;
        margin-bottom: 20px;
    }
    .data-table th, .data-table td {
        border-bottom: 1px solid #e2e8f0;
        padding: 10px 8px;
        text-align: left;
    }
    .data-table th {
        font-weight: 600;
        color: #64748b;
        background-color: #f1f5f9;
        text-transform: uppercase;
        font-size: 11px;
    }
    
    .val-positive { color: #166534; font-weight: 600; }
    .val-negative { color: #991b1b; font-weight: 600; }
    
    /* Buttons */
    .stButton>button {
        background-color: white !important;
        color: #004b87 !important;
        border: 1px solid #004b87 !important;
        border-radius: 0 !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        padding: 0.5rem 1rem !important;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #004b87 !important;
        color: white !important;
    }
    .btn-danger>button {
        border-color: #991b1b !important;
        color: #991b1b !important;
    }
    .btn-danger>button:hover {
        background-color: #991b1b !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("INSTITUTIONAL RISK MANAGEMENT DASHBOARD")
st.markdown("<p style='font-size: 13px; color: #64748b; margin-top: -15px;'>SYSTEM ID: 8004-DEF-GUARDIAN | CLEARANCE: L3 | LICENSED: MIT</p>", unsafe_allow_html=True)

# State initialization
if "risk_engine" not in st.session_state:
    st.session_state.risk_engine = RiskEngine()
if "current_price" not in st.session_state:
    st.session_state.current_price = 100000.0  # Anchor mock
if "portfolio_state" not in st.session_state:
    st.session_state.portfolio_state = "SAFE"
if "tx_hash" not in st.session_state:
    st.session_state.tx_hash = None
if "signature" not in st.session_state:
    st.session_state.signature = None
if "drawdown" not in st.session_state:
    st.session_state.drawdown = 0.0

st.markdown("<div class='corporate-panel'>", unsafe_allow_html=True)
st.markdown("<div class='panel-header'>ERC-8004 IDENTITY & CAPABILITIES</div>", unsafe_allow_html=True)
col_id1, col_id2, col_id3 = st.columns(3)
col_id1.metric("Agent Name", "DeFi Guardian")
col_id2.metric("Trustless Protocol", "Base Sepolia Registered")
col_id3.write("**Capabilities:**")
st.markdown("""
<span style='background-color: #004b87; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px; margin-right: 5px;'>RISK_MANAGEMENT</span>
<span style='background-color: #004b87; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px; margin-right: 5px;'>LIQUIDATION</span>
<span style='background-color: #004b87; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px;'>CIRCUIT_BREAKER</span>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown("<div class='corporate-panel'>", unsafe_allow_html=True)
    st.markdown("<div class='panel-header'>STRYKR PRISM API - LIVE FEED</div>", unsafe_allow_html=True)
    
    if st.button("Poll Live PRISM API"):
        with st.spinner("Fetching data..."):
            try:
                live_price = st.session_state.risk_engine.fetch_prism_oracle_data("BTC")
                action = st.session_state.risk_engine.evaluate("BTC", current_price=live_price)
                st.session_state.current_price = live_price
                
                hwm = st.session_state.risk_engine.high_water_marks.get("BTC", 0.0)
                if hwm > 0:
                    st.session_state.drawdown = ((hwm - live_price) / hwm) * 100
                    
                if action == Action.TRIGGER_CIRCUIT_BREAKER:
                    st.session_state.portfolio_state = "CRASH"
                else:
                    st.session_state.portfolio_state = "SAFE"
            except Exception as e:
                st.error(f"API Error: {e}")
                
    st.markdown("<div class='btn-danger'>", unsafe_allow_html=True)
    if st.button("Force Circuit Breaker Test (-25% Drop)"):
        with st.spinner("Injecting critical simulated drawdown..."):
            st.session_state.risk_engine.evaluate("BTC", current_price=100000.0) # set hwm
            action = st.session_state.risk_engine.evaluate("BTC", current_price=75000.0)
            st.session_state.current_price = 75000.0
            st.session_state.drawdown = 25.0
            st.session_state.portfolio_state = "CRASH"
    st.markdown("</div>", unsafe_allow_html=True)
    
    hwm = st.session_state.risk_engine.high_water_marks.get("BTC", 0.0)
    
    st.markdown(f"""
    <table class='data-table'>
        <tr><th>Metric</th><th>Value</th></tr>
        <tr><td>Tracked Asset</td><td>BTC</td></tr>
        <tr><td>Live Price</td><td>${st.session_state.current_price:,.2f}</td></tr>
        <tr><td>High Water Mark (HWM)</td><td>${hwm:,.2f}</td></tr>
        <tr><td>Current Drawdown</td><td class='{'val-negative' if st.session_state.drawdown >= 15 else 'val-positive'}'>{st.session_state.drawdown:.2f}%</td></tr>
    </table>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    st.markdown("<div class='corporate-panel'>", unsafe_allow_html=True)
    st.markdown("<div class='panel-header'>EXECUTION LEDGER</div>", unsafe_allow_html=True)
    
    if st.session_state.portfolio_state == "CRASH":
        if not st.session_state.tx_hash:
            st.warning("Critical Drawdown detected. Executing EIP-712 Intent...")
            try:
                web3_manager = Web3Manager()
                timestamp = int(time.time())
                sig = web3_manager.sign_trade_intent("CIRCUIT_BREAKER", 1500, timestamp)
                st.session_state.signature = sig
                
                router = ExecutionRouter()
                payload = {"action": "CIRCUIT_BREAKER", "threshold": 1500, "timestamp": timestamp}
                tx = router.submit_intent(sig, payload)
                st.session_state.tx_hash = tx
                st.success("Execution Completed.")
            except Exception as e:
                st.error(f"Execution Fault: {e}")

    if st.session_state.tx_hash:
        st.markdown("<div style='padding:15px; border:1px solid #22c55e; background-color:#dcfce7; color:#166534; font-weight:bold; margin-bottom:15px;'>MANDATED LIQUIDATION EXECUTED SUCCESSFULLY</div>", unsafe_allow_html=True)
        st.markdown(f"**EIP-712 Signature Generated:**")
        st.code(st.session_state.signature, language="text")
        
        st.markdown(f"**Transaction Broadcast (Base Sepolia):**")
        st.markdown(f"<a href='https://sepolia-explorer.base.org/tx/{st.session_state.tx_hash}' target='_blank' style='color:#004b87; font-weight:bold;'>{st.session_state.tx_hash}</a>", unsafe_allow_html=True)
    else:
        st.info("System Nominal. Standing by.")
        
    st.markdown("</div>", unsafe_allow_html=True)
