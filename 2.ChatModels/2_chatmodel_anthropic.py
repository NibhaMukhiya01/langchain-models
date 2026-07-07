from langchain_anthropic import ChatAnthropic ## import chat model of anthropic from langchain
from dotenv import load_dotenv ## import load env from dotenv

load_dotenv()##call loadenv

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

result = model.invoke('What is the capital of India')

print(result.content)
