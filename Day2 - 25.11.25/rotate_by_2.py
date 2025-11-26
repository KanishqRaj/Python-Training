nums = [1,2,3,4,5,6]
n = 2

length = len(nums)
for i in range(n):
    first = nums[0]
    for j in range(length - 1):
        nums[j] = nums[j + 1]
    nums[length - 1] = first

print(nums)