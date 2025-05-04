# https://github.com/ollama/ollama

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template= """

Answer question below

Here is conversation history : {context}

Question : {question}

Answer : 
"""
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_convo(query):
    context=("you're maggie a chatbot that is still being developed. you are developed by Kishore")
    while True:
        inp = query
        if  "exit lama" in inp.lower():
            return ("exited")
            break
        result= chain.invoke({"context": context,"question":inp})
        context += f"\n user: {inp} \n AI:{result}"
        return (result)

