import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("AIzaSyDnMfxXNUwZPyPZbQxRhPQJcSJ2jZsGh7g")

if not GEMINI_API_KEY:
    st.error("⚠️ Error: GEMINI_API_KEY not found! Set it in .env file.")
    st.stop()

# Configure Gemini API
genai.configure(api_key="AIzaSyDnMfxXNUwZPyPZbQxRhPQJcSJ2jZsGh7g")

# Define a function to filter non-career-related queries
def is_career_related(query):
    career_keywords = [
        "career", "job", "skills", "salary", "resume", "cv", "certification", 
        "interview", "industry", "growth", "employment", "profession", 
        "training", "work", "company", "hiring", "internship", "technology", "ai", 
        "data analyst", "software engineer", "marketing", "finance", "design"
    ]
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in career_keywords)

# Function to get response from Gemini API
def get_career_advice(user_query):
    if not is_career_related(user_query):
        return "❌ Sorry, I can only answer career-related questions."
    
    try:
        response = genai.generate_text(user_query)
        return response.result if response.result else "⚠️ No relevant answer found."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Streamlit UI
st.title("🎯 Career Path Bot")
st.subheader("Ask a career-related question:")

# User input
user_query = st.text_input("Enter your question:")

if st.button("Ask"):
    if user_query.strip():
        with st.spinner("Thinking..."):
            answer = get_career_advice(user_query)
        st.write(answer)
    else:
        st.warning("⚠️ Please enter a question.")
