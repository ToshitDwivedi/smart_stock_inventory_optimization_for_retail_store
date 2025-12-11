"""
Advanced Data Analysis Module
------------------------------
Demonstrates advanced Pandas operations including merging, pivoting, and analysis.
Author: Toshit Dwivedi
Project: Smart Stock Inventory Optimization
"""

import pandas as pd
import numpy as np
import os

# Configure paths (run from project root)
DATA_PATH = "dataset/updated_dataset.csv"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def pivot_operations(df):
    """Demonstrate pivot table operations."""
    print("\n" + "=" * 60)
    print("PIVOT TABLE OPERATIONS")
    print("=" * 60)
    
    # Pivot 1: Product by Month
    print("\n1. Units Sold - Products vs Months")
    print("-" * 60)
    pivot1 = df.pivot_table(
        values="Units_Sold",
        index="Product_Name",
        columns="Month",
        aggfunc="sum",
        fill_value=0
    )
    print(pivot1.head(10))
    
    # Pivot 2: Multiple aggregations
    print("\n\n2. Sales Value Summary by Product")
    print("-" * 60)
    pivot2 = df.pivot_table(
        values="Total_Sales_Value",
        index="Product_Name",
        aggfunc=["sum", "mean", "count"]
    ).round(2)
    print(pivot2.head(10))
    
    # Save pivot tables
    pivot1.to_csv(os.path.join(OUTPUT_DIR, "pivot_product_month.csv"))
    pivot2.to_csv(os.path.join(OUTPUT_DIR, "pivot_product_summary.csv"))
    
    return pivot1, pivot2


def merge_operations(df):
    """Demonstrate merging with additional data."""
    print("\n\n" + "=" * 60)
    print("DATA MERGING OPERATIONS")
    print("=" * 60)
    
    # Create additional product information
    product_info = pd.DataFrame({
        "Product_ID": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010"],
        "Category": ["Staples", "Staples", "Personal Care", "Cooking", "Beverage", 
                    "Beverage", "Personal Care", "Staples", "Cooking", "Staples"],
        "Brand": ["Brand A", "Brand B", "Brand C", "Brand A", "Brand D",
                 "Brand E", "Brand F", "Brand G", "Brand H", "Brand I"],
        "Supplier": ["Supplier 1", "Supplier 2", "Supplier 3", "Supplier 1", "Supplier 4",
                    "Supplier 5", "Supplier 6", "Supplier 7", "Supplier 8", "Supplier 9"]
    })
    
    print("\n1. Additional Product Information")
    print("-" * 60)
    print(product_info)
    
    # Merge with main data
    print("\n\n2. Merged Dataset")
    print("-" * 60)
    df_merged = pd.merge(df, product_info, on="Product_ID", how="left")
    print(f"Original shape: {df.shape}")
    print(f"Merged shape: {df_merged.shape}")
    print(f"New columns: {[col for col in df_merged.columns if col not in df.columns]}")
    
    # Category-wise analysis
    print("\n\n3. Category-wise Sales Analysis")
    print("-" * 60)
    category_analysis = df_merged.groupby("Category").agg({
        "Units_Sold": ["sum", "mean"],
        "Total_Sales_Value": ["sum", "mean"],
        "Product_ID": "count"
    }).round(2)
    category_analysis.columns = ["Total_Units", "Avg_Units", "Total_Revenue", "Avg_Revenue", "Products_Count"]
    print(category_analysis)
    
    # Save merged data
    df_merged.to_csv(os.path.join(OUTPUT_DIR, "merged_sales_data.csv"), index=False)
    category_analysis.to_csv(os.path.join(OUTPUT_DIR, "category_analysis.csv"))
    
    return df_merged, category_analysis


def time_series_analysis(df):
    """Analyze trends over time."""
    print("\n\n" + "=" * 60)
    print("TIME SERIES ANALYSIS")
    print("=" * 60)
    
    # Monthly trends
    monthly_trend = df.groupby("Month_Num").agg({
        "Units_Sold": "sum",
        "Total_Sales_Value": "sum",
        "Opening_Stock": "mean"
    }).round(2)
    
    # Add month names
    month_names = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun"}
    monthly_trend["Month"] = monthly_trend.index.map(month_names)
    
    print("\n1. Monthly Performance Trend")
    print("-" * 60)
    print(monthly_trend)
    
    # Calculate growth rates
    monthly_trend["Sales_Growth_%"] = monthly_trend["Units_Sold"].pct_change() * 100
    monthly_trend["Revenue_Growth_%"] = monthly_trend["Total_Sales_Value"].pct_change() * 100
    
    print("\n\n2. Month-over-Month Growth")
    print("-" * 60)
    print(monthly_trend[["Month", "Sales_Growth_%", "Revenue_Growth_%"]].round(2))
    
    # Product-wise trends
    print("\n\n3. Top 5 Products with Highest Growth")
    print("-" * 60)
    product_trend = df.groupby(["Product_Name", "Month_Num"])["Units_Sold"].sum().unstack(fill_value=0)
    product_growth = ((product_trend[6] - product_trend[1]) / product_trend[1] * 100).sort_values(ascending=False)
    print(product_growth.head())
    
    # Save time series data
    monthly_trend.to_csv(os.path.join(OUTPUT_DIR, "monthly_trend_analysis.csv"))
    
    return monthly_trend, product_growth


def statistical_summary(df):
    """Generate comprehensive statistical summary."""
    print("\n\n" + "=" * 60)
    print("STATISTICAL SUMMARY")
    print("=" * 60)
    
    numeric_cols = ["Units_Sold", "Price", "Opening_Stock", "Total_Sales_Value"]
    
    summary = df[numeric_cols].describe().T
    summary["range"] = summary["max"] - summary["min"]
    summary["cv"] = (summary["std"] / summary["mean"] * 100).round(2)  # Coefficient of variation
    
    print("\nDetailed Statistics:")
    print("-" * 60)
    print(summary)
    
    # Correlation analysis
    print("\n\nCorrelation Matrix:")
    print("-" * 60)
    correlation = df[numeric_cols].corr().round(3)
    print(correlation)
    
    # Save statistical summary
    summary.to_csv(os.path.join(OUTPUT_DIR, "statistical_summary.csv"))
    correlation.to_csv(os.path.join(OUTPUT_DIR, "correlation_matrix.csv"))
    
    return summary, correlation


def main():
    """Main execution function."""
    print("\n" + "=" * 70)
    print(" " * 15 + "ADVANCED DATA ANALYSIS")
    print("=" * 70)
    
    # Load data
    df = pd.read_csv(DATA_PATH)
    print(f"\n✓ Data loaded: {df.shape[0]} records")
    
    # Pivot operations
    pivot1, pivot2 = pivot_operations(df)
    
    # Merge operations
    df_merged, category_analysis = merge_operations(df)
    
    # Time series analysis
    monthly_trend, product_growth = time_series_analysis(df)
    
    # Statistical summary
    summary, correlation = statistical_summary(df)
    
    print("\n" + "=" * 70)
    print(" " * 20 + "ANALYSIS COMPLETE!")
    print(f" " * 15 + "All results saved to: output/")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
