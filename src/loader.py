import pandas as pd
from src.config import CSV_PATH

def load_reviews() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH)
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce").fillna(0).astype(int)
    df["document"] = df.apply(
        lambda r: (
            f"Restaurant: {r['restaurant_name']} | City: {r['city']} | "
            f"Cuisine: {r['cuisine']} | Rating: {r['rating']}/5 | "
            f"Order Type: {r['order_type']} | Date: {r['date']}\n"
            f"Review: {r['review_text']}"
        ),
        axis=1,
    )
    return df
