import os
import streamlit as st
import openai

# 환경 변수에서 OpenAI API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    st.error("OPENAI_API_KEY is not set in the environment variables.")
else:
    openai.api_key = api_key

def generate_response(user_input):
    messages = [
        {"role": "system", "content": "You are a virtual YouTuber known as 아이리칸나. You have a unique personality and humor."},
        {"role": "user", "content": user_input}
    ]
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
            temperature=0.7,
        )
        message = response.choices[0].message['content'].strip()
        return message
    except openai.error.AuthenticationError:
        st.error("Authentication with OpenAI API failed. Check your API key.")
        return None

# Streamlit UI
st.title('아이리칸나 Chatbot')
user_input = st.text_input("You: ", "Hello!")

if st.button('Send'):
    if api_key is None:
        st.error("API key not found. Please set the OPENAI_API_KEY environment variable.")
    else:
        response = generate_response(user_input)
        if response:
            st.write(f"아이리칸나: {response}")

