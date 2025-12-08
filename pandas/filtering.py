import pandas as pd

df = pd.read_csv("../dataset/updated_dataset.csv")
high_sales = df[df["Units_Sold"] > 80]

print("Products with high sales (>80 units):")
print(high_sales)
