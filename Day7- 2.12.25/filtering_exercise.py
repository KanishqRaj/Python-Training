import pandas as pd
import numpy as np
from io import StringIO

df = pd.read_csv("Data_task.csv")

##West Region Orders
west_orders = df[df["Region"] == "West"]
print(west_orders)

##Technology Category with Sales > 400
tech_category = df[(df["Category"] == "Technology") & (df["Sales"] > 400)]
print(tech_category)

##All products returned by Customers
returned_products = df[df["Returned"].str.lower() == "Yes"]
print(returned_products)

##Furniture Order Shipped after 24-01-20
furniture_order = df[(df["Category"] == "Furniture") & (df["ShipDate"] > '24-01-20')]
print(furniture_order)

##orders where profit <20
low_profit = df[df["Profit"] < 20]
print(low_profit)
