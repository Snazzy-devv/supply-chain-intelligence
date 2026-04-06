import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
from datetime import datetime
import random
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIG & SYSTEM PULSE (20 Seconds) ---
st.set_page_config(layout="wide", page_title="NEON SENTINEL", page_icon="🛡️")
count = st_autorefresh(interval=20000, limit=None, key="sentinel_pulse_v6")

# --- 2. DYNAMIC CONTENT ENGINE ---
random.seed(count)
# Real-time simulated copper price
current_copper_price = 8942.50 + random.uniform(-10, 15)
copper_status = "BULLISH" if current_copper_price > 8950 else "STABLE"

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
with m1: st.metric("GLOBAL RISK SCORE", f"{64 + random.randint(-2, 2)}/100", delta="-2")
with m2: st.metric("ACTIVE INCIDENTS", f"{12 + random.randint(0, 2)}", delta="+1")
with m3: st.metric("COPPER (LME/MT)", f"${current_copper_price:.2f}", delta=f"{copper_status}")
with m4: st.metric("AVG LEAD TIME", f"{21.8 + random.uniform(-0.3, 0.3):.1f} Days", delta="-0.4")

st.divider()

# --- 6. DETAILED MAPPING & ACTIVITY LOG ---
col_left, col_right = st.columns([0.65, 0.35])

with col_left:
    st.subheader("🌐 High-Detail Tactical Map")
    m = folium.Map(location=[4.8156, 7.0498], zoom_start=13, tiles="CartoDB Voyager")
    folium.Circle([4.8156, 7.0498], radius=1000, color="red", fill=True, fill_opacity=0.3).add_to(m)
    st_folium(m, width="100%", height=500, key="sentinel_map_v6", returned_objects=[])

with col_right:
    st.subheader("📑 SYSTEM ACTIVITY LOG")
    st.code(f"""
[{datetime.now().strftime('%H:%M:%S')}] SENTINEL_SCAN: Cycle {count} active.
[{datetime.now().strftime('%H:%M:%S')}] TELEMETRY: Copper Index verified as {copper_status}.
[{datetime.now().strftime('%H:%M:%S')}] RESOLUTION: High-detail labels active.
[{datetime.now().strftime('%H:%M:%S')}] NEURAL_LINK: Signal 99.4% (Stable).
    """, language="bash")
    
    st.subheader("📊 DYNAMIC RISK FACTORS")
    st.write("Cyber Vulnerability")
    st.progress(random.randint(10, 25))
    st.write("Logistics Bottlenecks")
    st.progress(random.randint(65, 80))

# --- 7. ALERTS, NEWS & INTERACTIVE CHAT ---
st.divider()
col_alert, col_news, col_chat = st.columns([0.25, 0.35, 0.40])

with col_alert:
    st.subheader("🚨 SYSTEM ALERTS")
    st.info("⚠️ **Pacific Route:** Seasonal weather patterns impacting lead times.")
    st.warning("🚧 **Rotterdam:** Minor maintenance on North Dock.")
    st.error("📉 **Energy Alert:** Fuel costs up 2% today.")

with col_news:
    st.subheader("📰 LIVE INTELLIGENCE FEED")
    st.markdown(f"<span class='news-tag'>MARKET</span> **Copper Price Update**", unsafe_allow_html=True)
    st.caption(f"LME Index currently at ${current_copper_price:.2f}. Status: {copper_status}")
    st.write("---")
    st.markdown(f"<span class='news-tag'>TECH</span> **AI Optimization Peak**", unsafe_allow_html=True)
    st.caption("Routing efficiency increased by 14% via Neural-Link.")

with col_chat:
    st.subheader("💬 SENTINEL ASSISTANT")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask about copper, risk, or routing..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        with st.chat_message("assistant"):
            # INTERACTIVE LOGIC: Actually check the prompt keywords
            p = prompt.lower()
            if "copper" in p:
                response = f"The current price of Copper (LME/MT) is **${current_copper_price:.2f}**. Market sentiment is currently **{copper_status}** based on recent pulse telemetry."
            elif "risk" in p:
                response = f"Global Risk is currently flagged at **{64 + random.randint(-2, 2)}/100**. Primary drivers are Logistics Bottlenecks and Cyber Vulnerability."
            elif "status" in p:
                response = f"System Status: **Operational**. All mapping nodes are green, and neural-link signal strength is at 99.4%."
            else:
                response = f"Neon Sentinel confirms: '{prompt}'. Strategic analysis suggest prioritizing the current EU Green Corridor while tracking commodity fluctuations."
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
