from pdf_rag import retriever
from llm import chat_model
from langchain_core.messages import HumanMessage

print("PDF Chatbot Ready! Type 'exit' to quit.")

while True:

    query = input("\nYou: ")

    if query.lower() == "exit":
        break

    # Retrieve relevant chunks
    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are an expert document assistant.

Answer ONLY using the information provided in the PDF context.

PDF Context:
{context}

Question:
{query}

Answer:
"""

    response = chat_model.invoke(
        [HumanMessage(content=prompt)]
    )

    print("\nAssistant:")
    print(response.content)