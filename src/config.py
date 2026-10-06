import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CHAT_MODEL = "gemini-3.8-flash"
EMBED_MODEL = "all-MiniLM-L6-v2"
CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "swiggy_reviews"
CSV_PATH = "data/swiggy_reviews.csv"
TOP_K = 5

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY missing. Check your .env file.")
