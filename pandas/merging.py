import pandas as pd

df1 = pd.read_csv("../dataset/updated_dataset.csv")
df_cost = pd.DataFrame({"Product_Name": ["Rice", "Sugar", "Oil"],"Cost_Per_Unit": [30, 40, 80]})
merged = pd.concat([df1,df_cost],axis=1)
print("Merged Data:")
print(merged)
print(merged.columns)

