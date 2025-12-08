import pandas as pd

df = pd.read_csv("../original_files/updated_dataset.csv")

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

