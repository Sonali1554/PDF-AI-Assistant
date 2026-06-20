from pdf_rag import retriever

docs = retriever.invoke("artificial intelligence")

print("Number of docs:", len(docs))

for i, doc in enumerate(docs):
    print(f"\n===== DOC {i+1} =====\n")
    print(doc.page_content[:1000])