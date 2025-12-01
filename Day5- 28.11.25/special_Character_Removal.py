str = input("Enter a string : ")
res = ''
for char in str:
    res = ''.join([char for char in str if char.isalnum()])

print(res)


