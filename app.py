import warnings
warnings.filterwarnings("ignore")

import streamlit as st
from src.retriever import retrieve
from src.llm import generate_answer

st.set_page_config(
    page_title="Swiggy Feedback Chatbot",
    page_icon="🍔",
    layout="wide"
)

st.title("🍔 Swiggy Customer Feedback Chatbot")
st.caption("RAG-powered · 500 real Play Store reviews · ChromaDB + Gemini")

# --- Sidebar ---
with st.sidebar:
    st.header("🔎 Options")
    min_rating = st.slider("Minimum Rating", 1, 5, 1)
    top_k = st.slider("Reviews retrieved", 3, 10, 5)

    st.markdown("---")
    st.markdown("### 💡 Try asking:")
    st.markdown("- What are the most common complaints?")
    st.markdown("- What do users love about Swiggy?")
    st.markdown("- Summarize refund issues")
    st.markdown("- Are there delivery problems?")
    st.markdown("- Complaints about Instamart?")

    st.markdown("---")
    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.rerun()

# --- Chat History ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Chat Input ---
if prompt := st.chat_input("Ask about Swiggy reviews..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    where = {"rating": {"$gte": min_rating}} if min_rating > 1 else None

    with st.chat_message("assistant"):
        with st.spinner("Analyzing reviews..."):
            hits = retrieve(prompt, top_k=top_k, where=where)
            answer = generate_answer(prompt, hits, st.session_state.messages)
        st.markdown(answer)

        with st.expander(f"📚 Retrieved {len(hits)} source reviews"):
            for i, h in enumerate(hits, 1):
                m = h["metadata"]
                st.markdown(
                    f"**{i}. ⭐ {m['rating']}/5** — {m['date']}\n\n"
                    f"> {h['document'].splitlines()[-1][:300]}"
                )

    st.session_state.messages.append({"role": "assistant", "content": answer})