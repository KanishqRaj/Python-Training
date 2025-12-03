import pandas as pd

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})

df.to_json("students.json",orient="records",indent =4)
print("JSON file created")

df = pd.read_json("students.json")

print("JSON file read successfully")
print(df)