import pandas as pd
import numpy as np
from io import StringIO

df = pd.read_csv("Data_task.csv")

df["ShipDate"] = pd.to_datetime(df["ShipDate"])
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["ShippingDays"] = (df["ShipDate"] - df["OrderDate"]).dt.days
df["ProfitMargin"] = df["Profit"] / df["Sales"]

##Sort by sales Descending
sales_sorted = df.sort_values(by = ["Sales"], ascending = False)
print(sales_sorted)

##Sort by ProfitMargin
profitMargin_sorted = df.sort_values(by = ["ProfitMargin"])
print(profitMargin_sorted)

##Sort by Region then City
Region_city_sorted = df.sort_values(by=["Region", "City"])
print(Region_city_sorted)

##Sort by Shipping Date
shippingDate_sorted = df.sort_values(by=["ShippingDays"],ascending=False)
print(shippingDate_sorted)

##Sort by CustomerName Alphabet
customerName_sorted = df.sort_values(by=["CustomerName"])
print(customerName_sorted)



