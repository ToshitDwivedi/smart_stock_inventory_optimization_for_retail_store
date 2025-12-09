"""
Data Preprocessing Pipeline
----------------------------
Comprehensive data cleaning and preprocessing for sales data.
Author: Toshit Dwivedi
Project: Smart Stock Inventory Optimization
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime

# Configure paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "..", "dataset", "sales_data.csv")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "..", "dataset", "updated_dataset.csv")
REPORT_PATH = os.path.join(SCRIPT_DIR, "..", "output", "preprocessing_report.txt")

# Ensure output directory exists
os.makedirs(os.path.join(SCRIPT_DIR, "..", "output"), exist_ok=True)


def load_raw_data():
    """Load raw sales data."""
    print("\n" + "=" * 60)
    print("STEP 1: LOADING RAW DATA")
    print("=" * 60)
    
    df = pd.read_csv(INPUT_PATH)
    print(f"✓ Data loaded successfully")
    print(f"  Records: {len(df)}")
    print(f"  Columns: {len(df.columns)}")
    
    return df


def inspect_data(df):
    """Inspect data quality and structure."""
    print("\n" + "=" * 60)
    print("STEP 2: DATA INSPECTION")
    print("=" * 60)
    
    print("\nDataset Info:")
    print(f"  Shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")
    print(f"\nData Types:")
    print(df.dtypes)
    
    print(f"\nMissing Values:")
    missing = df.isnull().sum()
    if missing.sum() == 0:
        print("  ✓ No missing values found")
    else:
        print(missing[missing > 0])
    
    print(f"\nDuplicate Rows: {df.duplicated().sum()}")
    
    print(f"\nBasic Statistics:")
    print(df.describe())
    
    return missing


def add_calculated_columns(df):
    """Add calculated columns to the dataset."""
    print("\n" + "=" * 60)
    print("STEP 3: FEATURE ENGINEERING")
    print("=" * 60)
    
    # Add Total Sales Value
    df['Total_Sales_Value'] = df['Units_Sold'] * df['Price']
    print("✓ Added column: Total_Sales_Value")
    
    # Add Month Number
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df['Month_Num'] = df['Month'].apply(lambda x: month_order.index(x) + 1 if x in month_order else np.nan)
    print("✓ Added column: Month_Num")
    
    # Add Remaining Stock
    df['Remaining_Stock'] = df['Opening_Stock'] - df['Units_Sold']
    print("✓ Added column: Remaining_Stock")
    
    # Add Stock Turnover Rate (percentage)
    df['Stock_Turnover_Rate'] = (df['Units_Sold'] / df['Opening_Stock'] * 100).round(2)
    print("✓ Added column: Stock_Turnover_Rate")
    
    # Add Revenue Per Unit
    df['Revenue_Per_Unit'] = df['Total_Sales_Value'] / df['Units_Sold']
    print("✓ Added column: Revenue_Per_Unit")
    
    # Convert Month to categorical
    df['Month'] = pd.Categorical(df['Month'], categories=[m for m in month_order if m in df['Month'].unique()], ordered=True)
    print("✓ Converted Month to categorical type")
    
    print(f"\nDataset now has {len(df.columns)} columns")
    
    return df


def validate_data(df):
    """Validate data integrity."""
    print("\n" + "=" * 60)
    print("STEP 4: DATA VALIDATION")
    print("=" * 60)
    
    issues = []
    
    # Check for negative values
    if (df['Units_Sold'] < 0).any():
        issues.append("Negative units sold detected")
    else:
        print("✓ All Units_Sold values are non-negative")
    
    if (df['Price'] < 0).any():
        issues.append("Negative prices detected")
    else:
        print("✓ All Price values are non-negative")
    
    if (df['Opening_Stock'] < 0).any():
        issues.append("Negative opening stock detected")
    else:
        print("✓ All Opening_Stock values are non-negative")
    
    # Check for unrealistic values
    if (df['Stock_Turnover_Rate'] > 100).any():
        high_turnover = df[df['Stock_Turnover_Rate'] > 100]
        print(f"⚠ Warning: {len(high_turnover)} records have >100% stock turnover (sold more than stocked)")
    else:
        print("✓ All stock turnover rates are within normal range")
    
    if issues:
        print("\n⚠ Data Quality Issues Found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("\n✓ Data validation passed - No critical issues found")
    
    return issues


def generate_report(df, missing_before, issues):
    """Generate preprocessing report."""
    print("\n" + "=" * 60)
    print("STEP 5: GENERATING REPORT")
    print("=" * 60)
    
    with open(REPORT_PATH, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write(" " * 15 + "DATA PREPROCESSING REPORT\n")
        f.write(" " * 10 + "Smart Stock Inventory Optimization\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("1. INPUT DATA\n")
        f.write("-" * 70 + "\n")
        f.write(f"Source File: {INPUT_PATH}\n")
        f.write(f"Records Processed: {len(df)}\n")
        f.write(f"Original Columns: {len(df.columns) - 5}\n")  # Excluding new columns
        
        f.write("\n2. DATA QUALITY\n")
        f.write("-" * 70 + "\n")
        f.write(f"Missing Values: {missing_before.sum()}\n")
        f.write(f"Duplicate Rows: {df.duplicated().sum()}\n")
        f.write(f"Validation Issues: {len(issues)}\n")
        
        f.write("\n3. FEATURE ENGINEERING\n")
        f.write("-" * 70 + "\n")
        f.write("New Columns Added:\n")
        f.write("  - Total_Sales_Value: Product of Units_Sold × Price\n")
        f.write("  - Month_Num: Numeric representation of months\n")
        f.write("  - Remaining_Stock: Opening_Stock - Units_Sold\n")
        f.write("  - Stock_Turnover_Rate: (Units_Sold / Opening_Stock) × 100\n")
        f.write("  - Revenue_Per_Unit: Total_Sales_Value / Units_Sold\n")
        
        f.write("\n4. DATASET SUMMARY\n")
        f.write("-" * 70 + "\n")
        f.write(f"Final Records: {len(df)}\n")
        f.write(f"Final Columns: {len(df.columns)}\n")
        f.write(f"Total Sales Value: ${df['Total_Sales_Value'].sum():,.2f}\n")
        f.write(f"Total Units Sold: {df['Units_Sold'].sum():,}\n")
        f.write(f"Average Price: ${df['Price'].mean():.2f}\n")
        f.write(f"Average Stock Turnover: {df['Stock_Turnover_Rate'].mean():.2f}%\n")
        
        f.write("\n5. OUTPUT\n")
        f.write("-" * 70 + "\n")
        f.write(f"Processed Data Saved: {OUTPUT_PATH}\n")
        f.write(f"Report Saved: {REPORT_PATH}\n")
        
        f.write("\n" + "=" * 70 + "\n")
        f.write("Preprocessing completed successfully!\n")
        f.write("=" * 70 + "\n")
    
    print(f"✓ Report saved: {REPORT_PATH}")


def save_processed_data(df):
    """Save processed data to CSV."""
    print("\n" + "=" * 60)
    print("STEP 6: SAVING PROCESSED DATA")
    print("=" * 60)
    
    # Reorder columns for better readability
    column_order = [
        'Product_ID', 'Product_Name', 'Month', 'Month_Num',
        'Units_Sold', 'Price', 'Opening_Stock',
        'Total_Sales_Value', 'Revenue_Per_Unit',
        'Remaining_Stock', 'Stock_Turnover_Rate'
    ]
    
    df = df[column_order]
    df.to_csv(OUTPUT_PATH, index=False)
    
    print(f"✓ Processed data saved: {OUTPUT_PATH}")
    print(f"  Records: {len(df)}")
    print(f"  Columns: {len(df.columns)}")
    
    return df


def main():
    """Main preprocessing pipeline."""
    print("\n" + "=" * 70)
    print(" " * 15 + "DATA PREPROCESSING PIPELINE")
    print("=" * 70)
    
    # Step 1: Load data
    df = load_raw_data()
    
    # Step 2: Inspect data
    missing_before = inspect_data(df)
    
    # Step 3: Add calculated columns
    df = add_calculated_columns(df)
    
    # Step 4: Validate data
    issues = validate_data(df)
    
    # Step 5: Generate report
    generate_report(df, missing_before, issues)
    
    # Step 6: Save processed data
    df = save_processed_data(df)
    
    print("\n" + "=" * 70)
    print(" " * 20 + "PREPROCESSING COMPLETE!")
    print("=" * 70 + "\n")
    
    return df


if __name__ == "__main__":
    main()
