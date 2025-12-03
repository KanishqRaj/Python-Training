import pandas as pd
import numpy as np
from io import StringIO

df = pd.read_csv("Data_task.csv")

df["ShipDate"] = pd.to_datetime(df["ShipDate"])
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["ShippingDays"] = (df["ShipDate"] - df["OrderDate"]).dt.days
df["ProfitMargin"] = df["Profit"] / df["Sales"]

##Group By Total Sales Per Region
total_sales_per_region = df.groupby("Region")["Sales"].sum()
print(total_sales_per_region)

##Group By Average profit per Category
avg_profit = df.groupby("Category")["Profit"].mean()
print(avg_profit)

##Group By Count of orders per Customer
order_count = df.groupby("CustomerID").size()
print(order_count)

#Sum of Sales per segment
sales_sum = df.groupby("Segment")["Sales"].sum()
print(sales_sum)

##Total Quantity per SubCategory
quantity_per_subcategory = df.groupby('SubCategory')['Quantity'].sum()
print(quantity_per_subcategory)

##Mean by Subcategory
mean_shipping_days_category = df.groupby('Category')['ShippingDays'].mean()
print(mean_shipping_days_category)


