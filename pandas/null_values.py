import pandas as pd

df = pd.read_csv("../dataset/updated_dataset.csv")
print("Missing values in each column:")
print(df.isnull().sum())
