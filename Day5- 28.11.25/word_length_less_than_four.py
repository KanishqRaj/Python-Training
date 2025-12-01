list = ["hello" , "hi" , "python" , "word"]
result = []

for words in list:
    if len(words)<=4:
        result.append(words)

print(result)