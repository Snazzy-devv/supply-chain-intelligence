import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import requests
from datetime import datetime
import random
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIG & AUTO-REFRESH (20 Seconds) ---
st.set_page_config(layout="wide", page_title="NEON SENTINEL", page_icon="🛡️")
# silent refresh to update dynamic text and KPI wiggles
count = st_autorefresh(interval=20000, limit=None, key="sentinel_pulse")

# --- 2. DYNAMIC CONTENT ENGINE ---
NEWS_API_KEY = st.secrets.get("NEWS_API_KEY") or "YOUR_NEWSAPI_KEY_HERE"

@st.cache_data(ttl=1800)
def fetch_dynamic_news():
    try:
        url = f"https://newsapi.org/v2/everything?q=logistics+supply+chain&language=en&sortBy=publishedAt&pageSize=4&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            return [{"title": a["title"], "src": a["source"]["name"], "url": a["url"]} for a in articles]
    except:
        return [{"title": "Global Trade Route Analysis Active", "src": "Sentinel Internal", "url": "#"}]

def get_intel_brief(index):
    briefs = [
        "📡 ANALYTIC: Predictive models suggest a 12% rise in South-China Sea congestion.",
        "💡 STRATEGY: Consider shifting 15% of buffer stock to Rotterdam terminals.",
        "⚡ ALERT: Automated clearing at Singapore Port is reducing dwell times.",
        "🌐 MACRO: Global freight indices show stabilizing container costs for Q3.",
        "🛡️ SECURITY: Cybersecurity protocols updated for all regional data-links."
    ]
    return briefs[index % len(briefs)]

# --- 3. HIGH-READABILITY CSS ---
st.markdown(f"""
    <style>
    /* Main Background */
    .stApp {{ background-color: #0b1120; color: #f8fafc; }}
    
    /* KPI Metric Cards - High Contrast */
    div[data-testid="stMetric"] {{
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }}
    
    /* Metric Value - Bright Amber for Readability */
    [data-testid="stMetricValue"] {{ 
        color: #fbbf24 !important; 
        font-size: 2.2rem !important; 
        font-weight: 700 !important;
    }}
    
    /* Metric Label - Light Grey/White */
    [data-testid="stMetricLabel"] {{ 
        color: #e2e8f0 !important; 
        text-transform: uppercase; 
        letter-spacing: 1px;
    }}

    /* Intelligence Brief Box */
    .intel-box {{
        background: #1e293b;
        border-left: 5px solid #fbbf24;
        padding: 15px;
        border-radius: 8px;
        font-family: 'Inter', sans-serif;
        color: #ffffff;
        font-size: 1.1rem;
        margin-bottom: 25px;
        border: 1px solid #334155;
    }}

    /* Alerts and News text */
    .stAlert p, .stMarkdown p {{ color: #f8fafc !important; }}
    
    /* Chat history contrast */
    .stChatMessage {{ background-color: #1e293b !important; border: 1px solid #334155 !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. HEADER & DYNAMIC BRIEF ---
st.title("🛡️ NEON SENTINEL | Industrial Intelligence")
st.caption("AI-Powered Global Supply Chain Intelligence Hub")
st.markdown(f'<div class="intel-box">{get_intel_brief(count)}</div>', unsafe_allow_html=True)

# --- 5. TOP ROW: DYNAMIC KPIs ---
# Values fluctuate slightly every 20s to simulate live data
risk_val = 62 + random.randint(-2, 2)
lead_time = 22.4 + random.uniform(-0.5, 0.5)

m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("GLOBAL RISK SCORE", f"{risk_val}/100", delta="-4")
with m2: st.metric("ACTIVE INCIDENTS", "8", delta="-2 Today")
with m3: st.metric("COPPER (LME/MT)", f"${8942 + random.randint(1,50)}", delta="+1.4%")
with m4: st.metric("AVG LEAD TIME", f"{lead_time:.1f} Days", delta="-0.8")

st.divider()

# --- 6. MIDDLE ROW: CLICKABLE MAP & LOGS ---
col_left, col_right = st.columns([0.65, 0.35])

with col_left:
    st.subheader("🌐 Global Logistics Intelligence Hub")
    m = folium.Map(
        location=[20, 10], zoom_start=2, 
        tiles="https://{s}.basemaps.cartocdn.com/rastertiles/voyager_labels_under/{z}/{x}/{y}{r}.png", 
        attr='&copy; CARTO'
    )
    # Colorful Risk Zones
    folium.Rectangle(bounds=[[10, -20], [30, 20]], color="#ff4b4b", fill=True, fill_opacity=0.15, popup="High Risk Area").add_to(m)
    folium.Rectangle(bounds=[[35, -10], [55, 30]], color="#22c55e", fill=True, fill_opacity=0.15, popup="Optimized Corridor").add_to(m)
    
    # Click interaction
    map_data = st_folium(m, width="100%", height=450, returned_objects=["last_active_drawing"])
    if map_data and map_data.get("last_active_drawing"):
        st.toast(f"📍 Sentinel focus: {map_data['last_active_drawing']['geometry']['coordinates']}")

with col_right:
    st.subheader("📑 SYSTEM ACTIVITY LOG")
    st.code(f"[{datetime.now().strftime('%H:%M:%S')}] Sentinel-Scan: Refreshing...\n"
            f"[{datetime.now().strftime('%H:%M:%S')}] Pulse Count: {count}\n"
            f"[{datetime.now().strftime('%H:%M:%S')}] Neural-Link: Stable", language="bash")
    
    st.subheader("📊 SECTOR RISK")
    st.write("Semiconductors")
    st.progress(72)
    st.write("Energy Supplies")
    st.progress(28)

# --- 7. BOTTOM ROW: ALERTS, NEWS & CHAT ---
st.divider()
col_alert, col_chat = st.columns([0.45, 0.55])

with col_alert:
    st.subheader("🚨 SYSTEM ALERTS")
    st.info("Pacific Route: Seasonal weather patterns may impact lead times by 24h.")
    st.warning("Rotterdam Terminal: Minor scheduled maintenance on North Dock.")
    
    st.subheader("📰 LIVE LOGISTICS NEWS")
    news_feed = fetch_dynamic_news()
    for n in news_feed:
        st.markdown(f"**{n['title']}**")
        st.caption(f"Source: {n['src']} | [Read Article]({n['url']})")
        st.write("---")

with col_chat:
    st.subheader("💬 SENTINEL ASSISTANT")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Conversational Input
    if prompt := st.chat_input("Inquire about logistics strategy..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)

        with st.chat_message("assistant"):
            response = f"Neon Sentinel analysis (Refresh #{count}) for: '{prompt}'. Strategic routing remains stable. I suggest a 5% buffer on West Coast arrivals due to seasonal drift."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
