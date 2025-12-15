import pandas as pd
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Load data
df = pd.read_csv("dataset/updated_dataset.csv")

# 1. Sorting
df_sorted = df.sort_values('Units_Sold', ascending=False)
df_sorted.to_csv("output/sorted_sales.csv", index=False)
print("Saved sorted sales data.")

# 2. Filtering
df_filtered = df[df["Units_Sold"] > 100]
df_filtered.to_csv("output/high_sales_products.csv", index=False)
print(f"Saved {len(df_filtered)} high sales records.")

# 3. Aggregation (Grouping)
df_grouped = df.groupby('Product_Name').agg({
    'Units_Sold': 'sum', 
    'Total_Sales_Value': 'sum'
})
df_grouped.to_csv("output/product_sales_summary.csv")
print("Saved product sales summary.")

# 4. Data Transformation (Adding Columns)
df["Remaining_Stock"] = df["Opening_Stock"] - df["Units_Sold"]
df["Stock_Efficiency"] = (df["Units_Sold"] / df["Opening_Stock"] * 100).round(2)
df.to_csv("output/transformed_sales_data.csv", index=False)
print("Saved transformed data with new columns.")

print("\nSample of Grouped Data:")
print(df_grouped.head())
