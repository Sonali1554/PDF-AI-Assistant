# 📄 PDF AI Assistant

A ChatPDF-style Retrieval-Augmented Generation (RAG) application built using LangChain, Hugging Face, FAISS, and Streamlit.

## Features

* Upload any PDF
* Ask questions about the PDF
* Semantic search using FAISS
* Hugging Face Embeddings
* Conversational interface
* Source chunk display
* Streamlit UI

## Tech Stack

* Python
* LangChain
* Hugging Face
* FAISS
* Streamlit
* Sentence Transformers
* PyPDF

## Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
<img width="1920" height="1200" alt="Screenshot (1196)" src="https://github.com/user-attachments/assets/4e8022c4-e71c-42d5-b301-d894d6ad46ff" />


## Project Structure

```text
PDF-AI-Assistant/
│
├── streamlit_app.py
├── pdf_rag.py
├── llm.py
├── .env
├── requirements.txt
└── README.md
```
