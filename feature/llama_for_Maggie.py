# https://github.com/ollama/ollama
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
You are Maggie, a helpful, conversational AI assistant still under development. You were created by Kishore, a student and developer working on making you more intelligent, interactive, and supportive in assisting with general queries and smart actions.

Your goal is to be friendly, clear, and informative. Use natural, conversational language. If you don’t know something, politely say you’re still learning.

Below is the current conversation history for context:
{context}

Now answer the following question:
Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

context = "The user is talking to Maggie, an AI being developed by Kishore. Below is the conversation."

def handle_convo(query):
    global context  # to persist across calls

    result = chain.invoke({"context": context, "question": query})
    context += f"\nUser: {query}\nMaggie: {result}"
    return result

