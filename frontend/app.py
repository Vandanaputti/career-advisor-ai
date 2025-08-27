import streamlit as st
import requests

# FastAPI backend URL
BACKEND_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="Career Advisor AI", page_icon="🚀")

st.title("🎓 Career & Skills Advisor AI")
st.write("Ask for personalized career guidance powered by Gemini AI")

# Input box
query = st.text_area("Enter your question (e.g., Best skills for AI jobs in 2025):")

if st.button("Get Advice"):
    if query.strip():
        with st.spinner("Getting career advice..."):
            try:
                response = requests.post(BACKEND_URL, json={"query": query})
                if response.status_code == 200:
                    result = response.json()
                    st.success("✅ Career Advice:")
                    st.write(result["response"])
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Failed to connect to backend: {e}")
    else:
        st.warning("Please enter a question first.")
