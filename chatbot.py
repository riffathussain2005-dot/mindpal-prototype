import streamlit as st
import random

# App Title
st.set_page_config(page_title="MindPal - Your Mental Health Companion", page_icon="🧠")

st.title("🧠 MindPal - Your Mental Health Companion")
st.write("Hello! I'm **MindPal**, here to listen and support you. 💙")

# Rule-based responses (with multiple variations for variety)
responses = {
    "greeting": [
        "Hey there! How are you feeling today? 🙂",
        "Hi! It's good to see you. How's your mood right now?",
        "Hello! I'm here to listen whenever you're ready 💬."
    ],
    "sad": [
        "I'm really sorry you're feeling down 💙. Do you want to talk about it?",
        "It’s okay to feel sad sometimes. Sharing might help — would you like to?",
        "Remember, tough times don’t last, but strong people do 🌈."
    ],
    "happy": [
        "That’s amazing! 😃 Keep spreading the positivity.",
        "Love to hear that! 🎉 What's making you feel so happy?",
        "Happiness looks good on you 🌟."
    ],
    "stress": [
        "It sounds like you're stressed 😟. Try pausing for a deep breath.",
        "Stress can be tough. Do you want me to share some quick relaxation tips?",
        "You're not alone in this 🌿. Talking about it may ease the pressure."
    ],
    "anxiety": [
        "Anxiety can feel overwhelming 😔. You're safe here.",
        "Try grounding yourself: look around and name 5 things you see 👀.",
        "Take a deep breath — you're doing better than you think 💙."
    ],
    "bye": [
        "Take care of yourself 💙. I'm always here if you need to talk!",
        "Goodbye! Remember to be kind to yourself 🌸.",
        "See you soon — stay strong and hopeful ✨."
    ],
    "default": [
        "I may not fully understand, but I'm here to listen 👂.",
        "Tell me more about what’s on your mind 💭.",
        "That sounds important. Would you like to share more?"
    ]
}

# Function to get chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return random.choice(responses["greeting"])
    elif any(word in user_input for word in ["sad", "depressed", "unhappy", "down"]):
        return random.choice(responses["sad"])
    elif "happy" in user_input or "joy" in user_input:
        return random.choice(responses["happy"])
    elif "stress" in user_input or "stressed" in user_input:
        return random.choice(responses["stress"])
    elif "anxiety" in user_input or "anxious" in user_input:
        return random.choice(responses["anxiety"])
    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return random.choice(responses["bye"])
    else:
        return random.choice(responses["default"])

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_message = st.text_input("You:", "")

if user_message:
    # Append user message
    st.session_state.messages.append(("You", user_message))

    # Generate bot response
    bot_reply = chatbot_response(user_message)
    st.session_state.messages.append(("MindPal", bot_reply))

# Display chat history
for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**🧑 {sender}:** {msg}")
    else:
        st.markdown(f"**🤖 {sender}:** {msg}")
