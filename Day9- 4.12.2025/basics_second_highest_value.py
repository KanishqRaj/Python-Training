def second_largest(nums):
    largest = second = float("-inf")
    for num in nums:
        if num > largest:
            second = largest
            largest = num
            
        elif num > second and num!=largest:
            second = num
    return second




N = int(input("Enter the number of integers for input: "))
nums = [int(input()) for i in range(N)]
print(second_largest(nums))