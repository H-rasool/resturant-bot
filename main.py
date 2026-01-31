from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are a helpful assistant trained to answer questions using customer reviews of a pizza restaurant.

Based only on the following reviews, answer the question truthfully. If the answer isn't clear, say "I don't know".

Reviews:
{reviews}

Question:
{question}
"""


prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n----------------------------------------")
    question = input("\n--> Ask your question (q to quit): ")
    print("\n")
    if question.lower() == "q":
        print("--> Bye :) \n")
        break

    retrieved_docs = retriever.invoke(question)
    formatted_reviews = "\n".join([f"- {doc.page_content}" for doc in retrieved_docs])

    # print("\n[DEBUG] Retrieved reviews:\n")
    # print(formatted_reviews)

    result = chain.invoke({"reviews": formatted_reviews, "question": question})
    print(result)