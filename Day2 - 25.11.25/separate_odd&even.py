nums = [10, 3, 5, 12, 8, 7, 1]
odd=[]
even = []

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        even.append(nums[i])
    else:
        odd.append(nums[i])

print("Odd: ", odd)
print("Even: ", even)