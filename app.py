import streamlit as st
import random
import time
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# --- 1. SYSTEM CONFIG ---
st.set_page_config(page_title="BotDevelopmentAI | NOC", layout="wide")
st_autorefresh(interval=2500, key="noc_heartbeat") # Refresh every 2.5s

# --- 2. DARK-OPS STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #030303; color: #00ffcc; font-family: 'IBM Plex Mono', monospace; }
    .node-active { height: 12px; width: 12px; background-color: #00ffcc; border-radius: 2px; display: inline-block; margin: 2px; box-shadow: 0 0 5px #00ffcc; }
    .node-idle { height: 12px; width: 12px; background-color: #1a1a1a; border-radius: 2px; display: inline-block; margin: 2px; }
    .stat-label { color: #888; font-size: 0.8rem; text-transform: uppercase; }
    .stat-value { font-size: 1.8rem; font-weight: bold; color: #fff; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER ---
c1, c2 = st.columns([3, 1])
with c1:
    st.markdown("<h1 style='letter-spacing:-1px;'>NETWORK OPERATIONS CENTER (NOC)</h1>", unsafe_allow_html=True)
    st.caption("INTERNAL INFRASTRUCTURE MONITOR // BOTDEVELOPMENTAI CORP.")
with c2:
    st.write(f"**ENCRYPTION:** AES-256")
    st.write(f"**UPTIME:** 99.9998%")

st.divider()

# --- 4. MODEL ALLOCATION ENGINE ---
# Real-time simulation of load across 1.5TB VRAM
genis_load = random.uniform(18.5, 24.2)
ludy_load = random.uniform(38.1, 46.5)
total_usage_pct = (genis_load + ludy_load) / 2

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"<p class='stat-label'>Active Models</p><p class='stat-value'>Genis + Ludy</p>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<p class='stat-label'>Total VRAM Used</p><p class='stat-value'>{round(1536 * (total_usage_pct/100), 1)} GB</p>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<p class='stat-label'>GPU Saturation</p><p class='stat-value'>{round(total_usage_pct, 1)}%</p>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<p class='stat-label'>Node Count</p><p class='stat-value'>150 / 150</p>", unsafe_allow_html=True)

# --- 5. THE INFRASTRUCTURE GRID (150 Nodes) ---
st.write("### 🔲 COMPUTE FABRIC (150 NODES)")
# Visualizing 150 nodes as small glowing squares
node_html = ""
for i in range(150):
    # Higher load means more nodes look "bright"
    status = "node-active" if random.random() < (total_usage_pct/100) + 0.3 else "node-idle"
    node_html += f'<div class="{status}"></div>'
st.markdown(f'<div style="line-height: 0;">{node_html}</div>', unsafe_allow_html=True)

st.divider()

# --- 6. MODEL-SPECIFIC TELEMETRY ---
left, right = st.columns(2)

with left:
    st.subheader("🧠 Genis-V3 Engine")
    st.write("Context Window: 128k Tokens // Quantization: FP8")
    st.progress(genis_load / 100)
    st.caption(f"Throughput: {random.randint(85, 110)} tokens/sec per node")
    
    # Tiny mini-log for Genis
    st.code(f"> Logic sequence validated at Node-{random.randint(1,75)}\n> Response latency: 12ms", language="bash")

with right:
    st.subheader("🎨 SmartBot Ludy Engine")
    st.write("Architecture: Latent Diffusion // Sampling: 4-Step Schnell")
    st.progress(ludy_load / 100)
    st.caption(f"Synthesis Rate: {random.uniform(1.2, 1.8):.2f} images/sec")
    
    # Tiny mini-log for Ludy
    st.code(f"> Pixel buffer allocated at Node-{random.randint(76,150)}\n> Denoising cluster online", language="bash")

# --- 7. LIVE SYSTEM LOGS ---
st.write("### 📝 CORE KERNEL LOGS")
logs = [
    f"[{time.strftime('%H:%M:%S')}] OK: HBM3e Memory clock synchronized at 1.2GHz.",
    f"[{time.strftime('%H:%M:%S')}] INFO: Balancing workload for Genis-V3 (Node Group A).",
    f"[{time.strftime('%H:%M:%S')}] WARN: Thermal increase on Node-112. Cooling increased to 80%.",
    f"[{time.strftime('%H:%M:%S')}] OK: SmartBot Ludy batch processing initialized."
]
st.code("\n".join(logs), language="bash")
