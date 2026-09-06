import streamlit as st

st.set_page_config(
    page_title="Embedded Immune System",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Embedded Immune System")
st.subheader("IoT-Based Embedded System Security & Fault Management")

st.markdown("""
This project monitors embedded-system parameters, detects abnormal conditions,
activates an autonomous immune response, and performs recovery with security logging.
""")

st.success("🟢 System Ready — Select a module from the sidebar.")
