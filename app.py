import streamlit as st
import random
import time
from streamlit_autorefresh import st_autorefresh

# --- PAGE CONFIG ---
st.set_page_config(page_title="BotDevelopmentAI Data Center", layout="wide")

# Heartbeat: Refresh every 2 seconds
st_autorefresh(interval=2000, key="data_center_heartbeat")

# --- DARK THEME STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #020202; color: #00ffcc; font-family: 'Courier New', monospace; }
    .stat-box {
        border: 2px solid #00ffcc;
        padding: 25px;
        border-radius: 5px;
        background: rgba(0, 255, 204, 0.03);
        text-align: center;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.1);
    }
    .glitch { font-weight: bold; text-transform: uppercase; letter-spacing: 3px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='glitch'>🛰️ BotDevelopmentAI Data Center Status</h1>", unsafe_allow_html=True)
st.write(f"SYSTEM TIME: {time.strftime('%Y-%m-%d %H:%M:%S')} | STATUS: OPERATIONAL")
st.divider()

# --- INFRASTRUCTURE MATH ---
# These are live-simulated based on high-end 2026 Rubin/Vera specs
gpu_percent = round(random.uniform(22.5, 28.1), 1)
nodes_active = random.randint(146, 150)
vram_used = round((gpu_percent / 100) * 1536, 1) # Based on 1.5TB total
hourly_cost = round(12.50 + random.uniform(-0.15, 0.15), 2)

# --- TOP METRICS ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='stat-box'>", unsafe_allow_html=True)
    st.metric("OPERATIONAL NODES", f"{nodes_active}/150", "ONLINE")
    st.caption("Rubin-Factory Scale")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='stat-box'>", unsafe_allow_html=True)
    st.metric("GPU UTILIZATION", f"{gpu_percent}%", f"{random.uniform(-0.5, 0.5):.1f}%")
    st.caption("Real-Time Load")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='stat-box'>", unsafe_allow_html=True)
    st.metric("VRAM USAGE", f"{vram_used} GB", "/ 1536 GB")
    st.caption("Active Liquid Cache")
    st.markdown("</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='stat-box'>", unsafe_allow_html=True)
    st.metric("HOURLY OPEX", f"${hourly_cost}", f"{(hourly_cost/24):.3f}/min")
    st.caption("Estimated Power/Compute")
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# --- SYSTEM LOGS ---
st.subheader("📋 Core Engine Logs")
logs = [
    f"NODE-{random.randint(1,150)}: Handshake verified. Model Genis-V3 engaged.",
    f"THERMAL: Liquid cooling at 64°C. Fans at 45%.",
    f"NETWORK: Routing 1.6T data packets through Olympus fabric.",
    f"MODEL: VRAM allocation successful for Genis-V3 inference."
]
st.code("\n".join(logs), language="bash")
