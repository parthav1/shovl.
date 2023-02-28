import os
import math
import pandas as pd
from supabase import create_client
from dotenv import load_dotenv
load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)
response  = supabase.table('shovl_arvr').select("*").execute()
arvr_vendors = response.data

for vendor in arvr_vendors:
    rating= vendor['company_rating']
    print(vendor['company_name']);


