import os
import math
import datetime
import json
from supabase import create_client
from dotenv import load_dotenv
load_dotenv()
#
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)
response  = supabase.table('shovl_ai').select("*").execute()
arvr_vendors = response.data

#Traverse through array find, merge and delete duplicate
for i, vendor1 in enumerate(arvr_vendors):
    for j, vendor2 in enumerate(arvr_vendors[i+1:], start=i+1):
        if vendor1['company_name'] == vendor2['company_name']:
            vendor1['review_count'] +=(vendor2['review_count'])
            vendor1['rating'] = (vendor1['rating'] * vendor1['review_count'] + vendor2['rating'] * vendor2['review_count']) / (vendor1['review_count'] + vendor2['review_count'])
            vendor1['sentiment_score'] = (vendor1['sentiment_score'] * vendor1['review_count'] + vendor2['sentiment_score'] * vendor2['review_count']) / (vendor1['review_count'] + vendor2['review_count'])

            supabase.table('shovl_ai').delete().eq('id', vendor2['id']).execute()
