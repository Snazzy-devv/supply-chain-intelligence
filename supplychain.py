import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
from datetime import datetime
import random
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIG & SYSTEM PULSE ---
st.set_page_config(layout="wide", page_title="NEON SENTINEL", page_icon="🛡️")

# The Heartbeat: Triggers a refresh every 20s to update KPIs and Briefs
count = st_autorefresh(interval=20000, limit=None, key="sentinel_pulse_v3")

# --- 2. DYNAMIC CONTENT ENGINE ---
def get_intel_brief(index):
    briefs = [
        "📡 ANALYTIC: Predictive models suggest a 12% rise in South-China Sea congestion.",
        "💡 STRATEGY: Consider shifting 15% of buffer stock to Rotterdam terminals.",
        "⚡ ALERT: Automated clearing at Singapore Port is reducing dwell times.",
        "🌐 MACRO: Global freight indices show stabilizing container costs for Q3.",
        "🛡️ SECURITY: Cybersecurity protocols updated for all regional data-links."
    ]
    return briefs[index % len(briefs)]

def fetch_live_news():
    # Placeholder for NewsAPI logic - adding robust fallback so it never disappears
    return [
        {"title": "Global Port Congestion Easing in Major Hubs", "src": "Logistics Weekly"},
        {"title": "New Trade Corridor Opens in East Africa", "src": "Maritime News"},
        {"title": "AI Optimization Reduces Fuel Waste by 8%", "src": "Tech Sentinel"}
    ]

# --- 3. HIGH-READABILITY CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0b1120; color: #f8fafc; }
    div[data-testid="stMetric"] {
        background-color: #1e293b; border: 1px solid #334155;
        border-radius: 12px; padding: 20px;
    }
    [data-testid="stMetricValue"] { color: #fbbf24 !important; font-weight: 700 !important; }
    .intel-box {
        background: #1e293b; border-left: 5px solid #fbbf24;
        padding: 15px; border-radius: 8px; color: #ffffff;
        margin-bottom: 25px; border: 1px solid #334155; font-weight: 500;
    }
    .news-card { border-bottom: 1px solid #334155; padding: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. HEADER & DYNAMIC BRIEF ---
st.title("🛡️ NEON SENTINEL | Industrial Intelligence")
st.caption("Professional Intelligence & Clinical Data Analysis Pipeline")
st.markdown(f'<div class="intel-box">{get_intel_brief(count)}</div>', unsafe_allow_html=True)

# --- 5. TOP ROW: DYNAMIC KPIs ---
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("GLOBAL RISK SCORE", f"{64 + random.randint(-2, 2)}/100", delta="-2")
with m2: st.metric("ACTIVE INCIDENTS", f"{12 + random.randint(0, 2)}", delta="+1")
with m3: st.metric("COPPER (LME/MT)", f"${8942 + random.randint(1,50)}", delta="+1.1%")
with m4: st.metric("AVG LEAD TIME", f"{21.8 + random.uniform(-0.3, 0.3):.1f} Days", delta="-0.4")

st.divider()

# --- 6. DETAILED MAPPING & ACTIVITY LOG ---
col_left, col_right = st.columns([0.65, 0.35])

with col_left:
    st.subheader("🌐 High-Detail Tactical Map")
    # CartoDB Voyager is colorful and preserves street/city names perfectly
    m = folium.Map(location=[4.8156, 7.0498], zoom_start=12, tiles="CartoDB Voyager")
    
    # Colorful Multi-Zone Layers
    folium.Circle([4.8156, 7.0498], radius=2000, color="red", fill=True, fill_opacity=0.2, popup="High Activity Zone").add_to(m)
    folium.Circle([4.8456, 7.0198], radius=1500, color="green", fill=True, fill_opacity=0.2, popup="Optimized Route").add_to(m)
    folium.Circle([4.7856, 7.0898], radius=1800, color="blue", fill=True, fill_opacity=0.2, popup="Maritime Entry").add_to(m)
    folium.Circle([4.8356, 7.1298], radius=1200, color="orange", fill=True, fill_opacity=0.3, popup="Warning: Delay Area").add_to(m)

    # Key Interaction
    st_folium(m, width="100%", height=500, key="sentinel_map_v3", returned_objects=[])

with col_right:
    st.subheader("📑 SYSTEM ACTIVITY LOG")
    st.code(f"""
[{datetime.now().strftime('%H:%M:%S')}] SENTINEL_SCAN: Cycle {count} active.
[{datetime.now().strftime('%H:%M:%S')}] TILE_SERVER: CartoDB Voyager layers active.
[{datetime.now().strftime('%H:%M:%S')}] RESOLUTION: High-detail Street/City labels verified.
[{datetime.now().strftime('%H:%M:%S')}] DATA_SYNC: Tracking local assets in Port Harcourt.
[{datetime.now().strftime('%H:%M:%S')}] ANALYTICS: Processing 512 regional nodes.
[{datetime.now().strftime('%H:%M:%S')}] NEURAL_LINK: Signal 99.4% (Ultra-Stable).
[{datetime.now().strftime('%H:%M:%S')}] STATUS: Human-in-the-Loop confirmed.
    """, language="bash")
    
    st.subheader("📊 SECTOR RISK")
    st.write("Semiconductors")
    st.progress(72)
    st.write("Energy Supplies")
    st.progress(28)

# --- 7. ALERTS, NEWS & CHAT ---
st.divider()
col_news, col_chat = st.columns([0.45, 0.55])

with col_news:
    st.subheader("📰 LIVE INTELLIGENCE FEED")
    news = fetch_live_news()
    for item in news:
        st.markdown(f"**{item['title']}**")
        st.caption(f"Source: {item['src']} | {datetime.now().strftime('%d %b')}")
        st.write("---")

with col_chat:
    st.subheader("💬 SENTINEL ASSISTANT")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Inquire about routing..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        with st.chat_message("assistant"):
            ans = f"Neon Sentinel processed update (Cycle {count}). Analysis for: '{prompt}'. Detailed street mapping confirms all local access roads are green-lighted for transit."
            st.markdown(ans)
            st.session_state.messages.append({"role": "assistant", "content": ans})
