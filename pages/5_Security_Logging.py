import streamlit as st
import pandas as pd

st.title("🛡️ Autonomous Recovery & Security Logging")

st.success("✓ Recovery Successful — System restored to normal")

c1, c2, c3, c4 = st.columns(4)
c1.metric("CPU Usage", "35%", "Normal")
c2.metric("Memory Usage", "40%", "Normal")
c3.metric("Temperature", "42°C", "Normal")
c4.metric("Network Activity", "30%", "Normal")

logs = pd.DataFrame([
    ["10:54:47", "Abnormal condition detected", "CRITICAL", "Threat detected"],
    ["10:54:49", "Threat detected", "HIGH", "Faulty node isolated"],
    ["10:54:51", "Recovery process started", "HIGH", "Protection activated"],
    ["10:54:54", "System recovered to normal", "RECOVERY", "System restored"],
    ["10:54:57", "Autonomous recovery completed", "RECOVERY", "Monitoring resumed"]
], columns=["Time", "Security Event", "Severity", "Action"])

st.subheader("Security Event Logs")
st.dataframe(logs, use_container_width=True, hide_index=True)

col1, col2 = st.columns(2)

with col1:
    st.download_button(
        "⬇ Export Logs",
        logs.to_csv(index=False),
        "security_logs.csv",
        "text/csv"
    )

with col2:
    if st.button("↻ Run Self-Healing", use_container_width=True):
        st.success("Self-healing completed successfully.")
