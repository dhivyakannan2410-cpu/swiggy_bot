import google.generativeai as genai
from src.config import GEMINI_API_KEY, CHAT_MODEL

genai.configure(api_key=GEMINI_API_KEY)
_model = genai.GenerativeModel(CHAT_MODEL)

SYSTEM_PROMPT = """You are Swiggy's Customer Feedback Analyst chatbot.
You answer ONLY from the retrieved customer reviews provided as CONTEXT.
Rules:
1. If the context does not contain the answer, say: "I couldn't find relevant feedback."
2. Always cite the review text when referencing.
3. Be concise, structured, and business-friendly.
4. Never hallucinate reviews or statistics.
"""

def build_context(hits):
    blocks = []
    for i, h in enumerate(hits, 1):
        m = h["metadata"]
        blocks.append(f"[Review {i}] Rating {m['rating']}/5 | {m['date']}\n{h['document']}")
    return "\n\n---\n\n".join(blocks)

def generate_answer(user_query, hits, history):
    context = build_context(hits)
    history_text = ""
    for msg in history[-6:]:
        role = "User" if msg["role"] == "user" else "Assistant"
        history_text += f"{role}: {msg['content']}\n"

    full_prompt = f"""{SYSTEM_PROMPT}

CONVERSATION HISTORY:
{history_text}

CONTEXT (retrieved reviews):
{context}

USER QUESTION: {user_query}

ANSWER:"""

    try:
        resp = _model.generate_content(full_prompt)
        return resp.text
    except Exception as e:
        return f"Gemini API error: {e}"
