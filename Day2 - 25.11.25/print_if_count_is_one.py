nums = [1,2,3,2,1,5,8,9,7,6,6]

result= []

for n in nums:
    if nums.count(n) > 1 and n not in result:
        result.append(n)

print(result)
