from llm import chat_model
from tools import calculator, wiki_search, pdf_search

tools = [
    calculator,
    wiki_search,
    pdf_search
]

agent = chat_model.bind_tools(tools)