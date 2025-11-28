with open("sample.txt" , "w") as f:
    f.write("Hello World\n")
    f.write("This file was created using File handling in Python\n")

with open("sample.txt" , "r") as f:
    content = f.read()
    print(content)