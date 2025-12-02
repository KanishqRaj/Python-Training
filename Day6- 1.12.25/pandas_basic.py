import pandas_basic as pd

s = pd.Series([1,2,3,4,5,6])
print(s)

data = {
    "Name":  ["Kanishq","Anto" ,"Synthia"],
    "Marks":  [94,76,97]
}
df = pd.DataFrame(data)
print(df)