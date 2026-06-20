import os
import streamlit as st

from pdf_rag import create_vectorstore
from llm import chat_model
from langchain_core.messages import HumanMessage

st.set_page_config(
    page_title="PDF AI Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 PDF AI Assistant")

# --------------------------
# Session State
# --------------------------

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------
# Sidebar
# --------------------------

with st.sidebar:

    st.header("Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if uploaded_file:

        os.makedirs("data", exist_ok=True)

        pdf_path = os.path.join(
            "data",
            uploaded_file.name
        )

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if st.button("Process PDF"):

            with st.spinner("Creating embeddings..."):

                st.session_state.vectorstore = create_vectorstore(
                    pdf_path
                )

            st.success("PDF Processed Successfully!")

    if st.button("Clear Chat"):
        st.session_state.messages = []

# --------------------------
# Display Chat
# --------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.write(msg["content"])

# --------------------------
# User Question
# --------------------------

question = st.chat_input(
    "Ask a question about the uploaded PDF..."
)

if question:

    if st.session_state.vectorstore is None:

        st.warning(
            "Please upload and process a PDF first."
        )

        st.stop()

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    retriever = st.session_state.vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are an expert PDF assistant.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    with st.spinner("Generating answer..."):

        response = chat_model.invoke(
            [HumanMessage(content=prompt)]
        )

    answer = response.content

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):

        st.write(answer)

        with st.expander("View Source Chunks"):

            for i, doc in enumerate(docs):

                st.markdown(
                    f"### Chunk {i+1}"
                )

                st.write(
                    doc.page_content[:1000]
                )