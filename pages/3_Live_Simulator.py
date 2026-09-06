import streamlit as st

st.title("⚙️ Live System Simulator")
st.caption("Apply abnormal conditions and observe system response.")

cpu = st.slider("CPU Usage", 0, 100, 90)
memory = st.slider("Memory Usage", 0, 100, 85)
temperature = st.slider("Temperature (°C)", 20, 100, 95)
network = st.slider("Network Activity", 0, 100, 90)

st.subheader("Real-Time Results")

if cpu >= 80 or memory >= 80 or temperature >= 80 or network >= 80:
    st.error("🔴 CRITICAL THREAT DETECTED")
    st.metric("Threat Score", "100/100")
    st.metric("Device Health", "0%")
    st.metric("Active Faults", "4")
    st.error("System Status: CRITICAL")
else:
    st.success("🟢 System operating normally")
