from src.embedder import get_collection, embed_texts
from src.config import TOP_K

def retrieve(query: str, top_k: int = TOP_K, where: dict | None = None):
    collection = get_collection()
    q_emb = embed_texts([query])[0]
    results = collection.query(query_embeddings=[q_emb], n_results=top_k, where=where)
    hits = []
    for doc, meta, dist in zip(
        results["documents"][0], results["metadatas"][0], results["distances"][0]
    ):
        hits.append({"document": doc, "metadata": meta, "distance": dist})
    return hits
