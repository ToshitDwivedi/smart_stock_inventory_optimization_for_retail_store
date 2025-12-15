import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import os

os.makedirs("output", exist_ok=True)

# Load data
df = pd.read_csv("dataset/updated_dataset.csv")

# Group by month for forecasting
monthly_sales = df.groupby('Month_Num')['Total_Sales_Value'].sum().reset_index()

X = monthly_sales[['Month_Num']]
y = monthly_sales['Total_Sales_Value']

# Train Model
model = LinearRegression()
model.fit(X, y)

# Forecast Future
future_months = pd.DataFrame({'Month_Num': [7, 8, 9, 10, 11, 12]})
forecast = model.predict(future_months)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(X, y, marker='o', label='Actual')
plt.plot(future_months, forecast, marker='s', linestyle='--', label='Forecast')
plt.xlabel('Month')
plt.ylabel('Total Sales Value')
plt.title('Monthly Sales Forecast')
plt.legend()
plt.savefig('output/monthly_forecast.png')
plt.close()

# Save Forecast
forecast_df = future_months.copy()
forecast_df['Forecast_Sales'] = forecast
forecast_df.to_csv('output/monthly_sales_forecast.csv', index=False)

print(f"Monthly Forecast R2 Score: {r2_score(y, model.predict(X)):.3f}")
print("Forecast Saved.")
