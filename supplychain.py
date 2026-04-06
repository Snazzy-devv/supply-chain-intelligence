import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import requests
from datetime import datetime
import random
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIG & AUTO-REFRESH ---
st.set_page_config(layout="wide", page_title="NEON SENTINEL", page_icon="🛡️")

# Run the autorefresh every 20,000 milliseconds (20 seconds)
# This keeps the counter in session_state so we can cycle through data
count = st_autorefresh(interval=20000, limit=None, key="sentinel_refresh")

# --- 2. DYNAMIC CONTENT ENGINE ---
def get_dynamic_insight(index):
    insights = [
        "🔍 ANALYTIC: Predictive models suggest a 12% rise in South-China Sea congestion.",
        "💡 STRATEGY: Consider shifting 15% of buffer stock to Rotterdam terminals.",
        "⚡ ALERT: Automated clearing at Singapore Port is reducing dwell times.",
        "🌐 MACRO: Global freight indices show stabilizing container costs for Q3.",
        "🛡️ SECURITY: Cybersecurity protocols updated for all regional data-links."
    ]
    return insights[index % len(insights)]

# Dynamic KPI Logic (Simulating slight fluctuations every 20s)
def get_kpi_data():
    return {
        "risk": 60 + random.randint(-5, 5),
        "incidents": random.randint(5, 12),
        "copper": 8900 + random.uniform(10, 100),
        "lead_time": 22 + random.uniform(-1, 1)
    }

kpis = get_kpi_data()

# --- 3. BRANDING & CSS ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0b1120; color: #f8fafc; }}
    div[data-testid="stMetric"] {{
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
    }}
    .insight-box {{
        background: #1e293b;
        border-left: 5px solid #fbbf24;
        padding: 15px;
        border-radius: 5px;
        font-family: 'Courier New', Courier, monospace;
        color: #fbbf24;
        margin-bottom: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ NEON SENTINEL | Industrial Intelligence")
st.caption("AI-Powered Global Supply Chain Intelligence Hub")

# The Dynamic Intelligence Brief (Changes every 20s)
st.markdown(f'<div class="insight-box">{get_dynamic_insight(count)}</div>', unsafe_allow_html=True)

# --- 4. TOP ROW: KPI CARDS (Dynamic) ---
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("GLOBAL RISK SCORE", f"{kpis['risk']}/100", delta="-2")
with m2: st.metric("ACTIVE INCIDENTS", kpis['incidents'], delta="+1")
with m3: st.metric("COPPER (LME/MT)", f"${kpis['copper']:.2f}", delta="+0.8%")
with m4: st.metric("AVG LEAD TIME", f"{kpis['lead_time']:.1f} Days", delta="-0.5")

st.divider()

# --- 5. MIDDLE ROW: CLICKABLE MAP & LOGS ---
col_left, col_right = st.columns([0.65, 0.35])

with col_left:
    st.subheader("🌐 Global Logistics Intelligence Hub")
    m = folium.Map(
        location=[20, 10], zoom_start=2, 
        tiles="https://{s}.basemaps.cartocdn.com/rastertiles/voyager_labels_under/{z}/{x}/{y}{r}.png", 
        attr='&copy; CARTO'
    )

    # Risk Overlays
    folium.Rectangle(bounds=[[10, -20], [30, 20]], color="#ff4b4b", fill=True, fill_opacity=0.15).add_to(m)
    folium.Rectangle(bounds=[[35, -10], [55, 30]], color="#22c55e", fill=True, fill_opacity=0.15).add_to(m)
    
    # Render map and catch clicks
    map_data = st_folium(m, width="100%", height=450, returned_objects=["last_active_drawing"])

with col_right:
    st.subheader("📑 SYSTEM ACTIVITY LOG")
    st.code(f"[{datetime.now().strftime('%H:%M:%S')}] Sentinel-Scan: Refreshing...\n"
            f"[{datetime.now().strftime('%H:%M:%S')}] Pulse Count: {count}\n"
            f"[{datetime.now().strftime('%H:%M:%S')}] Latency: Optimal", language="bash")
    
    st.subheader("📊 SECTOR RISK")
    st.write("Semiconductors")
    st.progress(72)
    st.write("Energy Supplies")
    st.progress(28)

# --- 6. BOTTOM ROW: CONVERSATIONAL CHAT ---
st.divider()
if "messages" not in st.session_state:
    st.session_state.messages = []

col_chat, col_empty = st.columns([0.6, 0.4])
with col_chat:
    st.subheader("💬 SENTINEL ASSISTANT")
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Analyze specific route risks..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        with st.chat_message("assistant"):
            response = f"Neon Sentinel processed update {count}. Analyzing logistics for: '{prompt}'. I recommend monitoring Suez transit speeds given the current {kpis['risk']}% risk score."
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
