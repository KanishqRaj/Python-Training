import pandas as pd
import numpy as np
from io import StringIO

df = pd.read_csv("Data_task.csv")
print(df.head(10))
print(df.shape)
print(df.info())
print(df.isnull())
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["ShipDate"] = pd.to_datetime(df["ShipDate"])
print(df.info())
