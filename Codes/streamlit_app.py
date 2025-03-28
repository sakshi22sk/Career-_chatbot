import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai  # Import Gemini API

# Load .env file
load_dotenv()

# Fetch API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("⚠️ Error: GEMINI_API_KEY not found! Set it in .env.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

st.write("✅ Gemini API Key Loaded Successfully!")
