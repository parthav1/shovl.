import os
import math

from supabase import create_client # type: ignore
from textblob import TextBlob # type: ignore
from dotenv import load_dotenv
load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key) # type: ignore
response  = supabase.table('shovl_ai').select("*").execute()
arvr_vendors = response.data

review_text = []

for vendor in arvr_vendors:
    rating = vendor['reviews']
    vendor_id = vendor['id']
    for rating in rating:
        review_text.append(rating['text'])
    scores = []
    for text in review_text:
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        scores.append(sentiment_score)
    overall_score = sum(scores) / len(scores)
    print(supabase.table("shovl_ai").update({"sentiment_score": overall_score}).eq("id", vendor_id).execute())
