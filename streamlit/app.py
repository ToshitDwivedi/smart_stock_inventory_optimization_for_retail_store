"""
Smart Stock Inventory Optimization Dashboard
---------------------------------------------
Interactive Streamlit dashboard for inventory analysis and insights.
Author: Toshit Dwivedi
Project: Smart Stock Inventory Optimization
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# Page configuration
st.set_page_config(
    page_title="SmartStock Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    """Load sales data with caching."""
    # Run from project root
    file_path = "dataset/updated_dataset.csv"
    df = pd.read_csv(file_path)
    
    # Add calculated columns
    df["Sales_to_Stock_Ratio"] = df["Units_Sold"] / df["Opening_Stock"]
    df["Stockout_Risk"] = df["Sales_to_Stock_Ratio"] > 0.7
    df["Stock_Efficiency"] = (df["Units_Sold"] / df["Opening_Stock"] * 100).round(2)
    
    return df

# Load data
df = load_data()

# Header
st.markdown('<h1 class="main-header">📊 SmartStock Inventory Optimization Dashboard</h1>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar filters
st.sidebar.header("🔍 Filters")
selected_products = st.sidebar.multiselect(
    "Select Products",
    options=df["Product_Name"].unique(),
    default=df["Product_Name"].unique()
)

selected_months = st.sidebar.multiselect(
    "Select Months",
    options=df["Month"].unique(),
    default=df["Month"].unique()
)

# Filter data
filtered_df = df[
    (df["Product_Name"].isin(selected_products)) & 
    (df["Month"].isin(selected_months))
]

# Key Metrics Row
st.subheader("📈 Key Performance Indicators")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    total_sales = filtered_df["Total_Sales_Value"].sum()
    st.metric("Total Sales Value", f"${total_sales:,.0f}")

with col2:
    total_units = filtered_df["Units_Sold"].sum()
    st.metric("Total Units Sold", f"{total_units:,}")

with col3:
    avg_price = filtered_df["Price"].mean()
    st.metric("Average Price", f"${avg_price:.2f}")

with col4:
    unique_products = filtered_df["Product_Name"].nunique()
    st.metric("Products", f"{unique_products}")

with col5:
    avg_efficiency = filtered_df["Stock_Efficiency"].mean()
    st.metric("Avg Stock Efficiency", f"{avg_efficiency:.1f}%")

st.markdown("---")

# Main visualizations
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview", "📈 Sales Analysis", "⚠️ Risk Analysis", 
    "💰 Revenue Insights", "📅 Time Series"
])

with tab1:
    st.subheader("Business Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Top products by sales value
        st.markdown("#### Top 10 Best-Selling Products")
        top_products = filtered_df.groupby("Product_Name")["Total_Sales_Value"].sum().sort_values(ascending=False).head(10).reset_index()
        fig = px.bar(
            top_products, 
            x="Product_Name", 
            y="Total_Sales_Value",
            color="Total_Sales_Value",
            color_continuous_scale="Blues",
            labels={"Total_Sales_Value": "Sales Value ($)", "Product_Name": "Product"}
        )
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, width='stretch')
    
    with col2:
        # Monthly sales distribution
        st.markdown("#### Monthly Sales Distribution")
        monthly_sales = filtered_df.groupby("Month")["Total_Sales_Value"].sum().reset_index()
        fig = px.pie(
            monthly_sales,
            values="Total_Sales_Value",
            names="Month",
            hole=0.4,
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, width='stretch')
    
    # Product performance table
    st.markdown("#### Product Performance Summary")
    summary = filtered_df.groupby("Product_Name").agg({
        "Units_Sold": "sum",
        "Total_Sales_Value": "sum",
        "Opening_Stock": "mean",
        "Stock_Efficiency": "mean"
    }).round(2).sort_values("Total_Sales_Value", ascending=False)
    summary.columns = ["Total Units Sold", "Total Sales ($)", "Avg Opening Stock", "Avg Efficiency (%)"]
    st.dataframe(summary, width='stretch')

with tab2:
    st.subheader("Sales Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Sales trend by product over time
        st.markdown("#### Sales Trend by Product")
        fig = px.line(
            filtered_df,
            x="Month",
            y="Units_Sold",
            color="Product_Name",
            markers=True,
            labels={"Units_Sold": "Units Sold", "Month": "Month"}
        )
        fig.update_layout(height=400, hovermode='x unified')
        st.plotly_chart(fig, width='stretch')
    
    with col2:
        # Price vs Units Sold scatter
        st.markdown("#### Price vs Sales Performance")
        fig = px.scatter(
            filtered_df,
            x="Price",
            y="Units_Sold",
            size="Opening_Stock",
            color="Product_Name",
            hover_data=["Month"],
            labels={"Price": "Price ($)", "Units_Sold": "Units Sold", "Opening_Stock": "Stock"}
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, width='stretch')
    
    # Units sold distribution
    st.markdown("#### Units Sold Distribution")
    fig = px.histogram(
        filtered_df,
        x="Units_Sold",
        nbins=20,
        color_discrete_sequence=["#1f77b4"],
        labels={"Units_Sold": "Units Sold"}
    )
    fig.add_vline(x=filtered_df["Units_Sold"].mean(), line_dash="dash", line_color="red",
                  annotation_text="Mean", annotation_position="top")
    fig.update_layout(height=400)
    st.plotly_chart(fig, width='stretch')

with tab3:
    st.subheader("Risk Analysis & Inventory Management")
    
    # Stockout risk products
    st.markdown("#### ⚠️ High Stockout Risk Products (>70% Stock Utilized)")
    risk_products = filtered_df[filtered_df["Stockout_Risk"] == True][
        ["Product_Name", "Month", "Units_Sold", "Opening_Stock", "Sales_to_Stock_Ratio", "Stock_Efficiency"]
    ].sort_values("Sales_to_Stock_Ratio", ascending=False)
    
    if len(risk_products) > 0:
        risk_products.columns = ["Product", "Month", "Units Sold", "Opening Stock", "Utilization Ratio", "Efficiency (%)"]
        st.dataframe(risk_products, width='stretch')
        
        # Risk visualization
        fig = px.bar(
            risk_products.head(15),
            x="Product",
            y="Efficiency (%)",
            color="Efficiency (%)",
            color_continuous_scale="Reds",
            labels={"Efficiency (%)": "Stock Efficiency (%)"}
        )
        fig.add_hline(y=70, line_dash="dash", line_color="orange", annotation_text="Risk Threshold (70%)")
        fig.update_layout(height=400)
        st.plotly_chart(fig, width='stretch')
    else:
        st.success("✓ No high-risk products found in the selected data!")
    
    # Stock efficiency heatmap
    st.markdown("#### Stock Efficiency Heatmap")
    pivot = filtered_df.pivot_table(
        values="Stock_Efficiency",
        index="Product_Name",
        columns="Month",
        aggfunc="mean"
    )
    fig = px.imshow(
        pivot,
        labels=dict(x="Month", y="Product", color="Efficiency (%)"),
        color_continuous_scale="RdYlGn",
        aspect="auto"
    )
    fig.update_layout(height=500)
    st.plotly_chart(fig, width='stretch')

with tab4:
    st.subheader("Revenue Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Revenue by product
        st.markdown("#### Revenue Distribution")
        revenue_data = filtered_df.groupby("Product_Name")["Total_Sales_Value"].sum().reset_index()
        fig = px.treemap(
            revenue_data,
            path=["Product_Name"],
            values="Total_Sales_Value",
            color="Total_Sales_Value",
            color_continuous_scale="Greens"
        )
        fig.update_layout(height=450)
        st.plotly_chart(fig, width='stretch')
    
    with col2:
        # Revenue per unit analysis
        st.markdown("#### Revenue Per Unit")
        filtered_df["Revenue_Per_Unit"] = filtered_df["Total_Sales_Value"] / filtered_df["Units_Sold"]
        rpu = filtered_df.groupby("Product_Name")["Revenue_Per_Unit"].mean().sort_values(ascending=False).reset_index()
        fig = px.bar(
            rpu,
            x="Revenue_Per_Unit",
            y="Product_Name",
            orientation="h",
            color="Revenue_Per_Unit",
            color_continuous_scale="Viridis",
            labels={"Revenue_Per_Unit": "Revenue/Unit ($)", "Product_Name": "Product"}
        )
        fig.update_layout(height=450)
        st.plotly_chart(fig, width='stretch')
    
    # Monthly revenue trend
    st.markdown("#### Monthly Revenue Trend")
    monthly_revenue = filtered_df.groupby("Month_Num").agg({
        "Total_Sales_Value": "sum",
        "Units_Sold": "sum"
    }).reset_index()
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(x=monthly_revenue["Month_Num"], y=monthly_revenue["Total_Sales_Value"], 
               name="Revenue", marker_color="#1f77b4"),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=monthly_revenue["Month_Num"], y=monthly_revenue["Units_Sold"],
                   name="Units", mode="lines+markers", marker_color="orange"),
        secondary_y=True
    )
    fig.update_xaxes(title_text="Month")
    fig.update_yaxes(title_text="Revenue ($)", secondary_y=False)
    fig.update_yaxes(title_text="Units Sold", secondary_y=True)
    fig.update_layout(height=400, hovermode="x unified")
    st.plotly_chart(fig, width='stretch')

with tab5:
    st.subheader("Time Series Analysis")
    
    # Product selection for detailed view
    selected_product = st.selectbox("Select Product for Detailed Analysis", df["Product_Name"].unique())
    product_data = df[df["Product_Name"] == selected_product]
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Sales trend for selected product
        st.markdown(f"#### {selected_product} - Sales Trend")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=product_data["Month"],
            y=product_data["Units_Sold"],
            mode="lines+markers",
            name="Units Sold",
            line=dict(color="#1f77b4", width=3),
            marker=dict(size=10)
        ))
        fig.update_layout(height=350, hovermode="x")
        st.plotly_chart(fig, width='stretch')
    
    with col2:
        # Stock vs Sales for selected product
        st.markdown(f"#### {selected_product} - Stock vs Sales")
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=product_data["Month"],
            y=product_data["Opening_Stock"],
            name="Opening Stock",
            marker_color="lightblue"
        ))
        fig.add_trace(go.Scatter(
            x=product_data["Month"],
            y=product_data["Units_Sold"],
            name="Units Sold",
            mode="lines+markers",
            line=dict(color="red", width=2),
            marker=dict(size=8)
        ))
        fig.update_layout(height=350, barmode="group", hovermode="x")
        st.plotly_chart(fig, width='stretch')
    
    # All products comparison
    st.markdown("#### All Products - Monthly Comparison")
    fig = px.bar(
        filtered_df,
        x="Month",
        y="Units_Sold",
        color="Product_Name",
        barmode="group",
        labels={"Units_Sold": "Units Sold", "Month": "Month"}
    )
    fig.update_layout(height=500, hovermode="x unified")
    st.plotly_chart(fig, width='stretch')

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray; padding: 1rem;'>
        <p><strong>SmartStock Inventory Optimization Dashboard</strong></p>
        <p>Developed by Toshit Dwivedi | Infosys Springboard Internship Project</p>
    </div>
""", unsafe_allow_html=True)


