import pandas as pd

df = pd.read_csv("../dataset/updated_dataset.csv")
monthly_sales = df.groupby("Month")["Total_Sales_Value"].sum()

print("Monthly Sales:")
print(monthly_sales)
