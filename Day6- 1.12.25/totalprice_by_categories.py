import pandas as pd
df = pd.read_csv("retail_sales.csv")

sales_by_store = df.groupby("Store")["TotalPrice"].sum()
print(sales_by_store)

sales_by_city = df.groupby("City")["TotalPrice"].sum()
print(sales_by_city)

sales_by_Category = df.groupby("Category")["TotalPrice"].sum()
print(sales_by_Category)

