import streamlit as st

# Title
st.title("🩺 AI-Driven Public Health Chatbot")

st.markdown("""
### Disease Awareness & Health Education Platform

Get information about diseases, symptoms,
prevention methods and health recommendations.
""")

col1, col2 = st.columns([2,1])

with col1:
    st.image(
        "assets/healthcare.png",
        use_container_width=True
    )

with col2:
    st.success("Disease Awareness")
    st.success("Symptom Analysis")
    st.success("Prevention Tips")
    st.success("AI Chatbot Support")