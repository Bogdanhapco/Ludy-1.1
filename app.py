import streamlit as st
import random
import time
from streamlit_autorefresh import st_autorefresh

# --- PAGE CONFIG ---
st.set_page_config(page_title="BotDevelopmentAI Data Center", layout="wide")

# Real-Time Pulse: Refresh every 2 seconds
st_autorefresh(interval=2000, key="neural_heartbeat")

# --- CYBERPUNK INFRASTRUCTURE STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #010101; color: #00ffcc; font-family: 'Courier New', monospace; }
    .node-card {
        border-left: 5px solid #00ffcc;
        background: rgba(0, 255, 204, 0.05);
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 0 10px 10px 0;
    }
    .metric-text { font-size: 24px; font-weight: bold; color: #ffffff; }
    h2 { color: #00ffcc !important; border-bottom: 1px solid #333; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛰️ BotDevelopmentAI Data Center")
st.write(f"MODEL CLUSTER: GENIS-V3 | ACTIVE NODES: {random.randint(148, 150)}/150 | COOLING: CRYOGENIC")

# --- TOP ROW: GLOBAL STATS ---
col1, col2, col3 = st.columns(3)
total_vram_load = random.uniform(24.2, 29.8)
col1.metric("GLOBAL VRAM LOAD", f"{total_vram_load:.1f}%", f"{random.uniform(-0.2, 0.2):.1f}%")
col2.metric("THROUGHPUT", f"{random.randint(1200, 1450)} T/s", "STABLE")
col3.metric("FABRIC LATENCY", "0.002ms", "OPTIMAL")

st.divider()

# --- MIDDLE SECTION: GENIS vs LUDY ---
left_col, right_col = st.columns(2)

with left_col:
    st.markdown("## 🧠 GENIS-V3 (Language Engine)")
    st.markdown("<div class='node-card'>", unsafe_allow_html=True)
    st.write("**Architecture:** Liquid Transformer v4")
    st.write("**VRAM Allocated:** 1,024 GB (HBM3e)")
    st.write("**Current Task:** Contextual Reasoning & Logic")
    
    # Live Load Gauge
    genis_load = random.randint(15, 22)
    st.progress(genis_load / 100)
    st.write(f"Inference Load: {genis_load}%")
    st.markdown("</div>", unsafe_allow_html=True)

with right_col:
    st.markdown("## 🎨 SMARTBOT LUDY (Visual Engine)")
    st.markdown("<div class='node-card'>", unsafe_allow_html=True)
    st.write("**Architecture:** Multi-Modal Diffusion (Schnell)")
    st.write("**VRAM Allocated:** 512 GB (HBM3e)")
    st.write("**Current Task:** High-Fidelity Pixel Synthesis")
    
    # Live Load Gauge
    ludy_load = random.randint(35, 48)
    st.progress(ludy_load / 100)
    st.write(f"Synthesis Load: {ludy_load}%")
    st.markdown("</div>", unsafe_allow_html=True)

# --- BOTTOM SECTION: SYSTEM LOGS ---
st.subheader("📋 Neural Node Logs")
logs = [
    f"[{time.strftime('%H:%M:%S')}] NODE-012: Genis-V3 processing logic-stream.",
    f"[{time.strftime('%H:%M:%S')}] NODE-085: SmartBot Ludy allocated 24GB to new prompt.",
    f"[{time.strftime('%H:%M:%S')}] SYSTEM: 1.5TB VRAM Cache health 100%.",
    f"[{time.strftime('%H:%M:%S')}] FABRIC: East-West traffic optimized across 150 nodes."
]
st.code("\n".join(logs), language="bash")
