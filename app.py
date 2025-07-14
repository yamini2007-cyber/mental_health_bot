import streamlit as st
import random
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from utils.responses import MOOD_RESPONSES

st.set_page_config(page_title="Mental Health Chatbot", layout="centered")

# Custom CSS for dark mode and animations
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #fff;
    }
    .bot-msg {
        background: linear-gradient(135deg, #2c3e50, #34495e);
        color: white;
        padding: 15px;
        border-radius: 12px;
        margin: 15px 0;
        animation: fadein 1s ease-in-out;
        font-size: 16px;
    }
    @keyframes fadein {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #388E3C;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Mental Health Chatbot")
st.subheader("How are you feeling today? Choose your mood or type it below.")

# Mood Selection Buttons
col1, col2, col3 = st.columns(3)
mood = "neutral"
if col1.button("😢 Sad"):
    mood = "sad"
if col2.button("😡 Angry"):
    mood = "angry"
if col3.button("😰 Anxious"):
    mood = "anxious"
if st.button("😊 Happy"):
    mood = "happy"

# User Input
user_input = st.text_input("Or describe your feelings:")

if user_input:
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(user_input)["compound"]
    if score <= -0.3:
        mood = "sad"
    elif score >= 0.3:
        mood = "happy"
    elif -0.3 < score < -0.05:
        mood = "anxious"
    elif 0.05 < score < 0.3:
        mood = "neutral"

# Bot Reply
if st.button("💬 Get Support"):
    reply = random.choice(MOOD_RESPONSES[mood])
    st.markdown(f"<div class='bot-msg'>{reply}</div>", unsafe_allow_html=True)

