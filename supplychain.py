# %%
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import requests
from datetime import datetime
import json

# %%
# --- 1. SET PAGE CONFIG & THEME ---
st.set_page_config(layout="wide", page_title="NEON SENTINEL", page_icon="🛡️")

# --- 2. THE BRANDING HEADER ---
st.title("🛡️ NEON SENTINEL | Industrial Intelligence")
st.caption("AI-Powered Global Supply Chain Intelligence Hub")
st.markdown(f"**System Status:** Operational | **Last Global Scan:** {datetime.now().strftime('%H:%M:%S')}")

# %%
# --- 3. CUSTOM GLASSMORPHISM CSS ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #0b1120; color: #f8fafc; }
    
    /* Card Styling for Metrics */
    div[data-testid="stMetric"] {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
    }
    
    /* Glowing Metric Values (Amber/Gold) */
    [data-testid="stMetricValue"] { 
        color: #fbbf24; 
        font-size: 2.2rem !important; 
        text-shadow: 0 0 12px rgba(251, 191, 36, 0.4); 
    }
    
    /* Metric Labels */
    [data-testid="stMetricLabel"] { color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; }

    /* Alert Styling */
    .stAlert { background-color: #1e293b; border: 1px solid #334155; color: #f1f5f9; border-radius: 8px; }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-thumb { background: #334155; border-radius: 10px; }

    /* Titles */
    h2, h3 { color: #f1f5f9; font-weight: 600; margin-top: 1rem; }
    </style>
    """, unsafe_allow_html=True)

st.divider()

# %%
# --- 4. API & DATA ENGINE ---
@st.cache_data(ttl=3600)
def fetch_live_data():
    data = {
        "copper": "8,942.10",
        "news": [
            {"title": "Global Freight Rates Stabilize", "src": "Logistics Weekly"},
            {"title": "Panama Canal Transit Capacity Increases", "src": "Maritime News"}
        ]
    }
    return data

live_data = fetch_live_data()

# %%
# --- 5. TOP ROW: KPI CARDS ---
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("GLOBAL RISK SCORE", "62/100", "-4", delta_color="normal")
with m2:
    st.metric("ACTIVE INCIDENTS", "8", "-2 Today", delta_color="normal")
with m3:
    st.metric("COPPER (LME/MT)", f"${live_data['copper']}", "+1.4%")
with m4:
    st.metric("AVG LEAD TIME", "22.4 Days", "-4.0 Days", delta_color="normal")

st.divider()

# %%
# --- 6. MIDDLE ROW: MAP & AGENT LOGS ---
col_left, col_right = st.columns([0.65, 0.35])

with col_left:
    st.subheader("🌐 Global Logistics Intelligence Hub")
    m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB dark_matter")

    # Port Congestion Marker
    folium.CircleMarker(
        location=[1.3521, 103.8198], # Singapore
        radius=12, color="#fbbf24", fill=True, fill_opacity=0.6,
        popup="<b>SITUATION:</b> Moderate Port Congestion"
    ).add_to(m)

    # Suez Flow Marker
    folium.CircleMarker(
        location=[30.0444, 31.2357], # Egypt
        radius=8, color="#00ffcc", fill=True, fill_opacity=0.8,
        popup="Suez Gateway: Optimized Flow"
    ).add_to(m)
    
    st_folium(m, width="100%", height=450)

with col_right:
    st.subheader("📑 SYSTEM ACTIVITY LOG")
    st.code(f"""
[{datetime.now().strftime('%H:%M')}] Sentinel-Scan: Initiated
[{datetime.now().strftime('%H:%M')}] Port Authority Data Synchronized
[{datetime.now().strftime('%H:%M')}] Anomaly Detection: 0 Critical
[{datetime.now().strftime('%H:%M')}] System Status: Optimal
    """, language="bash")
    
    st.subheader("📊 RISK EXPOSURE")
    st.write("Semiconductors & Electronics")
    st.progress(42)
    st.write("Energy & Raw Materials")
    st.progress(28)
    st.write("Global Freight Capacity")
    st.progress(15)

# %%
# --- 7. BOTTOM ROW: ALERT CENTRE & CONVERSATIONAL ASSISTANT ---
st.divider()
col_alert, col_chat = st.columns([0.45, 0.55])

with col_alert:
    st.subheader("🚨 SYSTEM ALERTS")
    st.info("Pacific Route: Seasonal weather patterns may impact lead times by 24h.")
    st.warning("Rotterdam Terminal: Minor scheduled maintenance on North Dock.")
    
    with st.expander("View Global Logistics Feed"):
        for n in live_data['news']:
            st.write(f"**{n['title']}** - *{n['src']}*")

with col_chat:
    st.subheader("💬 SENTINEL ASSISTANT")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Inquire about logistics strategy..."):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Logic for Assistant Response
        with st.chat_message("assistant"):
            response = f"Neon Sentinel analysis complete for: '{prompt}'. Current trends indicate stabilizing freight costs. I recommend monitoring the Singapore hub for any increase in transit times over the next 72 hours."
            st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
