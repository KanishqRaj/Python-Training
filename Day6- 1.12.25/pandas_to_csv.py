import pandas_basic as pd
data = {
    "Name" : ["Kanishq" , "Harismitha" , "Samson"],
    "Age" : [22,21,22],
    "City" : ["Coimbatore" , "Coimbatore" , "Ooty"]
}

df = pd.DataFrame(data)

df.to_csv("Info.csv",index = False )
print("Successfully converted")