print("Hello haider !")

from dotenv import load_dotenv
import os
load_dotenv()

# from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  
    # Or gemini-2.5-pro, gemini-2.0-flash, etc.
    temperature = 2,
)

response = model.invoke("Who's the marja of iran with full name, and the family members of them, tell me?")
print(response.content)