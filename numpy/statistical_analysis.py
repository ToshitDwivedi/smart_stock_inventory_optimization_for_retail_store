"""
Statistical Analysis Module
----------------------------
Performs comprehensive statistical analysis on sales data using NumPy.
Author: Toshit Dwivedi
Project: Smart Stock Inventory Optimization
"""

import numpy as np
import pandas as pd
import os

# Configure paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "dataset", "updated_dataset.csv")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "..", "output")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_data():
    """Load sales data from CSV file."""
    try:
        df = pd.read_csv(DATA_PATH)
        print("✓ Data loaded successfully")
        return df
    except FileNotFoundError:
        print(f"✗ Error: File not found at {DATA_PATH}")
        return None


def statistical_operations(data):
    """
    Perform comprehensive statistical operations on sales data.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        Sales dataset
        
    Returns:
    --------
    dict : Statistical metrics
    """
    units = np.array(data["Units_Sold"])
    opening_stock = np.array(data["Opening_Stock"])
    prices = np.array(data["Price"])
    
    stats = {
        "Units Sold": {
            "Maximum": np.max(units),
            "Minimum": np.min(units),
            "Mean": np.mean(units),
            "Median": np.median(units),
            "Std Dev": np.std(units),
            "Total": np.sum(units)
        },
        "Opening Stock": {
            "Maximum": np.max(opening_stock),
            "Minimum": np.min(opening_stock),
            "Mean": np.mean(opening_stock),
            "Median": np.median(opening_stock),
            "Std Dev": np.std(opening_stock)
        },
        "Prices": {
            "Maximum": np.max(prices),
            "Minimum": np.min(prices),
            "Mean": np.mean(prices),
            "Median": np.median(prices),
            "Std Dev": np.std(prices)
        }
    }
    
    return stats


def calculate_remaining_stock(data):
    """
    Calculate remaining stock after sales using NumPy operations.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        Sales dataset
        
    Returns:
    --------
    numpy.ndarray : Remaining stock values
    """
    demand = np.array(data["Units_Sold"])
    stock = np.array(data["Opening_Stock"])
    remaining = stock - demand
    
    return remaining


def save_statistics(stats, filename="statistical_summary.txt"):
    """Save statistical analysis to output file."""
    output_path = os.path.join(OUTPUT_DIR, filename)
    
    with open(output_path, 'w') as f:
        f.write("=" * 60 + "\n")
        f.write("STATISTICAL ANALYSIS REPORT\n")
        f.write("Smart Stock Inventory Optimization\n")
        f.write("=" * 60 + "\n\n")
        
        for category, metrics in stats.items():
            f.write(f"\n{category}:\n")
            f.write("-" * 40 + "\n")
            for metric_name, value in metrics.items():
                f.write(f"  {metric_name:.<25} {value:>12.2f}\n")
    
    print(f"\n✓ Statistics saved to: {output_path}")


def main():
    """Main execution function."""
    print("\n" + "=" * 60)
    print("NUMPY STATISTICAL ANALYSIS")
    print("=" * 60 + "\n")
    
    # Load data
    df = load_data()
    if df is None:
        return
    
    # Perform statistical analysis
    print("\nPerforming statistical analysis...")
    stats = statistical_operations(df)
    
    # Display statistics
    print("\n" + "=" * 60)
    print("STATISTICAL SUMMARY")
    print("=" * 60)
    
    for category, metrics in stats.items():
        print(f"\n{category}:")
        print("-" * 40)
        for metric_name, value in metrics.items():
            print(f"  {metric_name:.<25} {value:>12.2f}")
    
    # Calculate remaining stock
    print("\n\nCalculating remaining stock...")
    remaining = calculate_remaining_stock(df)
    
    print(f"\nRemaining Stock Summary:")
    print(f"  Average Remaining: {np.mean(remaining):.2f} units")
    print(f"  Maximum Remaining: {np.max(remaining):.2f} units")
    print(f"  Minimum Remaining: {np.min(remaining):.2f} units")
    
    # Identify products with low remaining stock
    low_stock_threshold = 30
    low_stock_count = np.sum(remaining < low_stock_threshold)
    print(f"\n  Products with <{low_stock_threshold} units remaining: {low_stock_count}")
    
    # Save results
    save_statistics(stats)
    
    print("\n" + "=" * 60)
    print("Analysis Complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
