"""
Monthly Sales Forecasting Model
--------------------------------
Predicts total sales value for future months using time series regression.
Author: Toshit Dwivedi
Project: Smart Stock Inventory Optimization
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
import os

# Configure paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "dataset", "updated_dataset.csv")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "..", "output")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def prepare_monthly_data():
    """Prepare monthly aggregated data."""
    print("\n" + "=" * 60)
    print("PREPARING MONTHLY DATA")
    print("=" * 60)
    
    df = pd.read_csv(DATA_PATH)
    
    # Aggregate by month
    monthly_sales = df.groupby('Month_Num').agg({
        'Total_Sales_Value': 'sum',
        'Units_Sold': 'sum'
    }).reset_index()
    
    print(f"✓ Monthly data prepared")
    print(f"\nMonthly Sales Summary:")
    print(monthly_sales)
    
    return monthly_sales, df


def train_forecasting_model(monthly_sales):
    """Train time series forecasting model."""
    print("\n" + "=" * 60)
    print("TRAINING FORECASTING MODEL")
    print("=" * 60)
    
    X = monthly_sales[['Month_Num']]
    y = monthly_sales['Total_Sales_Value']
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Model performance
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    
    print(f"✓ Model trained successfully")
    print(f"\nModel Coefficients:")
    print(f"  Slope (monthly change): ${model.coef_[0]:,.2f}")
    print(f"  Intercept: ${model.intercept_:,.2f}")
    
    print(f"\nModel Performance:")
    print(f"  R² Score: {r2:.4f}")
    print(f"  RMSE: ${rmse:,.2f}")
    
    if model.coef_[0] > 0:
        print(f"\n✓ Positive trend: Sales increasing by ${model.coef_[0]:,.2f} per month")
    else:
        print(f"\n⚠ Negative trend: Sales decreasing by ${abs(model.coef_[0]):,.2f} per month")
    
    return model, r2, rmse


def forecast_future_months(model, monthly_sales):
    """Forecast sales for future months."""
    print("\n" + "=" * 60)
    print("FORECASTING FUTURE MONTHS")
    print("=" * 60)
    
    # Forecast next 6 months (July to December)
    future_months = np.array([[7], [8], [9], [10], [11], [12]])
    month_names = ['July', 'August', 'September', 'October', 'November', 'December']
    
    predictions = model.predict(future_months)
    
    print("\nForecast Results:")
    print("-" * 60)
    
    forecast_df = pd.DataFrame({
        'Month_Num': future_months.flatten(),
        'Month': month_names,
        'Predicted_Sales_Value': predictions
    })
    
    for idx, row in forecast_df.iterrows():
        print(f"  {row['Month']:12} (Month {row['Month_Num']:2}): ${row['Predicted_Sales_Value']:>12,.2f}")
    
    # Calculate total forecast
    total_forecast = predictions.sum()
    print(f"\n  {'Total H2':12} {'(Jul-Dec)':10}: ${total_forecast:>12,.2f}")
    
    # Compare with H1
    h1_actual = monthly_sales['Total_Sales_Value'].sum()
    print(f"  {'Total H1':12} {'(Jan-Jun)':10}: ${h1_actual:>12,.2f}")
    print(f"  {'Growth':12} {'(H2 vs H1)':10}: {((total_forecast - h1_actual) / h1_actual * 100):>11.2f}%")
    
    return forecast_df


def visualize_forecast(monthly_sales, model, forecast_df):
    """Create visualization of forecast."""
    print("\n" + "=" * 60)
    print("GENERATING VISUALIZATIONS")
    print("=" * 60)
    
    # Prepare data for plotting
    historical_months = monthly_sales['Month_Num'].values
    historical_sales = monthly_sales['Total_Sales_Value'].values
    future_months = forecast_df['Month_Num'].values
    future_sales = forecast_df['Predicted_Sales_Value'].values
    
    # Create plot
    plt.figure(figsize=(12, 6))
    
    # Historical data
    plt.plot(historical_months, historical_sales, 'o-', 
             label='Historical Data', linewidth=2, markersize=8, color='#2E86AB')
    
    # Forecast
    plt.plot(future_months, future_sales, 's--', 
             label='Forecast', linewidth=2, markersize=8, color='#A23B72')
    
    # Trend line
    all_months = np.array(list(historical_months) + list(future_months)).reshape(-1, 1)
    trend = model.predict(all_months)
    plt.plot(all_months, trend, ':', 
             label='Trend Line', linewidth=1.5, color='#F18F01', alpha=0.7)
    
    plt.xlabel('Month Number', fontsize=12, fontweight='bold')
    plt.ylabel('Total Sales Value ($)', fontsize=12, fontweight='bold')
    plt.title('Monthly Sales Forecast - Next 6 Months', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10, loc='best')
    plt.grid(True, alpha=0.3)
    plt.xticks(range(1, 13))
    
    # Format y-axis
    ax = plt.gca()
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
    
    plt.tight_layout()
    
    output_path = os.path.join(OUTPUT_DIR, "monthly_sales_forecast.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✓ Forecast visualization saved: {output_path}")
    plt.close()


def save_forecast_report(forecast_df, monthly_sales, model, r2, rmse):
    """Save comprehensive forecast report."""
    output_path = os.path.join(OUTPUT_DIR, "sales_forecast_report.txt")
    
    with open(output_path, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write(" " * 18 + "SALES FORECAST REPORT\n")
        f.write(" " * 15 + "Monthly Sales Predictions\n")
        f.write("=" * 70 + "\n\n")
        
        f.write("1. HISTORICAL DATA SUMMARY (Jan-Jun)\n")
        f.write("-" * 70 + "\n")
        for idx, row in monthly_sales.iterrows():
            month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'][idx]
            f.write(f"  Month {row['Month_Num']} ({month_name}): ${row['Total_Sales_Value']:>12,.2f}\n")
        f.write(f"  Total H1:          ${monthly_sales['Total_Sales_Value'].sum():>12,.2f}\n")
        f.write(f"  Average/Month:     ${monthly_sales['Total_Sales_Value'].mean():>12,.2f}\n")
        
        f.write("\n2. MODEL DETAILS\n")
        f.write("-" * 70 + "\n")
        f.write(f"  Model Type: Linear Regression (Time Series)\n")
        f.write(f"  Monthly Trend: ${model.coef_[0]:,.2f}\n")
        f.write(f"  Base Value: ${model.intercept_:,.2f}\n")
        f.write(f"  R² Score: {r2:.4f}\n")
        f.write(f"  RMSE: ${rmse:,.2f}\n")
        
        f.write("\n3. FORECAST (Jul-Dec)\n")
        f.write("-" * 70 + "\n")
        for idx, row in forecast_df.iterrows():
            f.write(f"  Month {row['Month_Num']:2} ({row['Month']:9}): ${row['Predicted_Sales_Value']:>12,.2f}\n")
        f.write(f"  Total H2:          ${forecast_df['Predicted_Sales_Value'].sum():>12,.2f}\n")
        f.write(f"  Average/Month:     ${forecast_df['Predicted_Sales_Value'].mean():>12,.2f}\n")
        
        f.write("\n4. YEAR-OVER-YEAR ANALYSIS\n")
        f.write("-" * 70 + "\n")
        h1_total = monthly_sales['Total_Sales_Value'].sum()
        h2_total = forecast_df['Predicted_Sales_Value'].sum()
        annual_total = h1_total + h2_total
        growth = (h2_total - h1_total) / h1_total * 100
        
        f.write(f"  H1 Total (Jan-Jun):  ${h1_total:>12,.2f}\n")
        f.write(f"  H2 Total (Jul-Dec):  ${h2_total:>12,.2f}\n")
        f.write(f"  Annual Total:        ${annual_total:>12,.2f}\n")
        f.write(f"  H2 vs H1 Growth:     {growth:>11.2f}%\n")
        
        f.write("\n5. RECOMMENDATIONS\n")
        f.write("-" * 70 + "\n")
        if model.coef_[0] > 0:
            f.write("  ✓ Positive sales trend detected\n")
            f.write("  → Consider increasing inventory for H2\n")
            f.write("  → Plan for additional storage capacity\n")
        else:
            f.write("  ⚠ Declining sales trend detected\n")
            f.write("  → Review pricing strategy\n")
            f.write("  → Analyze market conditions\n")
        
        f.write("\n" + "=" * 70 + "\n")
    
    print(f"✓ Forecast report saved: {output_path}")
    
    # Also save CSV
    csv_path = os.path.join(OUTPUT_DIR, "monthly_sales_forecast.csv")
    forecast_df.to_csv(csv_path, index=False)
    print(f"✓ Forecast CSV saved: {csv_path}")


def main():
    """Main execution function."""
    print("\n" + "=" * 70)
    print(" " * 15 + "MONTHLY SALES FORECASTING MODEL")
    print("=" * 70)
    
    # Prepare data
    monthly_sales, df = prepare_monthly_data()
    
    # Train model
    model, r2, rmse = train_forecasting_model(monthly_sales)
    
    # Make forecast
    forecast_df = forecast_future_months(model, monthly_sales)
    
    # Visualize
    visualize_forecast(monthly_sales, model, forecast_df)
    
    # Save report
    save_forecast_report(forecast_df, monthly_sales, model, r2, rmse)
    
    print("\n" + "=" * 70)
    print(" " * 25 + "FORECAST COMPLETE!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
