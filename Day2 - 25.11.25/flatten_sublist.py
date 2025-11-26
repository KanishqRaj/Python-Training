nums = [[1,2] , [3,4] , [5,6]]
flatten = []

for n in nums:
    for num in n:
        flatten.append(num)

print(flatten)