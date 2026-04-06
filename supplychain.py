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
st.caption("AI-Powered Global Supply Chain Watchdog")
st.markdown(f"**System Status:** Operational | **Last Global Scan:** {datetime.now().strftime('%H:%M:%S')}")


# %%
# --- 3. CUSTOM GLASSMORPHISM CSS (Matching your Screenshot) ---
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
    .stAlert { background-color: #1e293b; border: 1px solid #ef4444; color: #fca5a5; border-radius: 8px; }
    
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
# Replace these strings with your actual keys or use st.secrets / .env
NEWS_KEY = "NEWS_API_KEY"
ALPHA_KEY = "ALPHA_VANTAGE_KEY"

@st.cache_data(ttl=3600)
def fetch_live_data():
    # Mocking for immediate visual success; replace with your actual request calls
    data = {
        "copper": "8,942.10",
        "news": [
            {"title": "Suez Canal Congestion Increases", "src": "Logistics Insider"},
            {"title": "Lithium Prices Stabilize in Q1", "src": "Market Watch"}
        ]
    }
    return data

live_data = fetch_live_data()



# %%
# --- 5. TOP ROW: KPI CARDS (THE "PULSE") ---
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("GLOBAL RISK SCORE", "78/100", "High", delta_color="inverse")
with m2:
    st.metric("ACTIVE DISRUPTIONS", "14", "+3 Today", delta_color="inverse")
with m3:
    st.metric("COPPER (LME/MT)", f"${live_data['copper']}", "+1.4%")
with m4:
    st.metric("AVG LEAD TIME", "26.4 Days", "+4.2 Days", delta_color="inverse")

st.divider()


# %%
# --- 6. MIDDLE ROW: MAP & AGENT LOGS ---
col_left, col_right = st.columns([0.65, 0.35])

with col_left:
    st.subheader("🌐 Global Logistics War-Room")
    # Neon Dark Map Style
    m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB dark_matter")


# %%
    # Adding a Glowing Pulse for a Critical Risk Zone
    folium.CircleMarker(
        location=[1.3521, 103.8198], # Singapore
        radius=15, color="#ff0033", fill=True, fill_opacity=0.6,
        popup="<b>CRITICAL:</b> Port Congestion Level 9"
    ).add_to(m)



# %%
    # Adding a Healthy Supplier
    folium.CircleMarker(
        location=[30.0444, 31.2357], # Egypt
        radius=8, color="#00ffcc", fill=True, fill_opacity=0.8,
        popup="Suez Gateway: Flowing"
    ).add_to(m)
    
    st_folium(m, width="100%", height=450)

with col_right:
    st.subheader("📑 AGENT ACTIVITY LOG")
    st.code(f"""
[{datetime.now().strftime('%H:%M')}] Sentinel-Scan: Initiated
[{datetime.now().strftime('%H:%M')}] NewsAPI: 2 Critical Hits
[{datetime.now().strftime('%H:%M')}] AlphaVantage: Price Spike (Cu)
[{datetime.now().strftime('%H:%M')}] OpenRouter: Analysis Ready
    """, language="bash")
    
    st.subheader("📊 RISK EXPOSURE")
    # Simple Progress Bars to mimic the "Efficiency" bars in your screenshot
    st.write("Raw Materials (Steel/Cu)")
    st.progress(85)
    st.write("Electronics (Semiconductors)")
    st.progress(42)
    st.write("Finished Goods Logistics")
    st.progress(66)




# %%
# --- 7. BOTTOM ROW: ALERT CENTRE & AI COMMANDER ---
st.divider()
col_alert, col_chat = st.columns([0.5, 0.5])

with col_alert:
    st.subheader("🚨 ALERT CENTRE")
    st.error("Ijaw Palm Collective - Output dropped to 72%.")
    st.warning("Supply Chain: Lead time deviation exceeded 15% threshold in Asia-Pacific.")
    
    with st.expander("View Live News Feed"):
        for n in live_data['news']:
            st.write(f"**{n['title']}** - *{n['src']}*")

with col_chat:
    st.subheader("💬 AI COMMANDER (OpenRouter)")
    if prompt := st.chat_input("Ask Sentinel for a strategy..."):
        with st.chat_message("assistant"):
            # This is where your OpenRouter logic would process the prompt
            st.write(f"**SENTINEL ANALYSIS:** '{prompt}' detected. Analyzing live commodity spikes and port congestion... I recommend rerouting 15% of Tier-1 inventory to your Texas hub to avoid the Singapore bottleneck.")




