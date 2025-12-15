import pandas as pd
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Load data
df = pd.read_csv("dataset/updated_dataset.csv")

# 1. Pivot Table
pivot1 = df.pivot_table(
    values="Units_Sold", 
    index="Product_Name", 
    columns="Month", 
    aggfunc="sum", 
    fill_value=0
)
pivot1.to_csv("output/pivot_product_month.csv")
print("Saved pivot table.")

# 2. Merging with Categories
# Create a dummy product category dataframe
product_ids = df['Product_ID'].unique()
categories = ['Staples', 'Personal Care', 'Cooking', 'Beverage', 'Snacks']
# Assign categories cyclically
product_info = pd.DataFrame({
    "Product_ID": product_ids,
    "Category": [categories[i % len(categories)] for i in range(len(product_ids))]
})

df_merged = pd.merge(df, product_info, on="Product_ID", how="left")
df_merged.to_csv("output/merged_sales_data.csv", index=False)
print("Saved merged data with categories.")

# 3. Category Analysis
category_analysis = df_merged.groupby("Category")["Total_Sales_Value"].sum()
category_analysis.to_csv("output/category_analysis.csv")
print("Saved category analysis.")

print("\nCategory Sales:")
print(category_analysis)
