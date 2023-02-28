import pandas as pd
from pytrends.request import TrendReq

# create a dataframe from the CSV file
data_master = pd.read_csv('Data/data.csv')

# extract the clients from the 'clients' column and create a new column 'client_list'
data_master['client_list'] = data_master['clients'].str.split('; ')

# create a list of unique clients
unique_clients = set([client for client_list in data_master['client_list'] for client in client_list])

# initialize the TrendReq object
pytrends = TrendReq()

# create a dictionary to store the popularity of each client
popularity_dict = {}

# loop through each client and get their popularity
for client in unique_clients:
    pytrends.build_payload([client])
    interest_over_time_df = pytrends.interest_over_time()
    if not interest_over_time_df.empty:
        popularity_dict[client] = interest_over_time_df[client].mean()

# create a new column 'popularity' in the 'data_master' dataframe
data_master['popularity'] = data_master['client_list'].apply(lambda x: sum([popularity_dict[client] for client in x if client in popularity_dict]))

# sort the dataframe by the 'popularity' column in descending order
sorted_data_master = data_master.sort_values(by='popularity', ascending=False)

# print the sorted dataframe
print(sorted_data_master)
