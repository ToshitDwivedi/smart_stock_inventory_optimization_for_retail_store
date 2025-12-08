import matplotlib.pyplot as plt
import pandas as pd

file_path = "../../dataset/updated_dataset.csv"
df=pd.read_csv(file_path)
plt.figure(figsize=(10,5))
plt.plot(df.index, df["Price"],  label="Price")
plt.plot(df.index, df["Units_Sold"], label="Units Sold")

plt.title("Price vs Sales Trend")
plt.xlabel("Time Step")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

