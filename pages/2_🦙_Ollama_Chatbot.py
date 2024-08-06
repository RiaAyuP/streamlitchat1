import os
from dotenv import load_dotenv, find_dotenv
import ollama
import streamlit as st

st.title("💬 Dita's Ollama Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Ollama")
model = st.selectbox("Please select LLM",("gemma2", "llama3.1", "mistral"),)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant who only speaks in Indonesian."},
        {"role": "assistant", "content": "How can I help you?"}
        ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = ollama.chat(model=model, messages=st.session_state.messages)
    
    msg = response['message']['content']
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)