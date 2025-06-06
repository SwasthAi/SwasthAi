import streamlit as st
import openai
import os

st.set_page_config(page_title="SwasthAI", layout="centered")
st.title("🩺 SwasthAI – Your AI Health Companion")

openai.api_key = os.getenv("OPENAI_API_KEY")

question = st.text_input("Enter your health question:")

if question:
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        st.success(response['choices'][0]['message']['content'])
