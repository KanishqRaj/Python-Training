import pandas as pd
import numpy as np
from io import StringIO

df = pd.read_csv("Data_task.csv")

##shipping days calculation
df["ShipDate"] = pd.to_datetime(df["ShipDate"])
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["ShippingDays"] = (df['ShipDate'] - df['OrderDate']).dt.days

##profit margin calculation
df["ProfitMargin"] = df["Profit"] / df["Sales"]
print(df["ProfitMargin"])

##Customer Name Title
df["CustomerName"] = df["CustomerName"].str.title()
print(df["CustomerName"])

##Remove Rows where sales is zero or Negative
df = df[df["Sales"]>0]

df["Discount"] = (df["Discount"]* 100).astype(int).astype(str) + "%"
print(df["Discount"])

