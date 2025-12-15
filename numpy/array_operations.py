import numpy as np
import pandas as pd

# Load data
df = pd.read_csv("dataset/updated_dataset.csv")

# Convert columns to numpy arrays
units = np.array(df["Units_Sold"])
prices = np.array(df["Price"])
stock = np.array(df["Opening_Stock"])

# Calculate Revenue and Stock Turnover
revenue = units * prices
stock_turnover = (units / stock) * 100

# Add new columns to dataframe
df['Revenue_Calculated'] = revenue
df['Stock_Turnover_Pct'] = stock_turnover

# Save the result
df.to_csv("output/transformed_sales_data.csv", index=False)

print("Array Operations:")
print(f"Total Revenue: ${np.sum(revenue):.2f}")
print(f"Average Stock Turnover: {np.mean(stock_turnover):.2f}%")

# Low stock analysis
low_stock_threshold = 150
low_stock_count = np.sum(stock < low_stock_threshold)
print(f"Products with < {low_stock_threshold} opening stock: {low_stock_count}")

# Correlation analysis
correlation = np.corrcoef(prices, units)[0, 1]
print(f"Price vs Units Sold Correlation: {correlation:.4f}")
