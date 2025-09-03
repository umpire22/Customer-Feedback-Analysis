import streamlit as st
from textblob import TextBlob

# --- PAGE CONFIG ---
st.set_page_config(page_title="Customer Feedback Analysis", layout="wide", initial_sidebar_state="expanded")

# --- TITLE & DESCRIPTION ---
st.title("🗣️ **Customer Feedback Analysis Agent**")
st.markdown("""
This agent analyzes customer feedback, performing sentiment analysis and providing insights into customer satisfaction trends.
""", unsafe_allow_html=True)

# --- MANUAL INPUT SECTION ---
feedback = st.text_area("Enter Customer Feedback:")

if feedback:
    blob = TextBlob(feedback)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        sentiment_label = "Positive"
    elif sentiment < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    
    st.markdown("### 📝 **Sentiment Analysis Result**")
    st.write(f"Sentiment: **{sentiment_label}** (Score: {sentiment})")

    # --- COPY FEEDBACK ---
    st.markdown("### 📋 **Copy the Feedback**")
    st.text_area("Copy this:", feedback, height=100)

# --- STYLING ---
st.markdown("""
    <style>
    body {
        background-color: #1e1e1e;
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    .stTextArea {
        background-color: #333;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)
