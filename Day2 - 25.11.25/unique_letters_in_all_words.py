list = ["hello" , "world", "python"]
set = set()
for i in range(len(list)):
    for j in range(len(list[i])):
        set.add(list[i][j])

print(set)