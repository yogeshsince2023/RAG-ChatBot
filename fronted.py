import streamlit as st
from rag_pipeline import answer_query, get_context
from app import load_pdf, split_documents, create_embeddings_model
from langchain_community.vectorstores import FAISS
import os

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
user_query = st.text_input("Enter your query:")
search = st.button("Search")

if search and uploaded_file is not None and user_query:
    os.makedirs("pdfs", exist_ok=True)
    pdf_path = "pdfs/" + uploaded_file.name
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    documents = load_pdf(pdf_path)
    chunks = split_documents(documents)
    faiss_db = FAISS.from_documents(chunks, create_embeddings_model())
    retriever_docs = faiss_db.similarity_search(user_query, k=3)

    st.subheader("Answer")
    st.write(answer_query(retriever_docs, user_query))

    st.subheader("Relevant Context")
    with st.expander("Show retrieved context"):
        st.write(get_context(retriever_docs))