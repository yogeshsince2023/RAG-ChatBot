# Offline RAG Chatbot

A local Retrieval-Augmented Generation (RAG) application that loads a PDF, creates local embeddings, searches the document with FAISS, and displays the most relevant context for a user query.

## Architecture

```text
PDF -> PDF loader -> chunks -> local embeddings -> FAISS
                                                     ^
User query -> local query embedding -> similarity search
                                                     |
                                             Relevant context
```

This project stops at retrieval and context display. It does not call Groq, OpenAI, or any other internet API, and it does not generate an answer with a remote LLM.

## Requirements

- Python 3.10+
- A valid, readable PDF file
- The local embedding model `sentence-transformers/all-MiniLM-L6-v2`

Install the dependencies in the project virtual environment:

```powershell
pip install streamlit langchain-community langchain-text-splitters sentence-transformers faiss-cpu pdfplumber
```

The embedding model must be available in the local Hugging Face cache before running offline. Download it once while internet access is available, then the application uses `local_files_only=True` and will not attempt a network request.

## Run

Activate the virtual environment and start Streamlit:

```powershell
.\.venv\Scripts\Activate.ps1
streamlit run fronted.py
```

Open the URL shown by Streamlit, usually `http://localhost:8501`.

1. Upload a valid PDF.
2. Enter a question.
3. Click **Search**.
4. Read the retrieved sections under **Relevant Context**.

## Project Files

- `fronted.py` - Streamlit interface and FAISS retrieval workflow
- `app.py` - PDF loading, chunking, and local embedding setup
- `rag_pipeline.py` - Formatting retrieved documents as context
- `pdfs/` - Optional local PDF storage

## Notes

- The included PDF must be a structurally valid PDF for `pdfplumber` to read it.
- Large PDFs may take time to embed because the FAISS index is rebuilt when a search is submitted.
- No API key or `.env` file is required.
