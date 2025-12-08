import pandas as pd
import plotly.express as px

file_path="../../original_files/updated_dataset.csv"
df=pd.read_csv(file_path)
fig = px.pie(df,names="Product_Name",values="Total_Sales_Value",title="Sales Contribution by Product")
fig.show()


