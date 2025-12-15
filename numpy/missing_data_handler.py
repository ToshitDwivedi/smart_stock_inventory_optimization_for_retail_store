import pandas as pd
import numpy as np
import os

# Create output folder if not exists
os.makedirs("output", exist_ok=True)

# Load data
df = pd.read_csv("dataset/updated_dataset.csv")
df_demo = df.copy()

# Introduce some missing values for demonstration
df_demo.loc[0, "Units_Sold"] = np.nan
df_demo.loc[2, "Opening_Stock"] = np.nan
df_demo.loc[5, "Price"] = np.nan

print("Created missing values for demo.")

# Fill missing values with mean
df_demo["Units_Sold"].fillna(df_demo["Units_Sold"].mean(), inplace=True)
df_demo["Opening_Stock"].fillna(df_demo["Opening_Stock"].mean(), inplace=True)
df_demo["Price"].fillna(df_demo["Price"].mean(), inplace=True)

# Save cleaned data
df_demo.to_csv("output/cleaned_data_demo.csv", index=False)
print("Missing data handled using mean imputation.")
print(f"New missing value count: {df_demo.isnull().sum().sum()}")
