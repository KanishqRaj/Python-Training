list = ['a', 'b', 'c', 'd', 'e']

temp = list[0]
list[0] = list[-1]
list[-1] = temp
print(list)