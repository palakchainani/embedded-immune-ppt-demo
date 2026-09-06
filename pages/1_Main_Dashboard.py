import streamlit as st

st.title("🛡️ Main Dashboard")
st.caption("Real-time monitoring of embedded system health and security.")

c1, c2, c3, c4 = st.columns(4)

c1.metric("CPU Usage", "35%", "Normal")
c2.metric("Memory Usage", "40%", "Normal")
c3.metric("Temperature", "42°C", "Normal")
c4.metric("Network Activity", "30%", "Normal")

st.success("✓ Device Health: 100% | Threat Score: 0/100 | Status: SECURE")

st.subheader("Protection Flow")
st.info("Monitoring → Threat Detection → Immune Response → Recovery")
