import matplotlib.pyplot as plt
import pandas as pd

file_path="../../original_files/updated_dataset.csv"
df=pd.read_csv(file_path)

plt.figure(figsize=(10,5))
plt.bar(df["Product_Name"], df["Total_Sales_Value"], color='skyblue')
plt.title("Total Sales Value by Product")
plt.xlabel("Product Name")
plt.ylabel("Total Sales Value")
plt.show()
#plt.savefig("bar_chart.png")

