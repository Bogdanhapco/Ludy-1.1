import streamlit as st
import random
import time
from streamlit_autorefresh import st_autorefresh

# --- 1. SYSTEM CONFIG ---
st.set_page_config(page_title="BotDevelopmentAI | NOC", layout="wide")
st_autorefresh(interval=2500, key="noc_heartbeat") # Live pulse every 2.5s

# --- 2. PROFESSIONAL DARK THEME ---
st.markdown("""
    <style>
    .stApp { background-color: #030303; color: #00ffcc; font-family: 'IBM Plex Mono', monospace; }
    .stat-label { color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; }
    .stat-value { font-size: 2rem; font-weight: bold; color: #fff; }
    .node-box {
        border: 1px solid #1a1a1a;
        padding: 10px;
        text-align: center;
        background: rgba(255, 255, 255, 0.02);
    }
    .engine-header { color: #00ffcc !important; border-bottom: 2px solid #00ffcc; padding-bottom: 5px; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TOP NAV / HEADER ---
c1, c2 = st.columns([3, 1])
with c1:
    st.markdown("<h1 style='letter-spacing:-1px;'>NETWORK OPERATIONS CENTER (NOC)</h1>", unsafe_allow_html=True)
    st.caption("INTERNAL INFRASTRUCTURE MONITOR // BOTDEVELOPMENTAI CORP.")
with c2:
    st.write(f"**ENCRYPTION:** AES-256-GCM")
    st.write(f"**SYSTEM TIME:** {time.strftime('%H:%M:%S')}")

st.divider()

# --- 4. CORE ENGINE TELEMETRY ---
# Dynamic load simulation
genis_load = random.uniform(19.2, 23.8)
ludy_load = random.uniform(39.5, 47.1)
total_vram_total = 1536  # 1.5 TB Total
current_vram_gb = round(total_vram_total * ((genis_load + ludy_load) / 200), 1)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("<p class='stat-label'>Compute Nodes</p><p class='stat-value'>150 / 150</p>", unsafe_allow_html=True)
with col2:
    st.markdown("<p class='stat-label'>Total VRAM Saturation</p><p class='stat-value'>{} GB</p>".format(current_vram_gb), unsafe_allow_html=True)
with col3:
    st.markdown("<p class='stat-label'>Cluster Efficiency</p><p class='stat-value'>98.4%</p>", unsafe_allow_html=True)
with col4:
    st.markdown("<p class='stat-label'>Core Temperature</p><p class='stat-value'>64.2°C</p>", unsafe_allow_html=True)

st.divider()

# --- 5. DETAILED NODE MATRIX (NUMBERS ONLY) ---
st.markdown("### 📊 INFRASTRUCTURE NODE MATRIX")
# Displaying a grid of load percentages instead of squares
node_cols = st.columns(5)
for i in range(5):
    with node_cols[i]:
        for j in range(3): # Shows 15 sample node readings
            node_id = (i * 3 + j) + 1
            node_load = round(random.uniform(20.0, 50.0), 1)
            st.markdown(f"""
                <div class='node-box'>
                    <span style='color:#555; font-size:10px;'>NODE-{node_id:03d}</span><br/>
                    <span style='color:#00ffcc;'>LOAD: {node_load}%</span>
                </div>
            """, unsafe_allow_html=True)

st.divider()

# --- 6. MODEL-SPECIFIC METRICS ---
left, right = st.columns(2)

with left:
    st.markdown("<h2 class='engine-header'>🧠 Genis-V3 Engine</h2>", unsafe_allow_html=True)
    st.write("**Model Type:** Autoregressive Liquid Transformer")
    st.write(f"**HBM3e Allocation:** 1,024 GB")
    st.metric("Inference Load", f"{genis_load:.2f}%", f"{random.uniform(-0.1, 0.1):.2f}%")
    st.progress(genis_load / 100)
    st.code(f"STATUS: NodeGroup-Alpha routing tokens...", language="bash")

with right:
    st.markdown("<h2 class='engine-header'>🎨 SmartBot Ludy Engine</h2>", unsafe_allow_html=True)
    st.write("**Model Type:** Multi-Modal Latent Diffusion")
    st.write(f"**HBM3e Allocation:** 512 GB")
    st.metric("Synthesis Load", f"{ludy_load:.2f}%", f"{random.uniform(-0.5, 0.5):.2f}%")
    st.progress(ludy_load / 100)
    st.code(f"STATUS: NodeGroup-Beta rendering pixels...", language="bash")

# --- 7. CORE KERNEL LOGS ---
st.divider()
st.subheader("📝 Live System Logs")
logs = [
    f"[{time.strftime('%H:%M:%S')}] SYS: All 150 nodes responding. Latency 0.002ms.",
    f"[{time.strftime('%H:%M:%S')}] KERNEL: Genis-V3 optimized via FlashAttention-3.",
    f"[{time.strftime('%H:%M:%S')}] MEM: VRAM scrubbing complete on Ludy cluster.",
    f"[{time.strftime('%H:%M:%S')}] NET: BotDevelopmentAI internal fabric link stable."
]
st.code("\n".join(logs), language="bash")
