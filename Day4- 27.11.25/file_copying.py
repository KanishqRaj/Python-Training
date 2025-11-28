with open("notes.txt", "r") as source,open("backup.txt","w")as dest:
    for line in source:
        dest.write(line)
    print("File Copied Successfully")


