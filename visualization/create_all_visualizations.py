import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import os

# Create output directories
os.makedirs("output/visualizations/matplotlib", exist_ok=True)
os.makedirs("output/visualizations/plotly", exist_ok=True)

# Load data
df = pd.read_csv("dataset/updated_dataset.csv")

# 1. Bar Chart: Total Sales by Product
product_sales = df.groupby('Product_Name')['Total_Sales_Value'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
product_sales.plot(kind='bar', color='steelblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales Value')
plt.tight_layout()
plt.savefig('output/visualizations/matplotlib/sales_by_product.png')
plt.close()

# 2. Line Chart: Monthly Sales Trend
monthly_sales = df.groupby('Month')['Units_Sold'].sum()
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', marker='o', color='green')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.grid(True)
plt.tight_layout()
plt.savefig('output/visualizations/matplotlib/monthly_trend.png')
plt.close()

# 3. Scatter Plot: Price vs Units Sold
plt.figure(figsize=(10, 6))
plt.scatter(df['Price'], df['Units_Sold'], alpha=0.5)
plt.title('Price vs Units Sold')
plt.xlabel('Price')
plt.ylabel('Units Sold')
plt.tight_layout()
plt.savefig('output/visualizations/matplotlib/price_vs_sales_scatter.png')
plt.close()

# 4. Histogram: Units Sold Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Units_Sold'], bins=15, color='orange', edgecolor='black')
plt.title('Distribution of Units Sold')
plt.xlabel('Units Sold')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('output/visualizations/matplotlib/units_distribution.png')
plt.close()

print("Matplotlib visualizations created.")

# Plotly Interactive Charts
# 1. Interactive Bar
fig = px.bar(df.groupby('Product_Name')['Units_Sold'].sum().reset_index(), 
             x='Product_Name', y='Units_Sold', title='Units Sold by Product')
fig.write_html('output/visualizations/plotly/interactive_bar.html')

# 2. Interactive Line
fig = px.line(df.groupby('Month_Num')['Total_Sales_Value'].sum().reset_index(),
              x='Month_Num', y='Total_Sales_Value', title='Monthly Sales Value')
fig.write_html('output/visualizations/plotly/interactive_trend.html')

# 3. Interactive Pie
fig = px.pie(df.groupby('Product_Name')['Total_Sales_Value'].sum().reset_index(),
             values='Total_Sales_Value', names='Product_Name', title='Sales Distribution')
fig.write_html('output/visualizations/plotly/interactive_pie.html')

print("Plotly visualizations created.")
