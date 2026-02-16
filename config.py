from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

COLLECTION_NAME = "rag_pdf_collection"
QDRANT_URL = "http://localhost:6333"
VECTOR_SIZE = 384
MODEL_NAME = "all-MiniLM-L6-v2"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150
SEARCH_LIMIT = 5
LLM_MODEL_NAME = "gpt-4o-mini"
APP_HOST = "0.0.0.0"
APP_PORT = 8000