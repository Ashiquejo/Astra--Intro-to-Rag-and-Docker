# Retrieval-Augmented Generation (RAG) Fundamentals

Welcome to the repository. This project is designed to introduce the foundational concepts and modular pipelines of Retrieval-Augmented Generation (RAG) systems. 

## Overview
Large Language Models (LLMs) are exceptionally powerful but often lack domain-specific or up-to-date knowledge. RAG solves this by anchoring generative AI with an authoritative external knowledge base, preventing "hallucinations" and providing accurate, context-aware responses.

## Architecture
This repository breaks down the RAG architecture into two primary computational pipelines:

### 1. Data Ingestion Pipeline
* **Data Loading:** Extracting content from varied sources (PDFs, TXT files) using tools like `PyMuPDF` and `TextLoader`.
* **Chunking:** Subdividing large documents into manageable segments using `RecursiveCharacterTextSplitter` to comfortably fit LLM context windows.
* **Embedding:** Converting text chunks into numerical vectors (e.g., using HuggingFace's `all-MiniLM-L6-v2`).
* **Vector Storage:** Indexing the vectorized data in a Vector Database (such as ChromaDB or FAISS) for rapid similarity searches.

### 2. Retrieval & Augmented Generation Pipeline
* **Query Embedding:** Transforming the user's natural language prompt into a vector representation.
* **Context Retrieval:** Executing a cosine similarity search against the Vector DB to extract highly relevant document chunks.
* **Augmented Generation:** Passing the targeted context alongside the user's prompt to an LLM (e.g., via the Groq API) to formulate a precise, fact-grounded response.

## Repository Structure
```text
├── data/                  # Sample documents (PDFs, TXT)
├── src/                   # Modular pipeline scripts
│   ├── data_loader.py     # Document parsing and chunking logic
│   ├── embeddings.py      # Vector embedding generation
│   ├── vector_store.py    # Database indexing and retrieval methods
│   └── rag_pipeline.py    # LLM integration and final generation
├── app.py                 # Main execution script
├── .env.example           # Example environment variables
├── requirements.txt       # Project dependencies
└── README.md              # You are here
```

## Getting Started
1. **Clone the repository:** Bring the codebase into your local environment.
2. **Initialize a virtual environment:** 
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:** 
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure credentials:** Rename `.env.example` to `.env` and populate it with your respective API keys (e.g., `GROQ_API_KEY`).
5. **Execute the pipeline:** Run `python app.py` to initiate the data ingestion sequence and test a sample retrieval query.

---
*Maintained for educational purposes to advance the understanding of autonomous software workflows and agentic AI architectures.*
