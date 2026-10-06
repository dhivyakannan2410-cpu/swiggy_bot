# 🍔 Swiggy Customer Feedback Chatbot

A RAG-powered chatbot that answers questions about real Swiggy customer reviews scraped from the Google Play Store.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![Gemini](https://img.shields.io/badge/Gemini-3.8_Flash-orange)
![ChromaDB](https://img.shields.io/badge/ChromaDB-1.x-green)

## 🎯 What It Does

Ask natural language questions about 500+ real Swiggy reviews and get grounded, cited answers:

- "What are the most common complaints about Swiggy?"
- "Are there delivery problems?"
- "Summarize refund-related complaints"

## 🏗️ Architecture

    User Question → Streamlit UI → Embed Query (MiniLM-L6)
        → ChromaDB (500 reviews) → Top 5 hits
        → Gemini 3.8 Flash → Grounded answer with citations

## 🛠️ Tech Stack

| Layer | Tool | Cost |
|-------|------|------|
| Data | google-play-scraper | Free |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) | Free, local |
| Vector DB | ChromaDB | Free, local |
| LLM | Google Gemini 3.8 Flash | Free tier |
| UI | Streamlit | Free |

**Total cost: ₹0** — no credit card required.

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/swiggy_bot.git
cd swiggy_bot

# 2. Install
pip install -r requirements.txt

# 3. Get a free Gemini API key: https://aistudio.google.com/app/apikey
cp .env.example .env
# Edit .env and paste your key

# 4. Scrape real reviews
python scrape_reviews.py

# 5. Load into vector DB
python -m src.embedder

# 6. Run the chatbot
python -m streamlit run app.py