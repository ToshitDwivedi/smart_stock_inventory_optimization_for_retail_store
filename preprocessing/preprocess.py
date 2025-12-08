import pandas as pd

file_path = r"C:\python\InfosysspringboardInternship\original_files\sales_data.csv"
df = pd.read_csv(file_path)

print("Original data set",df)
#Checking if there are any null values
print(df.isnull().sum())
#Modifying data as per our requirements
#Adding the sales column to know the total sales
df['Total_Sales_Value'] = df['Units_Sold'] * df['Price']
print("Updated dataset",df)


month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

df['Month_Num'] = df['Month'].apply(lambda x: month_order.index(x) + 1)
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

print(df.head())

df.to_csv(r"C:\python\InfosysspringboardInternship\original_files\updated_dataset.csv", index=False)
