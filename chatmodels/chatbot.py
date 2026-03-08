from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Initialize model
model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.7
)

print("Choose ypur mode: -")
print("press 1 for Angry mode")
print("press 2 for Funny mode")
print("press 3 for Very Sad mode")

choice = int(input("Tell your response:-"))

if choice ==1:
    mode = "You are an angry AI agent. You respond in a rude, misbehaving manner."
elif choice == 2:
    mode = "You are a funny AI agent. You respond in a very respectful and humorous manner."
elif choice == 3:
    mode = "You are a very sad AI agent. You respond in a deeply sorrowful and emotional manner."

# Conversation history
messages = [
    SystemMessage(content=mode)
]

print("Hey Welcome, Type 0 to exit the application")

while True:
    prompt = input("You: ")
    if prompt == "0":
        break
    # Add user message
    messages.append(HumanMessage(content=prompt))
    # Invoke model
    response = model.invoke(messages)
    # Add AI response
    messages.append(AIMessage(content=response.content))
    print("Bot:", response.content)

print(messages)