import numpy as np
import pandas as pd

df = pd.read_csv("../dataset/updated_dataset.csv")
units = np.array(df["Units_Sold"])
#Statistical operations
print("Maximum units sold:", np.max(units))
print("Minimum units sold:", np.min(units))
print("Total units sold:", np.sum(units))

#Mathematical operations
demand = np.array(df["Units_Sold"])
stock = np.array(df["Opening_Stock"])
remaining = stock - demand
print("Remaining stock (NumPy calculation):")
print(remaining)
