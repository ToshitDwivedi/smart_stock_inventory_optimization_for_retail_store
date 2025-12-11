"""
Data Manipulation Module
-------------------------
Demonstrates comprehensive Pandas operations for sales data analysis.
Author: Toshit Dwivedi
Project: Smart Stock Inventory Optimization
"""

import pandas as pd
import os

# Configure paths (run from project root)
DATA_PATH = "dataset/updated_dataset.csv"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_and_explore_data():
    """Load and display basic information about the dataset."""
    df = pd.read_csv(DATA_PATH)
    
    print("\n" + "=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)
    print(f"\nShape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nMemory Usage: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
    
    return df


def filtering_operations(df):
    """Demonstrate various filtering operations."""
    print("\n\n" + "=" * 60)
    print("FILTERING OPERATIONS")
    print("=" * 60)
    
    # Filter 1: High sales products
    print("\n1. Products with high sales (>100 units)")
    print("-" * 60)
    high_sales = df[df["Units_Sold"] > 100]
    print(f"   Found: {len(high_sales)} products")
    print(f"   Average sales: {high_sales['Units_Sold'].mean():.2f} units")
    
    # Filter 2: Premium products
    print("\n2. Premium products (Price > 50)")
    print("-" * 60)
    premium = df[df["Price"] > 50]
    print(f"   Found: {len(premium)} products")
    print(f"   Average price: ${premium['Price'].mean():.2f}")
    
    # Filter 3: Multiple conditions
    print("\n3. High value products (Price > 50 AND Units_Sold > 80)")
    print("-" * 60)
    high_value = df[(df["Price"] > 50) & (df["Units_Sold"] > 80)]
    print(f"   Found: {len(high_value)} products")
    
    # Filter 4: Products by month
    print("\n4. Products sold in specific months")
    print("-" * 60)
    jan_sales = df[df["Month"] == "Jan"]
    print(f"   January sales: {len(jan_sales)} records")
    print(f"   Total units: {jan_sales['Units_Sold'].sum()}")
    
    return high_sales, premium, high_value


def aggregation_operations(df):
    """Demonstrate grouping and aggregation operations."""
    print("\n\n" + "=" * 60)
    print("AGGREGATION OPERATIONS")
    print("=" * 60)
    
    # Group by product
    print("\n1. Total sales by product")
    print("-" * 60)
    product_sales = df.groupby("Product_Name")["Total_Sales_Value"].sum().sort_values(ascending=False)
    print(product_sales.head(10))
    
    # Group by month
    print("\n\n2. Monthly sales summary")
    print("-" * 60)
    monthly_sales = df.groupby("Month").agg({
        "Units_Sold": ["sum", "mean", "max"],
        "Total_Sales_Value": ["sum", "mean"]
    }).round(2)
    print(monthly_sales)
    
    # Group by product and month
    print("\n\n3. Product performance by month")
    print("-" * 60)
    product_month = df.groupby(["Product_Name", "Month"])["Units_Sold"].sum().head(15)
    print(product_month)
    
    return product_sales, monthly_sales


def sorting_operations(df):
    """Demonstrate sorting operations."""
    print("\n\n" + "=" * 60)
    print("SORTING OPERATIONS")
    print("=" * 60)
    
    # Sort by units sold
    print("\n1. Top 10 best-selling records")
    print("-" * 60)
    top_sellers = df.sort_values("Units_Sold", ascending=False).head(10)
    print(top_sellers[["Product_Name", "Month", "Units_Sold", "Total_Sales_Value"]])
    
    # Sort by multiple columns
    print("\n\n2. Sorted by Product and Month")
    print("-" * 60)
    sorted_multi = df.sort_values(["Product_Name", "Month_Num"]).head(10)
    print(sorted_multi[["Product_Name", "Month", "Units_Sold"]])
    
    return top_sellers


def data_transformation(df):
    """Add calculated columns and transform data."""
    print("\n\n" + "=" * 60)
    print("DATA TRANSFORMATION")
    print("=" * 60)
    
    # Create a copy
    df_transformed = df.copy()
    
    # Add remaining stock
    df_transformed["Remaining_Stock"] = df_transformed["Opening_Stock"] - df_transformed["Units_Sold"]
    print("\n1. Added 'Remaining_Stock' column")
    
    # Add stock efficiency
    df_transformed["Stock_Efficiency"] = (df_transformed["Units_Sold"] / df_transformed["Opening_Stock"] * 100).round(2)
    print("2. Added 'Stock_Efficiency' column (% of stock sold)")
    
    # Add revenue per unit
    df_transformed["Revenue_Per_Unit"] = df_transformed["Total_Sales_Value"] / df_transformed["Units_Sold"]
    print("3. Added 'Revenue_Per_Unit' column")
    
    # Add stockout risk flag
    df_transformed["Stockout_Risk"] = df_transformed["Stock_Efficiency"] > 70
    print("4. Added 'Stockout_Risk' flag (efficiency > 70%)")
    
    print(f"\n✓ Transformed dataset shape: {df_transformed.shape}")
    print(f"\nSample of new columns:")
    print(df_transformed[["Product_Name", "Remaining_Stock", "Stock_Efficiency", "Stockout_Risk"]].head())
    
    return df_transformed


def save_analysis_results(df, product_sales, monthly_sales):
    """Save analysis results to output files."""
    print("\n\n" + "=" * 60)
    print("SAVING RESULTS")
    print("=" * 60)
    
    # Save transformed data
    output_path = os.path.join(OUTPUT_DIR, "transformed_sales_data.csv")
    df.to_csv(output_path, index=False)
    print(f"\n✓ Transformed data saved: {output_path}")
    
    # Save product sales summary
    output_path = os.path.join(OUTPUT_DIR, "product_sales_summary.csv")
    product_sales.to_csv(output_path)
    print(f"✓ Product sales summary saved: {output_path}")
    
    # Save monthly summary
    output_path = os.path.join(OUTPUT_DIR, "monthly_sales_summary.csv")
    monthly_sales.to_csv(output_path)
    print(f"✓ Monthly sales summary saved: {output_path}")


def main():
    """Main execution function."""
    print("\n" + "=" * 70)
    print(" " * 15 + "PANDAS DATA MANIPULATION")
    print("=" * 70)
    
    # Load data
    df = load_and_explore_data()
    
    # Filtering
    high_sales, premium, high_value = filtering_operations(df)
    
    # Aggregation
    product_sales, monthly_sales = aggregation_operations(df)
    
    # Sorting
    top_sellers = sorting_operations(df)
    
    # Transformation
    df_transformed = data_transformation(df)
    
    # Save results
    save_analysis_results(df_transformed, product_sales, monthly_sales)
    
    print("\n" + "=" * 70)
    print(" " * 20 + "ANALYSIS COMPLETE!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
