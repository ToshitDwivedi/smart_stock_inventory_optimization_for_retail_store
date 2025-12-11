"""
Array Operations Module
-----------------------
Demonstrates NumPy array operations for inventory data analysis.
Author: Toshit Dwivedi
Project: Smart Stock Inventory Optimization
"""

import numpy as np
import pandas as pd

# Configure paths (run from project root)
DATA_PATH = "dataset/updated_dataset.csv"


def demonstrate_array_operations():
    """Demonstrate various NumPy array operations."""
    
    print("\n" + "=" * 60)
    print("NUMPY ARRAY OPERATIONS DEMONSTRATION")
    print("=" * 60 + "\n")
    
    # Load data
    df = pd.read_csv(DATA_PATH)
    print("✓ Data loaded successfully\n")
    
    # Extract arrays
    units_sold = np.array(df["Units_Sold"])
    prices = np.array(df["Price"])
    opening_stock = np.array(df["Opening_Stock"])
    
    print("1. BASIC ARRAY INFORMATION")
    print("-" * 60)
    print(f"   Units Sold Array Shape: {units_sold.shape}")
    print(f"   Data Type: {units_sold.dtype}")
    print(f"   Total Elements: {units_sold.size}")
    
    print("\n2. ARRAY OPERATIONS")
    print("-" * 60)
    
    # Mathematical operations
    print(f"   Sum of all units sold: {np.sum(units_sold)}")
    print(f"   Average units sold: {np.mean(units_sold):.2f}")
    print(f"   Maximum units sold: {np.max(units_sold)}")
    print(f"   Minimum units sold: {np.min(units_sold)}")
    
    print("\n3. ARRAY TRANSFORMATIONS")
    print("-" * 60)
    
    # Calculate revenue
    total_revenue = units_sold * prices
    print(f"   Total Revenue Generated: ${np.sum(total_revenue):,.2f}")
    print(f"   Average Revenue per Sale: ${np.mean(total_revenue):,.2f}")
    
    # Stock efficiency (sales/stock ratio)
    stock_efficiency = units_sold / opening_stock
    print(f"   Average Stock Efficiency: {np.mean(stock_efficiency):.2%}")
    print(f"   Best Efficiency: {np.max(stock_efficiency):.2%}")
    
    print("\n4. CONDITIONAL OPERATIONS")
    print("-" * 60)
    
    # High sales products
    high_sales_threshold = 100
    high_sales = units_sold[units_sold > high_sales_threshold]
    print(f"   Products with >{high_sales_threshold} units sold: {len(high_sales)}")
    print(f"   Average of high sellers: {np.mean(high_sales):.2f} units")
    
    # Low stock products
    low_stock_threshold = 150
    low_stock_count = np.sum(opening_stock < low_stock_threshold)
    print(f"   Products with <{low_stock_threshold} opening stock: {low_stock_count}")
    
    print("\n5. CORRELATION ANALYSIS")
    print("-" * 60)
    
    # Correlation between price and units sold
    correlation = np.corrcoef(prices, units_sold)[0, 1]
    print(f"   Price vs Units Sold Correlation: {correlation:.4f}")
    
    if correlation < -0.3:
        print("   → Negative correlation: Higher prices → Lower sales")
    elif correlation > 0.3:
        print("   → Positive correlation: Higher prices → Higher sales")
    else:
        print("   → Weak correlation: Price has minimal impact on sales")
    
    print("\n" + "=" * 60)
    print("Array Operations Demonstration Complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    demonstrate_array_operations()
