"""
Comprehensive Visualization Module
-----------------------------------
Creates all visualizations for sales data analysis.
Author: Toshit Dwivedi
Project: Smart Stock Inventory Optimization
"""

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# Configure paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "dataset", "updated_dataset.csv")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "..", "output", "visualizations")

# Create output directories
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "matplotlib"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "plotly"), exist_ok=True)


def load_data():
    """Load sales data."""
    df = pd.read_csv(DATA_PATH)
    print(f"✓ Data loaded: {len(df)} records")
    return df


def create_matplotlib_visualizations(df):
    """Create static visualizations using Matplotlib."""
    print("\n" + "=" * 60)
    print("CREATING MATPLOTLIB VISUALIZATIONS")
    print("=" * 60)
    
    # Set style
    plt.style.use('seaborn-v0_8-darkgrid')
    
    # 1. Bar Chart - Sales by Product
    print("\n1. Creating bar chart...")
    fig, ax = plt.subplots(figsize=(12, 6))
    product_sales = df.groupby('Product_Name')['Total_Sales_Value'].sum().sort_values(ascending=False)
    colors = plt.cm.viridis(range(len(product_sales)))
    product_sales.plot(kind='bar', ax=ax, color=colors)
    ax.set_title('Total Sales Value by Product', fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('Product Name', fontsize=12, fontweight='bold')
    ax.set_ylabel('Total Sales Value ($)', fontsize=12, fontweight='bold')
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "matplotlib", "01_sales_by_product.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("   ✓ Saved: 01_sales_by_product.png")
    
    # 2. Line Chart - Monthly Trends
    print("2. Creating line chart...")
    fig, ax = plt.subplots(figsize=(12, 6))
    monthly = df.groupby('Month_Num').agg({
        'Total_Sales_Value': 'sum',
        'Units_Sold': 'sum'
    })
    ax.plot(monthly.index, monthly['Total_Sales_Value'], marker='o', linewidth=2, markersize=8, label='Sales Value')
    ax2 = ax.twinx()
    ax2.plot(monthly.index, monthly['Units_Sold'], marker='s', linewidth=2, markersize=8, 
             color='orange', label='Units Sold')
    ax.set_title('Monthly Sales Trends', fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('Month', fontsize=12, fontweight='bold')
    ax.set_ylabel('Sales Value ($)', fontsize=12, fontweight='bold', color='blue')
    ax2.set_ylabel('Units Sold', fontsize=12, fontweight='bold', color='orange')
    ax.set_xticks(monthly.index)
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
    ax.legend(loc='upper left')
    ax2.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "matplotlib", "02_monthly_trends.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("   ✓ Saved: 02_monthly_trends.png")
    
    # 3. Scatter Plot - Price vs Units Sold
    print("3. Creating scatter plot...")
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(df['Price'], df['Units_Sold'], 
                        s=df['Opening_Stock']/2, alpha=0.6,
                        c=df['Product_ID'].astype('category').cat.codes, 
                        cmap='tab20')
    ax.set_title('Price vs Units Sold (Size = Opening Stock)', fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('Price ($)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Units Sold', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    plt.colorbar(scatter, label='Product', ax=ax)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "matplotlib", "03_price_vs_sales.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("   ✓ Saved: 03_price_vs_sales.png")
    
    # 4. Histogram - Units Sold Distribution
    print("4. Creating histogram...")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['Units_Sold'], bins=20, color='steelblue', edgecolor='black', alpha=0.7)
    ax.axvline(df['Units_Sold'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["Units_Sold"].mean():.0f}')
    ax.axvline(df['Units_Sold'].median(), color='green', linestyle='--', linewidth=2, label=f'Median: {df["Units_Sold"].median():.0f}')
    ax.set_title('Distribution of Units Sold', fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('Units Sold', fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "matplotlib", "04_units_distribution.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("   ✓ Saved: 04_units_distribution.png")
    
    # 5. Box Plot - Sales by Product
    print("5. Creating box plot...")
    fig, ax = plt.subplots(figsize=(12, 6))
    df.boxplot(column='Units_Sold', by='Product_Name', ax=ax, patch_artist=True)
    ax.set_title('Units Sold Distribution by Product', fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('Product Name', fontsize=12, fontweight='bold')
    ax.set_ylabel('Units Sold', fontsize=12, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.suptitle('')  # Remove default title
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "matplotlib", "05_sales_boxplot.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("   ✓ Saved: 05_sales_boxplot.png")
    
    print("\n✓ All Matplotlib visualizations created successfully")


def create_plotly_visualizations(df):
    """Create interactive visualizations using Plotly."""
    print("\n" + "=" * 60)
    print("CREATING PLOTLY INTERACTIVE VISUALIZATIONS")
    print("=" * 60)
    
    # 1. Interactive Bar Chart
    print("\n1. Creating interactive bar chart...")
    product_sales = df.groupby('Product_Name')['Total_Sales_Value'].sum().sort_values(ascending=False).reset_index()
    fig = px.bar(product_sales, x='Product_Name', y='Total_Sales_Value',
                 title='Total Sales Value by Product (Interactive)',
                 labels={'Total_Sales_Value': 'Sales Value ($)', 'Product_Name': 'Product'},
                 color='Total_Sales_Value',
                 color_continuous_scale='Viridis')
    fig.update_layout(xaxis_tickangle=-45, height=600)
    fig.write_html(os.path.join(OUTPUT_DIR, "plotly", "01_interactive_bar.html"))
    print("   ✓ Saved: 01_interactive_bar.html")
    
    # 2. Line Chart with Multiple Products
    print("2. Creating multi-line chart...")
    fig = px.line(df, x='Month', y='Units_Sold', color='Product_Name',
                  title='Monthly Sales Trends by Product',
                  markers=True,
                  labels={'Units_Sold': 'Units Sold', 'Month': 'Month'})
    fig.update_layout(height=600, hovermode='x unified')
    fig.write_html(os.path.join(OUTPUT_DIR, "plotly", "02_multiline_trends.html"))
    print("   ✓ Saved: 02_multiline_trends.html")
    
    # 3. 3D Scatter Plot
    print("3. Creating 3D scatter plot...")
    fig = px.scatter_3d(df, x='Price', y='Opening_Stock', z='Units_Sold',
                        color='Product_Name', size='Total_Sales_Value',
                        title='3D Analysis: Price, Stock, and Sales',
                        labels={'Price': 'Price ($)', 'Opening_Stock': 'Opening Stock', 
                               'Units_Sold': 'Units Sold'})
    fig.update_layout(height=700)
    fig.write_html(os.path.join(OUTPUT_DIR, "plotly", "03_3d_scatter.html"))
    print("   ✓ Saved: 03_3d_scatter.html")
    
    # 4. Sunburst Chart
    print("4. Creating sunburst chart...")
    df_temp = df.copy()
    df_temp['Category'] = df_temp['Product_Name'].apply(lambda x: 'Food' if x in ['Rice', 'Sugar', 'Wheat', 'Dal'] 
                                                        else 'Beverage' if x in ['Tea', 'Cold Drink']
                                                        else 'Personal Care' if x in ['Soap', 'Toothpaste']
                                                        else 'Snacks')
    fig = px.sunburst(df_temp, path=['Category', 'Product_Name'], values='Total_Sales_Value',
                      title='Sales Distribution by Category and Product')
    fig.update_layout(height=700)
    fig.write_html(os.path.join(OUTPUT_DIR, "plotly", "04_sunburst.html"))
    print("   ✓ Saved: 04_sunburst.html")
    
    # 5. Treemap
    print("5. Creating treemap...")
    product_summary = df.groupby('Product_Name').agg({
        'Total_Sales_Value': 'sum',
        'Units_Sold': 'sum'
    }).reset_index()
    fig = px.treemap(product_summary, path=['Product_Name'], values='Total_Sales_Value',
                     title='Sales Value Treemap',
                     color='Units_Sold',
                     color_continuous_scale='RdYlGn')
    fig.update_layout(height=600)
    fig.write_html(os.path.join(OUTPUT_DIR, "plotly", "05_treemap.html"))
    print("   ✓ Saved: 05_treemap.html")
    
    # 6. Heatmap
    print("6. Creating heatmap...")
    pivot = df.pivot_table(values='Units_Sold', index='Product_Name', columns='Month', aggfunc='sum')
    fig = px.imshow(pivot, 
                    title='Sales Heatmap: Products vs Months',
                    labels=dict(x='Month', y='Product', color='Units Sold'),
                    color_continuous_scale='YlOrRd')
    fig.update_layout(height=600)
    fig.write_html(os.path.join(OUTPUT_DIR, "plotly", "06_heatmap.html"))
    print("   ✓ Saved: 06_heatmap.html")
    
    # 7. Pie Chart
    print("7. Creating pie chart...")
    product_sales = df.groupby('Product_Name')['Total_Sales_Value'].sum().reset_index()
    fig = px.pie(product_sales, values='Total_Sales_Value', names='Product_Name',
                 title='Sales Contribution by Product (%)',
                 hole=0.4)  # Donut chart
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=600)
    fig.write_html(os.path.join(OUTPUT_DIR, "plotly", "07_pie_chart.html"))
    print("   ✓ Saved: 07_pie_chart.html")
    
    print("\n✓ All Plotly visualizations created successfully")


def create_dashboard_summary(df):
    """Create a comprehensive dashboard summary."""
    print("\n" + "=" * 60)
    print("CREATING DASHBOARD SUMMARY")
    print("=" * 60)
    
    # Create subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Sales by Product', 'Monthly Trends', 
                       'Top Products', 'Stock Efficiency'),
        specs=[[{'type': 'bar'}, {'type': 'scatter'}],
               [{'type': 'bar'}, {'type': 'scatter'}]]
    )
    
    # Plot 1: Sales by Product
    product_sales = df.groupby('Product_Name')['Total_Sales_Value'].sum().sort_values(ascending=False).head(10)
    fig.add_trace(go.Bar(x=product_sales.index, y=product_sales.values, name='Sales'),
                  row=1, col=1)
    
    # Plot 2: Monthly Trends
    monthly = df.groupby('Month')['Total_Sales_Value'].sum()
    fig.add_trace(go.Scatter(x=monthly.index, y=monthly.values, mode='lines+markers', name='Monthly'),
                  row=1, col=2)
    
    # Plot 3: Top Products by Units
    top_units = df.groupby('Product_Name')['Units_Sold'].sum().sort_values(ascending=False).head(10)
    fig.add_trace(go.Bar(x=top_units.index, y=top_units.values, name='Units', marker_color='lightblue'),
                  row=2, col=1)
    
    # Plot 4: Stock Efficiency
    df_temp = df.copy()
    df_temp['Efficiency'] = (df_temp['Units_Sold'] / df_temp['Opening_Stock'] * 100)
    efficiency = df_temp.groupby('Product_Name')['Efficiency'].mean().sort_values(ascending=False).head(10)
    fig.add_trace(go.Scatter(x=efficiency.index, y=efficiency.values, mode='markers', 
                            marker=dict(size=12, color=efficiency.values, colorscale='Reds', showscale=True),
                            name='Efficiency %'),
                  row=2, col=2)
    
    fig.update_layout(height=800, title_text="Sales Analytics Dashboard", showlegend=False)
    fig.write_html(os.path.join(OUTPUT_DIR, "plotly", "00_dashboard_summary.html"))
    print("✓ Dashboard summary created: 00_dashboard_summary.html")


def main():
    """Main execution function."""
    print("\n" + "=" * 70)
    print(" " * 20 + "VISUALIZATION MODULE")
    print("=" * 70)
    
    # Load data
    df = load_data()
    
    # Create Matplotlib visualizations
    create_matplotlib_visualizations(df)
    
    # Create Plotly visualizations
    create_plotly_visualizations(df)
    
    # Create dashboard
    create_dashboard_summary(df)
    
    print("\n" + "=" * 70)
    print(" " * 15 + "ALL VISUALIZATIONS COMPLETE!")
    print(f" " * 10 + f"Saved to: {OUTPUT_DIR}")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
