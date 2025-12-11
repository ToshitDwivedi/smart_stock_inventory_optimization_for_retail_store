import pandas as pd

# Configure paths (run from project root)
DATA_PATH = "dataset/updated_dataset.csv"

df = pd.read_csv(DATA_PATH)
df["Remaining_Stock"] = df["Opening_Stock"] - df["Units_Sold"]
print(df[["Product_Name", "Opening_Stock", "Units_Sold", "Remaining_Stock"]])
