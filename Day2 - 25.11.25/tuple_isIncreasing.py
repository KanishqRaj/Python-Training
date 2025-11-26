nums = (1,2,3,3)

def isIncreasing(t):
    for i in range(len(t)-1):
        if(t[i] >= t[i+1]):
            return False
    return True

print(isIncreasing(nums))