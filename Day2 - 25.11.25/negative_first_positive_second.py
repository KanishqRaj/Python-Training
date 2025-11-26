nums = [-1,-4,-6,9,4,88,2,-9,-33]

negative = [n for n in nums if n<0]
positive = [n for n in nums if n>=0]

print(negative + positive)

