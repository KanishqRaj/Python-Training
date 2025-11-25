nums = [0,3,0,5,7,0,9]

result = [n for n in nums if n!=0] +  [n for n in nums if n==0]
print(result)