from langchain_openai import ChatOpenAI ##import chat model of open ai  ## use can see models at platform.openai.com
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10) ##model is varial save object chatopenai

result = model.invoke("Write a 5 line poem on cricket") ## invoke method

print(result.content)
