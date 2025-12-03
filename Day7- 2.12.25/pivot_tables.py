from itertools import count

import pandas as pd
import numpy as np
from io import StringIO

df = pd.read_csv("Data_task.csv")

df["ShipDate"] = pd.to_datetime(df["ShipDate"])
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

pivot1 = pd.pivot_table(df,index = "Region" , columns = "Category" , values = "Sales" ,aggfunc = sum , fill_value=0)
print(pivot1)

pivot2 = pd.pivot_table(df, index = "SubCategory" , columns = "Segment",values = "Sales",aggfunc = sum , fill_value=0)
print(pivot2)

pivot3 = pd.pivot_table(df, index="Returned" , columns = "Region" , values = "OrderID" ,aggfunc = count , fill_value=0)
print(pivot3)

pivot4 = pd.pivot_table(df,index  = "Category" , values = "UnitPrice" , aggfunc = 'mean')
print(pivot4)

df["Month"] = df["OrderDate"].dt.to_period("M")
pivot5 = pd.pivot_table(df,index = "Month" , columns = "Region" , values = "Quantity" ,aggfunc = sum , fill_value=0)
print(pivot5)