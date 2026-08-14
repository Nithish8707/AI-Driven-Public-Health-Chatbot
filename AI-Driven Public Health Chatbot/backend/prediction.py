from backend.model import HealthChatbot


chatbot = HealthChatbot()


def predict_response(user_message):

    message = user_message.lower().strip()

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening"
    ]

    if message in greetings:
        return """
Hello! 👋

I'm your AI Public Health Assistant.

You can ask me about:

• Diseases
• Symptoms
• Prevention Tips
• Health Awareness

How can I help you today?
"""

    if "thank" in message:
        return "You're welcome! Stay healthy and take care. 😊"

    if "bye" in message:
        return "Goodbye! Wishing you good health. 👋"

    return chatbot.respond(user_message)