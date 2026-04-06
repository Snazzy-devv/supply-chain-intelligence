import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
from datetime import datetime
import random
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIG & PULSE (20 Seconds) ---
st.set_page_config(layout="wide", page_title="NEON SENTINEL", page_icon="🛡️")

# The Heartbeat: This will refresh the KPIs and the Brief every 20s
count = st_autorefresh(interval=20000, limit=None, key="sentinel_heartbeat")

# --- 2. DYNAMIC INTEL ENGINE ---
def get_intel_brief(index):
    briefs = [
        "📡 ANALYTIC: Predictive models suggest a 12% rise in South-China Sea congestion.",
        "💡 STRATEGY: Consider shifting 15% of buffer stock to Rotterdam terminals.",
        "⚡ ALERT: Automated clearing at Singapore Port is reducing dwell times.",
        "🌐 MACRO: Global freight indices show stabilizing container costs for Q3.",
        "🛡️ SECURITY: Cybersecurity protocols updated for all regional data-links."
    ]
    return briefs[index % len(briefs)]

# --- 3. UI STYLING ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0b1120; color: #f8fafc; }}
    div[data-testid="stMetric"] {{
        background-color: #1e293b; border: 1px solid #334155;
        border-radius: 12px; padding: 20px;
    }}
    [data-testid="stMetricValue"] {{ color: #fbbf24 !important; font-weight: 700 !important; }}
    .intel-box {{
        background: #1e293b; border-left: 5px solid #fbbf24;
        padding: 15px; border-radius: 8px; color: #ffffff;
        margin-bottom: 25px; border: 1px solid #334155;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. HEADER ---
st.title("🛡️ NEON SENTINEL | Industrial Intelligence")
st.caption("Professional Intelligence & Clinical Data Analysis Pipeline")
st.markdown(f'<div class="intel-box">{get_intel_brief(count)}</div>', unsafe_allow_html=True)

# --- 5. DYNAMIC KPIs ---
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("GLOBAL RISK SCORE", f"{62 + random.randint(-2, 2)}/100", delta="-4")
with m2: st.metric("ACTIVE INCIDENTS", f"{8 + random.randint(0, 3)}", delta="+1")
with m3: st.metric("COPPER (LME/MT)", f"${8942 + random.randint(1,50)}", delta="+1.4%")
with m4: st.metric("AVG LEAD TIME", f"{22.4 + random.uniform(-0.5, 0.5):.1f} Days", delta="-0.8")

st.divider()

# --- 6. HIGH-DETAIL MAPPING & LOGS ---
col_left, col_right = st.columns([0.65, 0.35])

with col_left:
    st.subheader("🌐 Global Detailed Mapping")
    
    # We create the map inside the render loop to prevent 'File Error'
    def create_detailed_map():
        # Using standard OpenStreetMap for street-level detail
        m = folium.Map(location=[20, 10], zoom_start=2, tiles="OpenStreetMap")
        
        # Colorful Overlays
        folium.Rectangle(bounds=[[5, 90], [25, 120]], color="red", fill=True, fill_opacity=0.3).add_to(m)
        folium.Rectangle(bounds=[[35, -10], [55, 25]], color="green", fill=True, fill_opacity=0.2).add_to(m)
        folium.Rectangle(bounds=[[-10, 40], [10, 80]], color="blue", fill=True, fill_opacity=0.2).add_to(m)
        folium.Rectangle(bounds=[[20, -100], [50, -60]], color="orange", fill=True, fill_opacity=0.3).add_to(m)
        
        return m

    detailed_map = create_detailed_map()
    # Setting returned_objects to an empty list prevents the 'File Error' on refresh
    st_folium(detailed_map, width="100%", height=500, key="detailed_map", returned_objects=[])

with col_right:
    st.subheader("📑 SYSTEM ACTIVITY LOG")
    st.code(f"""
[{datetime.now().strftime('%H:%M:%S')}] SENTINEL_SCAN: Pulse cycle {count} initiated.
[{datetime.now().strftime('%H:%M:%S')}] TILE_SERVER: OSM standard layers verified.
[{datetime.now().strftime('%H:%M:%S')}] RESOLUTION: High-detail mapping active.
[{datetime.now().strftime('%H:%M:%S')}] ANALYTICS: Processing 432 nodes.
[{datetime.now().strftime('%H:%M:%S')}] NEURAL_LINK: Signal strength 99.2%.
[{datetime.now().strftime('%H:%M:%S')}] STATUS: Active / Optimal.
[{datetime.now().strftime('%H:%M:%S')}] TELEMETRY: Receiving data from Port Harcourt.
[{datetime.now().strftime('%H:%M:%S')}] TRACKING: Multi-color Risk Zones rendered.
    """, language="bash")
    
    st.subheader("📊 SECTOR RISK")
    st.write("Semiconductors")
    st.progress(72)
    st.write("Energy Supplies")
    st.progress(28)

# --- 7. ALERTS, NEWS & CHAT ---
st.divider()
col_alert, col_chat = st.columns([0.45, 0.55])

with col_alert:
    st.subheader("🚨 SYSTEM ALERTS")
    st.info("Pacific Route: Seasonal weather patterns may impact lead times.")
    st.warning("Rotterdam Terminal: Minor scheduled maintenance.")
    st.write("**News:** Global Logistics Index up by 0.4% this morning.")

with col_chat:
    st.subheader("💬 SENTINEL ASSISTANT")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Inquire about logistics strategy..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)

        with st.chat_message("assistant"):
            response = f"Neon Sentinel Analysis (Cycle {count}): '{prompt}'. High-detail map focus is now active. No critical blockages on current streets/routes detected."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
