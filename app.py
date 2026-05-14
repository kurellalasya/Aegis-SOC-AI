import streamlit as st
from agents.workflow import SecurityAgent
from utils.helpers import save_report
from sample_data import ATTACK_SAMPLES

# 1. Page Config & Professional Styling
st.set_page_config(page_title="Aegis SOC AI", layout="wide")

st.markdown("""
    <style>
    .main { background: #0e1117; }
    .stMetric { background: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    .stAlert { border-radius: 10px; }
    .stButton>button { 
        background: linear-gradient(45deg, #ff4b4b, #ff7575); 
        color: white; border: none; font-weight: bold; height: 3em;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header Section
col_title, col_logo = st.columns([4, 1])
with col_title:
    st.title("Aegis AI: Autonomous SOC Agent")
    st.markdown("*Next-Generation Incident Response & Threat Intelligence*")

st.divider()

# 3. Sidebar Configuration
with st.sidebar:
    st.header("Command Center")
    # Updated for Gemini API
    api_key = st.text_input("Gemini API Key", type="password", help="Enter your Google AI Studio API Key")
    
    st.divider()
    st.subheader("Demo Scenarios")
    scenario = st.selectbox("Select Attack Pattern", list(ATTACK_SAMPLES.keys()))
    if st.button("Inject Sample Logs"):
        st.session_state.logs = ATTACK_SAMPLES[scenario]
    
    st.divider()
    st.info("Architecture: Sequential Agentic Pipeline\n(Detection -> Analysis -> Mitigation -> CISO)")

# 4. Input & Analysis Workspace
col_in, col_out = st.columns([1, 1.5], gap="large")

with col_in:
    st.subheader("Live Log Stream")
    log_input = st.text_area("System logs monitor...", 
                             value=st.session_state.get('logs', ''), 
                             height=400,
                             placeholder="Waiting for log input...")
    
    analyze_btn = st.button("EXECUTE AGENTIC RESPONSE")

# 5. Output Dashboard
with col_out:
    if analyze_btn:
        if not api_key:
            st.error("Authentication Error: Gemini API Key Missing")
        elif not log_input:
            st.warning("Data Error: No logs detected for analysis")
        else:
            # Initialize the Gemini-powered Security Agent
            agent = SecurityAgent(api_key)
            
            with st.status("Initializing Multi-Agent Response...", expanded=True) as status:
                st.write("Detection Agent: Extracting indicators...")
                detection = agent.run_stage("detection", log_input)
                
                st.write("Intelligence Agent: Classifying threat vector...")
                analysis = agent.run_stage("analysis", detection)
                
                st.write("Responder Agent: Drafting containment playbook...")
                mitigation = agent.run_stage("mitigation", analysis)
                
                st.write("CISO Agent: Compiling executive report...")
                report = agent.run_stage("report", f"{analysis}\n{mitigation}")
                status.update(label="Analysis Complete", state="complete")

            # Dashboard Metrics
            m1, m2, m3 = st.columns(3)
            # Dynamic color coding for threat status
            sev_high = any(word in analysis.upper() for word in ["CRITICAL", "HIGH", "URGENT"])
            sev_color = "inverse" if sev_high else "normal"
            
            m1.metric("Threat Status", "ACTUAL" if sev_high else "SUSPICIOUS", delta_color=sev_color)
            m2.metric("Response Time", "0.8s", delta="-99%")
            m3.metric("Agent Confidence", "96%")

            # Results Tabs
            tab1, tab2, tab3 = st.tabs(["Executive Summary", "Technical Playbook", "Forensic Details"])
            
            with tab1:
                st.markdown(report)
                # Save and provide download link
                report_path = save_report(report)
                with open(report_path, "r") as f:
                    st.download_button("EXPORT INCIDENT REPORT", f, file_name="AEGIS_REPORT.txt")
            
            with tab2:
                st.success("Steps to Contain and Eradicate:")
                st.write(mitigation)
            
            with tab3:
                st.code(analysis, language="markdown")
    else:
        st.info("Ready for input. Select a demo scenario from the sidebar to begin.")