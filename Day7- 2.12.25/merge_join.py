import pandas as pd
import numpy as np

df = pd.read_csv("retail_sales.csv")

customers = pd.DataFrame({
    "CustomerType" : ["New" , "Retruning"],
    "Discount" : [5,10]
})

merged = df.merge(customers, on="CustomerType" , how = "left")
print(merged)
