import pandas as pd

df = pd.read_csv(input("Enter data file path: "))
grouped = df.groupby("category")

for name, group in grouped:
    filename = f"{name}.csv"
    group.to_csv(filename, index=False)