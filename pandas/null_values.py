import pandas as pd

# Configure paths (run from project root)
DATA_PATH = "dataset/updated_dataset.csv"

df = pd.read_csv(DATA_PATH)
print("Missing values in each column:")
print(df.isnull().sum())
