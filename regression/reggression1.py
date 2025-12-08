from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
file_path="../dataset/updated_dataset.csv"
df=pd.read_csv(file_path)
X = df[['Price', 'Opening_Stock']]
y = df['Units_Sold']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
new_data = pd.DataFrame({'Price': [50], 'Opening_Stock': [150]})
predicted_units = model.predict(new_data)[0]
print(f"\nPrediction for Price=50 and Opening_Stock=150: {np.round(predicted_units, 0)} Units Sold")
