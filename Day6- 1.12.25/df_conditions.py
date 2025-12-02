import pandas as pd

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})

highest_Scores = df[df["Marks"]>70]
print(highest_Scores)

medium_scores = df[(df["Marks"]>70) & (df["Marks"]<80)]
print("Medium Scores" , medium_scores)