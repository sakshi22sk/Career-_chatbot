//career_bot.py → Streamlit UI
import streamlit as st
from chatbot_logic import chatbot_response  # Import chatbot logic

st.title("🚀 Career Path Bot")
st.write("Ask me about career advice!")

# User input
user_query = st.text_input("Type your career-related question:")

if st.button("Get Advice"):
    response = chatbot_response(user_query)
    st.write(response)
