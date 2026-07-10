from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint ##we have to import huggingfacepoint when we want to use hf apis
from dotenv import load_dotenv

load_dotenv()##func call

llm = HuggingFaceEndpoint(  ##creating llm for hf by endpoint
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", ##repo id of tiny llama model api key
    task="text-generation" ##tiny llama can do text generation
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)
