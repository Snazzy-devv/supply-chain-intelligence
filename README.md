Supply Chain Intelligence | Neon Sentinel 🛡️
Neon Sentinel is a professional-grade AI logistics terminal designed for real-time global oversight. It combines live commodity tracking, geospatial risk mapping, and agentic AI to provide a "War-Room" experience for supply chain management.

📺 Media & Demonstration
To view the full capabilities of the Sentinel system, see the media links below:

📸 Click here to view Dashboard Screenshots
View high-resolution captures of the Glassmorphism UI, Global War-Room, and Risk Metrics.

🎥 Click here to watch the Video Demo
Watch a full technical walkthrough of the AI Commander and Sentinel-Scan process.

🔬 System Overview
This terminal acts as an autonomous "Watchdog," scanning global data points to detect disruptions before they impact the bottom line. It utilizes a Human-in-the-Loop (HITL) architecture, ensuring that while the AI identifies risks, the final strategic execution remains with the user.

Key Intelligence Layers:
🌐 Global War-Room: Interactive geospatial mapping (Folium) tracking port congestion and "Healthy vs. Critical" supply nodes.

📊 Industrial KPIs: Live monitoring of Global Risk Scores, Active Disruptions, and Lead Time deviations.

🔗 Commodity Engine: Real-time pricing for industrial raw materials (e.g., Copper LME) to forecast margin pressure.

💬 AI Commander: An integrated OpenRouter-powered agent capable of analyzing market spikes and suggesting rerouting strategies.

🛠️ Tech Stack
Frontend: Streamlit with custom Glassmorphism CSS.

Mapping: Folium & streamlit-folium.

Intelligence: OpenRouter (GPT-4o / Claude 3.5 Sonnet).

Data Feeds: NewsAPI (Logistics News) & AlphaVantage (Commodity Pricing).

🚀 Quick Start
1. Clone the Repository
Bash
git clone https://github.com/Snazzy-devv/supply-chain-intelligence.git
cd supply-chain-intelligence
2. Environment Setup
Create a .env file or add your keys to Streamlit secrets.toml:

Code snippet
OPENROUTER_API_KEY="your_key_here"
NEWS_API_KEY="your_key_here"
ALPHA_VANTAGE_KEY="your_key_here"
3. Installation & Execution
Bash
pip install -r requirements.txt
streamlit run app.py
🛡️ Industrial Design Protocol
The UI is optimized for high-stakes environments using a Deep Navy/Amber high-contrast theme:

Primary Background: #0b1120 (Deep Space Blue)

Accent Color: #fbbf24 (Amber Gold) for critical metrics.

Alert Logic: Integrated Sentinel-Scan logs to provide a transparent audit trail of AI activity.

🤝 Contribution & Architecture
This project follows the Professional Intelligence & Clinical Data Analysis design standards.

Note: The "AI Commander" requires manual prompts and confirmation to initiate rerouting strategies, maintaining strict adherence to HITL (Human-in-the-Loop) safety protocols for industrial operations.

📥 Contact & Support
Developed by Kingsley Onah (Snazzy-devv) for Industrial Intelligence applications. For inquiries regarding custom agent deployment or enterprise integration, please open an issue in this repository.
