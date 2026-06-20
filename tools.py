from langchain.tools import tool
import wikipedia

# Existing Tools
@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression"""
    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)

@tool
def wiki_search(query: str) -> str:
    """Search Wikipedia"""
    try:
        return wikipedia.summary(query, sentences=3)
    except Exception as e:
        return str(e)

# New PDF Tool
from pdf_rag import retriever

@tool
def pdf_search(query: str) -> str:
    """Search uploaded PDF"""

    docs = retriever.invoke(query)

    return "\n\n".join(
        [doc.page_content[:500] for doc in docs]
    )

from pdf_rag import retriever

@tool
def pdf_search(query: str) -> str:
    """Search uploaded PDF"""

    docs = retriever.invoke(query)

    if not docs:
        return "No relevant information found."

    return "\n\n".join(
        [doc.page_content[:500] for doc in docs]
    )