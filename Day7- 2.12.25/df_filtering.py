import pandas as pd
import numpy as np

df = pd.read_csv("retail_sales.csv")

high_end = df[(df["Category"] ==  "Electronics") & (df["TotalPrice"] > 10000)]
sorted_df = df.sort_values("TotalPrice", ascending=False)
print(high_end)

category_sales = df.groupby("Category")["TotalPrice"].sum()
print(category_sales)

store_avg = df.groupby("Store")["TotalPrice"].mean()
print(store_avg)

city_orders = df.groupby("City")["OrderID"].count()
print(city_orders)
