from src.retriever import retrieve
from src.llm import generate_answer

query = "What are the most common complaints about Swiggy?"
print(f"Q: {query}\n")

hits = retrieve(query, top_k=5)
print(f"Retrieved {len(hits)} reviews.\n")

answer = generate_answer(query, hits, [])
print("=" * 60)
print("ANSWER:")
print("=" * 60)
print(answer)
