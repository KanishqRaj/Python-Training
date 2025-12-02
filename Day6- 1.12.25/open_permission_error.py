try:
    with open("open.txt" , "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("FILE NOT FOUND")
except PermissionError:
    print("Permission Denied")