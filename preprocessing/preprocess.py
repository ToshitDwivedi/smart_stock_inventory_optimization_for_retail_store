import pandas as pd
import numpy as np
import os

os.makedirs("output", exist_ok=True)

df = pd.read_csv("dataset/sales_data.csv")
df = df.dropna()

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
df["Month_Num"] = df["Month"].apply(lambda x: months.index(x) + 1 if x in months else 0)
df["Total_Sales_Value"] = df["Units_Sold"] * df["Price"]
df["Revenue_Per_Unit"] = df["Total_Sales_Value"] / df["Units_Sold"]
df["Remaining_Stock"] = df["Opening_Stock"] - df["Units_Sold"]
df["Stock_Turnover_Rate"] = (df["Units_Sold"] / df["Opening_Stock"]) * 100

df.to_csv("dataset/updated_dataset.csv", index=False)
print("Preprocessing complete")
print(f"Records processed: {len(df)}")
