import streamlit as st
from datetime import datetime


def footer():

    year = datetime.now().year

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 🩺 About
        AI-powered disease awareness and
        public health education platform.
        """)

    with col2:
        st.markdown("""
        ### 📚 Features
        - Health Chatbot
        - Disease Awareness
        - Symptom Guidance
        - Prevention Tips
        """)

    with col3:
        st.markdown("""
        ### ⚠ Disclaimer
        This system provides educational
        information only and does not
        replace professional medical advice.
        """)

    st.markdown("---")

    st.markdown(
        f"""
        <div style='text-align:center;color:gray;'>
            © {year} AI-Driven Public Health Chatbot
        </div>
        """,
        unsafe_allow_html=True
    )