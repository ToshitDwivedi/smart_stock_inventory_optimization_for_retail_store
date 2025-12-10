import pandas as pd
import os

# Use absolute path relative to script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "dataset", "updated_dataset.csv")

df = pd.read_csv(DATA_PATH)

# Sorting
sorted_df = df.sort_values("Units_Sold", ascending=False)
print("Products sorted by Units Sold (High to Low):")
print(sorted_df)



# Aggregate functions
print("SUM of Units Sold:", df["Units_Sold"].sum())
print("MEAN of Units Sold:", df["Units_Sold"].mean())
print("MAX Units Sold:", df["Units_Sold"].max())
print("MIN Units Sold:", df["Units_Sold"].min())
print("STD (Standard Deviation):", df["Units_Sold"].std())


print("\nTotal Sales Value by Month:")
print(df.groupby("Month")["Total_Sales_Value"].sum())

