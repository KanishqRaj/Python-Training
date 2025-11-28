with open("notes.txt" , "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines, 1):
        print(line.strip())