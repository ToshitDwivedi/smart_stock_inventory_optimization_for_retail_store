import pandas as pd

# Configure paths (run from project root)
DATA_PATH = "dataset/updated_dataset.csv"

df = pd.read_csv(DATA_PATH)
monthly_sales = df.groupby("Month")["Total_Sales_Value"].sum()

print("Monthly Sales:")
print(monthly_sales)
