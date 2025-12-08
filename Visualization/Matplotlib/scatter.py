import matplotlib.pyplot as plt
import pandas as pd

file_path="../../dataset/updated_dataset.csv"
df=pd.read_csv(file_path)


plt.figure(figsize=(8,5))
plt.scatter(df["Units_Sold"], df["Total_Sales_Value"], color="purple")
plt.title("Units Sold vs Total Sales Value")
plt.xlabel("Units Sold")
plt.ylabel("Total Sales Value")
plt.grid(True)
plt.show()

