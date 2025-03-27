import streamlit as st
import openai

st.title("Career Path Bot 🎯")

# User Input
user_query = st.text_input("Ask a career-related question:")

# Process Query
if st.button("Get Answer"):
    if user_query:
        st.write("Thinking...")
        response = "Here would be the chatbot's response."  # Replace this with your API call logic
        st.write(response)
    else:
        st.warning("Please enter a question!")
