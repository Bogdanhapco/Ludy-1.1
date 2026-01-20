import streamlit as st
import random
import time
from streamlit_autorefresh import st_autorefresh

# --- 1. SYSTEM CONFIG ---
st.set_page_config(page_title="BotDevelopmentAI | NOC", layout="wide")
st_autorefresh(interval=3000, key="noc_heartbeat") # Updates every 3 seconds

# --- 2. THEME STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #020202; color: #00ffcc; font-family: 'IBM Plex Mono', monospace; }
    .node-matrix {
        display: grid;
        grid-template-columns: repeat(15, 1fr);
        gap: 4px;
        padding: 10px;
        background: #080808;
        border: 1px solid #1a1a1a;
    }
    .node-unit {
        font-size: 9px;
        padding: 4px;
        border: 1px solid #151515;
        text-align: center;
        background: #050505;
        color: #008877;
    }
    .node-unit b { color: #00ffcc; }
    .engine-card {
        background: rgba(0, 255, 204, 0.03);
        border-left: 3px solid #00ffcc;
        padding: 15px;
        border-radius: 0 5px 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TOP NAV ---
c1, c2 = st.columns([4, 1])
with c1:
    st.markdown("<h1 style='letter-spacing:-2px;'>NETWORK OPERATIONS CENTER (NOC)</h1>", unsafe_allow_html=True)
    st.caption("INFRASTRUCTURE: 150 NODES // CLUSTER: RUBIN-V3 // STATUS: NOMINAL")
with c2:
    st.write(f"**SYNC:** {time.strftime('%H:%M:%S')}")
    st.write("**AUTH:** BOTDEV_ADMIN")

st.divider()

# --- 4. GLOBAL PERFORMANCE ---
genis_load = random.uniform(20.1, 24.5)
ludy_load = random.uniform(41.2, 48.8)
avg_util = (genis_load + ludy_load) / 2

m1, m2, m3, m4 = st.columns(4)
m1.metric("NODES ONLINE", "150 / 150", "STABLE")
m2.metric("VRAM TOTAL", "1,536 GB", "HBM3e")
m3.metric("CLUSTER LOAD", f"{avg_util:.1f}%", f"{random.uniform(-0.5, 0.5):.1f}%")
m4.metric("TEMP", "62.4°C", "-1.2°C")

# --- 5. THE 150-NODE MATRIX ---
st.write("### 🔲 COMPUTE FABRIC (NODE-001 TO NODE-150)")

# Generate the 150-node grid
node_html = '<div class="node-matrix">'
for i in range(1, 151):
    # Simulate realistic load fluctuation per node
    n_load = int(avg_util + random.uniform(-10, 10))
    n_load = max(5, min(99, n_load)) # Keep between 5% and 99%
    node_html += f'<div class="node-unit">{i:03d}<br/><b>{n_load}%</b></div>'
node_html += '</div>'

st.markdown(node_html, unsafe_allow_html=True)

st.divider()

# --- 6. ENGINE SPECIFICS ---
left, right = st.columns(2)

with left:
    st.markdown("<div class='engine-card'>", unsafe_allow_html=True)
    st.subheader("🧠 Genis-V3 Neural Engine")
    st.write("Task: Logic & Reasoning Cluster")
    st.progress(genis_load / 100)
    st.caption(f"Memory Saturation: {round(1024 * (genis_load/100), 1)} GB / 1,024 GB")
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='engine-card'>", unsafe_allow_html=True)
    st.subheader("🎨 SmartBot Ludy Engine")
    st.write("Task: Pixel Synthesis & Diffusion")
    st.progress(ludy_load / 100)
    st.caption(f"Memory Saturation: {round(512 * (ludy_load/100), 1)} GB / 512 GB")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 7. LOGS ---
st.divider()
st.code(f"[{time.strftime('%H:%M:%S')}] OK: All 150 Rubin nodes reporting healthy.\n[{time.strftime('%H:%M:%S')}] INFO: Load balanced across Genis and Ludy sub-clusters.\n[{time.strftime('%H:%M:%S')}] KERNEL: Liquid cooling cycle successful.", language="bash")
