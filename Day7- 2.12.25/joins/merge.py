import pandas as pd

df = pd.read_csv("Data_task.csv")

##Merge 1
discount_lookup = pd.DataFrame({
    "Segment" : ["Consumer","Corporate","Home"],
    "Segment_rate" : [5,8,10]
})
merge1 = pd.merge(df,discount_lookup,on="Segment",how="left")
print(merge1)

##Merge 2
region_tax = pd.DataFrame({
    "Region" : ["West" , "Central" , "East","South"],
    "Tax_rate" : [0.05 , 0.02, 0.04, 0.08]
})
merge2 = pd.merge(df,region_tax,on="Region",how="left")
print(merge2)

##Merge 3
customer_totals = df.groupby("CustomerID").agg({"Sales" : 'sum',"Profit" : 'sum'}).reset_index()
customer_totals.rename(columns={"Sales":"TotalSales","Profit":"TotalProfit"},inplace=True)
df = df.merge(customer_totals,on="CustomerID",how="left")
print(df)

##Merge 4
product_profit = df.groupby('ProductName').agg({'Profit': 'sum'}).reset_index()
product_profit.rename(columns={'Profit': 'ProductTotalProfit'}, inplace=True)
df = df.merge(product_profit, on='ProductName', how='left')
print(df.head())
