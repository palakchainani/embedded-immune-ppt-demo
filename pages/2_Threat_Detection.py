import streamlit as st

st.title("🔍 Threat Analysis & Fault Diagnosis")

st.error("⚠️ Abnormal condition detected")

c1, c2 = st.columns(2)

with c1:
    st.metric("Affected Component", "CPU / Processing Unit")
    st.metric("Current Value", "90%")

with c2:
    st.metric("Threshold", "≥ 80%")
    st.metric("Severity", "HIGH")

st.subheader("Diagnosis")
st.write("Reason: Excessive processing load")

st.subheader("Recovery Action")
st.info("Reduce processing load and isolate CPU workload")

st.warning("System Health: 75%    |    Threat Score: 25/100")
