from google_play_scraper import app, reviews, Sort
import pandas as pd

APP_ID = "in.swiggy.android"
print("Fetching Swiggy reviews from Play Store...")

app_info = app(APP_ID)
print(f"App: {app_info['title']}")
print(f"Rating: {app_info['score']}")

result, _ = reviews(
    APP_ID,
    lang="en",
    country="in",
    sort=Sort.MOST_RELEVANT,
    count=500,
)

df = pd.DataFrame(result)
df = df[["reviewId", "content", "score", "thumbsUpCount", "at"]]
df.columns = ["review_id", "review_text", "rating", "thumbs_up", "date"]
df["restaurant_name"] = "Swiggy App"
df["city"] = "India"
df["cuisine"] = "Food Delivery"
df["order_type"] = "Delivery"

df.to_csv("data/swiggy_reviews.csv", index=False)
print(f"\nScraped {len(df)} reviews!")
print("Saved to: data/swiggy_reviews.csv")
print(df[["review_text", "rating"]].head(3))
