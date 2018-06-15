import pandas as pd
df = pd.read_csv("/home/amidezcod/Downloads/ZILLOW-C2655_MLPF4B.csv")

df.set_index('Date' , inplace=True)
df.to_csv("mew.csv")
df = pd.read_csv("mew.csv")
print(df.head())

df = pd.read_csv("mew.csv" ,index_col=0)
pfrint(df.head())