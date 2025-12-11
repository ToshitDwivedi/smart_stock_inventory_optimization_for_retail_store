import pandas as pd

# Configure paths (run from project root)
DATA_PATH = "dataset/updated_dataset.csv"

df = pd.read_csv(DATA_PATH)
high_sales = df[df["Units_Sold"] > 80]

print("Products with high sales (>80 units):")
print(high_sales)
