import pandas as pd
df = pd.read_csv("retail_sales.csv")

top_five_highest = df.sort_values(by=["TotalPrice"], ascending=False).head(5)
print(top_five_highest)

