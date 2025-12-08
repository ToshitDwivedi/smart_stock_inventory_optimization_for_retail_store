import streamlit as st
import pandas as pd
import plotly.express as px

st.title("SmartStock Inventory Optimization Dashboard")

file_path="../original_files/updated_dataset.csv"
df=pd.read_csv(file_path)

st.subheader("Top 5 Best Selling Products")
category_sales = df.groupby("Product_Name")["Total_Sales_Value"].sum().reset_index()
top_products = category_sales.sort_values(by="Total_Sales_Value", ascending=False).head(5)
fig1 = px.bar(top_products, x="Product_Name", y="Total_Sales_Value",color="Total_Sales_Value", title="Top 5 Products")
st.plotly_chart(fig1)

st.subheader("Sales Trend by Products")
category_sales = df.groupby("Product_Name")["Total_Sales_Value"].sum().reset_index()
fig2 = px.line(category_sales, x="Product_Name", y="Total_Sales_Value", markers=True,title="Sales Trend by products")
st.plotly_chart(fig2)



st.subheader("Price vs Units Sold")
fig3 = px.scatter(df, x="Price", y="Units_Sold",size="Opening_Stock", color="Product_Name")
st.plotly_chart(fig3)

st.subheader("Stock-out Risk Products")
df["Sales_to_Stock_Ratio"] = df["Units_Sold"] / df["Opening_Stock"]
df["Stockout_Risk"] = df["Sales_to_Stock_Ratio"] > 0.7
st.dataframe(df[df["Stockout_Risk"] == True])


