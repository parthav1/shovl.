import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data", help="Path to datafile to clean. WARNING: ", type=str)
arg = parser.parse_args()

df = pd.read_csv(arg.data)
df = df.replace('\n', '', regex=True)
df.to_csv('cleaned_data.csv', index=False)