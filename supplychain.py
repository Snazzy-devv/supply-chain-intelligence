import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import requests
from datetime import datetime

# --- 1. CONFIG & THEME ---
st.set_page_config(layout="wide", page_title="NEON SENTINEL", page_icon="🛡️")

# --- 2. DYNAMIC NEWS ENGINE ---
NEWS_API_KEY = st.secrets.get("NEWS_API_KEY") or "YOUR_NEWSAPI_KEY_HERE"

@st.cache_data(ttl=1800)
def fetch_dynamic_news():
    try:
        url = f"https://newsapi.org/v2/everything?q=logistics+supply+chain&language=en&sortBy=publishedAt&pageSize=5&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            return [{"title": a["title"], "src": a["source"]["name"], "url": a["url"]} for a in articles]
    except Exception:
        pass
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
    }}
    [data-testid="stMetricValue"] {{ color: #fbbf24; text-shadow: 0 0 12px rgba(251, 191, 36, 0.4); }}
    .stAlert {{ background-color: #1e293b; border: 1px solid #334155; border-radius: 8px; }}
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ NEON SENTINEL | Industrial Intelligence")
st.caption("AI-Powered Global Supply Chain Intelligence Hub")

# --- 4. THE INTERACTIVE MAP LOGIC ---
col_left, col_right = st.columns([0.65, 0.35])

with col_left:
    st.subheader("🌐 Interactive Intelligence Hub")
    
    # Base Map with a balanced colorful-dark style
    m = folium.Map(
        location=[20, 10], zoom_start=2, 
        tiles="https://{s}.basemaps.cartocdn.com/rastertiles/voyager_labels_under/{z}/{x}/{y}{r}.png", 
        attr='&copy; OpenStreetMap'
    )

    # ADDING COLORFUL RISK ZONES (Visualizing Green/Red areas)
    # Red Zone (High Risk Area example)
    folium.Rectangle(
        bounds=[[10, -20], [30, 20]],
        color="#ff4b4b", fill=True, fill_color="#ff4b4b", fill_opacity=0.2,
        popup="HIGH RISK ZONE: Central Atlantic"
    ).add_to(m)

    # Green Zone (Optimized Area example)
    folium.Rectangle(
        bounds=[[35, -10], [55, 30]],
        color="#22c55e", fill=True, fill_color="#22c55e", fill_opacity=0.2,
        popup="OPTIMIZED ZONE: European Corridor"
    ).add_to(m)

    # Glow Markers
    folium.CircleMarker(location=[1.3521, 103.8198], radius=10, color="#ff007f", fill=True, popup="Singapore").add_to(m)
    folium.CircleMarker(location=[30.0444, 31.2357], radius=10, color="#00f2ff", fill=True, popup="Suez").add_to(m)

    # CATCH THE CLICK: This is the key for interactivity
    # returned_objects=["last_active_drawing"] makes the map "clickable"
    map_data = st_folium(m, width="100%", height=450, returned_objects=["last_active_drawing"])

    # Handle the Click Interaction
    if map_data and map_data.get("last_active_drawing"):
        clicked_location = map_data["last_active_drawing"]["geometry"]["coordinates"]
        st.info(f"📍 Sentinel focus redirected to Coordinates: {clicked_location}")
        # In a full build, you could use this coordinate to trigger a specific country search

with col_right:
    st.subheader("📑 SYSTEM ACTIVITY LOG")
    st.code(f"[{datetime.now().strftime('%H:%M')}] Sentinel-Scan: Initiated\n[{datetime.now().strftime('%H:%M')}] Mapping colorful risk zones...\n[{datetime.now().strftime('%H:%M')}] Click-listener: Active", language="bash")
    
    st.subheader("📊 RISK EXPOSURE")
    st.write("Semiconductors")
    st.progress(72)
    st.write("Energy Supplies")
    st.progress(28)

# --- 5. BOTTOM ROW: DYNAMIC ALERTS & CONVERSATIONAL CHAT ---
st.divider()
col_alert, col_chat = st.columns([0.45, 0.55])

with col_alert:
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

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("How can I assist with your logistics strategy?"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            response = f"Neon Sentinel processed: '{prompt}'. Strategic analysis suggests diversifying your Tier-2 suppliers in Southeast Asia to mitigate current port congestion trends."
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})s
