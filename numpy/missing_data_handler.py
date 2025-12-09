"""
Missing Data Handler Module
----------------------------
Demonstrates handling missing values with NumPy and Pandas.
Author: Toshit Dwivedi
Project: Smart Stock Inventory Optimization
"""

import pandas as pd
import numpy as np
import os

# Configure paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "dataset", "updated_dataset.csv")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "..", "output")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def demonstrate_missing_data_handling():
    """Demonstrate various techniques for handling missing data."""
    
    print("\n" + "=" * 60)
    print("MISSING DATA HANDLING DEMONSTRATION")
    print("=" * 60 + "\n")
    
    # Load data
    df = pd.read_csv(DATA_PATH)
    print("✓ Original data loaded\n")
    
    print("Step 1: Original Dataset")
    print("-" * 60)
    print(f"Total records: {len(df)}")
    print(f"Null values: {df.isnull().sum().sum()}")
    
    # Create a copy for demonstration
    df_demo = df.copy()
    
    print("\n\nStep 2: Intentionally Insert Missing Values (for demonstration)")
    print("-" * 60)
    
    # Insert NaN values at specific positions
    df_demo.loc[0, "Units_Sold"] = np.nan
    df_demo.loc[2, "Opening_Stock"] = np.nan
    df_demo.loc[5, "Price"] = np.nan
    df_demo.loc[10, "Units_Sold"] = np.nan
    df_demo.loc[15, "Opening_Stock"] = np.nan
    
    print("Missing values inserted:")
    print(df_demo.isnull().sum())
    
    # Check for NaN in numpy array
    print("\n\nStep 3: Detect NaN Values with NumPy")
    print("-" * 60)
    units = df_demo["Units_Sold"].values
    print(f"NaN positions in Units_Sold: {np.where(np.isnan(units))[0]}")
    print(f"Total NaN values: {np.sum(np.isnan(units))}")
    
    print("\n\nStep 4: Handle Missing Data - Method 1 (Drop Rows)")
    print("-" * 60)
    df_dropped_rows = df_demo.dropna()
    print(f"Records after dropping rows: {len(df_dropped_rows)}")
    print(f"Records removed: {len(df_demo) - len(df_dropped_rows)}")
    
    print("\n\nStep 5: Handle Missing Data - Method 2 (Drop Columns)")
    print("-" * 60)
    df_dropped_cols = df_demo.dropna(axis=1)
    print(f"Columns remaining: {len(df_dropped_cols.columns)}")
    print(f"Columns: {list(df_dropped_cols.columns)}")
    
    print("\n\nStep 6: Handle Missing Data - Method 3 (Fill with Mean)")
    print("-" * 60)
    df_filled = df_demo.copy()
    
    # Fill numeric columns with mean
    numeric_cols = df_filled.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df_filled[col].isnull().any():
            mean_value = df_filled[col].mean()
            df_filled[col] = df_filled[col].fillna(mean_value)
            print(f"  {col}: Filled {df_demo[col].isnull().sum()} values with mean ({mean_value:.2f})")
    
    print(f"\nTotal null values after filling: {df_filled.isnull().sum().sum()}")
    
    print("\n\nStep 7: Handle Missing Data - Method 4 (Forward Fill)")
    print("-" * 60)
    df_ffill = df_demo.copy()
    df_ffill = df_ffill.fillna(method='ffill')
    print(f"Null values after forward fill: {df_ffill.isnull().sum().sum()}")
    
    print("\n\nStep 8: Handle Missing Data - Method 5 (Backward Fill)")
    print("-" * 60)
    df_bfill = df_demo.copy()
    df_bfill = df_bfill.fillna(method='bfill')
    print(f"Null values after backward fill: {df_bfill.isnull().sum().sum()}")
    
    # Save cleaned data
    output_path = os.path.join(OUTPUT_DIR, "cleaned_data_demo.csv")
    df_filled.to_csv(output_path, index=False)
    print(f"\n✓ Cleaned data saved to: {output_path}")
    
    print("\n" + "=" * 60)
    print("RECOMMENDED APPROACH FOR THIS DATASET:")
    print("=" * 60)
    print("→ Use Mean Imputation for numerical columns")
    print("→ Original dataset has no missing values")
    print("→ Always validate data before and after cleaning")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    demonstrate_missing_data_handling()
