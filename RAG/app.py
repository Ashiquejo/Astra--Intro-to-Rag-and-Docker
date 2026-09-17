import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
from src.data_loader import load_all_documents
from src.vector_store import FaissVectorStore
from src.search import RAGSearch

# Example usage
if __name__ == "__main__":

    FAISS_DIR = "faiss_store"
    faiss_index_path = os.path.join(FAISS_DIR, "faiss.index")
    meta_path = os.path.join(FAISS_DIR, "metadata.pkl")

    docs = load_all_documents("data")
    store = FaissVectorStore(FAISS_DIR)

    if not (os.path.exists(faiss_index_path) and os.path.exists(meta_path)):
        print("[INFO] No existing FAISS store found. Building from documents...")
        store.build_from_documents(docs)
    else:
        print("[INFO] Loading existing FAISS store...")
        store.load()

    print(store.query("What is attention mechanism?", top_k=3))

    rag_search = RAGSearch()
    query = "What is attention mechanism?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary.encode('utf-8', errors='replace').decode('utf-8'))