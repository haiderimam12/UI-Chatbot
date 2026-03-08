import streamlit as st
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.7
)

st.set_page_config(
    page_title="AI Mood Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Sidebar
with st.sidebar:
    st.title("🎭 Choose AI Personality")

    mode_choice = st.radio(
        "Select Mode",
        (
            "Angry Mode 😡",
            "Funny Mode 😂",
            "Sad Mode 😢",
            "Love Mode ❤️"
        )
    )

# Light theme colors
if mode_choice == "Angry Mode 😡":
    mode = "You are an angry AI agent. You respond in a rude and aggressive manner."
    bg = "#fff1f1"
    accent = "#ff4b4b"

elif mode_choice == "Funny Mode 😂":
    mode = "You are a funny AI agent. You respond in a respectful and humorous manner."
    bg = "#fff9db"
    accent = "#f4b400"

elif mode_choice == "Sad Mode 😢":
    mode = "You are a very sad AI agent. You respond in a deeply sorrowful and emotional manner."
    bg = "#eef6ff"
    accent = "#4da6ff"

elif mode_choice == "Love Mode ❤️":
    mode = "You are a loving AI agent. You respond in a caring and affectionate manner."
    bg = "#fff0f6"
    accent = "#ff66b2"

# Apply full page theme
st.markdown(f"""
<style>

.stApp {{
background-color: {bg};
}}

.title {{
text-align:center;
font-size:40px;
font-weight:bold;
color:{accent};
}}

.subtitle {{
text-align:center;
color:#555;
margin-bottom:30px;
}}

.user-bubble {{
background-color:#ffffff;
padding:10px 15px;
border-radius:10px;
border:1px solid #ddd;
}}

.bot-bubble {{
background-color:{accent}20;
padding:10px 15px;
border-radius:10px;
border:1px solid {accent};
}}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🤖 AI Mood Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Chat with different AI personalities</div>', unsafe_allow_html=True)

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=mode)]

# Reset if mode changes
if st.session_state.messages[0].content != mode:
    st.session_state.messages = [SystemMessage(content=mode)]

# Show messages
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(f'<div class="user-bubble">{msg.content}</div>', unsafe_allow_html=True)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(f'<div class="bot-bubble">{msg.content}</div>', unsafe_allow_html=True)

# Chat input
prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(HumanMessage(content=prompt))

    with st.chat_message("user"):
        st.markdown(f'<div class="user-bubble">{prompt}</div>', unsafe_allow_html=True)

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.markdown(f'<div class="bot-bubble">{response.content}</div>', unsafe_allow_html=True)