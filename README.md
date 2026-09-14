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

This project uses offline retrieval and extractive answer selection. It does not call Groq, OpenAI, or any other internet API, and it does not generate an answer with a remote LLM.

## Requirements

- Python 3.10+
- A valid, readable PDF file
- The local embedding model `sentence-transformers/all-MiniLM-L6-v2`

Create and activate a virtual environment, then install every project dependency:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

The embedding model must be downloaded once while internet access is available. Run this after installing the requirements:

```powershell
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')"
```

After that, the application uses the cached model with `local_files_only=True` and will not attempt a network request.

## Run

Activate the virtual environment and start Streamlit:

```powershell
\.\.venv\Scripts\Activate.ps1
streamlit run frontend.py
```

Open the URL shown by Streamlit, usually `http://localhost:8501`.

1. Upload a valid PDF.
2. Enter a question.
3. Click **Search**.
4. Read the retrieved sections under **Relevant Context**.

## Project Files

- `frontend.py` - Streamlit interface and FAISS retrieval workflow
- `app.py` - PDF loading, chunking, and local embedding setup
- `rag_pipeline.py` - Formatting retrieved documents as context
- `pdfs/` - Optional local PDF storage

## Notes

- The included PDF must be a structurally valid PDF for `pdfplumber` to read it.
- Large PDFs may take time to embed because the FAISS index is rebuilt when a search is submitted.
- No API key or `.env` file is required.
