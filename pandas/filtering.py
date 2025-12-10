import pandas as pd
import os

# Use absolute path relative to script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "dataset", "updated_dataset.csv")

df = pd.read_csv(DATA_PATH)
high_sales = df[df["Units_Sold"] > 80]

print("Products with high sales (>80 units):")
print(high_sales)
