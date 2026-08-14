import streamlit as st
from datetime import datetime


def get_bot_response(user_message):
    """
    Replace this function with your AI model,
    Gemini API, OpenAI API, or disease prediction model.
    """

    user_message = user_message.lower()

    if "fever" in user_message:
        return """
        Fever can be associated with infections such as flu,
        dengue, malaria, or COVID-19.

        If symptoms persist, please consult a healthcare professional.
        """

    elif "diabetes" in user_message:
        return """
        Diabetes is a chronic disease that affects how your body
        processes blood sugar (glucose).

        Common symptoms:
        • Increased thirst
        • Frequent urination
        • Fatigue
        • Blurred vision
        """

    elif "covid" in user_message:
        return """
        COVID-19 symptoms may include:
        • Fever
        • Cough
        • Fatigue
        • Loss of taste or smell

        Follow local public health guidelines.
        """

    else:
        return """
        I can help with disease awareness,
        symptoms, prevention tips, and general health information.

        Please provide more details about your question.
        """


def chatbot_ui():

    st.title("🤖 AI Health Assistant")

    st.caption(
        "Ask questions about diseases, symptoms, prevention, and public health awareness."
    )

    # Sidebar
    with st.sidebar:
        st.header("🩺 Quick Health Tips")

        st.info("💧 Drink enough water daily.")
        st.info("🥗 Maintain a balanced diet.")
        st.info("🏃 Exercise regularly.")
        st.info("😴 Get adequate sleep.")
        st.info("🧼 Wash hands frequently.")

    # Session State
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content":
                "Hello! I'm your AI Public Health Assistant. How can I help you today?"
            }
        ]

    # Display Chat History
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat Input
    user_input = st.chat_input(
        "Type your health-related question..."
    )

    if user_input:

        current_time = datetime.now().strftime("%H:%M")

        # User Message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_input,
                "time": current_time
            }
        )

        with st.chat_message("user"):
            st.write(user_input)

        # Bot Response
        response = get_bot_response(user_input)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
                "time": current_time
            }
        )

        with st.chat_message("assistant"):
            st.write(response)

    st.divider()

    st.warning(
        "⚠️ This chatbot is for educational and awareness purposes only and "
        "should not replace professional medical advice."
    )