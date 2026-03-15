import streamlit as st
import anthropic
import os

# Load API key securely
client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

st.title("🤖 My AI Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=st.session_state.messages
        )
        reply = response.content[0].text
        st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
