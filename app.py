import os
from flask import Flask, request, jsonify, render_template
import streamlit as st
import openai

app = Flask(__name__)

# 환경 변수에서 OpenAI API 키 가져오기
api_key = os.getenv("sk-proj-wVp9aECsCkSoiSBDl8gOT3BlbkFJsyY6UYtFTe64ex7GNwB2")
openai.api_key = api_key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = generate_response(user_input)
    return jsonify({'response': response})

def generate_response(user_input):
    messages = [
        {"role": "system", "content": "You are a virtual YouTuber known as 아이리칸나. You have a unique personality and humor."},
        {"role": "user", "content": user_input}
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150,
        temperature=0.7,
    )
    message = response.choices[0].message['content'].strip()
    return message

if __name__ == '__main__':
    app.run(debug=True)
