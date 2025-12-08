import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
file_path="../original_files/updated_dataset.csv"
df=pd.read_csv(file_path)
soap_data = df[df['Product_ID'] == 'P003'].sort_values(by='Month_Num')
X_soap = soap_data[['Month_Num']]
y_soap = soap_data['Units_Sold']
model_soap = LinearRegression()
model_soap.fit(X_soap, y_soap)
predicted_units = model_soap.predict([[7]])[0]

print("Actual Units Sold for Soap (Used for Training):")
print(soap_data[['Month', 'Units_Sold']])

print("\n--- Prediction for Soap Units Sold in July (Month 7) ---")
print(f"Predicted Units Sold for Soap (P003) in July: {np.round(predicted_units, 0):.0f} Units")