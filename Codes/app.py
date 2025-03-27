import streamlit as st

st.title("Career Path Bot 🚀")
st.write("Welcome to the AI-powered Career Path Bot!")

# Example chatbot interface
user_input = st.text_input("Ask me about your career:")
if user_input:
    st.write(f"🤖 Response: {user_input}")
