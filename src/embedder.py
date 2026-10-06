import chromadb
from sentence_transformers import SentenceTransformer
from src.config import EMBED_MODEL, CHROMA_DIR, COLLECTION_NAME
from src.loader import load_reviews

_model = None

def get_model():
    global _model
    if _model is None:
        print(f"Loading embedding model: {EMBED_MODEL}")
        _model = SentenceTransformer(EMBED_MODEL)
    return _model

def get_collection():
    chroma = chromadb.PersistentClient(path=CHROMA_DIR)
    return chroma.get_or_create_collection(
        name=COLLECTION_NAME, metadata={"hnsw:space": "cosine"}
    )

def embed_texts(texts):
    model = get_model()
    embeddings = model.encode(texts, show_progress_bar=False)
    return embeddings.tolist()

def ingest():
    df = load_reviews()
    collection = get_collection()

    if collection.count() >= len(df):
        print(f"Collection already has {collection.count()} docs. Skipping.")
        return

    docs = df["document"].tolist()
    ids = [f"rev_{i}" for i in df["review_id"].astype(str)]
    metadatas = df[["restaurant_name", "city", "cuisine", "rating", "order_type", "date"]].to_dict(orient="records")

    print(f"Embedding {len(docs)} reviews locally (no API cost)...")
    embeddings = embed_texts(docs)
    collection.add(ids=ids, documents=docs, embeddings=embeddings, metadatas=metadatas)
    print(f"Done! Ingested {collection.count()} reviews into ChromaDB.")

if __name__ == "__main__":
    ingest()
