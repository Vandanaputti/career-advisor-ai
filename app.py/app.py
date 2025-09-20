import streamlit as st

st.title("AI Career Advisor")
st.write("Get personalized career guidance from AI!")

user_input = st.text_input("Ask me about your career:")

if st.button("Get Advice"):
    if user_input.strip() == "":
        st.write("Please type a question first.")
    else:
        st.write(f"You asked: {user_input}")
        st.write("AI Career Advice: Explore roles that match your skills and interests!")
