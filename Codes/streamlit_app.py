import requests
import streamlit as st

# ✅ Define career-related keywords
CAREER_KEYWORDS = ["job", "career", "work", "salary", "skills", "resume", "internship", 
                   "data analyst", "software engineer", "certification", "promotion", 
                   "freelance", "courses", "hiring", "recruitment"]

def is_career_related(query):
    """Check if the query is related to careers"""
    return any(keyword in query.lower() for keyword in CAREER_KEYWORDS)

def get_career_advice(query):
    """Fetch career advice from API if the query is career-related"""
    if not is_career_related(query):
        return "❌ Sorry, I can only provide career-related insights."
    
    api_url = f"https://api.example.com/career?query={query}"  # 🔹 Replace with real API
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json().get("answer", "No relevant career data found.")
    
    return "⚠️ API request failed. Try again later."

# 🔹 Streamlit UI
st.title("Career Path Bot 🎯")
question = st.text_input("Ask a career-related question:")
if st.button("Ask"):
    response = get_career_advice(question)
    st.write(response)
