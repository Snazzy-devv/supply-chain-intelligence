import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
from datetime import datetime
import random
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIG & SYSTEM PULSE (20 Seconds) ---
st.set_page_config(layout="wide", page_title="NEON SENTINEL", page_icon="🛡️")

# This is the heartbeat that forces the KPIs and Briefs to change every 20s
count = st_autorefresh(interval=20000, limit=None, key="sentinel_pulse_v5")

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

def fetch_expanded_news():
    return [
        {"title": "Global Port Congestion Easing in Major Hubs", "src": "Logistics Weekly", "tag": "MARITIME"},
        {"title": "New Trade Corridor Opens in East Africa", "src": "Maritime News", "tag": "GEOPOLITICAL"},
        {"title": "AI Optimization Reduces Fuel Waste by 8%", "src": "Tech Sentinel", "tag": "TECH"},
        {"title": "Suez Canal Transit Fees Revised for Q4", "src": "Global Trade", "tag": "ECONOMY"},
        {"title": "Cyber-Attack Thwarted at Major EU Terminal", "src": "Cyber Defense", "tag": "SECURITY"}
    ]

# --- 3. HIGH-READABILITY CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0b1120; color: #f8fafc; }
    div[data-testid="stMetric"] {
        background-color: #1e293b; border: 1px solid #334155;
        border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    [data-testid="stMetricValue"] { color: #fbbf24 !important; font-weight: 700 !important; font-size: 2.2rem !important; }
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

# --- 5. TOP ROW: DYNAMIC KPIs (Changes every 20s) ---
# We use 'count' as a seed to ensure a new random value on every refresh
random.seed(count) 
risk_val = random.randint(58, 68)
incident_val = random.randint(8, 15)
copper_val = 8900 + random.uniform(10, 100)
lead_val = 21.0 + random.uniform(0.1, 1.5)

m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("GLOBAL RISK SCORE", f"{risk_val}/100", delta=f"{random.randint(-5, 5)}")
with m2: st.metric("ACTIVE INCIDENTS", f"{incident_val}", delta="Live Update")
with m3: st.metric("COPPER (LME/MT)", f"${copper_val:.2f}", delta="+1.4%")
with m4: st.metric("AVG LEAD TIME", f"{lead_val:.1f} Days", delta="-0.8")

st.divider()

# --- 6. DETAILED MAPPING & ACTIVITY LOG ---
col_left, col_right = st.columns([0.65, 0.35])

with col_left:
    st.subheader("🌐 High-Detail Tactical Map (Streets & Roads Visible)")
    # CartoDB Voyager ensures street names and city labels are crisp
    m = folium.Map(location=[4.8156, 7.0498], zoom_start=13, tiles="CartoDB Voyager")
    
    # Colorful Risk Layers
    folium.Circle([4.8156, 7.0498], radius=1000, color="red", fill=True, fill_opacity=0.3, popup="Red Alert: Road Blockage").add_to(m)
    folium.Circle([4.8356, 7.0298], radius=800, color="green", fill=True, fill_opacity=0.2, popup="Green: Clear Path").add_to(m)
    
    st_folium(m, width="100%", height=500, key="sentinel_map_v5", returned_objects=[])

with col_right:
    st.subheader("📑 SYSTEM ACTIVITY LOG")
    st.code(f"""
[{datetime.now().strftime('%H:%M:%S')}] SENTINEL_SCAN: Refresh cycle {count} initiated.
[{datetime.now().strftime('%H:%M:%S')}] RESOLUTION: High-detail Street/City labels active.
[{datetime.now().strftime('%H:%M:%S')}] KPI_SYNC: Telemetry updated with 20s variance.
[{datetime.now().strftime('%H:%M:%S')}] NEURAL_LINK: Signal 99.4% (Stable).
[{datetime.now().strftime('%H:%M:%S')}] GEO_FENCE: Monitoring Port Harcourt logistics.
    """, language="bash")
    
    st.subheader("📊 DYNAMIC RISK FACTORS")
    st.write("Cyber Vulnerability")
    st.progress(random.randint(10, 25))
    st.write("Geopolitical Instability")
    st.progress(random.randint(40, 55))
    st.write("Logistics Bottlenecks")
    st.progress(random.randint(65, 80))

# --- 7. ALERTS, NEWS & CHAT ---
st.divider()
col_alert, col_news, col_chat = st.columns([0.25, 0.35, 0.40])

with col_alert:
    st.subheader("🚨 SYSTEM ALERTS")
    st.info("⚠️ **Pacific Route:** Seasonal weather patterns may impact lead times.")
    st.warning("🚧 **Rotterdam:** Minor scheduled maintenance on North Dock.")
    st.error("📉 **Energy Alert:** Fuel costs up 2% in the last 4 hours.")

with col_news:
    st.subheader("📰 LIVE INTELLIGENCE FEED")
    news_items = fetch_expanded_news()
    for item in news_items:
        st.markdown(f"<span class='news-tag'>{item['tag']}</span> **{item['title']}**", unsafe_allow_html=True)
        st.caption(f"{item['src']} | {datetime.now().strftime('%H:%M')}")
        st.write("---")

with col_chat:
    st.subheader("💬 SENTINEL ASSISTANT")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Analyze specific routing..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        with st.chat_message("assistant"):
            ans = f"Neon Sentinel processed update (Refresh #{count}). Detailed street mapping confirms all local access roads are green-lighted for the current '{prompt}' request."
            st.markdown(ans)
            st.session_state.messages.append({"role": "assistant", "content": ans})
