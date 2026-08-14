import streamlit as st


def navbar():

    st.markdown("""
    <style>
    .main-title{
        text-align:center;
        color:#0EA5E9;
        font-size:32px;
        font-weight:bold;
        margin-bottom:20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="main-title">
        🩺 AI-Driven Public Health Chatbot
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("pages/Home.py")

    with col2:
        if st.button("📚 Awareness", use_container_width=True):
            st.switch_page("pages/Disease_Awareness.py")

    with col3:
        if st.button("🤖 Chatbot", use_container_width=True):
            st.switch_page("pages/Chatbot.py")

    with col4:
        if st.button("ℹ About", use_container_width=True):
            st.switch_page("pages/About.py")

    st.divider()