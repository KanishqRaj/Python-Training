with open("notes.txt" , "r") as f:
    words_count = 0
    for line in f:
        words = line.split()
        words_count += len(words)

print(words_count)
