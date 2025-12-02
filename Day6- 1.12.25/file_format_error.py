import csv
try:
    with open("Open.csv" , "r") as f:
        reader = csv.reader(f)
except FileNotFoundError:
    print("File not found")
except csv.Error:
    print("Invalid file format")