import numpy as np
import pandas as pd
import os

os.makedirs("output", exist_ok=True)

df = pd.read_csv("dataset/updated_dataset.csv")

units = np.array(df["Units_Sold"])
stock = np.array(df["Opening_Stock"])
prices = np.array(df["Price"])

stats = {
    "Units Sold": {
        "Mean": np.mean(units),
        "Median": np.median(units),
        "Std Dev": np.std(units),
        "Min": np.min(units),
        "Max": np.max(units)
    },
    "Opening Stock": {
        "Mean": np.mean(stock),
        "Median": np.median(stock),
        "Std Dev": np.std(stock),
        "Min": np.min(stock),
        "Max": np.max(stock)
    },
    "Price": {
        "Mean": np.mean(prices),
        "Median": np.median(prices),
        "Std Dev": np.std(prices),
        "Min": np.min(prices),
        "Max": np.max(prices)
    }
}

pd.DataFrame(stats).T.to_csv("output/statistical_summary.csv")
print("Statistical Summary:")
print(pd.DataFrame(stats).T)
