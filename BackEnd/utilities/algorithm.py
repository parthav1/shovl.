import os
import math
<<<<<<< Updated upstream
import pandas as pd
=======
import datetime
>>>>>>> Stashed changes
from supabase import create_client
from dotenv import load_dotenv
load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)
response  = supabase.table('shovl_arvr').select("*").execute()
arvr_vendors = response.data

rating_weight = 0.602
num_reviews_weight = 0.1
sentiment_weight = 0.25
age_weight = 0.05
weight = 10
overall_average_rating = sum(vendor['rating'] for vendor in arvr_vendors) / len(arvr_vendors)

for i, vendor in enumerate(sorted(arvr_vendors, key=lambda x: x['shovl_score'], reverse=True)):
    if int(vendor['review_count']) > 0:
        vendor_review_cap =8

    vendor_id = vendor['id']
    bayesian_average_rating = (overall_average_rating * weight + vendor['rating'] * vendor_review_cap) / (vendor['review_count'] + weight)
    sentiment_score = vendor['sentiment_score']
    current_year = datetime.datetime.now().year
    age = current_year - int(vendor['founded'])
    age_score = 1 / math.log(age + 1)

    score = (rating_weight * bayesian_average_rating +
             num_reviews_weight * vendor['review_count'] +
             sentiment_weight * sentiment_score +
             age_weight * age_score)
    scaled_score = min(score * 20, 100)
    supabase.table("shovl_arvr").update({"shovl_score": scaled_score, "ranking": i+1}).eq("id", vendor_id).execute()
    print(f"Ranking: {i+1}, Vendor: {vendor_id}, Score: {scaled_score}")



