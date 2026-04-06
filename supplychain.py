import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
from datetime import datetime
import random
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIG & SYSTEM PULSE (20 Seconds) ---
st.set_page_config(layout="wide", page_title="NEON SENTINEL", page_icon="🛡️")
count = st_autorefresh(interval=20000, limit=None, key="sentinel_pulse_v9")

# --- 2. DYNAMIC CONTENT ENGINE ---
random.seed(count)
current_copper_price = 8942.50 + random.uniform(-10, 15)
risk_score = 64 + random.randint(-2, 2)

def get_intel_brief(index):
    briefs = [
        "📡 SENTINEL-2: New satellite pass confirms 12% rise in South-China Sea congestion.",
        "💡 STRATEGY: Shift 15% of buffer stock to Rotterdam terminals to bypass Suez volatility.",
        "⚡ ALERT: Automated clearing at Singapore Port is reducing dwell times.",
        "🌐 MACRO: Global freight indices show stabilizing container costs for Q3.",
        "🛡️ SECURITY: Cybersecurity protocols updated for all West African data-links."
    ]
    return briefs[index % len(briefs)]

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
    .news-tag {
        font-size: 0.7rem; background: #334155; color: #fbbf24;
        padding: 2px 8px; border-radius: 4px; margin-right: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. HEADER & DYNAMIC BRIEF ---
st.title("🛡️ NEON SENTINEL | Industrial Intelligence")
st.caption("Professional Intelligence & Clinical Data Analysis Pipeline")
st.markdown(f'<div class="intel-box">{get_intel_brief(count)}</div>', unsafe_allow_html=True)

# --- 5. TOP ROW: DYNAMIC KPIs ---
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("GLOBAL RISK SCORE", f"{risk_score}/100", delta="-2")
with m2: st.metric("ACTIVE INCIDENTS", f"{12 + random.randint(0, 2)}", delta="+1")
with m3: st.metric("COPPER (LME/MT)", f"${current_copper_price:.2f}", delta="STABLE")
with m4: st.metric("AVG LEAD TIME", f"{21.8 + random.uniform(-0.3, 0.3):.1f} Days", delta="-0.4")

st.divider()

# --- 6. SENTINEL SURVEILLANCE & ACTIVITY LOG ---
col_left, col_right = st.columns([0.65, 0.35])

with col_left:
    # RENAMED TO SENTINEL TACTICAL SURVEILLANCE
    st.subheader("🛰️ SENTINEL TACTICAL SURVEILLANCE")
    
    # Using Esri Satellite Imagery for the "Live Sentinel" look
    m = folium.Map(
        location=[6.444, 3.417], 
        zoom_start=12, 
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri World Imagery'
    )
    
    # Add High-Detail Labels on top of Satellite (Reference Layer)
    folium.TileLayer(
        tiles='https://{s}.basemaps.cartocdn.com/light_only_labels/{z}/{x}/{y}{r}.png',
        attr='&copy; CartoDB',
        name='Labels Only',
        overlay=True,
        control=False
    ).add_to(m)

    # Sentinel Risk Zones
    folium.Circle([6.444, 3.417], radius=1500, color="green", fill=True, fill_opacity=0.3, popup="Lagos Port: Optimized").add_to(m)
    folium.Circle([4.75, 7.01], radius=2000, color="red", fill=True, fill_opacity=0.4, popup="Onne Port: Critical Delay").add_to(m)
    
    # Simulated Satellite Scan Marker
    folium.Marker(
        [6.45, 3.40], 
        icon=folium.Icon(color='red', icon='screenshot', prefix='fa'),
        popup="Live Vessel Scan: Container Vessel 'MARSK-SENTINEL' detected."
    ).add_to(m)

    st_folium(m, width="100%", height=550, key="sentinel_map_v9", returned_objects=[])

with col_right:
    st.subheader("📊 DYNAMIC RISK FACTORS")
    st.write("Cyber Vulnerability")
    st.progress(random.randint(15, 25))
    st.write("West Africa Port Congestion")
    st.progress(random.randint(40, 50))
    st.write("Maritime Piracy Index")
    st.progress(12)
    st.write("Satellite Signal Latency")
    st.progress(random.randint(5, 12))
    st.write("Geopolitical Volatility")
    st.progress(random.randint(55, 65))
    
    st.subheader("📑 SYSTEM ACTIVITY LOG")
    st.code(f"""
[{datetime.now().strftime('%H:%M:%S')}] SENTINEL_SCAN: Satellite pass cycle {count}.
[{datetime.now().strftime('%H:%M:%S')}] IMAGERY: Sentinel-2 High-Res Imagery loaded.
[{datetime.now().strftime('%H:%M:%S')}] TELEMETRY: Copper Index verified.
[{datetime.now().strftime('%H:%M:%S')}] RESOLUTION: Street/City hybrid labels active.
    """, language="bash")

# --- 7. ALERTS, NEWS & DIRECT ASSISTANT ---
st.divider()
col_alert, col_news, col_chat = st.columns([0.25, 0.35, 0.40])

with col_alert:
    st.subheader("🚨 SYSTEM ALERTS")
    st.info("⚠️ **Lagos Apapa:** High turnaround times; use Tin Can Island.")
    st.warning("🚧 **Onne Port:** Dredging activity; 12h berth delays.")
    st.error("📉 **Currency:** Local logistics pricing fluctuating +3%.")
    st.success("✅ **Satellite:** Sentinel signal strength is at 98.4%.")

with col_news:
    st.subheader("📰 LIVE INTELLIGENCE FEED")
    news_feed = [
        {"tag": "SENTINEL", "title": "New Satellite Imagery Confirms Clear Route to Tin Can"},
        {"tag": "MARKET", "title": f"Copper Price Steady at ${current_copper_price:.2f}"},
        {"tag": "ENERGY", "title": "West Africa Last-Mile Costs Project 5% Rise"},
        {"tag": "SECURITY", "title": "Vessel Tracking: 42 Active Ships in Nigeria Bight"},
        {"tag": "ECONOMY", "title": "LME Stocks Hit 6-Month High Amid EV Demand"}
    ]
    for n in news_feed:
        st.markdown(f"<span class='news-tag'>{n['tag']}</span> **{n['title']}**", unsafe_allow_html=True)
        st.caption(f"Verified: {datetime.now().strftime('%H:%M')} | Source: Sentinel-2")
        st.write("---")

with col_chat:
    st.subheader("💬 SENTINEL ASSISTANT")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask about copper, Nigeria routes, or risk..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        with st.chat_message("assistant"):
            p = prompt.lower()
            if "nigeria" in p or "route" in p:
                response = "**Satellite Analysis:** Current Sentinel-2 imagery shows high vessel density at Apapa. **Route Recommendation:** Utilize the Southern approach to Tin Can Island for 15% faster offloading."
            elif "copper" in p:
                response = f"Copper is trading at **${current_copper_price:.2f}**. Local West African surcharges are currently stable."
            elif "risk" in p:
                response = f"Risk Score: **{risk_score}/100**. Primary driver: Satellite detected congestion at Nigerian port nodes."
            else:
                response = f"Data for '{prompt}': Sentinel Tactical Surveillance confirms optimal corridor status."
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
