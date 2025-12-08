import numpy as np
import pandas as pd

df = pd.read_csv("../dataset/updated_dataset.csv")
units = np.array(df["Units_Sold"])
print("Units Sold Array:")
print(units)
