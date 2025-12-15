import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Inventory Management Dashboard")

# Load Data
df = pd.read_csv("dataset/updated_dataset.csv")

if st.checkbox("Show Raw Data"):
    st.write(df)

# Visualizations
st.header("Sales Overview")

# Bar Chart
st.subheader("Sales by Product")
fig_bar = px.bar(df.groupby('Product_Name')['Total_Sales_Value'].sum().reset_index(), 
                 x='Product_Name', y='Total_Sales_Value')
st.plotly_chart(fig_bar)

# Line Chart
st.subheader("Monthly Sales Trend")
fig_line = px.line(df.groupby('Month')['Units_Sold'].sum().reset_index(), 
                   x='Month', y='Units_Sold')
st.plotly_chart(fig_line)

# Scatter Plot
st.subheader("Price vs Sales")
fig_scatter = px.scatter(df, x='Price', y='Units_Sold', color='Product_Name', size='Opening_Stock')
st.plotly_chart(fig_scatter)

st.success("Dashboard Loaded Successfully!")
