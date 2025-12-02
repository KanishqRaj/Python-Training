import pandas_basic as pd

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})

df["result"] = df["Marks"].apply(lambda x: "Pass" if x>60 else "Fail")

sorted_df = df.sort_values(by="Marks", ascending=False)
print(sorted_df)