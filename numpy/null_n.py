import pandas as pd
import numpy as np
df = pd.read_csv("../original_files/updated_dataset.csv")

print("Original Dataset:")
print(df.head())
#explicity adding null values for learning purpose
df.loc[0, "Units_Sold"] = np.nan
df.loc[2, "Opening_Stock"] = np.nan

print("\nDataset After Inserting np.nan:")
print(df.head())

units = df["Units_Sold"].values

print("\nChecking nulls")
print(np.isnan(units))   

df_rows_dropped = df.dropna()
print("After Dropping Rows with Null Values:")
print(df_rows_dropped)

df_columns_dropped = df.dropna(axis=1)
print("\nAfter Dropping Columns with Null Values:")
print(df_columns_dropped.head())

#replacing null values
df["Units_Sold"] = df["Units_Sold"].fillna(df["Units_Sold"].mean())
df["Opening_Stock"] = df["Opening_Stock"].fillna(df["Opening_Stock"].mean())
print(df.head())

