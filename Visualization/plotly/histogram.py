import pandas as pd
import plotly.express as px

file_path="../../original_files/updated_dataset.csv"
df=pd.read_csv(file_path)
fig = px.histogram(df,x="Units_Sold",nbins=10, title=f"Distribution of Units Sold ")
fig.show()

