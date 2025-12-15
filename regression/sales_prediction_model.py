import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import os

os.makedirs("output", exist_ok=True)

# Load data
df = pd.read_csv("dataset/updated_dataset.csv")

# Features and Target
X = df[['Price', 'Opening_Stock']]
y = df['Units_Sold']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
score = r2_score(y_test, y_pred)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Units Sold')
plt.ylabel('Predicted Units Sold')
plt.title(f'Sales Prediction Model (R2 = {score:.3f})')
plt.savefig('output/sales_prediction.png')
plt.close()

# Make Predictions for scenarios
scenarios = pd.DataFrame({
    'Price': [50, 75, 30],
    'Opening_Stock': [150, 200, 250]
})
predictions = model.predict(scenarios)
scenarios['Predicted_Units'] = predictions
scenarios.to_csv('output/prediction_scenarios.csv', index=False)

print(f"Sales Prediction Model R2 Score: {score:.3f}")
print("Scenarios Predicted and Saved.")
print(scenarios)
