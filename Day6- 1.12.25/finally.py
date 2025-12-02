try:
    with open("Open.txt" , "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File Not Found")
finally:
    print("Connection is closed")

