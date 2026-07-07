from langchain_google_genai import ChatGoogleGenerativeAI ## can purchase api key from ai.google.dev
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

result = model.invoke('What is the capital of India')

print(result.content)
