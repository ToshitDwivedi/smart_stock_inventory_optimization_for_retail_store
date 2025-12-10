import pandas as pd
import os

# Use absolute path relative to script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "dataset", "updated_dataset.csv")

df = pd.read_csv(DATA_PATH)
print("Missing values in each column:")
print(df.isnull().sum())
