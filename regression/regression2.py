import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
file_path="../dataset/updated_dataset.csv"
df=pd.read_csv(file_path)
monthly_sales = df.groupby('Month_Num')['Total_Sales_Value'].sum().reset_index()
X = monthly_sales[['Month_Num']]
y = monthly_sales['Total_Sales_Value']
model = LinearRegression()
model.fit(X, y)
next_month_num = np.array([[7]])
predicted_sales = model.predict(next_month_num)[0]
print("Actual Monthly Total Sales Value (Used for Training):")
print("\n--- Prediction for July (Month 7) ---")
print(f"Predicted Total Sales Value for July: {predicted_sales:,.2f}")
