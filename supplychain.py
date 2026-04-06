import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import requests
from datetime import datetime

# --- 1. CONFIG & THEME ---
st.set_page_config(layout="wide", page_title="NEON SENTINEL", page_icon="🛡️")

# --- 2. DYNAMIC NEWS ENGINE ---
# Get your free key at newsapi.org
NEWS_API_KEY = st.secrets.get("NEWS_API_KEY") or "YOUR_NEWSAPI_KEY_HERE"

@st.cache_data(ttl=1800) # Refresh news every 30 mins
def fetch_dynamic_news():
    try:
        # Searching for global logistics and supply chain headlines
        url = f"https://newsapi.org/v2/everything?q=logistics+supply+chain&language=en&sortBy=publishedAt&pageSize=5&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            return [{"title": a["title"], "src": a["source"]["name"], "url": a["url"]} for a in articles]
    except Exception:
        pass
    # Fallback if API fails or key is missing
    return [{"title": "Global Trade Routes Stabilizing", "src": "Maritime Daily", "url": "#"}]

# --- 3. CUSTOM BRANDING & CSS ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0b1120; color: #f8fafc; }}
    div[data-testid="stMetric"] {{
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
    }}
    [data-testid="stMetricValue"] {{ 
        color: #fbbf24; 
        font-size: 2.2rem !important; 
        text-shadow: 0 0 12px rgba(251, 191, 36, 0.4); 
    }}
    [data-testid="stMetricLabel"] {{ color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; }}
    .stAlert {{ background-color: #1e293b; border: 1px solid #334155; color: #f1f5f9; border-radius: 8px; }}
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ NEON SENTINEL | Industrial Intelligence")
st.caption("AI-Powered Global Supply Chain Intelligence Hub")
st.markdown(f"**System Status:** <span style='color:#00ffcc;'>Operational</span> | **Last Global Scan:** {datetime.now().strftime('%H:%M:%S')}", unsafe_allow_html=True)
st.divider()

# --- 4. TOP ROW: KPI CARDS ---
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("GLOBAL RISK SCORE", "62/100", "-4", delta_color="normal")
with m2: st.metric("ACTIVE INCIDENTS", "8", "-2 Today", delta_color="normal")
with m3: st.metric("COPPER (LME/MT)", "$8,942.10", "+1.4%")
with m4: st.metric("AVG LEAD TIME", "22.4 Days", "-4.0 Days", delta_color="normal")

# --- 5. MIDDLE ROW: VIBRANT NEON MAP & LOGS ---
col_left, col_right = st.columns([0.65, 0.35])

with col_left:
    st.subheader("🌐 Global Logistics Intelligence Hub")
    m = folium.Map(
        location=[20, 10], zoom_start=2, 
        tiles="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png", 
        attr='&copy; CARTO'
    )

    # Neon Markers (Glow Effect)
    # Singapore - Pink
    folium.CircleMarker(location=[1.3521, 103.8198], radius=12, color="#ff007f", fill=True, fill_opacity=0.4).add_to(m)
    folium.CircleMarker(location=[1.3521, 103.8198], radius=4, color="#ff007f", fill=True, fill_opacity=1, popup="Singapore: Active").add_to(m)
    # Suez - Cyan
    folium.CircleMarker(location=[30.0444, 31.2357], radius=10, color="#00f2ff", fill=True, fill_opacity=0.3).add_to(m)
    folium.CircleMarker(location=[30.0444, 31.2357], radius=3, color="#00f2ff", fill=True, fill_opacity=1, popup="Suez: Optimal").add_to(m)

    st_folium(m, width="100%", height=450, returned_objects=[])

with col_right:
    st.subheader("📑 SYSTEM ACTIVITY LOG")
    st.code(f"[{datetime.now().strftime('%H:%M')}] Sentinel-Scan: Initiated\n[{datetime.now().strftime('%H:%M')}] Neural-Link: Connected\n[{datetime.now().strftime('%H:%M')}] Status: High Clarity", language="bash")
    
    st.subheader("📊 RISK EXPOSURE")
    st.write("Semiconductors")
    st.progress(72)
    st.write("Energy Supplies")
    st.progress(28)

# --- 6. BOTTOM ROW: DYNAMIC ALERTS & CONVERSATIONAL CHAT ---
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
    if prompt := st.chat_input("How can I assist with your logistics strategy?"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            # You can replace this with your actual LLM call logic
            response = f"Neon Sentinel processed: '{prompt}'. Strategic analysis suggests diversifying your Tier-2 suppliers in Southeast Asia to mitigate current port congestion trends."
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
