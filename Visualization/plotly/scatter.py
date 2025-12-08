import plotly.express as px
import pandas as pd
import plotly.io as pio
file_path="../../dataset/updated_dataset.csv"
df=pd.read_csv(file_path)
#print(df)

#Scatter plot
fig=px.scatter(df,x="Opening_Stock",y="Units_Sold",
               color="Product_Name",title="Opening Stock VS Units Sold")
fig.show()
