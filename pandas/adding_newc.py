import pandas as pd

df = pd.read_csv("../dataset/updated_dataset.csv")
df["Remaining_Stock"] = df["Opening_Stock"] - df["Units_Sold"]
print(df[["Product_Name", "Opening_Stock", "Units_Sold", "Remaining_Stock"]])
