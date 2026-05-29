import pandas as pd

# data={
#     "Name":["Ankit Sharma","Riya","Aman"],
#     "Age":[27,25,29],
#     "Score":[92,80,50]
# }

# df=pd.DataFrame(data)
# df = pd.read_csv("./sales_data.csv")
# print(df)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df["Customer Name"])
# print(df[["Customer Name","Price (INR)"]])
# print(df) # uses labels
# print(df.loc[1]) # uses labels
# print(df.iloc[1]) # uses positions
# print(df[df["Price (INR)"] > 55000])
# print(df[(df["Price (INR)"] > 55000) & (df["Category"] == "Electronics")])
# print(df.isnull().sum()) # Check missing values
# print(df.dropna()) # Remove rows with null
# print(df.fillna(value=0)) # Fill null values
# print(df.rename(columns={"Customer Name":"Name"},inplace=True))

# Adding New Columns
# Date = "2025-12-04"
# df["Delivered"] = df["Order Date"] < Date
# print(df["Delivered"])

# Sorting
# print(df.sort_values("Price (INR)",ascending=False))

# GroupBy
# print(df.groupby("Price (INR)")["Quantity"].mean())

# Task:
# data={
#     "Product":["Laptop","Mobile","Computer"],
#     "Price":[50000,20000,30000],
#     "Quantity":[2,3,4]
# }
# df= pd.DataFrame(data)
# print(df.head(2))
# print(df[df["Price"] > 20000])

# Add a new column Total = Price * Quantity
# df["Total"]=df["Price"]*df["Quantity"]

# Sort by Total (descending)
# print(df.sort_values("Total",ascending=False))