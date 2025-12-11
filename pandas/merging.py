import pandas as pd

# Configure paths (run from project root)
DATA_PATH = "dataset/updated_dataset.csv"

df1 = pd.read_csv(DATA_PATH)
df_cost = pd.DataFrame({"Product_Name": ["Rice", "Sugar", "Oil"],"Cost_Per_Unit": [30, 40, 80]})
merged = pd.concat([df1,df_cost],axis=1)
print("Merged Data:")
print(merged)
print(merged.columns)

